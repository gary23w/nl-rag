---
title: "Eloquent: Getting Started (part 1/3)"
source: https://laravel.com/docs/11.x/eloquent
domain: laravel
license: CC-BY-SA-4.0
tags: laravel framework, eloquent orm, php framework, blade templating
fetched: 2026-07-02
part: 1/3
---

# Eloquent: Getting Started

- Introduction
- Generating Model Classes
- Eloquent Model Conventions
  - Table Names
  - Primary Keys
  - UUID and ULID Keys
  - Timestamps
  - Database Connections
  - Default Attribute Values
  - Configuring Eloquent Strictness
- Retrieving Models
  - Collections
  - Chunking Results
  - Chunk Using Lazy Collections
  - Cursors
  - Advanced Subqueries
- Retrieving Single Models / Aggregates
  - Retrieving or Creating Models
  - Retrieving Aggregates
- Inserting and Updating Models
  - Inserts
  - Updates
  - Mass Assignment
  - Upserts
- Deleting Models
  - Soft Deleting
  - Querying Soft Deleted Models
- Pruning Models
- Replicating Models
- Query Scopes
  - Global Scopes
  - Local Scopes
  - Pending Attributes
- Comparing Models
- Events
  - Using Closures
  - Observers
  - Muting Events


## Introduction

Laravel includes Eloquent, an object-relational mapper (ORM) that makes it enjoyable to interact with your database. When using Eloquent, each database table has a corresponding "Model" that is used to interact with that table. In addition to retrieving records from the database table, Eloquent models allow you to insert, update, and delete records from the table as well.

Before getting started, be sure to configure a database connection in your application's `config/database.php` configuration file. For more information on configuring your database, check out the database configuration documentation.

#### Laravel Bootcamp

If you're new to Laravel, feel free to jump into the Laravel Bootcamp. The Laravel Bootcamp will walk you through building your first Laravel application using Eloquent. It's a great way to get a tour of everything that Laravel and Eloquent have to offer.


## Generating Model Classes

To get started, let's create an Eloquent model. Models typically live in the `app\Models` directory and extend the `Illuminate\Database\Eloquent\Model` class. You may use the `make:model` Artisan command to generate a new model:

```
1php artisan make:model Flight

php artisan make:model Flight
```

If you would like to generate a database migration when you generate the model, you may use the `--migration` or `-m` option:

```
1php artisan make:model Flight --migration

php artisan make:model Flight --migration
```

You may generate various other types of classes when generating a model, such as factories, seeders, policies, controllers, and form requests. In addition, these options may be combined to create multiple classes at once:

```
 1# Generate a model and a FlightFactory class...
 2php artisan make:model Flight --factory
 3php artisan make:model Flight -f
 4 
 5# Generate a model and a FlightSeeder class...
 6php artisan make:model Flight --seed
 7php artisan make:model Flight -s
 8 
 9# Generate a model and a FlightController class...
10php artisan make:model Flight --controller
11php artisan make:model Flight -c
12 
13# Generate a model, FlightController resource class, and form request classes...
14php artisan make:model Flight --controller --resource --requests
15php artisan make:model Flight -crR
16 
17# Generate a model and a FlightPolicy class...
18php artisan make:model Flight --policy
19 
20# Generate a model and a migration, factory, seeder, and controller...
21php artisan make:model Flight -mfsc
22 
23# Shortcut to generate a model, migration, factory, seeder, policy, controller, and form requests...
24php artisan make:model Flight --all
25php artisan make:model Flight -a
26 
27# Generate a pivot model...
28php artisan make:model Member --pivot
29php artisan make:model Member -p

# Generate a model and a FlightFactory class...
php artisan make:model Flight --factory
php artisan make:model Flight -f

# Generate a model and a FlightSeeder class...
php artisan make:model Flight --seed
php artisan make:model Flight -s

# Generate a model and a FlightController class...
php artisan make:model Flight --controller
php artisan make:model Flight -c

# Generate a model, FlightController resource class, and form request classes...
php artisan make:model Flight --controller --resource --requests
php artisan make:model Flight -crR

# Generate a model and a FlightPolicy class...
php artisan make:model Flight --policy

# Generate a model and a migration, factory, seeder, and controller...
php artisan make:model Flight -mfsc

# Shortcut to generate a model, migration, factory, seeder, policy, controller, and form requests...
php artisan make:model Flight --all
php artisan make:model Flight -a

# Generate a pivot model...
php artisan make:model Member --pivot
php artisan make:model Member -p
```

