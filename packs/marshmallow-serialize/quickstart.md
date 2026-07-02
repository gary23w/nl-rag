---
title: "Quickstart"
source: https://marshmallow.readthedocs.io/en/stable/quickstart.html
domain: marshmallow-serialize
license: CC-BY-SA-4.0
tags: python marshmallow, marshmallow serialization, object schema python
fetched: 2026-07-02
---

# Quickstart

This guide will walk you through the basics of creating schemas for serializing and deserializing data.

## Declaring schemas

Let’s start with a basic user “model”.

```python
from dataclasses import dataclass, field
import datetime as dt

@dataclass
class User:
    name: str
    email: str
    created_at: dt.datetime = field(default_factory=dt.datetime.now)
```

Create a schema by defining a class with variables mapping attribute names to `Field` objects.

```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()
```

See also

For a full reference on the available field classes, see the `fields module documentation`.

Creating schemas from dictionaries

You can also create a schema from a dictionary of fields using the `from_dict` method.

```python
from marshmallow import Schema, fields

UserSchema = Schema.from_dict(
    {
        "name": fields.Str(),
        "email": fields.Email(),
        "created_at": fields.DateTime(),
    }
)
```

`from_dict` is especially useful for generating schemas at runtime.

## Serializing objects (“dumping”)

Serialize objects by passing them to your schema’s `dump` method, which returns the formatted result.

```python
from pprint import pprint

user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
pprint(result)
# {"name": "Monty",
#  "email": "monty@python.org",
#  "created_at": "2014-08-17T14:54:16.049594+00:00"}
```

You can also serialize to a JSON-encoded string using `dumps`.

```python
json_result = schema.dumps(user)
print(json_result)
# '{"name": "Monty", "email": "monty@python.org", "created_at": "2014-08-17T14:54:16.049594+00:00"}'
```

## Filtering output

You may not need to output all declared fields every time you use a schema. You can specify which fields to output with the `only` parameter.

```python
summary_schema = UserSchema(only=("name", "email"))
summary_schema.dump(user)
# {"name": "Monty", "email": "monty@python.org"}
```

You can also exclude fields by passing in the `exclude` parameter.

## Deserializing objects (“loading”)

The reverse of the `dump` method is `load`, which validates and deserializes an input dictionary to an application-level data structure.

By default, `load` will return a dictionary of field names mapped to deserialized values (or raise a `ValidationError` with a dictionary of validation errors, which we’ll revisit later).

```python
from pprint import pprint

user_data = {
    "created_at": "2014-08-11T05:26:03.869245",
    "email": "ken@yahoo.com",
    "name": "Ken",
}
schema = UserSchema()
result = schema.load(user_data)
pprint(result)
# {'name': 'Ken',
#  'email': 'ken@yahoo.com',
#  'created_at': datetime.datetime(2014, 8, 11, 5, 26, 3, 869245)},
```

Notice that the datetime string was converted to a `datetime` object.

### Deserializing to objects

In order to deserialize to an object, define a method of your `Schema` and decorate it with `post_load`. The method receives a dictionary of deserialized data.

```python
from marshmallow import Schema, fields, post_load

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
```

Now, the `load` method return a `User` instance.

```python
user_data = {"name": "Ronnie", "email": "ronnie@stones.com"}
schema = UserSchema()
result = schema.load(user_data)
print(result)  # => <User(name='Ronnie')>
```

## Handling collections of objects

Set `many=True` when dealing with iterable collections of objects.

```python
user1 = User(name="Mick", email="mick@stones.com")
user2 = User(name="Keith", email="keith@stones.com")
users = [user1, user2]
schema = UserSchema(many=True)
result = schema.dump(users)  # OR UserSchema().dump(users, many=True)
pprint(result)
# [{'name': u'Mick',
#   'email': u'mick@stones.com',
#   'created_at': '2014-08-17T14:58:57.600623+00:00'}
#  {'name': u'Keith',
#   'email': u'keith@stones.com',
#   'created_at': '2014-08-17T14:58:57.600623+00:00'}]
```

## Validation

`Schema.load` (and its JSON-decoding counterpart, `Schema.loads`) raises a `ValidationError` error when invalid data are passed in. You can access the dictionary of validation errors from the `ValidationError.messages` attribute. The data that were correctly deserialized are accessible in `ValidationError.valid_data`. Some fields, such as the `Email` and `URL` fields, have built-in validation.

