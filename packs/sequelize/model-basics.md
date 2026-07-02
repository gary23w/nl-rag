---
title: "Model Basics"
source: https://www.sequelize.org/docs/v6/core-concepts/model-basics/
domain: sequelize
license: CC-BY-SA-4.0
tags: sequelize orm, node.js orm, javascript orm, model definition
fetched: 2026-07-02
---

# Model Basics

Version: v6 - stable

# Model Basics

In this tutorial you will learn what models are in Sequelize and how to use them.

## Concept

Models are the essence of Sequelize. A model is an abstraction that represents a table in your database. In Sequelize, it is a class that extends Model.

The model tells Sequelize several things about the entity it represents, such as the name of the table in the database and which columns it has (and their data types).

A model in Sequelize has a name. This name does not have to be the same name of the table it represents in the database. Usually, models have singular names (such as `User`) while tables have pluralized names (such as `Users`), although this is fully configurable.

## Model Definition

Models can be defined in two equivalent ways in Sequelize:

- Calling `sequelize.define(modelName, attributes, options)`
- Extending Model and calling `init(attributes, options)`

After a model is defined, it is available within `sequelize.models` by its model name.

To learn with an example, we will consider that we want to create a model to represent users, which have a `firstName` and a `lastName`. We want our model to be called `User`, and the table it represents is called `Users` in the database.

Both ways to define this model are shown below. After being defined, we can access our model with `sequelize.models.User`.

### Using `sequelize.define`:

```js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

const User = sequelize.define(
  'User',
  {
    
    firstName: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    lastName: {
      type: DataTypes.STRING,
      
    },
  },
  {
    
  },
);

console.log(User === sequelize.models.User); 
```

### Extending Model

```js
const { Sequelize, DataTypes, Model } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

class User extends Model {}

User.init(
  {
    
    firstName: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    lastName: {
      type: DataTypes.STRING,
      
    },
  },
  {
    
    sequelize, 
    modelName: 'User', 
  },
);

console.log(User === sequelize.models.User); 
```

Internally, `sequelize.define` calls `Model.init`, so both approaches are essentially equivalent.

#### Caveat with Public Class Fields

Adding a Public Class Field with the same name as one of the model's attribute is going to cause issues. Sequelize adds a getter & a setter for each attribute defined through `Model.init`. Adding a Public Class Field will shadow those getter and setters, blocking access to the model's actual data.

```typescript
class User extends Model {
  id; 
  otherPublicField; 
}

User.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
  },
  { sequelize },
);

const user = new User({ id: 1 });
user.id; 
```

```typescript
class User extends Model {
  otherPublicField;
}

User.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
  },
  { sequelize },
);

const user = new User({ id: 1 });
user.id; 
```

In TypeScript, you can add typing information without adding an actual public class field by using the `declare` keyword:

```typescript
class User extends Model {
  declare id: number; 
}

User.init(
  {
    id: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
  },
  { sequelize },
);

const user = new User({ id: 1 });
user.id; 
```

## Table name inference

Observe that, in both methods above, the table name (`Users`) was never explicitly defined. However, the model name was given (`User`).

By default, when the table name is not given, Sequelize automatically pluralizes the model name and uses that as the table name. This pluralization is done under the hood by a library called inflection, so that irregular plurals (such as `person -> people`) are computed correctly.

Of course, this behavior is easily configurable.

### Enforcing the table name to be equal to the model name

You can stop the auto-pluralization performed by Sequelize using the `freezeTableName: true` option. This way, Sequelize will infer the table name to be equal to the model name, without any modifications:

```js
sequelize.define(
  'User',
  {
    
  },
  {
    freezeTableName: true,
  },
);
```

The example above will create a model named `User` pointing to a table also named `User`.

This behavior can also be defined globally for the sequelize instance, when it is created:

```js
const sequelize = new Sequelize('sqlite::memory:', {
  define: {
    freezeTableName: true,
  },
});
```

This way, all tables will use the same name as the model name.

### Providing the table name directly

You can simply tell Sequelize the name of the table directly as well:

```js
sequelize.define(
  'User',
  {
    
  },
  {
    tableName: 'Employees',
  },
);
```

## Model synchronization

When you define a model, you're telling Sequelize a few things about its table in the database. However, what if the table actually doesn't even exist in the database? What if it exists, but it has different columns, less columns, or any other difference?

This is where model synchronization comes in. A model can be synchronized with the database by calling `model.sync(options)`, an asynchronous function (that returns a Promise). With this call, Sequelize will automatically perform an SQL query to the database. Note that this changes only the table in the database, not the model in the JavaScript side.

- `User.sync()` - This creates the table if it doesn't exist (and does nothing if it already exists)
- `User.sync({ force: true })` - This creates the table, dropping it first if it already existed
- `User.sync({ alter: true })` - This checks what is the current state of the table in the database (which columns it has, what are their data types, etc), and then performs the necessary changes in the table to make it match the model.

Example:

```js
await User.sync({ force: true });
console.log('The table for the User model was just (re)created!');
```

### Synchronizing all models at once

You can use `sequelize.sync()` to automatically synchronize all models. Example:

```js
await sequelize.sync({ force: true });
console.log('All models were synchronized successfully.');
```

### Dropping tables

To drop the table related to a model:

```js
await User.drop();
console.log('User table dropped!');
```

To drop all tables:

```js
await sequelize.drop();
console.log('All tables dropped!');
```

### Database safety check

As shown above, the `sync` and `drop` operations are destructive. Sequelize accepts a `match` option as an additional safety check, which receives a RegExp:

```js
sequelize.sync({ force: true, match: /_test$/ });
```

### Synchronization in production

As shown above, `sync({ force: true })` and `sync({ alter: true })` can be destructive operations. Therefore, they are not recommended for production-level software. Instead, synchronization should be done with the advanced concept of Migrations, with the help of the Sequelize CLI.

## Timestamps

By default, Sequelize automatically adds the fields `createdAt` and `updatedAt` to every model, using the data type `DataTypes.DATE`. Those fields are automatically managed as well - whenever you use Sequelize to create or update something, those fields will be set correctly. The `createdAt` field will contain the timestamp representing the moment of creation, and the `updatedAt` will contain the timestamp of the latest update.

**Note:** This is done in the Sequelize level (i.e. not done with *SQL triggers*). This means that direct SQL queries (for example queries performed without Sequelize by any other means) will not cause these fields to be updated automatically.

This behavior can be disabled for a model with the `timestamps: false` option:

```js
sequelize.define(
  'User',
  {
    
  },
  {
    timestamps: false,
  },
);
```

It is also possible to enable only one of `createdAt`/`updatedAt`, and to provide a custom name for these columns:

```js
class Foo extends Model {}
Foo.init(
  {
    
  },
  {
    sequelize,

    
    timestamps: true,

    
    createdAt: false,

    
    updatedAt: 'updateTimestamp',
  },
);
```

## Column declaration shorthand syntax

If the only thing being specified about a column is its data type, the syntax can be shortened:

```js
sequelize.define('User', {
  name: {
    type: DataTypes.STRING,
  },
});

sequelize.define('User', { name: DataTypes.STRING });
```

## Default Values

By default, Sequelize assumes that the default value of a column is `NULL`. This behavior can be changed by passing a specific `defaultValue` to the column definition:

```js
sequelize.define('User', {
  name: {
    type: DataTypes.STRING,
    defaultValue: 'John Doe',
  },
});
```

Some special values, such as `DataTypes.NOW`, are also accepted:

```js
sequelize.define('Foo', {
  bar: {
    type: DataTypes.DATETIME,
    defaultValue: DataTypes.NOW,
    
  },
});
```

## Data Types

Every column you define in your model must have a data type. Sequelize provides a lot of built-in data types. To access a built-in data type, you must import `DataTypes`:

```js
const { DataTypes } = require('sequelize'); 
```

### Strings

```js
DataTypes.STRING; 
DataTypes.STRING(1234); 
DataTypes.STRING.BINARY; 
DataTypes.TEXT; 
DataTypes.TEXT('tiny'); 
DataTypes.CITEXT; 
DataTypes.TSVECTOR; 
```

