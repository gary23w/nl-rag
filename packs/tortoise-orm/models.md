---
title: "Models"
source: https://tortoise.github.io/models.html
domain: tortoise-orm
license: CC-BY-SA-4.0
tags: python tortoise orm, async orm python, tortoise models
fetched: 2026-07-02
---

# Models

## Usage

All models should be derived from `Model`. To start describing the models, import `Model` from `tortoise.models`.

```python3
from tortoise.models import Model
```

With that start describing the models

```python3
class Tournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    tournament = fields.ForeignKeyField('models.Tournament', related_name='events')
    participants = fields.ManyToManyField('models.Team', related_name='events', through='event_team')
    modified = fields.DatetimeField(auto_now=True)
    prize = fields.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name

class Team(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()

    def __str__(self):
        return self.name
```

Let’s look at the details of what we accomplished here:

```python3
class Tournament(Model):
```

Every model should be derived from `Model` or its subclasses. Custom `Model` subclasses can be created in the following way:

```python3
class AbstractTournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    created = fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
```

This model will not affect the schema, but it will be available for inheritance.

Further we have field `fields.DatetimeField(auto_now=True)`. Options `auto_now` and `auto_now_add` work like Django’s options — they are handled purely in Python and do **not** add a `DEFAULT` clause to the database schema. If you need a database-level default timestamp, use `db_default`:

```python3
from tortoise.fields import DatetimeField, Now

class MyModel(Model):
    # Python-only: value set by ORM on save, no DB DEFAULT
    modified = DatetimeField(auto_now=True)

    # DB-level: emits DEFAULT CURRENT_TIMESTAMP in the schema
    created_at = DatetimeField(db_default=Now())
```

### Use of `__models__`

If you define the variable `__models__` in the module which you load your models from, `generate_schema` will use that list, rather than automatically finding models for you.

### Primary Keys

In Tortoise ORM, every model must have a primary key.

That primary key will be accessible through a reserved field `pk` which will be an alias of whichever field has been nominated as a primary key. That alias field can be used as a field name when doing filtering e.g. `.filter(pk=...)` etc…

Note

We currently support single (non-composite) primary keys of any indexable field type, but only these field types are recommended:

```python3
IntField
BigIntField
CharField
UUIDField
```

One must define a primary key by setting the `primary_key` parameter to `True`. If you don’t define a primary key, the primary key will be generated as an `IntField` with name of `id`.

Note

If this is used on an Integer Field, `generated` will be set to `True` unless you explicitly pass `generated=False` as well.

Any of these are valid primary key definitions:

```python3
id = fields.IntField(primary_key=True)

checksum = fields.CharField(primary_key=True)

guid = fields.UUIDField(primary_key=True)
```

### Inheritance

When defining models in Tortoise ORM, you can save a lot of repetitive work by leveraging from inheritance.

You can define fields in more generic classes and they are automatically available in derived classes. Base classes are not limited to Model classes. Any class will work. This way you are able to define your models in a natural and easy to maintain way.

Let’s have a look at some examples.

```python3
from tortoise import fields
from tortoise.models import Model

class TimestampMixin():
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    modified_at = fields.DatetimeField(null=True, auto_now=True)

class NameMixin():
    name = fields.CharField(40, unique=True)

class MyAbstractBaseModel(Model):
    id = fields.IntField(primary_key=True)

    class Meta:
        abstract = True

class UserModel(TimestampMixin, MyAbstractBaseModel):
    # Overriding the id definition
    # from MyAbstractBaseModel
    id = fields.UUIDField(primary_key=True)

    # Adding additional fields
    first_name = fields.CharField(20, null=True)

    class Meta:
        table = "user"

class RoleModel(TimestampMixin, NameMixin, MyAbstractBaseModel):

    class Meta:
        table = "role"
```

Using the `Meta` class is not necessary. But it is a good habit, to give your table an explicit name. This way you can change the model name without breaking the schema. So the following definition is valid.

```python3
class RoleModel(TimestampMixin, NameMixin, MyAbstractBaseModel):
    pass
```

### The `Meta` class

***class*tortoise.models.Model.Meta**

The `Meta` class is used to configure metadata for the Model.

Usage:

```python3
class Foo(Model):
    ...

    class Meta:
        table="custom_table"
        unique_together=(("field_a", "field_b"), )
```

**abstract*= False***

Set to `True` to indicate this is an abstract class

**schema*= ""***

Set this to configure a schema name, where table exists

**table*= ""***

Set this to configure a manual table name, instead of a generated one

