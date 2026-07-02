---
title: "Using factory_boy with ORMs"
source: https://factoryboy.readthedocs.io/en/stable/orms.html
domain: factory-boy
license: CC-BY-SA-4.0
tags: python factory boy, factory boy fixtures, test object factory python
fetched: 2026-07-02
---

# Using factory_boy with ORMs

factory_boy provides custom `Factory` subclasses for various ORMs, adding dedicated features.

## Django

The first versions of factory_boy were designed specifically for Django, but the library has now evolved to be framework-independent.

Most features should thus feel quite familiar to Django users.

### The `DjangoModelFactory` subclass

All factories for a Django `Model` should use the `DjangoModelFactory` base class.

***class*factory.django.DjangoModelFactory(*factory.Factory*)**

Dedicated class for Django `Model` factories.

This class provides the following features:

- The `model` attribute also supports the `'app.Model'` syntax
- `create()` uses `Model.objects.create()`
- When using `RelatedFactory` or `PostGeneration` attributes, the base object will be `saved` once all post-generation hooks have run.

***class*factory.django.DjangoOptions(*factory.base.FactoryOptions*)**

The `class Meta` on a `DjangoModelFactory` supports extra parameters:

**database**

Added in version 2.5.0.

All queries to the related model will be routed to the given database. It defaults to `'default'`.

**django_get_or_create**

Added in version 2.4.0.

Fields whose name are passed in this list will be used to perform a `Model.objects.get_or_create()` instead of the usual `Model.objects.create()`:

```python
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'myapp.User'  # Equivalent to ``model = myapp.models.User``
        django_get_or_create = ('username',)

    username = 'john'
```

```pycon
>>> User.objects.all()
[]
>>> UserFactory()                   # Creates a new user
<User: john>
>>> User.objects.all()
[<User: john>]

>>> UserFactory()                   # Fetches the existing user
<User: john>
>>> User.objects.all()              # No new user!
[<User: john>]

>>> UserFactory(username='jack')    # Creates another user
<User: jack>
>>> User.objects.all()
[<User: john>, <User: jack>]
```

Warning

When `django_get_or_create` is used, be aware that any new values passed to the Factory are **not** used to update an existing model.

```pycon
>>> john = UserFactory(username="john")   # Fetches the existing user
<User: john>

>>> john.email
"john@example.com"

>>> john = UserFactory(                   # Fetches the existing user
>>>     username="john",                  # and provides a new email value
>>>     email="a_new_email@example.com"
>>> )
<User: john>

>>> john.email                            # The email value was not updated
"john@example.com"
```

**skip_postgeneration_save**

Transitional option to prevent `DjangoModelFactory`’s `_after_postgeneration` from issuing a duplicate call to `save()` on the created instance when `factory.PostGeneration` hooks return a value.

### Extra fields

***class*factory.django.Password**

Applies `make_password()` to the clear-text argument before to generate the object.

**__init__(*self*, *password*)**

**Parameters:**

**password** (*str**or**None*) – Default password.

Note

When the `password` argument is `None`, the resulting password is unusable as if `set_unusable_password()` were used. This is distinct from setting the password to an empty string.

```python
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    password = factory.django.Password('pw')
```

```pycon
>>> from django.contrib.auth.hashers import check_password
>>> # Create user with the default password from the factory.
>>> user = UserFactory.create()
>>> check_password('pw', user.password)
True
>>> # Override user password at call time.
>>> other_user = UserFactory.create(password='other_pw')
>>> check_password('other_pw', other_user.password)
True
>>> # Set unusable password
>>> no_password_user = UserFactory.create(password=None)
>>> no_password_user.has_usable_password()
False
```

***class*factory.django.FileField**

Custom declarations for `django.db.models.FileField`

**__init__(*self*, *from_path=''*, *from_file=''*, *from_func=''*, *data=b''*, *filename='example.dat'*)**

**Parameters:**

- **from_path** (*str*) – Use data from the file located at `from_path`, and keep its filename
- **from_file** (*io.BytesIO*) – Use the contents of the provided file object; use its filename if available, unless `filename` is also provided.
- **from_func** (*Callable*) – Use function that returns a file object
- **data** (*bytes*) – Use the provided bytes as file contents
- **filename** (*str*) – The filename for the FileField

Note

If the value `None` was passed for the `FileField` field, this will disable field generation:

```python
class MyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.MyModel

    the_file = factory.django.FileField(filename='the_file.dat')
```

```pycon
>>> MyFactory(the_file__data=b'uhuh').the_file.read()
b'uhuh'
>>> MyFactory(the_file=None).the_file
None
```