#### Inspecting Models

Sometimes it can be difficult to determine all of a model's available attributes and relationships just by skimming its code. Instead, try the `model:show` Artisan command, which provides a convenient overview of all the model's attributes and relations:

```
1php artisan model:show Flight

php artisan model:show Flight
```


## Eloquent Model Conventions

Models generated by the `make:model` command will be placed in the `app/Models` directory. Let's examine a basic model class and discuss some of Eloquent's key conventions:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Model;
 6 
 7class Flight extends Model
 8{
 9    // ...
10}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    // ...
}
```

### Table Names

After glancing at the example above, you may have noticed that we did not tell Eloquent which database table corresponds to our `Flight` model. By convention, the "snake case", plural name of the class will be used as the table name unless another name is explicitly specified. So, in this case, Eloquent will assume the `Flight` model stores records in the `flights` table, while an `AirTrafficController` model would store records in an `air_traffic_controllers` table.

If your model's corresponding database table does not fit this convention, you may manually specify the model's table name by defining a `table` property on the model:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Model;
 6 
 7class Flight extends Model
 8{
 9    /**
10     * The table associated with the model.
11     *
12     * @var string
13     */
14    protected $table = 'my_flights';
15}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     * The table associated with the model.
     *
     * @var string
     */
    protected $table = 'my_flights';
}
```

### Primary Keys

Eloquent will also assume that each model's corresponding database table has a primary key column named `id`. If necessary, you may define a protected `$primaryKey` property on your model to specify a different column that serves as your model's primary key:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Model;
 6 
 7class Flight extends Model
 8{
 9    /**
10     * The primary key associated with the table.
11     *
12     * @var string
13     */
14    protected $primaryKey = 'flight_id';
15}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     * The primary key associated with the table.
     *
     * @var string
     */
    protected $primaryKey = 'flight_id';
}
```

In addition, Eloquent assumes that the primary key is an incrementing integer value, which means that Eloquent will automatically cast the primary key to an integer. If you wish to use a non-incrementing or a non-numeric primary key you must define a public `$incrementing` property on your model that is set to `false`:

```
 1<?php
 2 
 3class Flight extends Model
 4{
 5    /**
 6     * Indicates if the model's ID is auto-incrementing.
 7     *
 8     * @var bool
 9     */
10    public $incrementing = false;
11}

<?php

class Flight extends Model
{
    /**
     * Indicates if the model's ID is auto-incrementing.
     *
     * @var bool
     */
    public $incrementing = false;
}
```

If your model's primary key is not an integer, you should define a protected `$keyType` property on your model. This property should have a value of `string`:

```
 1<?php
 2 
 3class Flight extends Model
 4{
 5    /**
 6     * The data type of the primary key ID.
 7     *
 8     * @var string
 9     */
10    protected $keyType = 'string';
11}

<?php

class Flight extends Model
{
    /**
     * The data type of the primary key ID.
     *
     * @var string
     */
    protected $keyType = 'string';
}
```

#### "Composite" Primary Keys

Eloquent requires each model to have at least one uniquely identifying "ID" that can serve as its primary key. "Composite" primary keys are not supported by Eloquent models. However, you are free to add additional multi-column, unique indexes to your database tables in addition to the table's uniquely identifying primary key.

### UUID and ULID Keys

Instead of using auto-incrementing integers as your Eloquent model's primary keys, you may choose to use UUIDs instead. UUIDs are universally unique alpha-numeric identifiers that are 36 characters long.

If you would like a model to use a UUID key instead of an auto-incrementing integer key, you may use the `Illuminate\Database\Eloquent\Concerns\HasUuids` trait on the model. Of course, you should ensure that the model has a UUID equivalent primary key column:

```
 1use Illuminate\Database\Eloquent\Concerns\HasUuids;
 2use Illuminate\Database\Eloquent\Model;
 3 
 4class Article extends Model
 5{
 6    use HasUuids;
 7 
 8    // ...
 9}
10 
11$article = Article::create(['title' => 'Traveling to Europe']);
12 
13$article->id; // "8f8e8478-9035-4d23-b9a7-62f4d2612ce5"

use Illuminate\Database\Eloquent\Concerns\HasUuids;
use Illuminate\Database\Eloquent\Model;

