---
title: "Schemas"
source: https://mongoosejs.com/docs/guide.html
domain: mongoose-odm
license: CC-BY-SA-4.0
tags: mongoose odm, mongodb object modeling, schema-based document model, odm population query
fetched: 2026-07-02
---

# Schemas

If you haven't yet done so, please take a minute to read the quickstart to get an idea of how Mongoose works. If you are migrating from 7.x to 8.x please take a moment to read the migration guide.

## Defining your schema

Everything in Mongoose starts with a Schema. Each schema maps to a MongoDB collection and defines the shape of the documents within that collection.

```
import mongoose from 'mongoose';
const { Schema } = mongoose;

const blogSchema = new Schema({
  title: String, 
  author: String,
  body: String,
  comments: [{ body: String, date: Date }],
  date: { type: Date, default: Date.now },
  hidden: Boolean,
  meta: {
    votes: Number,
    favs: Number
  }
});
```

If you want to add additional keys later, use the Schema#add method.

Each key in our code `blogSchema` defines a property in our documents which will be cast to its associated SchemaType. For example, we've defined a property `title` which will be cast to the String SchemaType and property `date` which will be cast to a `Date` SchemaType.

Notice above that if a property only requires a type, it can be specified using a shorthand notation (contrast the `title` property above with the `date` property).

Keys may also be assigned nested objects containing further key/type definitions like the `meta` property above. This will happen whenever a key's value is a POJO that doesn't have a `type` property.

In these cases, Mongoose only creates actual schema paths for leaves in the tree. (like `meta.votes` and `meta.favs` above), and the branches do not have actual paths. A side-effect of this is that `meta` above cannot have its own validation. If validation is needed up the tree, a path needs to be created up the tree - see the Subdocuments section for more information on how to do this. Also read the Mixed subsection of the SchemaTypes guide for some gotchas.

The permitted SchemaTypes are:

- String
- Number
- Date
- Buffer
- Boolean
- Mixed
- ObjectId
- Array
- Decimal128
- Map
- UUID
- Double
- Int32

Read more about SchemaTypes here.

Schemas not only define the structure of your document and casting of properties, they also define document instance methods, static Model methods, compound indexes, and document lifecycle hooks called middleware.

## Creating a model

To use our schema definition, we need to convert our `blogSchema` into a Model we can work with. To do so, we pass it into `mongoose.model(modelName, schema)`:

```
const Blog = mongoose.model('Blog', blogSchema);
```

## Ids

By default, Mongoose adds an `_id` property to your schemas.

```
const schema = new Schema();

schema.path('_id'); 
```

When you create a new document with the automatically added `_id` property, Mongoose creates a new `_id` of type ObjectId to your document.

```
const Model = mongoose.model('Test', schema);

const doc = new Model();
doc._id instanceof mongoose.Types.ObjectId; 
```

You can also overwrite Mongoose's default `_id` with your own `_id`. Just be careful: Mongoose will refuse to save a top-level document that doesn't have an `_id`, so you're responsible for setting `_id` if you define your own `_id` path.

```
const schema = new Schema({
  _id: Number 
});
const Model = mongoose.model('Test', schema);

const doc = new Model();
await doc.save(); 

doc._id = 1;
await doc.save(); 
```

Mongoose also adds an `_id` property to subdocuments. You can disable the `_id` property on your subdocuments as follows. Mongoose does allow saving subdocuments without an `_id` property.

```
const nestedSchema = new Schema(
  { name: String },
  { _id: false } 
);
const schema = new Schema({
  subdoc: nestedSchema,
  docArray: [nestedSchema]
});
const Test = mongoose.model('Test', schema);

await Test.create({
  subdoc: { name: 'test 1' },
  docArray: [{ name: 'test 2' }]
});
```

Alternatively, you can disable `_id` using the following syntax:

```
const nestedSchema = new Schema({
  _id: false, 
  name: String
});
```

## Instance methods

Instances of `Models` are documents. Documents have many of their own built-in instance methods. We may also define our own custom document instance methods.

```
const animalSchema = new Schema({ name: String, type: String },
  {
  
  
    methods: {
      findSimilarTypes(cb) {
        return mongoose.model('Animal').find({ type: this.type }, cb);
      }
    }
  });

animalSchema.methods.findSimilarTypes = function(cb) {
  return mongoose.model('Animal').find({ type: this.type }, cb);
};
```

Now all of our `animal` instances have a `findSimilarTypes` method available to them.

```
const Animal = mongoose.model('Animal', animalSchema);
const dog = new Animal({ type: 'dog' });

dog.findSimilarTypes((err, dogs) => {
  console.log(dogs); 
});
```