```python
from marshmallow import ValidationError

try:
    result = UserSchema().load({"name": "John", "email": "foo"})
except ValidationError as err:
    print(err.messages)  # => {"email": ['"foo" is not a valid email address.']}
    print(err.valid_data)  # => {"name": "John"}
```

When validating a collection, the errors dictionary will be keyed on the indices of invalid items.

```python
from pprint import pprint

from marshmallow import Schema, fields, ValidationError

class BandMemberSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email()

user_data = [
    {"email": "mick@stones.com", "name": "Mick"},
    {"email": "invalid", "name": "Invalid"},  # invalid email
    {"email": "keith@stones.com", "name": "Keith"},
    {"email": "charlie@stones.com"},  # missing "name"
]

try:
    BandMemberSchema(many=True).load(user_data)
except ValidationError as err:
    pprint(err.messages)
    # {1: {'email': ['Not a valid email address.']},
    #  3: {'name': ['Missing data for required field.']}}
```

You can perform additional validation for a field by passing the `validate` argument. There are a number of built-in validators in the marshmallow.validate module.

```python
from pprint import pprint

from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min=1))
    permission = fields.Str(validate=validate.OneOf(["read", "write", "admin"]))
    age = fields.Int(validate=validate.Range(min=18, max=40))

in_data = {"name": "", "permission": "invalid", "age": 71}
try:
    UserSchema().load(in_data)
except ValidationError as err:
    pprint(err.messages)
    # {'age': ['Must be greater than or equal to 18 and less than or equal to 40.'],
    #  'name': ['Shorter than minimum length 1.'],
    #  'permission': ['Must be one of: read, write, admin.']}
```

You may implement your own validators. A validator is a callable that accepts a single argument, the value to validate. If validation fails, the callable should raise a `ValidationError` with an error message.

```python
from marshmallow import Schema, fields, ValidationError

def validate_quantity(n):
    if n < 0:
        raise ValidationError("Quantity must be greater than 0.")
    if n > 30:
        raise ValidationError("Quantity must not be greater than 30.")

class ItemSchema(Schema):
    quantity = fields.Integer(validate=validate_quantity)

in_data = {"quantity": 31}
try:
    result = ItemSchema().load(in_data)
except ValidationError as err:
    print(err.messages)  # => {'quantity': ['Quantity must not be greater than 30.']}
```

You may also pass a collection (list, tuple, generator) of callables to `validate`.

Warning

Validation occurs on deserialization but not on serialization. To improve serialization performance, data passed to `Schema.dump` are considered valid.

See also

You can register a custom error handler function for a schema by overriding the `handle_error` method. See the Custom error handling page for more info.

See also

If you need to validate multiple fields within a single validator, see Schema-level validation.

See also

Need to *transform* a field’s value? Use the `pre_load` and `post_load` field parameters. See Field-level pre- and post-processing.

### Field validators as methods

It is sometimes convenient to write validators as methods. Use the `validates` decorator to register field validator methods.

```python
from marshmallow import fields, Schema, validates, ValidationError

class ItemSchema(Schema):
    quantity = fields.Integer()

    @validates("quantity")
    def validate_quantity(self, value: int, data_key: str) -> None:
        if value < 0:
            raise ValidationError("Quantity must be greater than 0.")
        if value > 30:
            raise ValidationError("Quantity must not be greater than 30.")
```

Note

You can pass multiple field names to the `validates` decorator.

```python
from marshmallow import Schema, fields, validates, ValidationError

class UserSchema(Schema):
    name = fields.Str(required=True)
    nickname = fields.Str(required=True)

    @validates("name", "nickname")
    def validate_names(self, value: str, data_key: str) -> None:
        if len(value) < 3:
            raise ValidationError("Too short")
```

## Required fields

Make a field required by passing `required=True`. An error will be raised if the the value is missing from the input to `Schema.load`.

To customize the error message for required fields, pass a `dict` with a `required` key as the `error_messages` argument for the field.

```python
from pprint import pprint

from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True, error_messages={"required": "Age is required."})
    city = fields.String(
        required=True,
        error_messages={"required": {"message": "City required", "code": 400}},
    )
    email = fields.Email()

try:
    result = UserSchema().load({"email": "foo@bar.com"})
except ValidationError as err:
    pprint(err.messages)
    # {'age': ['Age is required.'],
    # 'city': {'code': 400, 'message': 'City required'},
    # 'name': ['Missing data for required field.']}
```

## Partial loading

When using the same schema in multiple places, you may only want to skip `required` validation by passing `partial`.