class Article extends Model
{
    use HasUuids;

    // ...
}

$article = Article::create(['title' => 'Traveling to Europe']);

$article->id; // "8f8e8478-9035-4d23-b9a7-62f4d2612ce5"
```

By default, The `HasUuids` trait will generate "ordered" UUIDs for your models. These UUIDs are more efficient for indexed database storage because they can be sorted lexicographically.

You can override the UUID generation process for a given model by defining a `newUniqueId` method on the model. In addition, you may specify which columns should receive UUIDs by defining a `uniqueIds` method on the model:

```
 1use Ramsey\Uuid\Uuid;
 2 
 3/**
 4 * Generate a new UUID for the model.
 5 */
 6public function newUniqueId(): string
 7{
 8    return (string) Uuid::uuid4();
 9}
10 
11/**
12 * Get the columns that should receive a unique identifier.
13 *
14 * @return array<int, string>
15 */
16public function uniqueIds(): array
17{
18    return ['id', 'discount_code'];
19}

use Ramsey\Uuid\Uuid;

/**
 * Generate a new UUID for the model.
 */
public function newUniqueId(): string
{
    return (string) Uuid::uuid4();
}

/**
 * Get the columns that should receive a unique identifier.
 *
 * @return array<int, string>
 */
public function uniqueIds(): array
{
    return ['id', 'discount_code'];
}
```

If you wish, you may choose to utilize "ULIDs" instead of UUIDs. ULIDs are similar to UUIDs; however, they are only 26 characters in length. Like ordered UUIDs, ULIDs are lexicographically sortable for efficient database indexing. To utilize ULIDs, you should use the `Illuminate\Database\Eloquent\Concerns\HasUlids` trait on your model. You should also ensure that the model has a ULID equivalent primary key column:

```
 1use Illuminate\Database\Eloquent\Concerns\HasUlids;
 2use Illuminate\Database\Eloquent\Model;
 3 
 4class Article extends Model
 5{
 6    use HasUlids;
 7 
 8    // ...
 9}
10 
11$article = Article::create(['title' => 'Traveling to Asia']);
12 
13$article->id; // "01gd4d3tgrrfqeda94gdbtdk5c"

use Illuminate\Database\Eloquent\Concerns\HasUlids;
use Illuminate\Database\Eloquent\Model;

class Article extends Model
{
    use HasUlids;

    // ...
}

$article = Article::create(['title' => 'Traveling to Asia']);

$article->id; // "01gd4d3tgrrfqeda94gdbtdk5c"
```

### Timestamps

By default, Eloquent expects `created_at` and `updated_at` columns to exist on your model's corresponding database table. Eloquent will automatically set these column's values when models are created or updated. If you do not want these columns to be automatically managed by Eloquent, you should define a `$timestamps` property on your model with a value of `false`:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Model;
 6 
 7class Flight extends Model
 8{
 9    /**
10     * Indicates if the model should be timestamped.
11     *
12     * @var bool
13     */
14    public $timestamps = false;
15}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     * Indicates if the model should be timestamped.
     *
     * @var bool
     */
    public $timestamps = false;
}
```

If you need to customize the format of your model's timestamps, set the `$dateFormat` property on your model. This property determines how date attributes are stored in the database as well as their format when the model is serialized to an array or JSON:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Model;
 6 
 7class Flight extends Model
 8{
 9    /**
10     * The storage format of the model's date columns.
11     *
12     * @var string
13     */
14    protected $dateFormat = 'U';
15}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     * The storage format of the model's date columns.
     *
     * @var string
     */
    protected $dateFormat = 'U';
}
```

If you need to customize the names of the columns used to store the timestamps, you may define `CREATED_AT` and `UPDATED_AT` constants on your model:

```
1<?php
2 
3class Flight extends Model
4{
5    const CREATED_AT = 'creation_date';
6    const UPDATED_AT = 'updated_date';
7}

<?php

class Flight extends Model
{
    const CREATED_AT = 'creation_date';
    const UPDATED_AT = 'updated_date';
}
```

If you would like to perform model operations without the model having its `updated_at` timestamp modified, you may operate on the model within a closure given to the `withoutTimestamps` method:

```
1Model::withoutTimestamps(fn () => $post->increment('reads'));