***class*factory.django.ImageField**

Custom declarations for `django.db.models.ImageField`

**__init__(*self*, *from_path=''*, *from_file=''*, *from_func=''*, *filename='example.jpg'*, *width=100*, *height=100*, *color='green'*, *format='JPEG'*)**

**Parameters:**

- **from_path** (*str*) – Use data from the file located at `from_path`, and keep its filename
- **from_file** (*io.BytesIO*) – Use the contents of the provided file object; use its filename if available
- **from_func** (*Callable*) – Use function that returns a file object
- **filename** (*str*) – The filename for the ImageField
- **width** (*int*) – The width of the generated image (default: `100`)
- **height** (*int*) – The height of the generated image (default: `100`)
- **color** (*str*) – The color of the generated image (default: `'green'`)
- **format** (*str*) – The image format (as supported by PIL) (default: `'JPEG'`)
- **palette** (*str*) – The image palette (as supported by PIL) (default: `'RGB'`)

Note

If the value `None` was passed for the `ImageField` field, this will disable field generation:

Note

Just as Django’s `django.db.models.ImageField` requires the Python Imaging Library, this `ImageField` requires it too.

```python
class MyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.MyModel

    the_image = factory.django.ImageField(color='blue')
```

```pycon
>>> MyFactory(the_image__width=42).the_image.width
42
>>> MyFactory(the_image=None).the_image
None
```

### Disabling signals

Signals are often used to plug some custom code into external components code; for instance to create `Profile` objects on-the-fly when a new `User` object is saved.

This may interfere with finely tuned `factories`, which would create both using `RelatedFactory`.

To work around this problem, use the `mute_signals()` decorator/context manager:

**factory.django.mute_signals(*signal1*, *...*)**

Disable the list of selected signals when calling the factory, and reactivate them upon leaving.

```python
# foo/factories.py

import factory

from . import models
from . import signals

@factory.django.mute_signals(signals.pre_save, signals.post_save)
class FooFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Foo

    # ...

def make_chain():
    with factory.django.mute_signals(signals.pre_save, signals.post_save):
        # pre_save/post_save won't be called here.
        return SomeFactory(), SomeOtherFactory()
```

## Mogo

factory_boy supports Mogo-style models, through the `MogoFactory` class.

Mogo is a wrapper around the `pymongo` library for MongoDB.

***class*factory.mogo.MogoFactory(*factory.Factory*)[source]**

Dedicated class for Mogo models.

This class provides the following features:

- `build()` calls a model’s `new()` method
- `create()` builds an instance through `new()` then saves it.

## MongoEngine

factory_boy supports MongoEngine-style models, through the `MongoEngineFactory` class.

mongoengine is a wrapper around the `pymongo` library for MongoDB.

***class*factory.mongoengine.MongoEngineFactory(*factory.Factory*)[source]**

Dedicated class for MongoEngine models.

This class provides the following features:

- `build()` calls a model’s `__init__` method
- `create()` builds an instance through `__init__` then saves it.

Note

If the `associated class` is a `mongoengine.EmbeddedDocument`, the `MongoEngineFactory`’s `create` function won’t “save” it, since this wouldn’t make sense.

This feature makes it possible to use `SubFactory` to create embedded document.

A minimalist example:

```python
import mongoengine

class Address(mongoengine.EmbeddedDocument):
    street = mongoengine.StringField()

class Person(mongoengine.Document):
    name = mongoengine.StringField()
    address = mongoengine.EmbeddedDocumentField(Address)

import factory

class AddressFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Address

    street = factory.Sequence(lambda n: 'street%d' % n)

class PersonFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = Person

    name = factory.Sequence(lambda n: 'name%d' % n)
    address = factory.SubFactory(AddressFactory)
```

## SQLAlchemy

Factory_boy also supports SQLAlchemy models through the `SQLAlchemyModelFactory` class.

To work, this class needs an SQLAlchemy session object affected to the `Meta.sqlalchemy_session` attribute.

***class*factory.alchemy.SQLAlchemyModelFactory(*factory.Factory*)**

Dedicated class for SQLAlchemy models.

This class provides the following features:

- `create()` uses `sqlalchemy.orm.Session.add()`

***class*factory.alchemy.SQLAlchemyOptions(*factory.base.FactoryOptions*)**

In addition to the usual parameters available in `class Meta`, a `SQLAlchemyModelFactory` also supports the following settings:

**sqlalchemy_session**

SQLAlchemy session to use to communicate with the database when creating an object through this `SQLAlchemyModelFactory`.