- Overwriting a default mongoose document method may lead to unpredictable results. See this for more details.
- The example above uses the `Schema.methods` object directly to save an instance method. You can also use the `Schema.method()` helper.
- Do **not** declare methods using ES6 arrow functions (`=>`). Arrow functions explicitly prevent binding `this`, so your method will **not** have access to the document and the above examples will not work.

## Statics

You can also add static functions to your model. There are three equivalent ways to add a static:

- Add a function property to the second argument of the schema-constructor (`statics`)
- Add a function property to `schema.statics`
- Call the `Schema#static()` function

```
const animalSchema = new Schema({ name: String, type: String },
  {
  
  
    statics: {
      findByName(name) {
        return this.find({ name: new RegExp(name, 'i') });
      }
    }
  });

animalSchema.statics.findByName = function(name) {
  return this.find({ name: new RegExp(name, 'i') });
};

animalSchema.static('findByBreed', function(breed) { return this.find({ breed }); });

const Animal = mongoose.model('Animal', animalSchema);
let animals = await Animal.findByName('fido');
animals = animals.concat(await Animal.findByBreed('Poodle'));
```

Do **not** declare statics using ES6 arrow functions (`=>`). Arrow functions explicitly prevent binding `this`, so the above examples will not work because of the value of `this`.

## Query Helpers

You can also add query helper functions, which are like instance methods but for mongoose queries. Query helper methods let you extend mongoose's chainable query builder API.

```
const animalSchema = new Schema({ name: String, type: String },
  {
  
  
    query: {
      byName(name) {
        return this.where({ name: new RegExp(name, 'i') });
      }
    }
  });

animalSchema.query.byName = function(name) {
  return this.where({ name: new RegExp(name, 'i') });
};

const Animal = mongoose.model('Animal', animalSchema);

Animal.find().byName('fido').exec((err, animals) => {
  console.log(animals);
});

Animal.findOne().byName('fido').exec((err, animal) => {
  console.log(animal);
});
```

## Indexes

MongoDB supports secondary indexes. With mongoose, we define these indexes within our `Schema` at the path level or the `schema` level. Defining indexes at the schema level is necessary when creating compound indexes.

```
const animalSchema = new Schema({
  name: String,
  type: String,
  tags: { type: [String], index: true } 
});

animalSchema.index({ name: 1, type: -1 }); 
```

See SchemaType#index() for other index options.

When your application starts up, Mongoose automatically calls `createIndex` for each defined index in your schema. Mongoose will call `createIndex` for each index sequentially, and emit an 'index' event on the model when all the `createIndex` calls succeeded or when there was an error. While nice for development, it is recommended this behavior be disabled in production since index creation can cause a significant performance impact. Disable the behavior by setting the `autoIndex` option of your schema to `false`, or globally on the connection by setting the option `autoIndex` to `false`.

```
mongoose.connect('mongodb://user:pass@127.0.0.1:port/database', { autoIndex: false });

mongoose.createConnection('mongodb://user:pass@127.0.0.1:port/database', { autoIndex: false });

mongoose.set('autoIndex', false);

animalSchema.set('autoIndex', false);

new Schema({  }, { autoIndex: false });
```

Mongoose will emit an `index` event on the model when indexes are done building or an error occurred.

```
animalSchema.index({ _id: 1 }, { sparse: true });
const Animal = mongoose.model('Animal', animalSchema);

Animal.on('index', error => {
  
  console.log(error.message);
});
```

See also the Model#ensureIndexes method.

## Virtuals

Virtuals are document properties that you can get and set but that do not get persisted to MongoDB. The getters are useful for formatting or combining fields, while setters are useful for de-composing a single value into multiple values for storage.

```
const personSchema = new Schema({
  name: {
    first: String,
    last: String
  }
});

const Person = mongoose.model('Person', personSchema);

const axl = new Person({
  name: { first: 'Axl', last: 'Rose' }
});
```

Suppose you want to print out the person's full name. You could do it yourself:

```
console.log(axl.name.first + ' ' + axl.name.last); 
```

But concatenating the first and last name every time can get cumbersome. And what if you want to do some extra processing on the name, like removing diacritics? A virtual property getter lets you define a `fullName` property that won't get persisted to MongoDB.

```
const personSchema = new Schema({
  name: {
    first: String,
    last: String
  }
}, {
  virtuals: {
    fullName: {
      get() {
        return this.name.first + ' ' + this.name.last;
      }
    }
  }
});

personSchema.virtual('fullName').get(function() {
  return this.name.first + ' ' + this.name.last;
});
```

Now, mongoose will call your getter function every time you access the `fullName` property:

```
console.log(axl.fullName); 
```

If you use `toJSON()` or `toObject()` Mongoose will *not* include virtuals by default. Pass `{ virtuals: true }` to `toJSON()` or `toObject()` to include virtuals.

```
doc.toObject({ virtuals: true });

doc.toJSON({ virtuals: true });
```