Model::withoutTimestamps(fn () => $post->increment('reads'));
```

### Database Connections

By default, all Eloquent models will use the default database connection that is configured for your application. If you would like to specify a different connection that should be used when interacting with a particular model, you should define a `$connection` property on the model:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Model;
 6 
 7class Flight extends Model
 8{
 9    /**
10     * The database connection that should be used by the model.
11     *
12     * @var string
13     */
14    protected $connection = 'mysql';
15}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     * The database connection that should be used by the model.
     *
     * @var string
     */
    protected $connection = 'mysql';
}
```

### Default Attribute Values

By default, a newly instantiated model instance will not contain any attribute values. If you would like to define the default values for some of your model's attributes, you may define an `$attributes` property on your model. Attribute values placed in the `$attributes` array should be in their raw, "storable" format as if they were just read from the database:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Model;
 6 
 7class Flight extends Model
 8{
 9    /**
10     * The model's default values for attributes.
11     *
12     * @var array
13     */
14    protected $attributes = [
15        'options' => '[]',
16        'delayed' => false,
17    ];
18}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     * The model's default values for attributes.
     *
     * @var array
     */
    protected $attributes = [
        'options' => '[]',
        'delayed' => false,
    ];
}
```

### Configuring Eloquent Strictness

Laravel offers several methods that allow you to configure Eloquent's behavior and "strictness" in a variety of situations.

First, the `preventLazyLoading` method accepts an optional boolean argument that indicates if lazy loading should be prevented. For example, you may wish to only disable lazy loading in non-production environments so that your production environment will continue to function normally even if a lazy loaded relationship is accidentally present in production code. Typically, this method should be invoked in the `boot` method of your application's `AppServiceProvider`:

```
1use Illuminate\Database\Eloquent\Model;
2 
3/**
4 * Bootstrap any application services.
5 */
6public function boot(): void
7{
8    Model::preventLazyLoading(! $this->app->isProduction());
9}

use Illuminate\Database\Eloquent\Model;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Model::preventLazyLoading(! $this->app->isProduction());
}
```

Also, you may instruct Laravel to throw an exception when attempting to fill an unfillable attribute by invoking the `preventSilentlyDiscardingAttributes` method. This can help prevent unexpected errors during local development when attempting to set an attribute that has not been added to the model's `fillable` array:

```
1Model::preventSilentlyDiscardingAttributes(! $this->app->isProduction());

Model::preventSilentlyDiscardingAttributes(! $this->app->isProduction());
```


## Retrieving Models

Once you have created a model and its associated database table, you are ready to start retrieving data from your database. You can think of each Eloquent model as a powerful query builder allowing you to fluently query the database table associated with the model. The model's `all` method will retrieve all of the records from the model's associated database table:

```
1use App\Models\Flight;
2 
3foreach (Flight::all() as $flight) {
4    echo $flight->name;
5}

use App\Models\Flight;

foreach (Flight::all() as $flight) {
    echo $flight->name;
}
```

#### Building Queries

The Eloquent `all` method will return all of the results in the model's table. However, since each Eloquent model serves as a query builder, you may add additional constraints to queries and then invoke the `get` method to retrieve the results:

```
1$flights = Flight::where('active', 1)
2    ->orderBy('name')
3    ->take(10)
4    ->get();

$flights = Flight::where('active', 1)
    ->orderBy('name')
    ->take(10)
    ->get();
```

Since Eloquent models are query builders, you should review all of the methods provided by Laravel's query builder. You may use any of these methods when writing your Eloquent queries.

#### Refreshing Models

If you already have an instance of an Eloquent model that was retrieved from the database, you can "refresh" the model using the `fresh` and `refresh` methods. The `fresh` method will re-retrieve the model from the database. The existing model instance will not be affected:

```
1$flight = Flight::where('number', 'FR 900')->first();
2 
3$freshFlight = $flight->fresh();

$flight = Flight::where('number', 'FR 900')->first();

$freshFlight = $flight->fresh();
```

The `refresh` method will re-hydrate the existing model using fresh data from the database. In addition, all of its loaded relationships will be refreshed as well:

```
1$flight = Flight::where('number', 'FR 900')->first();
2 
3$flight->number = 'FR 456';
4 
5$flight->refresh();
6 
7$flight->number; // "FR 900"

$flight = Flight::where('number', 'FR 900')->first();

$flight->number = 'FR 456';

$flight->refresh();