**table_description*= ""***

Set this to generate a comment message for the table being created for the current model

**unique_together*= None***

Specify `unique_together` to set up compound unique indexes for sets of columns.

It should be a tuple of tuples (lists are fine) in the format of:

```python3
unique_together=("field_a", "field_b")
unique_together=(("field_a", "field_b"), )
unique_together=(("field_a", "field_b"), ("field_c", "field_d", "field_e"))
```

**indexes*= None***

Specify `indexes` to set up compound non-unique indexes for sets of columns.

It should be a tuple of tuples (lists are fine) in the format of:

```python3
indexes=("field_a", "field_b")
indexes=(("field_a", "field_b"), )
indexes=(("field_a", "field_b"), ("field_c", "field_d", "field_e"))
```

**constraints*= None***

Specify `constraints` to add named database constraints to the model. Supports `UniqueConstraint` and `CheckConstraint` objects, which are tracked by the migration autodetector and generate `AddConstraint`, `RemoveConstraint`, and `RenameConstraint` operations automatically.

```python3
from tortoise.migrations.constraints import CheckConstraint, UniqueConstraint

class MyModel(Model):
    name = fields.CharField(max_length=100)
    category = fields.CharField(max_length=50)
    score = fields.IntField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=("name", "category"), name="uid_name_category"),
            CheckConstraint(check="score >= 0", name="chk_score_positive"),
        ]
```

`UniqueConstraint` accepts:

- `fields` — tuple of field names (resolved to DB column names, including FK fields).
- `name` — explicit constraint name. Required for migration tracking.
- `condition` — *(PostgreSQL only)* a SQL `WHERE` clause for partial unique indexes.

`CheckConstraint` accepts:

- `check` — a raw SQL expression for the `CHECK (...)` clause.
- `name` — explicit constraint name. Required.

Note

`unique_together` is the legacy way to define compound unique indexes. `constraints` with `UniqueConstraint` objects is preferred for new code, as it supports explicit naming, partial indexes (PostgreSQL), and is handled by the migration framework.

**ordering*= None***

Specify `ordering` to set up default ordering for given model. It should be iterable of strings formatted in same way as `.order_by(...)` receives. If query is built with `GROUP_BY` clause using `.annotate(...)` default ordering is not applied.

```python3
ordering = ["name", "-score"]
```

**fetch_db_defaults*= True***

When `True` (the default), after an INSERT on a non-RETURNING backend (e.g. MySQL), Tortoise will issue a follow-up `SELECT` to fetch database-applied default values for fields declared with `db_default`.

Set to `False` to skip the extra query when you don’t need the database-generated values back on the Python instance immediately. On RETURNING backends (PostgreSQL, SQLite) the values are always returned in the INSERT response regardless of this setting.

```python3
class MyModel(Model):
    score = fields.IntField(db_default=0)

    class Meta:
        fetch_db_defaults = False
```

**manager*= tortoise.manager.Manager***

Specify `manager` to override the default manager. It should be instance of `tortoise.manager.Manager` or subclass.

```python3
manager = CustomManager()
```

### `ForeignKeyField`

```python3
tournament = fields.ForeignKeyField('models.Tournament', related_name='events')
participants = fields.ManyToManyField('models.Team', related_name='events')
modified = fields.DatetimeField(auto_now=True)
prize = fields.DecimalField(max_digits=10, decimal_places=2, null=True)
```

In event model we got some more fields, that could be interesting for us.

**`fields.ForeignKeyField('models.Tournament', related_name='events')`**

Here we create foreign key reference to tournament. You can refer to the model either by string literal (`"app_name.ModelName"`) or by passing the model class directly (e.g. `fields.ForeignKeyField(Tournament)`). String references are required for forward references where the target model is not yet defined. `models` is default app name, but you can change it in `class Meta` with `app = 'other'`.

**`related_name`**

Is keyword argument, that defines field for related query on referenced models, so with that you could fetch all tournaments’s events with like this:

```python3
await Tournament.first().prefetch_related("events")
```

#### The DB-backing field

Note