The above caveat for `toJSON()` also includes the output of calling `JSON.stringify()` on a Mongoose document, because `JSON.stringify()` calls `toJSON()`. To include virtuals in `JSON.stringify()` output, you can either call `toObject({ virtuals: true })` on the document before calling `JSON.stringify()`, or set the `toJSON: { virtuals: true }` option on your schema.

```
JSON.stringify(doc.toObject({ virtuals: true }));

const personSchema = new Schema({
  name: {
    first: String,
    last: String
  }
}, {
  toJSON: { virtuals: true } 
});
```

You can also add a custom setter to your virtual that will let you set both first name and last name via the `fullName` virtual.

```
const personSchema = new Schema({
  name: {
    first: String,
    last: String
  }
}, {
  virtuals: {
    fullName: {
      get() {
        return this.name.first + ' ' + this.name.last;
      },
      set(v) {
        this.name.first = v.substr(0, v.indexOf(' '));
        this.name.last = v.substr(v.indexOf(' ') + 1);
      }
    }
  }
});

personSchema.virtual('fullName').
  get(function() {
    return this.name.first + ' ' + this.name.last;
  }).
  set(function(v) {
    this.name.first = v.substr(0, v.indexOf(' '));
    this.name.last = v.substr(v.indexOf(' ') + 1);
  });

axl.fullName = 'William Rose'; 
```

Virtual property setters are applied before other validation. So the example above would still work even if the `first` and `last` name fields were required.

Only non-virtual properties work as part of queries and for field selection. Since virtuals are not stored in MongoDB, you can't query with them.

You can learn more about virtuals here.

## Aliases

Aliases are a particular type of virtual where the getter and setter seamlessly get and set another property. This is handy for saving network bandwidth, so you can convert a short property name stored in the database into a longer name for code readability.

```
const personSchema = new Schema({
  n: {
    type: String,
    
    alias: 'name'
  }
});

const person = new Person({ name: 'Val' });
console.log(person); 
console.log(person.toObject({ virtuals: true })); 
console.log(person.name); 

person.name = 'Not Val';
console.log(person); 
```

You can also declare aliases on nested paths. It is easier to use nested schemas and subdocuments, but you can also declare nested path aliases inline as long as you use the full nested path `nested.myProp` as the alias.

```
const childSchema = new Schema({
  n: {
    type: String,
    alias: 'name'
  }
}, { _id: false });

const parentSchema = new Schema({
  
  c: childSchema,
  name: {
    f: {
      type: String,
      
      alias: 'name.first'
    }
  }
});
```

## Options

Schemas have a few configurable options which can be passed to the constructor or to the `set` method:

```
new Schema({  }, options);

const schema = new Schema({  });
schema.set(option, value);
```

Valid options:

- autoIndex
- autoCreate
- bufferCommands
- bufferTimeoutMS
- capped
- collection
- discriminatorKey
- excludeIndexes
- id
- _id
- minimize
- read
- writeConcern
- shardKey
- statics
- strict
- strictQuery
- toJSON
- toObject
- typeKey
- validateBeforeSave
- versionKey
- optimisticConcurrency
- collation
- timeseries
- selectPopulatedPaths
- skipVersioning
- timestamps
- storeSubdocValidationError
- collectionOptions
- methods
- query
- autoSearchIndex
- readConcern

## option: autoIndex

By default, Mongoose's `init()` function creates all the indexes defined in your model's schema by calling `Model.createIndexes()` after you successfully connect to MongoDB. Creating indexes automatically is great for development and test environments. But index builds can also create significant load on your production database. If you want to manage indexes carefully in production, you can set `autoIndex` to false.

```
const schema = new Schema({  }, { autoIndex: false });
const Clock = mongoose.model('Clock', schema);
Clock.ensureIndexes(callback);
```

The `autoIndex` option is set to `true` by default. You can change this default by setting `mongoose.set('autoIndex', false);`

A common pattern is to disable `autoIndex` only in production:

```
mongoose.set('autoIndex', process.env.NODE_ENV !== 'production');
```

## option: autoCreate

Before Mongoose builds indexes, it calls `Model.createCollection()` to create the underlying collection in MongoDB by default. Calling `createCollection()` sets the collection's default collation based on the collation option and establishes the collection as a capped collection if you set the `capped` schema option.

You can disable this behavior by setting `autoCreate` to `false` using `mongoose.set('autoCreate', false)`. Like `autoIndex`, `autoCreate` is helpful for development and test environments, but you may want to disable it for production to avoid unnecessary database calls.

Unfortunately, `createCollection()` cannot change an existing collection. For example, if you add `capped: { size: 1024 }` to your schema and the existing collection is not capped, `createCollection()` will **not** overwrite the existing collection. That is because the MongoDB server does not allow changing a collection's options without dropping the collection first.