$flight->number; // "FR 900"
```

### Collections

As we have seen, Eloquent methods like `all` and `get` retrieve multiple records from the database. However, these methods don't return a plain PHP array. Instead, an instance of `Illuminate\Database\Eloquent\Collection` is returned.

The Eloquent `Collection` class extends Laravel's base `Illuminate\Support\Collection` class, which provides a variety of helpful methods for interacting with data collections. For example, the `reject` method may be used to remove models from a collection based on the results of an invoked closure:

```
1$flights = Flight::where('destination', 'Paris')->get();
2 
3$flights = $flights->reject(function (Flight $flight) {
4    return $flight->cancelled;
5});

$flights = Flight::where('destination', 'Paris')->get();

$flights = $flights->reject(function (Flight $flight) {
    return $flight->cancelled;
});
```

In addition to the methods provided by Laravel's base collection class, the Eloquent collection class provides a few extra methods that are specifically intended for interacting with collections of Eloquent models.

Since all of Laravel's collections implement PHP's iterable interfaces, you may loop over collections as if they were an array:

```
1foreach ($flights as $flight) {
2    echo $flight->name;
3}

foreach ($flights as $flight) {
    echo $flight->name;
}
```

### Chunking Results

Your application may run out of memory if you attempt to load tens of thousands of Eloquent records via the `all` or `get` methods. Instead of using these methods, the `chunk` method may be used to process large numbers of models more efficiently.

The `chunk` method will retrieve a subset of Eloquent models, passing them to a closure for processing. Since only the current chunk of Eloquent models is retrieved at a time, the `chunk` method will provide significantly reduced memory usage when working with a large number of models:

```
1use App\Models\Flight;
2use Illuminate\Database\Eloquent\Collection;
3 
4Flight::chunk(200, function (Collection $flights) {
5    foreach ($flights as $flight) {
6        // ...
7    }
8});

use App\Models\Flight;
use Illuminate\Database\Eloquent\Collection;

Flight::chunk(200, function (Collection $flights) {
    foreach ($flights as $flight) {
        // ...
    }
});
```

The first argument passed to the `chunk` method is the number of records you wish to receive per "chunk". The closure passed as the second argument will be invoked for each chunk that is retrieved from the database. A database query will be executed to retrieve each chunk of records passed to the closure.

If you are filtering the results of the `chunk` method based on a column that you will also be updating while iterating over the results, you should use the `chunkById` method. Using the `chunk` method in these scenarios could lead to unexpected and inconsistent results. Internally, the `chunkById` method will always retrieve models with an `id` column greater than the last model in the previous chunk:

```
1Flight::where('departed', true)
2    ->chunkById(200, function (Collection $flights) {
3        $flights->each->update(['departed' => false]);
4    }, column: 'id');

Flight::where('departed', true)
    ->chunkById(200, function (Collection $flights) {
        $flights->each->update(['departed' => false]);
    }, column: 'id');
```

Since the `chunkById` and `lazyById` methods add their own "where" conditions to the query being executed, you should typically logically group your own conditions within a closure:

```
1Flight::where(function ($query) {
2    $query->where('delayed', true)->orWhere('cancelled', true);
3})->chunkById(200, function (Collection $flights) {
4    $flights->each->update([
5        'departed' => false,
6        'cancelled' => true
7    ]);
8}, column: 'id');

Flight::where(function ($query) {
    $query->where('delayed', true)->orWhere('cancelled', true);
})->chunkById(200, function (Collection $flights) {
    $flights->each->update([
        'departed' => false,
        'cancelled' => true
    ]);
}, column: 'id');
```

### Chunking Using Lazy Collections

The `lazy` method works similarly to the `chunk` method in the sense that, behind the scenes, it executes the query in chunks. However, instead of passing each chunk directly into a callback as is, the `lazy` method returns a flattened `LazyCollection` of Eloquent models, which lets you interact with the results as a single stream:

```
1use App\Models\Flight;
2 
3foreach (Flight::lazy() as $flight) {
4    // ...
5}

use App\Models\Flight;

foreach (Flight::lazy() as $flight) {
    // ...
}
```

If you are filtering the results of the `lazy` method based on a column that you will also be updating while iterating over the results, you should use the `lazyById` method. Internally, the `lazyById` method will always retrieve models with an `id` column greater than the last model in the previous chunk:

```
1Flight::where('departed', true)
2    ->lazyById(200, column: 'id')
3    ->each->update(['departed' => false]);