**sqlalchemy_session_factory**

Added in version 3.3.0:

> `Callable` returning a `Session` instance to use to communicate with the database. You can either provide the session through this attribute, or through `sqlalchemy_session`, but not both at the same time.

```python
from . import common

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session_factory = lambda: common.Session()

    username = 'john'
```

**sqlalchemy_session_persistence**

Control the action taken by `sqlalchemy_session` at the end of a create call.

Valid values are:

- `None`: do nothing
- `'flush'`: perform a session `flush()`
- `'commit'`: perform a session `commit()`

The default value is `None`.

**sqlalchemy_get_or_create**

Added in version 3.0.0.

Fields whose name are passed in this list will be used to perform a `Model.query.one_or_none()` or the usual `Session.add()`:

```python
class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = session
        sqlalchemy_get_or_create = ('username',)

    username = 'john'
```

```pycon
>>> User.query.all()
[]
>>> UserFactory()                   # Creates a new user
<User: john>
>>> User.query.all()
[<User: john>]

>>> UserFactory()                   # Fetches the existing user
<User: john>
>>> User.query.all()                # No new user!
[<User: john>]

>>> UserFactory(username='jack')    # Creates another user
<User: jack>
>>> User.query.all()
[<User: john>, <User: jack>]
```

Warning

When `sqlalchemy_get_or_create` is used, be aware that any new values passed to the Factory are **not** used to update an existing model.

```pycon
>>> john = UserFactory(username="john")   # Fetches the existing user
<User: john>

>>> john.email
"john@example.com"

>>> john = UserFactory(                   # Fetches the existing user
>>>     username="john",                  # and provides a new email value
>>>     email="a_new_email@example.com"
>>> )
<User: john>

>>> john.email                            # The email value was not updated
"john@example.com"
```

A (very) simple example:

```python
from sqlalchemy import Column, Integer, Unicode, create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

engine = create_engine('sqlite://')
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

class User(Base):
    """ A SQLAlchemy simple model class who represents a user """
    __tablename__ = 'UserTable'

    id = Column(Integer(), primary_key=True)
    name = Column(Unicode(20))

Base.metadata.create_all(engine)

import factory

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = session   # the SQLAlchemy session object

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: 'User %d' % n)
```

```pycon
>>> session.query(User).all()
[]
>>> UserFactory()
<User: User 0>
>>> session.query(User).all()
[<User: User 0>]
```

### Managing sessions

Since SQLAlchemy is a general purpose library, there is no “global” session management system.

The most common pattern when working with unit tests and `factory_boy` is to use SQLAlchemy’s `sqlalchemy.orm.scoping.scoped_session`:

- The test runner configures some project-wide `scoped_session`
- Each `SQLAlchemyModelFactory` subclass uses this `scoped_session` as its `sqlalchemy_session`
- The `tearDown()` method of tests calls `Session.remove` to reset the session.

Note

See the excellent SQLAlchemy guide on scoped_session for details of `scoped_session`’s usage.

The basic idea is that declarative parts of the code (including factories) need a simple way to access the “current session”, but that session will only be created and configured at a later point.

The `scoped_session` handles this, by virtue of only creating the session when a query is sent to the database.

Here is an example layout:

- A global (test-only?) file holds the `scoped_session`:

```python
# myproject/test/common.py

from sqlalchemy import orm
Session = orm.scoped_session(orm.sessionmaker())
```

- All factory access it:

```python
# myproject/factories.py

import factory

from . import models
from .test import common

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.User

        # Use the not-so-global scoped_session
        # Warning: DO NOT USE common.Session()!
        sqlalchemy_session = common.Session

    name = factory.Sequence(lambda n: "User %d" % n)
```

- The test runner configures the `scoped_session` when it starts:

```python
# myproject/test/runtests.py

import sqlalchemy

from . import common

def runtests():
    engine = sqlalchemy.create_engine('sqlite://')

    # It's a scoped_session, and now is the time to configure it.
    common.Session.configure(bind=engine)

    run_the_tests
```

- `test cases` use this `scoped_session`, and clear it after each test (for isolation):

```python
# myproject/test/test_stuff.py

import unittest

from . import common

class MyTest(unittest.TestCase):

    def setUp(self):
        # Prepare a new, clean session
        self.session = common.Session()

    def test_something(self):
        u = factories.UserFactory()
        self.assertEqual([u], self.session.query(User).all())

    def tearDown(self):
        # Rollback the session => no changes to the database
        self.session.rollback()
        # Remove it, so that the next test gets a new Session()
        common.Session.remove()
```