```
const schema = new Schema({ name: String }, {
  autoCreate: false,
  capped: { size: 1024 }
});
const Test = mongoose.model('Test', schema);

await Test.createCollection();
```

## option: bufferCommands

By default, mongoose buffers commands when the connection goes down until the driver manages to reconnect. To disable buffering, set `bufferCommands` to false.

```
const schema = new Schema({  }, { bufferCommands: false });
```

The schema `bufferCommands` option overrides the global `bufferCommands` option.

```
mongoose.set('bufferCommands', true);

const schema = new Schema({  }, { bufferCommands: false });
```

## option: bufferTimeoutMS

If `bufferCommands` is on, this option sets the maximum amount of time Mongoose buffering will wait before throwing an error. If not specified, Mongoose will use 10000 (10 seconds).

```
const schema = new Schema({  }, { bufferTimeoutMS: 1000 });
```

## option: capped

Mongoose supports MongoDBs capped collections. To specify the underlying MongoDB collection be `capped`, set the `capped` option to the maximum size of the collection in bytes.

```
new Schema({  }, { capped: 1024 });
```

The `capped` option may also be set to an object if you want to pass additional options like max. In this case you must explicitly pass the `size` option, which is required.

```
new Schema({  }, { capped: { size: 1024, max: 1000, autoIndexId: true } });
```

## option: collection

Mongoose by default produces a collection name by passing the model name to the `utils.toCollectionName` method. This method pluralizes the name. Set this option if you need a different name for your collection.

```
const dataSchema = new Schema({  }, { collection: 'data' });
```

## option: discriminatorKey

When you define a discriminator, Mongoose adds a path to your schema that stores which discriminator a document is an instance of. By default, Mongoose adds an `__t` path, but you can set `discriminatorKey` to overwrite this default.

```
const baseSchema = new Schema({}, { discriminatorKey: 'type' });
const BaseModel = mongoose.model('Test', baseSchema);

const personSchema = new Schema({ name: String });
const PersonModel = BaseModel.discriminator('Person', personSchema);

const doc = new PersonModel({ name: 'James T. Kirk' });

doc.type; 
```

## option: excludeIndexes

When `excludeIndexes` is `true`, Mongoose will not create indexes from the given subdocument schema. This option only works when the schema is used in a subdocument path or document array path, Mongoose ignores this option if set on the top-level schema for a model. Defaults to `false`.

```
const childSchema1 = Schema({
  name: { type: String, index: true }
});

const childSchema2 = Schema({
  name: { type: String, index: true }
}, { excludeIndexes: true });

const User = new Schema({
  name: { type: String, index: true },
  child1: childSchema1,
  child2: childSchema2
});
```

## option: id

Mongoose assigns each of your schemas an `id` virtual getter by default which returns the document's `_id` field cast to a string, or in the case of ObjectIds, its hexString. If you don't want an `id` getter added to your schema, you may disable it by passing this option at schema construction time.

```
const schema = new Schema({ name: String });
const Page = mongoose.model('Page', schema);
const p = new Page({ name: 'mongodb.org' });
console.log(p.id); 

const schema = new Schema({ name: String }, { id: false });
const Page = mongoose.model('Page', schema);
const p = new Page({ name: 'mongodb.org' });
console.log(p.id); 
```

## option: _id

Mongoose assigns each of your schemas an `_id` field by default if one is not passed into the Schema constructor. The type assigned is an ObjectId to coincide with MongoDB's default behavior. If you don't want an `_id` added to your schema at all, you may disable it using this option.

You can **only** use this option on subdocuments. Mongoose can't save a document without knowing its id, so you will get an error if you try to save a document without an `_id`.

```
const schema = new Schema({ name: String });
const Page = mongoose.model('Page', schema);
const p = new Page({ name: 'mongodb.org' });
console.log(p); 

const childSchema = new Schema({ name: String }, { _id: false });
const parentSchema = new Schema({ children: [childSchema] });

const Model = mongoose.model('Model', parentSchema);

Model.create({ children: [{ name: 'Luke' }] }, (error, doc) => {
  
});
```

## option: minimize

Mongoose will, by default, "minimize" schemas by removing empty objects.

```
const schema = new Schema({ name: String, inventory: {} });
const Character = mongoose.model('Character', schema);

const frodo = new Character({ name: 'Frodo', inventory: { ringOfPower: 1 } });
await frodo.save();
let doc = await Character.findOne({ name: 'Frodo' }).lean();
doc.inventory; 

const sam = new Character({ name: 'Sam', inventory: {} });
await sam.save();
doc = await Character.findOne({ name: 'Sam' }).lean();
doc.inventory; 
```

This behavior can be overridden by setting `minimize` option to `false`. It will then store empty objects.