Flight::where('departed', true)
    ->lazyById(200, column: 'id')
    ->each->update(['departed' => false]);
```

You may filter the results based on the descending order of the `id` using the `lazyByIdDesc` method.

### Cursors

Similar to the `lazy` method, the `cursor` method may be used to significantly reduce your application's memory consumption when iterating through tens of thousands of Eloquent model records.

The `cursor` method will only execute a single database query; however, the individual Eloquent models will not be hydrated until they are actually iterated over. Therefore, only one Eloquent model is kept in memory at any given time while iterating over the cursor.

Since the `cursor` method only ever holds a single Eloquent model in memory at a time, it cannot eager load relationships. If you need to eager load relationships, consider using the `lazy` method instead.

Internally, the `cursor` method uses PHP generators to implement this functionality:

```
1use App\Models\Flight;
2 
3foreach (Flight::where('destination', 'Zurich')->cursor() as $flight) {
4    // ...
5}

use App\Models\Flight;

foreach (Flight::where('destination', 'Zurich')->cursor() as $flight) {
    // ...
}
```

The `cursor` returns an `Illuminate\Support\LazyCollection` instance. Lazy collections allow you to use many of the collection methods available on typical Laravel collections while only loading a single model into memory at a time:

```
1use App\Models\User;
2 
3$users = User::cursor()->filter(function (User $user) {
4    return $user->id > 500;
5});
6 
7foreach ($users as $user) {
8    echo $user->id;
9}

use App\Models\User;

$users = User::cursor()->filter(function (User $user) {
    return $user->id > 500;
});

foreach ($users as $user) {
    echo $user->id;
}
```

Although the `cursor` method uses far less memory than a regular query (by only holding a single Eloquent model in memory at a time), it will still eventually run out of memory. This is due to PHP's PDO driver internally caching all raw query results in its buffer. If you're dealing with a very large number of Eloquent records, consider using the `lazy` method instead.

### Advanced Subqueries

#### Subquery Selects

Eloquent also offers advanced subquery support, which allows you to pull information from related tables in a single query. For example, let's imagine that we have a table of flight `destinations` and a table of `flights` to destinations. The `flights` table contains an `arrived_at` column which indicates when the flight arrived at the destination.

Using the subquery functionality available to the query builder's `select` and `addSelect` methods, we can select all of the `destinations` and the name of the flight that most recently arrived at that destination using a single query:

```
1use App\Models\Destination;
2use App\Models\Flight;
3 
4return Destination::addSelect(['last_flight' => Flight::select('name')
5    ->whereColumn('destination_id', 'destinations.id')
6    ->orderByDesc('arrived_at')
7    ->limit(1)
8])->get();

use App\Models\Destination;
use App\Models\Flight;

return Destination::addSelect(['last_flight' => Flight::select('name')
    ->whereColumn('destination_id', 'destinations.id')
    ->orderByDesc('arrived_at')
    ->limit(1)
])->get();
```

#### Subquery Ordering

In addition, the query builder's `orderBy` function supports subqueries. Continuing to use our flight example, we may use this functionality to sort all destinations based on when the last flight arrived at that destination. Again, this may be done while executing a single database query:

```
1return Destination::orderByDesc(
2    Flight::select('arrived_at')
3        ->whereColumn('destination_id', 'destinations.id')
4        ->orderByDesc('arrived_at')
5        ->limit(1)
6)->get();

return Destination::orderByDesc(
    Flight::select('arrived_at')
        ->whereColumn('destination_id', 'destinations.id')
        ->orderByDesc('arrived_at')
        ->limit(1)
)->get();
```


## Retrieving Single Models / Aggregates

In addition to retrieving all of the records matching a given query, you may also retrieve single records using the `find`, `first`, or `firstWhere` methods. Instead of returning a collection of models, these methods return a single model instance:

```
 1use App\Models\Flight;
 2 
 3// Retrieve a model by its primary key...
 4$flight = Flight::find(1);
 5 
 6// Retrieve the first model matching the query constraints...
 7$flight = Flight::where('active', 1)->first();
 8 
 9// Alternative to retrieving the first model matching the query constraints...
10$flight = Flight::firstWhere('active', 1);

use App\Models\Flight;

// Retrieve a model by its primary key...
$flight = Flight::find(1);