```python
class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)

result = UserSchema().load({"age": 42}, partial=("name",))
# OR UserSchema(partial=('name',)).load({'age': 42})
print(result)  # => {'age': 42}
```

You can ignore missing fields entirely by setting `partial=True`.

```python
class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)

result = UserSchema().load({"age": 42}, partial=True)
# OR UserSchema(partial=True).load({'age': 42})
print(result)  # => {'age': 42}
```

## Specifying defaults

`load_default` specifies the default deserialization value for a field. Likewise, `dump_default` specifies the default serialization value.

```python
class UserSchema(Schema):
    id = fields.UUID(load_default=uuid.uuid1)
    birthdate = fields.DateTime(dump_default=dt.datetime(2017, 9, 29))

UserSchema().load({})
# {'id': UUID('337d946c-32cd-11e8-b475-0022192ed31b')}
UserSchema().dump({})
# {'birthdate': '2017-09-29T00:00:00+00:00'}
```

## Handling unknown fields

By default, `load` will raise a `ValidationError` if it encounters a key with no matching `Field` in the schema.

```python
from marshmallow import Schema, fields

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

UserSchema().load(
    {
        "name": "Monty",
        "email": "monty@python.org",
        "created_at": "2014-08-17T14:54:16.049594+00:00",
        "extra": "Not a field",
    }
)
# raises marshmallow.exceptions.ValidationError: {'extra': ['Unknown field.']}
```

This behavior can be modified with the `unknown` option, which accepts one of the following:

- `RAISE` (default): raise a `ValidationError` if there are any unknown fields
- `EXCLUDE`: exclude unknown fields
- `INCLUDE`: accept and include the unknown fields

You can specify `unknown` in the `class Meta` of your `Schema`,

```python
from pprint import pprint
from marshmallow import Schema, fields, INCLUDE

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    class Meta:
        unknown = INCLUDE

result = UserSchema().load(
    {
        "name": "Monty",
        "email": "monty@python.org",
        "created_at": "2014-08-17T14:54:16.049594+00:00",
        "extra": "Not a field",
    }
)
pprint(result)
# {'created_at': datetime.datetime(2014, 8, 17, 14, 54, 16, 49594, tzinfo=datetime.timezone(datetime.timedelta(0), '+0000')),
#  'email': 'monty@python.org',
#  'extra': 'Not a field',
#  'name': 'Monty'}
```

at instantiation time,

```python
schema = UserSchema(unknown=INCLUDE)
```

or when calling `load`.

```python
UserSchema().load(data, unknown=INCLUDE)
```

The `unknown` option value set in `load` will override the value applied at instantiation time, which itself will override the value defined in the `class Meta`.

This order of precedence allows you to change the behavior of a schema for different contexts.

## Validation without deserialization

If you only need to validate input data (without deserializing to an object), you can use `Schema.validate`.

```python
errors = UserSchema().validate({"name": "Ronnie", "email": "invalid-email"})
print(errors)  # {'email': ['Not a valid email address.']}
```

## “Read-only” and “write-only” fields

In the context of a web API, the `dump_only` and `load_only` parameters are conceptually equivalent to “read-only” and “write-only” fields, respectively.

```python
class UserSchema(Schema):
    name = fields.Str()
    # password is "write-only"
    password = fields.Str(load_only=True)
    # created_at is "read-only"
    created_at = fields.DateTime(dump_only=True)
```

Warning

When loading, dump-only fields are considered unknown. If the `unknown` option is set to `INCLUDE`, values with keys corresponding to those fields are therefore loaded with no validation.

## Specifying serialization/deserialization keys

Schemas will (de)serialize an input dictionary from/to an output dictionary whose keys are identical to the field names. If you are consuming and producing data that does not match your schema, you can specify the output keys via the `data_key` argument.

```python
class UserSchema(Schema):
    name = fields.String()
    email = fields.Email(data_key="emailAddress")

s = UserSchema()

data = {"name": "Mike", "email": "foo@bar.com"}
result = s.dump(data)
# {'name': u'Mike',
# 'emailAddress': 'foo@bar.com'}

data = {"name": "Mike", "emailAddress": "foo@bar.com"}
result = s.load(data)
# {'name': u'Mike',
# 'email': 'foo@bar.com'}
```

## Next steps

- Need to represent relationships between objects? See the Nesting schemas page.
- Want to create your own field type? See the Custom fields page.
- Need to add schema-level validation, post-processing, or error handling behavior? See the Extending schemas page.
- For more detailed usage examples, check out the Examples page.