### Boolean

```js
DataTypes.BOOLEAN; 
```

### Numbers

```js
DataTypes.INTEGER; 
DataTypes.BIGINT; 
DataTypes.BIGINT(11); 

DataTypes.FLOAT; 
DataTypes.FLOAT(11); 
DataTypes.FLOAT(11, 10); 

DataTypes.REAL; 
DataTypes.REAL(11); 
DataTypes.REAL(11, 12); 

DataTypes.DOUBLE; 
DataTypes.DOUBLE(11); 
DataTypes.DOUBLE(11, 10); 

DataTypes.DECIMAL; 
DataTypes.DECIMAL(10, 2); 
```

#### Unsigned & Zerofill integers - MySQL/MariaDB only

In MySQL and MariaDB, the data types `INTEGER`, `BIGINT`, `FLOAT` and `DOUBLE` can be set as unsigned or zerofill (or both), as follows:

```js
DataTypes.INTEGER.UNSIGNED;
DataTypes.INTEGER.ZEROFILL;
DataTypes.INTEGER.UNSIGNED.ZEROFILL;
```

### Dates

```js
DataTypes.DATE; 
DataTypes.DATE(6); 
DataTypes.DATEONLY; 
```

### UUIDs

For UUIDs, use `DataTypes.UUID`. It becomes the `UUID` data type for PostgreSQL and SQLite, and `CHAR(36)` for MySQL. Sequelize can generate UUIDs automatically for these fields, simply use `DataTypes.UUIDV1` or `DataTypes.UUIDV4` as the default value:

```js
{
  type: DataTypes.UUID,
  defaultValue: DataTypes.UUIDV4 
}
```

### Others

There are other data types, covered in a separate guide.

## Column Options

When defining a column, apart from specifying the `type` of the column, and the `allowNull` and `defaultValue` options mentioned above, there are a lot more options that can be used. Some examples are below.

```js
const { Model, DataTypes, Deferrable } = require('sequelize');

class Foo extends Model {}
Foo.init(
  {
    
    flag: { type: DataTypes.BOOLEAN, allowNull: false, defaultValue: true },

    
    myDate: { type: DataTypes.DATE, defaultValue: DataTypes.NOW },

    
    
    
    title: { type: DataTypes.STRING, allowNull: false },

    
    
    
    uniqueOne: { type: DataTypes.STRING, unique: 'compositeIndex' },
    uniqueTwo: { type: DataTypes.INTEGER, unique: 'compositeIndex' },

    
    someUnique: { type: DataTypes.STRING, unique: true },

    
    identifier: { type: DataTypes.STRING, primaryKey: true },

    
    incrementMe: { type: DataTypes.INTEGER, autoIncrement: true },

    
    fieldWithUnderscores: {
      type: DataTypes.STRING,
      field: 'field_with_underscores',
    },

    
    bar_id: {
      type: DataTypes.INTEGER,

      references: {
        
        model: Bar,

        
        key: 'id',

        
        deferrable: Deferrable.INITIALLY_IMMEDIATE,
        
        
        
        
      },
    },

    
    commentMe: {
      type: DataTypes.INTEGER,
      comment: 'This is a column name that has a comment',
    },
  },
  {
    sequelize,
    modelName: 'foo',

    
    indexes: [{ unique: true, fields: ['someUnique'] }],
  },
);
```

## Taking advantage of Models being classes

The Sequelize models are ES6 classes. You can very easily add custom instance or class level methods.

```js
class User extends Model {
  static classLevelMethod() {
    return 'foo';
  }
  instanceLevelMethod() {
    return 'bar';
  }
  getFullname() {
    return [this.firstname, this.lastname].join(' ');
  }
}
User.init(
  {
    firstname: Sequelize.TEXT,
    lastname: Sequelize.TEXT,
  },
  { sequelize },
);

console.log(User.classLevelMethod()); 
const user = User.build({ firstname: 'Jane', lastname: 'Doe' });
console.log(user.instanceLevelMethod()); 
console.log(user.getFullname()); 
```