// Retrieve the first model matching the query constraints...
$flight = Flight::where('active', 1)->first();

// Alternative to retrieving the first model matching the query constraints...
$flight = Flight::firstWhere('active', 1);
```

Sometimes you may wish to perform some other action if no results are found. The `findOr` and `firstOr` methods will return a single model instance or, if no results are found, execute the given closure. The value returned by the closure will be considered the result of the method:

```
1$flight = Flight::findOr(1, function () {
2    // ...
3});
4 
5$flight = Flight::where('legs', '>', 3)->firstOr(function () {
6    // ...
7});

$flight = Flight::findOr(1, function () {
    // ...
});

$flight = Flight::where('legs', '>', 3)->firstOr(function () {
    // ...
});
```

#### Not Found Exceptions

Sometimes you may wish to throw an exception if a model is not found. This is particularly useful in routes or controllers. The `findOrFail` and `firstOrFail` methods will retrieve the first result of the query; however, if no result is found, an `Illuminate\Database\Eloquent\ModelNotFoundException` will be thrown:

```
1$flight = Flight::findOrFail(1);
2 
3$flight = Flight::where('legs', '>', 3)->firstOrFail();

$flight = Flight::findOrFail(1);

$flight = Flight::where('legs', '>', 3)->firstOrFail();
```

If the `ModelNotFoundException` is not caught, a 404 HTTP response is automatically sent back to the client:

```
1use App\Models\Flight;
2 
3Route::get('/api/flights/{id}', function (string $id) {
4    return Flight::findOrFail($id);
5});

use App\Models\Flight;

Route::get('/api/flights/{id}', function (string $id) {
    return Flight::findOrFail($id);
});
```

### Retrieving or Creating Models

The `firstOrCreate` method will attempt to locate a database record using the given column / value pairs. If the model cannot be found in the database, a record will be inserted with the attributes resulting from merging the first array argument with the optional second array argument:

The `firstOrNew` method, like `firstOrCreate`, will attempt to locate a record in the database matching the given attributes. However, if a model is not found, a new model instance will be returned. Note that the model returned by `firstOrNew` has not yet been persisted to the database. You will need to manually call the `save` method to persist it:

```
 1use App\Models\Flight;
 2 
 3// Retrieve flight by name or create it if it doesn't exist...
 4$flight = Flight::firstOrCreate([
 5    'name' => 'London to Paris'
 6]);
 7 
 8// Retrieve flight by name or create it with the name, delayed, and arrival_time attributes...
 9$flight = Flight::firstOrCreate(
10    ['name' => 'London to Paris'],
11    ['delayed' => 1, 'arrival_time' => '11:30']
12);
13 
14// Retrieve flight by name or instantiate a new Flight instance...
15$flight = Flight::firstOrNew([
16    'name' => 'London to Paris'
17]);
18 
19// Retrieve flight by name or instantiate with the name, delayed, and arrival_time attributes...
20$flight = Flight::firstOrNew(
21    ['name' => 'Tokyo to Sydney'],
22    ['delayed' => 1, 'arrival_time' => '11:30']
23);

use App\Models\Flight;

// Retrieve flight by name or create it if it doesn't exist...
$flight = Flight::firstOrCreate([
    'name' => 'London to Paris'
]);

// Retrieve flight by name or create it with the name, delayed, and arrival_time attributes...
$flight = Flight::firstOrCreate(
    ['name' => 'London to Paris'],
    ['delayed' => 1, 'arrival_time' => '11:30']
);

// Retrieve flight by name or instantiate a new Flight instance...
$flight = Flight::firstOrNew([
    'name' => 'London to Paris'
]);

// Retrieve flight by name or instantiate with the name, delayed, and arrival_time attributes...
$flight = Flight::firstOrNew(
    ['name' => 'Tokyo to Sydney'],
    ['delayed' => 1, 'arrival_time' => '11:30']
);
```

### Retrieving Aggregates

When interacting with Eloquent models, you may also use the `count`, `sum`, `max`, and other aggregate methods provided by the Laravel query builder. As you might expect, these methods return a scalar value instead of an Eloquent model instance:

```
1$count = Flight::where('active', 1)->count();
2 
3$max = Flight::where('active', 1)->max('price');

$count = Flight::where('active', 1)->count();

$max = Flight::where('active', 1)->max('price');
```