```
const schema = new Schema({ name: String, inventory: {} }, { minimize: false });
const Character = mongoose.model('Character', schema);

const sam = new Character({ name: 'Sam', inventory: {} });
await sam.save();
doc = await Character.findOne({ name: 'Sam' }).lean();
doc.inventory; 
```

To check whether an object is empty, you can use the `$isEmpty()` helper:

```
const sam = new Character({ name: 'Sam', inventory: {} });
sam.$isEmpty('inventory'); 

sam.inventory.barrowBlade = 1;
sam.$isEmpty('inventory'); 
```

## option: read

Allows setting query#read options at the schema level, providing us a way to apply default ReadPreferences to all queries derived from a model.

```
const schema = new Schema({  }, { read: 'primary' });            
const schema = new Schema({  }, { read: 'primaryPreferred' });   
const schema = new Schema({  }, { read: 'secondary' });          
const schema = new Schema({  }, { read: 'secondaryPreferred' }); 
const schema = new Schema({  }, { read: 'nearest' });            
```

The alias of each pref is also permitted so instead of having to type out 'secondaryPreferred' and getting the spelling wrong, we can simply pass 'sp'.

The read option also allows us to specify *tag sets*. These tell the driver from which members of the replica-set it should attempt to read. Read more about tag sets in the MongoDB documentation on replica set tag sets and in the MongoDB core documentation on read preference.

*NOTE: you may also specify the driver read preference strategy option when connecting:*

```
const options = { replset: { strategy: 'ping' } };
mongoose.connect(uri, options);

const schema = new Schema({  }, { read: ['nearest', { disk: 'ssd' }] });
mongoose.model('JellyBean', schema);
```

## option: writeConcern

Allows setting write concern at the schema level.

```
const schema = new Schema({ name: String }, {
  writeConcern: {
    w: 'majority',
    j: true,
    wtimeout: 1000
  }
});
```

## option: shardKey

The `shardKey` option is used when we have a sharded MongoDB architecture. Each sharded collection is given a shard key which must be present in all insert/update operations. We just need to set this schema option to the same shard key and we’ll be all set.

```
new Schema({  }, { shardKey: { tag: 1, name: 1 } });
```

*Note that Mongoose does not send the `shardcollection` command for you. You must configure your shards yourself.*

## option: strict

The strict option, (enabled by default), ensures that values passed to our model constructor that were not specified in our schema do not get saved to the db.

```
const thingSchema = new Schema({  })
const Thing = mongoose.model('Thing', thingSchema);
const thing = new Thing({ iAmNotInTheSchema: true });
thing.save(); 

const thingSchema = new Schema({  }, { strict: false });
const thing = new Thing({ iAmNotInTheSchema: true });
thing.save(); 
```

This also affects the use of `doc.set()` to set a property value.

```
const thingSchema = new Schema({  });
const Thing = mongoose.model('Thing', thingSchema);
const thing = new Thing;
thing.set('iAmNotInTheSchema', true);
thing.save(); 
```

This value can be overridden at the model instance level by passing a second boolean argument:

```
const Thing = mongoose.model('Thing');
const thing = new Thing(doc, true);  
const thing = new Thing(doc, false); 
```

The `strict` option may also be set to `"throw"` which will cause errors to be produced instead of dropping the bad data.

*NOTE: Any key/val set on the instance that does not exist in your schema is always ignored, regardless of schema option.*

```
const thingSchema = new Schema({  });
const Thing = mongoose.model('Thing', thingSchema);
const thing = new Thing;
thing.iAmNotInTheSchema = true;
thing.save(); 
```

## option: strictQuery

Mongoose supports a separate `strictQuery` option to avoid strict mode for query filters. This is because empty query filters cause Mongoose to return all documents in the model, which can cause issues.

```
const mySchema = new Schema({ field: Number }, { strict: true });
const MyModel = mongoose.model('Test', mySchema);

MyModel.find({ notInSchema: 1 });
```

The `strict` option does apply to updates. The `strictQuery` option is **just** for query filters.

```
MyModel.updateMany({}, { $set: { notInSchema: 1 } });
```

Mongoose has a separate `strictQuery` option to toggle strict mode for the `filter` parameter to queries.

```
const mySchema = new Schema({ field: Number }, {
  strict: true,
  strictQuery: false 
});
const MyModel = mongoose.model('Test', mySchema);

MyModel.find({ notInSchema: 1 });
```

In general, we do **not** recommend passing user-defined objects as query filters:

```
const docs = await MyModel.find(req.query);

const docs = await MyModel.find({ name: req.query.name, age: req.query.age }).setOptions({ sanitizeFilter: true });
```

In Mongoose 7, `strictQuery` is `false` by default. However, you can override this behavior globally:

```
mongoose.set('strictQuery', true);
```