A `ForeignKeyField` is a virtual field, meaning it has no direct DB backing. Instead it has a field (by default called `*FKNAME*_id` (that is, just an `_id` is appended) that is the actual DB-backing field.

It will just contain the Key value of the related table.

This is an important detail as it would allow one to assign/read the actual value directly, which could be considered an optimization if the entire foreign object isn’t needed.

Specifying an FK can be done via either passing the object:

```python3
await SomeModel.create(tournament=the_tournament)
# or
somemodel.tournament=the_tournament
```

or by directly accessing the DB-backing field:

```python3
await SomeModel.create(tournament_id=the_tournament.pk)
# or
somemodel.tournament_id=the_tournament.pk
```

Querying a relationship is typically done by appending a double underscore, and then the foreign object’s field. Then a normal query attr can be appended. This can be chained if the next key is also a foreign object:

> `*FKNAME*__*FOREIGNFIELD*__gt=3`
> 
> or
> 
> `*FKNAME*__*FOREIGNFK*__*VERYFOREIGNFIELD*__gt=3`

There is however one major limitation. We don’t want to restrict foreign column names, or have ambiguity (e.g. a foreign object may have a field called `isnull`)

Then this would be entirely ambiguous:

> `*FKNAME*__isnull`

To prevent that we require that direct filters be applied to the DB-backing field of the foreign key:

> `*FKNAME*_id__isnull`

#### Fetching the foreign object

Fetching foreign keys can be done with both async and sync interfaces.

Async fetch:

```python3
events = await tournament.events.all()
```

You can async iterate over it like this:

```python3
async for event in tournament.events:
    ...
```

Sync usage requires that you call *fetch_related* before the time, and then you can use common functions such as:

```python3
await tournament.fetch_related('events')
events = list(tournament.events)
eventlen = len(tournament.events)
if SomeEvent in tournament.events:
    ...
if tournament.events:
    ...
firstevent = tournament.events[0]
```

To get the Reverse-FK, e.g. an *event.tournament* we currently only support the sync interface.

```python3
await event.fetch_related('tournament')
tournament = event.tournament
```

### `ManyToManyField`

Next field is `fields.ManyToManyField('models.Team', related_name='events')`. It describes many to many relation to model Team.

To add to a `ManyToManyField` both the models need to be saved, else you will get an `OperationalError` raised.

Resolving many to many fields can be done with both async and sync interfaces.

Async fetch:

```python3
participants = await tournament.participants.all()
```

You can async iterate over it like this:

```python3
async for participant in tournament.participants:
    ...
```

Sync usage requires that you call *fetch_related* before the time, and then you can use common functions such as:

```python3
await tournament.fetch_related('participants')
participants = list(tournament.participants)
participantlen = len(tournament.participants)
if SomeParticipant in tournament.participants:
    ...
if tournament.participants:
    ...
firstparticipant = tournament.participants[0]
```

The reverse lookup of `team.event_team` works exactly the same way.

## Improving relational type hinting

Since Tortoise ORM is still a young project, it does not have such widespread support by various editors who help you writing code using good autocomplete for models and different relations between them. However, you can get such autocomplete by doing a little work yourself. All you need to do is add a few annotations to your models for fields that are responsible for the relations.

Here is an updated example from Getting started, that will add autocomplete for all models including fields for the relations between models.

```python3
from tortoise.models import Model
from tortoise import fields

class Tournament(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)

    events: fields.ReverseRelation["Event"]

    def __str__(self):
        return self.name

class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
        "models.Tournament", related_name="events"
    )
    participants: fields.ManyToManyRelation["Team"] = fields.ManyToManyField(
        "models.Team", related_name="events", through="event_team"
    )

    def __str__(self):
        return self.name

class Team(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)

    events: fields.ManyToManyRelation[Event]

    def __str__(self):
        return self.name
```

## Reference

***class*tortoise.models.Model(***kwargs*)[source]**

Base class for all Tortoise ORM Models.

***class*Meta[source]**

The `Meta` class is used to configure metadata for the Model.

Usage:

```python3
class Foo(Model):
    ...

    class Meta:
        table="custom_table"
        unique_together=(("field_a", "field_b"), )
```

***classmethod*all(*using_db=`None`*)[source]**

Returns the complete QuerySet.

**Return type:**

QuerySet[Self]

***classmethod*annotate(***kwargs*)[source]**

Annotates the result set with extra Functions/Aggregations/Expressions.

**Parameters:**

**kwargs : Expression | Term**

Parameter name and the Function/Aggregation to annotate with.

**Return type:**

QuerySet[Self]

***classmethod*bulk_create(*objects*, *batch_size=`None`*, *ignore_conflicts=`False`*, *update_fields=`None`*, *on_conflict=`None`*, *using_db=`None`*)[source]**

Bulk insert operation:

Note

The bulk insert operation will do the minimum to ensure that the object created in the DB has all the defaults and generated fields set, but may be incomplete reference in Python.

e.g. `IntField` primary keys will not be populated.

This is recommended only for throw away inserts where you want to ensure optimal insert performance.

```python3
User.bulk_create([
    User(name="...", email="..."),
    User(name="...", email="...")
])
```

**db_default behaviour:** Fields with `db_default` that are not explicitly set will use the database DEFAULT. However, within a single `bulk_create` call, each `db_default` field must be treated consistently across *all* instances — either every instance provides an explicit value, or none of them do. Mixing explicit values and database defaults for the same field raises `OperationalError`.

**Parameters:**

**on_conflict=`None`**

On conflict index name

**update_fields=`None`**

Update fields when conflicts

**ignore_conflicts=`False`**

Ignore conflicts when inserting

**objects**

List of objects to bulk create

**batch_size=`None`**

How many objects are created in a single query

**using_db=`None`**

Specific DB connection to use instead of default bound

**Raises:**

**OperationalError** – If a `db_default` field has mixed usage across instances (some provide a value, others rely on the database default).

**Return type:**

`BulkCreateQuery`[Model]

***classmethod*bulk_update(*objects*, *fields*, *batch_size=`None`*, *using_db=`None`*)[source]**

Update the given fields in each of the given objects in the database. This method efficiently updates the given fields on the provided model instances, generally with one query.

```python3
users = [
    await User.create(name="...", email="..."),
    await User.create(name="...", email="...")
]
users[0].name = 'name1'
users[1].name = 'name2'

await User.bulk_update(users, fields=['name'])
```

**Parameters:**

**objects**

List of objects to bulk create

**fields**

The fields to update

**batch_size=`None`**

How many objects are created in a single query

**using_db=`None`**

Specific DB connection to use instead of default bound

**Return type:**

`BulkUpdateQuery`[Model]

**clone(*pk=<object object>*)[source]**

Create a new clone of the object that when you do a `.save()` will create a new record.

**Parameters:**

**pk : `Any`**

An optionally required value if the model doesn’t generate its own primary key. Any value you specify here will always be used.

**Return type:**

Model

**Returns:**

A copy of the current object without primary key information.

**Raises:**

**ParamsError** – If pk is required but not provided.

***classmethod*construct(*_saved_in_db=`False`*, ***kwargs*)[source]**

Create a model instance without validation, DB checks, or FK restrictions.

This creates a “detached” instance that has the right shape for reading attributes and iterating relations, but is not part of the ORM lifecycle. Useful for unit testing and serialization without a database connection.

Unlike `__init__`, this method: - Does NOT validate field values (nullability, type checks) - Does NOT require FK objects to be saved to the database - Does NOT prevent setting backward FK, backward O2O, or M2M fields - Does NOT call `to_python_value` on data fields - Skips async defaults (sets them to `None`)

Backward FK and M2M fields are wrapped in `ReverseRelation` and `ManyToManyRelation` respectively with `_fetched=True` so that iteration, `len()`, `in`, and `bool()` work without raising `NoValuesFetched`.

Example:

```
tournament = Tournament.construct(id=1, name="Test")
event = Event.construct(
    name="Game",
    tournament=tournament,
    participants=[
        Team.construct(id=1, name="Team A"),
        Team.construct(id=2, name="Team B"),
    ],
)
assert event.tournament.name == "Test"
assert event.tournament_id == 1
assert len(event.participants) == 2
```

**Parameters:**

**_saved_in_db=`False`**

Whether to mark the instance as saved in DB. Defaults to `False`.

****kwargs**

Field values to set on the instance.

**Return type:**

Model

**Returns:**

A new model instance with the given field values.

***async classmethod*create(*using_db=`None`*, ***kwargs*)[source]**

Create a record in the DB and returns the object.

```python3
user = await User.create(name="...", email="...")
```

Equivalent to:

```python3
user = User(name="...", email="...")
await user.save()
```

**Parameters:**

**using_db=`None`**

Specific DB connection to use instead of default bound

****kwargs**

Model parameters.

**Return type:**

Model

***async*delete(*using_db=`None`*)[source]**

Deletes the current model object.

**Parameters:**

**using_db=`None`**

Specific DB connection to use instead of default bound

**Raises:**

**OperationalError** – If object has never been persisted.

**Return type:**

`None`

***classmethod*describe(*serializable=`True`*)[source]**

Describes the given list of models or ALL registered models.

**Parameters:**

**serializable=`True`**

`False` if you want raw python objects, `True` for JSON-serializable data. (Defaults to `True`)

**Return type:**

`dict`

**Returns:**

A dictionary containing the model description.

The base dict has a fixed set of keys that reference a list of fields (or a single field in the case of the primary key):

```python3
{
    "name":                 str     # Qualified model name
    "app":                  str     # 'App' namespace
    "table":                str     # DB table name
    "abstract":             bool    # Is the model Abstract?
    "description":          str     # Description of table (nullable)
    "docstring":            str     # Model docstring (nullable)
    "unique_together":      [...]   # List of List containing field names that
                                    #  are unique together
    "pk_field":             {...}   # Primary key field
    "data_fields":          [...]   # Data fields
    "fk_fields":            [...]   # Foreign Key fields FROM this model
    "backward_fk_fields":   [...]   # Foreign Key fields TO this model
    "o2o_fields":           [...]   # OneToOne fields FROM this model
    "backward_o2o_fields":  [...]   # OneToOne fields TO this model
    "m2m_fields":           [...]   # Many-to-Many fields
}
```

Each field is specified as defined in `tortoise.fields.base.Field.describe()`

***classmethod*earliest(**orderings*)[source]**

Generates a QuerySet with the filter applied that returns the first record.

**Params orderings:**

Fields to order by.

**Return type:**

QuerySetSingle[Self | None]

***classmethod*exclude(**args*, ***kwargs*)[source]**

Generates a QuerySet with the exclude applied.

**Parameters:**

**args : Q**

Q functions containing constraints. Will be AND’ed.

**kwargs : Any**

Simple filter constraints.

**Return type:**

QuerySet[Self]

***classmethod*exists(**args*, *using_db=`None`*, ***kwargs*)[source]**

Return True/False whether record exists with the provided filter parameters.

```python3
result = await User.exists(username="foo")
```

**Parameters:**

**using_db=`None`**

The specific DB connection to use.

***args**

Q functions containing constraints. Will be AND’ed.

****kwargs**

Simple filter constraints.

**Return type:**

`ExistsQuery`

***async classmethod*fetch_for_list(*instance_list*, **args*, *using_db=`None`*)[source]**

Fetches related models for provided list of Model objects.

**Parameters:**

**instance_list**

List of Model objects to fetch relations for.

***args**

Relation names to fetch.

**using_db=`None`**

DO NOT USE

**Return type:**

`None`

Fetch related fields.

```python3
User.fetch_related("emails", "manager")
```

***args**

The related fields that should be fetched.

**using_db=`None`**

Specific DB connection to use instead of default bound

`None`

***classmethod*filter(**args*, ***kwargs*)[source]**

Generates a QuerySet with the filter applied.

**Parameters:**

**args : Q**

Q functions containing constraints. Will be AND’ed.

**kwargs : Any**

Simple filter constraints.

**Return type:**

QuerySet[Self]

***classmethod*first(*using_db=`None`*)[source]**

Generates a QuerySet that returns the first record.

**Return type:**

QuerySetSingle[Self | None]

***classmethod*get(**args*, *using_db=`None`*, ***kwargs*)[source]**

Fetches a single record for a Model type using the provided filter parameters.

```python3
user = await User.get(username="foo")
```

**Parameters:**

**using_db : BaseDBAsyncClient | None**

The DB connection to use

**args : Q**

Q functions containing constraints. Will be AND’ed.

**kwargs : Any**

Simple filter constraints.

**Raises:**

- **MultipleObjectsReturned** – If provided search returned more than one object.
- **DoesNotExist** – If object can not be found.

**Return type:**

QuerySetSingle[Self]

***async classmethod*get_or_create(*defaults=`None`*, *using_db=`None`*, ***kwargs*)[source]**

Fetches the object if exists (filtering on the provided parameters), else creates an instance with any unspecified parameters as default values.

**Parameters:**

**defaults : dict | None**

Default values to be added to a created instance if it can’t be fetched.

**using_db : BaseDBAsyncClient | None**

Specific DB connection to use instead of default bound

**kwargs : Any**

Query parameters.

**Raises:**

- **IntegrityError** – If create failed
- **TransactionManagementError** – If transaction error
- **ParamsError** – If defaults conflict with kwargs

**Return type:**

tuple[Self, bool]

***classmethod*get_or_none(**args*, *using_db=`None`*, ***kwargs*)[source]**

Fetches a single record for a Model type using the provided filter parameters or None.

```python3
user = await User.get_or_none(username="foo")
```

**Parameters:**

**using_db : BaseDBAsyncClient | None**

The specific DB connection to use.

**args : Q**

Q functions containing constraints. Will be AND’ed.

**kwargs : Any**

Simple filter constraints.

**Return type:**

QuerySetSingle[Self | None]

***classmethod*get_table()[source]**

Return a PyPika table for this model.

**Return type:**

`Table`

***async classmethod*in_bulk(*id_list*, *field_name=`'pk'`*, *using_db=`None`*)[source]**

Return a dictionary mapping each of the given IDs to the object with that ID. If *id_list* isn’t provided, evaluate the entire QuerySet.

**Parameters:**

**id_list**

A list of field values

**field_name=`'pk'`**

Must be a unique field

**using_db=`None`**

Specific DB connection to use instead of default bound

**Return type:**

`dict`

***classmethod*last(*using_db=`None`*)[source]**

Generates a QuerySet that returns the last record.

**Return type:**

QuerySetSingle[Self | None]

***classmethod*latest(**orderings*)[source]**

Generates a QuerySet with the filter applied that returns the last record.

**Params orderings:**

Fields to order by.

**Return type:**

QuerySetSingle[Self | None]

***property*pk : Any**

Alias to the models Primary Key. Can be used as a field name when doing filtering e.g. `.filter(pk=...)` etc…

**Return type:**

`Any`

***classmethod*raw(*sql*, *using_db=`None`*)[source]**

Executes a RAW SQL and returns the result

```python3
result = await User.raw("select * from users where name like '%test%'")
```

**Parameters:**

**using_db=`None`**

The specific DB connection to use

**sql**

The raw sql.

**Return type:**

`RawSQLQuery`

***async*refresh_from_db(*fields=`None`*, *using_db=`None`*)[source]**

Refresh latest data from db. When this method is called without arguments all db fields of the model are updated to the values currently present in the database.

```python3
user.refresh_from_db(fields=['name'])
```

**Parameters:**

**fields=`None`**

The special fields that to be refreshed.

**using_db=`None`**

Specific DB connection to use instead of default bound.

**Raises:**

**OperationalError** – If object has never been persisted.

**Return type:**

`None`

***classmethod*register_listener(*signal*, *listener*)[source]**

Register listener to current model class for special Signal.

**Parameters:**

**signal**

one of tortoise.signals.Signals

**listener**

callable listener

**Raises:**

**ConfigurationError** – When listener is not callable

**Return type:**

`None`

***async*save(*using_db=`None`*, *update_fields=`None`*, *force_create=`False`*, *force_update=`False`*)[source]**

Creates/Updates the current model object.

**Parameters:**

**update_fields=`None`**

If provided, it should be a tuple/list of fields by name.

This is the subset of fields that should be updated. If the object needs to be created `update_fields` will be ignored.

**using_db=`None`**

Specific DB connection to use instead of default bound

**force_create=`False`**

Forces creation of the record

**force_update=`False`**

Forces updating of the record

**Raises:**

- **IncompleteInstanceError** – If the model is partial and the fields are not available for persistence.
- **IntegrityError** – If the model can’t be created or updated (specifically if force_create or force_update has been set)
- **OperationalError** – If update_fields include pk field.

**Return type:**

`None`

***classmethod*select_for_update(*nowait=`False`*, *skip_locked=`False`*, *of=`()`*, *using_db=`None`*, *no_key=`False`*)[source]**

Make QuerySet select for update.

Returns a queryset that will lock rows until the end of the transaction, generating a SELECT … FOR UPDATE SQL statement on supported databases.

**Return type:**

QuerySet[Self]

**update_from_dict(*data*)[source]**

Updates the current model with the provided dict. This can allow mass-updating a model from a dict, also ensuring that datatype conversions happen.

This will ignore any extra fields, and NOT update the model with them, but will raise errors on bad types or updating Many-instance relations.

**Parameters:**

**data**

The parameters you want to update in a dict format

**Return type:**

Model

**Returns:**

The current model instance

**Raises:**

- **ConfigurationError** – When attempting to update a remote instance (e.g. a reverse ForeignKey or ManyToMany relation)
- **ValueError** – When a passed parameter is not type compatible

***async classmethod*update_or_create(*defaults=`None`*, *using_db=`None`*, ***kwargs*)[source]**

A convenience method for updating an object with the given kwargs, creating a new one if necessary.

**Parameters:**

**defaults=`None`**

Default values used to update the object.

**using_db=`None`**

Specific DB connection to use instead of default bound

****kwargs**

Query parameters.

**Return type:**

`tuple`