## option: toJSON

Exactly the same as the toObject option but only applies when the document's `toJSON` method is called.

```
const schema = new Schema({ name: String });
schema.path('name').get(function(v) {
  return v + ' is my name';
});
schema.set('toJSON', { getters: true, virtuals: false });
const M = mongoose.model('Person', schema);
const m = new M({ name: 'Max Headroom' });
console.log(m.toObject()); 
console.log(m.toJSON()); 

console.log(JSON.stringify(m)); 
```

To see all available `toJSON/toObject` options, read this.

## option: toObject

Documents have a toObject method which converts the mongoose document into a plain JavaScript object. This method accepts a few options. Instead of applying these options on a per-document basis, we may declare the options at the schema level and have them applied to all of the schema's documents by default.

To have all virtuals show up in your `console.log` output, set the `toObject` option to `{ getters: true }`:

```
const schema = new Schema({ name: String });
schema.path('name').get(function(v) {
  return v + ' is my name';
});
schema.set('toObject', { getters: true });
const M = mongoose.model('Person', schema);
const m = new M({ name: 'Max Headroom' });
console.log(m); 
```

To see all available `toObject` options, read this.

## option: typeKey

By default, if you have an object with key 'type' in your schema, mongoose will interpret it as a type declaration.

```
const schema = new Schema({ loc: { type: String, coordinates: [Number] } });
```

However, for applications like geoJSON, the 'type' property is important. If you want to control which key mongoose uses to find type declarations, set the 'typeKey' schema option.

```
const schema = new Schema({
  
  loc: { type: String, coordinates: [Number] },
  
  name: { $type: String }
}, { typeKey: '$type' }); 
```

## option: validateBeforeSave

By default, documents are automatically validated before they are saved to the database. This is to prevent saving an invalid document. If you want to handle validation manually, and be able to save objects which don't pass validation, you can set `validateBeforeSave` to false.

```
const schema = new Schema({ name: String });
schema.set('validateBeforeSave', false);
schema.path('name').validate(function(value) {
  return value != null;
});
const M = mongoose.model('Person', schema);
const m = new M({ name: null });
try {
  await m.validate();
} catch (err) {
  console.log(err); 
}
await m.save(); 
```

## option: versionKey

The `versionKey` is a property set on each document when first created by Mongoose. This keys value contains the internal revision of the document. The `versionKey` option is a string that represents the path to use for versioning. The default is `__v`. If this conflicts with your application you can configure as such:

```
const schema = new Schema({ name: 'string' });
const Thing = mongoose.model('Thing', schema);
const thing = new Thing({ name: 'mongoose v3' });
await thing.save(); 

new Schema({  }, { versionKey: '_somethingElse' })
const Thing = mongoose.model('Thing', schema);
const thing = new Thing({ name: 'mongoose v3' });
thing.save(); 
```

Note that Mongoose's default versioning is **not** a full optimistic concurrency solution. Mongoose's default versioning only operates on arrays as shown below.

```
const doc1 = await Model.findOne({ _id });
const doc2 = await Model.findOne({ _id });

doc1.comments.splice(0, 3);
await doc1.save();

doc2.set('comments.1.body', 'new comment');
await doc2.save();
```

If you need optimistic concurrency support for `save()`, you can set the `optimisticConcurrency` option.

Document versioning can also be disabled by setting the `versionKey` to `false`. *DO NOT disable versioning unless you know what you are doing.*

```
new Schema({  }, { versionKey: false });
const Thing = mongoose.model('Thing', schema);
const thing = new Thing({ name: 'no versioning please' });
thing.save(); 
```

Mongoose *only* updates the version key when you use `save()`. If you use `update()`, `findOneAndUpdate()`, etc. Mongoose will **not** update the version key. As a workaround, you can use the below middleware.

```
schema.pre('findOneAndUpdate', function() {
  const update = this.getUpdate();
  if (update.__v != null) {
    delete update.__v;
  }
  const keys = ['$set', '$setOnInsert'];
  for (const key of keys) {
    if (update[key] != null && update[key].__v != null) {
      delete update[key].__v;
      if (Object.keys(update[key]).length === 0) {
        delete update[key];
      }
    }
  }
  update.$inc = update.$inc || {};
  update.$inc.__v = 1;
});
```

## option: optimisticConcurrency

Optimistic concurrency is a strategy to ensure the document you're updating didn't change between when you loaded it using `find()` or `findOne()`, and when you update it using `save()`.

For example, suppose you have a `House` model that contains a list of `photos`, and a `status` that represents whether this house shows up in searches. Suppose that a house that has status `'APPROVED'` must have at least two `photos`. You might implement the logic of approving a house document as shown below:

```
async function markApproved(id) {
  const house = await House.findOne({ _id });
  if (house.photos.length < 2) {
    throw new Error('House must have at least two photos!');
  }

  house.status = 'APPROVED';
  await house.save();
}
```

The `markApproved()` function looks right in isolation, but there might be a potential issue: what if another function removes the house's photos between the `findOne()` call and the `save()` call? For example, the below code will succeed:

```
const house = await House.findOne({ _id });
if (house.photos.length < 2) {
  throw new Error('House must have at least two photos!');
}

const house2 = await House.findOne({ _id });
house2.photos = [];
await house2.save();

house.status = 'APPROVED';
await house.save();
```

If you set the `optimisticConcurrency` option on the `House` model's schema, the above script will throw an error.

```
const House = mongoose.model('House', Schema({
  status: String,
  photos: [String]
}, { optimisticConcurrency: true }));

const house = await House.findOne({ _id });
if (house.photos.length < 2) {
  throw new Error('House must have at least two photos!');
}

const house2 = await House.findOne({ _id });
house2.photos = [];
await house2.save();

house.status = 'APPROVED';
await house.save();
```

You can also set `optimisticConcurrency` to an array of field names to only use optimistic concurrency when one of those fields is modified. Note that setting `optimisticConcurrency` to an array of field names **replaces the default array versioning behavior**. For example, if you set `optimisticConcurrency: ['status']`, Mongoose will only throw a `VersionError` if `status` is modified concurrently, and will **not** throw a `VersionError` if an array like `photos` is modified concurrently.

```
const House = mongoose.model('House', Schema({
  status: String,
  photos: [String]
}, { optimisticConcurrency: ['status'] }));
```

You can also set `optimisticConcurrency` to an object with an `exclude` property to exclude certain fields from optimistic concurrency. This enables optimistic concurrency for all fields except the excluded fields, while still replacing default array versioning behavior.

```
const House = mongoose.model('House', Schema({
  status: String,
  photos: [String],
  rawResult: Object 
}, { optimisticConcurrency: { exclude: ['rawResult'] } }));
```

## option: collation

Sets a default collation for every query and aggregation. Here's a beginner-friendly overview of collations.

```
const schema = new Schema({
  name: String
}, { collation: { locale: 'en_US', strength: 1 } });

const MyModel = db.model('MyModel', schema);

MyModel.create([{ name: 'val' }, { name: 'Val' }]).
  then(() => {
    return MyModel.find({ name: 'val' });
  }).
  then((docs) => {
    
    
  });
```

## option: timeseries

If you set the `timeseries` option on a schema, Mongoose will create a timeseries collection for any model that you create from that schema.

```
const schema = Schema({ name: String, timestamp: Date, metadata: Object }, {
  timeseries: {
    timeField: 'timestamp',
    metaField: 'metadata',
    granularity: 'hours'
  },
  autoCreate: false,
  expireAfterSeconds: 86400
});

const Test = db.model('Test', schema);

await Test.createCollection();
```

## option: skipVersioning

`skipVersioning` allows excluding paths from versioning (i.e., the internal revision will not be incremented even if these paths are updated). DO NOT do this unless you know what you're doing. For subdocuments, include this on the parent document using the fully qualified path.

```
new Schema({  }, { skipVersioning: { dontVersionMe: true } });
thing.dontVersionMe.push('hey');
thing.save(); 
```

## option: timestamps

The `timestamps` option tells Mongoose to assign `createdAt` and `updatedAt` fields to your schema. The type assigned is Date.

By default, the names of the fields are `createdAt` and `updatedAt`. Customize the field names by setting `timestamps.createdAt` and `timestamps.updatedAt`.

The way `timestamps` works under the hood is:

- If you create a new document, mongoose simply sets `createdAt`, and `updatedAt` to the time of creation.
- If you update a document, mongoose will add `updatedAt` to the `$set` object.
- If you set `upsert: true` on an update operation, mongoose will use `$setOnInsert` operator to add `createdAt` to the document in case the `upsert` operation resulted into a new inserted document.

```
const thingSchema = new Schema({  }, { timestamps: { createdAt: 'created_at' } });
const Thing = mongoose.model('Thing', thingSchema);
const thing = new Thing();
await thing.save(); 

await Thing.updateOne({}, { $set: { name: 'Test' } });

await Thing.findOneAndUpdate({}, { $set: { name: 'Test2' } });

await Thing.bulkWrite([
  {
    insertOne: {
      document: {
        name: 'Jean-Luc Picard',
        ship: 'USS Stargazer'
      
      }
    }
  },
  {
    updateOne: {
      filter: { name: 'Jean-Luc Picard' },
      update: {
        $set: {
          ship: 'USS Enterprise'
        
        }
      }
    }
  }
]);
```

By default, Mongoose uses `new Date()` to get the current time. If you want to overwrite the function Mongoose uses to get the current time, you can set the `timestamps.currentTime` option. Mongoose will call the `timestamps.currentTime` function whenever it needs to get the current time.

```
const schema = Schema({
  createdAt: Number,
  updatedAt: Number,
  name: String
}, {
  
  timestamps: { currentTime: () => Math.floor(Date.now() / 1000) }
});
```

## option: pluginTags

Mongoose supports defining global plugins, plugins that apply to all schemas.

```
mongoose.plugin(function myPlugin(schema) {
  schema.add({ meta: {} });
});
```

Sometimes, you may only want to apply a given plugin to some schemas. In that case, you can add `pluginTags` to a schema:

```
const schema1 = new Schema({
  name: String
}, { pluginTags: ['useMetaPlugin'] });

const schema2 = new Schema({
  name: String
});
```

If you call `plugin()` with a `tags` option, Mongoose will only apply that plugin to schemas that have a matching entry in `pluginTags`.

```
mongoose.plugin(function myPlugin(schema) {
  schema.add({ meta: {} });
}, { tags: ['useMetaPlugin'] });
```

## option: selectPopulatedPaths

By default, Mongoose will automatically `select()` any populated paths for you, unless you explicitly exclude them.

```
const bookSchema = new Schema({
  title: 'String',
  author: { type: 'ObjectId', ref: 'Person' }
});
const Book = mongoose.model('Book', bookSchema);

await Book.find().select('title').populate('author');

await Book.find().select('title author').populate('author');
```

To opt out of selecting populated fields by default, set `selectPopulatedPaths` to `false` in your schema.

```
const bookSchema = new Schema({
  title: 'String',
  author: { type: 'ObjectId', ref: 'Person' }
}, { selectPopulatedPaths: false });
const Book = mongoose.model('Book', bookSchema);

const doc = await Book.findOne().select('title').populate('author');
```

## option: storeSubdocValidationError

For legacy reasons, when there is a validation error in subpath of a single nested schema, Mongoose will record that there was a validation error in the single nested schema path as well. For example:

```
const childSchema = new Schema({ name: { type: String, required: true } });
const parentSchema = new Schema({ child: childSchema });

const Parent = mongoose.model('Parent', parentSchema);

new Parent({ child: {} }).validateSync().errors;
```

Set the `storeSubdocValidationError` to `false` on the child schema to make Mongoose only reports the parent error.

```
const childSchema = new Schema({
  name: { type: String, required: true }
}, { storeSubdocValidationError: false }); 
const parentSchema = new Schema({ child: childSchema });

const Parent = mongoose.model('Parent', parentSchema);

new Parent({ child: {} }).validateSync().errors;
```

## option: collectionOptions

Options like `collation` and `capped` affect the options Mongoose passes to MongoDB when creating a new collection. Mongoose schemas support most MongoDB `createCollection()` options, but not all. You can use the `collectionOptions` option to set any `createCollection()` options; Mongoose will use `collectionOptions` as the default values when calling `createCollection()` for your schema.

```
const schema = new Schema({ name: String }, {
  autoCreate: false,
  collectionOptions: {
    capped: true,
    max: 1000
  }
});
const Test = mongoose.model('Test', schema);

await Test.createCollection();
```

## option: autoSearchIndex

Similar to `autoIndex`, except for automatically creates any Atlas search indexes defined in your schema. Unlike `autoIndex`, this option defaults to false.

```
const schema = new Schema({ name: String }, { autoSearchIndex: true });
schema.searchIndex({
  name: 'my-index',
  definition: { mappings: { dynamic: true } }
});

const Test = mongoose.model('Test', schema);
```

## option: readConcern

Read concerns are similar to `writeConcern`, but for read operations like `find()` and `findOne()`. To set a default `readConcern`, pass the `readConcern` option to the schema constructor as follows.

```
const eventSchema = new mongoose.Schema(
  { name: String },
  {
    readConcern: { level: 'available' } 
  }
);
```

## With ES6 Classes

Schemas have a `loadClass()` method that you can use to create a Mongoose schema from an ES6 class:

- ES6 class methods become Mongoose methods
- ES6 class statics become Mongoose statics
- ES6 getters and setters become Mongoose virtuals

Here's an example of using `loadClass()` to create a schema from an ES6 class:

```
class MyClass {
  myMethod() { return 42; }
  static myStatic() { return 42; }
  get myVirtual() { return 42; }
}

const schema = new mongoose.Schema();
schema.loadClass(MyClass);

console.log(schema.methods); 
console.log(schema.statics); 
console.log(schema.virtuals); 
```

## Pluggable

Schemas are also pluggable which allows us to package up reusable features into plugins that can be shared with the community or just between your projects.

## Next Up

Now that we've covered `Schemas`, let's take a look at SchemaTypes.
