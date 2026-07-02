---
title: "Eloquent: Getting Started (part 2/3)"
source: https://laravel.com/docs/11.x/eloquent
domain: laravel
license: CC-BY-SA-4.0
tags: laravel framework, eloquent orm, php framework, blade templating
fetched: 2026-07-02
part: 2/3
---

## Inserting and Updating Models

### Inserts

Of course, when using Eloquent, we don't only need to retrieve models from the database. We also need to insert new records. Thankfully, Eloquent makes it simple. To insert a new record into the database, you should instantiate a new model instance and set attributes on the model. Then, call the `save` method on the model instance:

```
 1<?php
 2 
 3namespace App\Http\Controllers;
 4 
 5use App\Http\Controllers\Controller;
 6use App\Models\Flight;
 7use Illuminate\Http\RedirectResponse;
 8use Illuminate\Http\Request;
 9 
10class FlightController extends Controller
11{
12    /**
13     * Store a new flight in the database.
14     */
15    public function store(Request $request): RedirectResponse
16    {
17        // Validate the request...
18 
19        $flight = new Flight;
20 
21        $flight->name = $request->name;
22 
23        $flight->save();
24 
25        return redirect('/flights');
26    }
27}

<?php

namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\Models\Flight;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;

class FlightController extends Controller
{
    /**
     * Store a new flight in the database.
     */
    public function store(Request $request): RedirectResponse
    {
        // Validate the request...

        $flight = new Flight;

        $flight->name = $request->name;

        $flight->save();

        return redirect('/flights');
    }
}
```

In this example, we assign the `name` field from the incoming HTTP request to the `name` attribute of the `App\Models\Flight` model instance. When we call the `save` method, a record will be inserted into the database. The model's `created_at` and `updated_at` timestamps will automatically be set when the `save` method is called, so there is no need to set them manually.

Alternatively, you may use the `create` method to "save" a new model using a single PHP statement. The inserted model instance will be returned to you by the `create` method:

```
1use App\Models\Flight;
2 
3$flight = Flight::create([
4    'name' => 'London to Paris',
5]);

use App\Models\Flight;

$flight = Flight::create([
    'name' => 'London to Paris',
]);
```

However, before using the `create` method, you will need to specify either a `fillable` or `guarded` property on your model class. These properties are required because all Eloquent models are protected against mass assignment vulnerabilities by default. To learn more about mass assignment, please consult the mass assignment documentation.

### Updates

The `save` method may also be used to update models that already exist in the database. To update a model, you should retrieve it and set any attributes you wish to update. Then, you should call the model's `save` method. Again, the `updated_at` timestamp will automatically be updated, so there is no need to manually set its value:

```
1use App\Models\Flight;
2 
3$flight = Flight::find(1);
4 
5$flight->name = 'Paris to London';
6 
7$flight->save();

use App\Models\Flight;

$flight = Flight::find(1);

$flight->name = 'Paris to London';

$flight->save();
```

Occasionally, you may need to update an existing model or create a new model if no matching model exists. Like the `firstOrCreate` method, the `updateOrCreate` method persists the model, so there's no need to manually call the `save` method.

In the example below, if a flight exists with a `departure` location of `Oakland` and a `destination` location of `San Diego`, its `price` and `discounted` columns will be updated. If no such flight exists, a new flight will be created which has the attributes resulting from merging the first argument array with the second argument array:

```
1$flight = Flight::updateOrCreate(
2    ['departure' => 'Oakland', 'destination' => 'San Diego'],
3    ['price' => 99, 'discounted' => 1]
4);

$flight = Flight::updateOrCreate(
    ['departure' => 'Oakland', 'destination' => 'San Diego'],
    ['price' => 99, 'discounted' => 1]
);
```

#### Mass Updates

Updates can also be performed against models that match a given query. In this example, all flights that are `active` and have a `destination` of `San Diego` will be marked as delayed:

```
1Flight::where('active', 1)
2    ->where('destination', 'San Diego')
3    ->update(['delayed' => 1]);

Flight::where('active', 1)
    ->where('destination', 'San Diego')
    ->update(['delayed' => 1]);
```

The `update` method expects an array of column and value pairs representing the columns that should be updated. The `update` method returns the number of affected rows.

When issuing a mass update via Eloquent, the `saving`, `saved`, `updating`, and `updated` model events will not be fired for the updated models. This is because the models are never actually retrieved when issuing a mass update.

#### Examining Attribute Changes

Eloquent provides the `isDirty`, `isClean`, and `wasChanged` methods to examine the internal state of your model and determine how its attributes have changed from when the model was originally retrieved.

The `isDirty` method determines if any of the model's attributes have been changed since the model was retrieved. You may pass a specific attribute name or an array of attributes to the `isDirty` method to determine if any of the attributes are "dirty". The `isClean` method will determine if an attribute has remained unchanged since the model was retrieved. This method also accepts an optional attribute argument:

```
 1use App\Models\User;
 2 
 3$user = User::create([
 4    'first_name' => 'Taylor',
 5    'last_name' => 'Otwell',
 6    'title' => 'Developer',
 7]);
 8 
 9$user->title = 'Painter';
10 
11$user->isDirty(); // true
12$user->isDirty('title'); // true
13$user->isDirty('first_name'); // false
14$user->isDirty(['first_name', 'title']); // true
15 
16$user->isClean(); // false
17$user->isClean('title'); // false
18$user->isClean('first_name'); // true
19$user->isClean(['first_name', 'title']); // false
20 
21$user->save();
22 
23$user->isDirty(); // false
24$user->isClean(); // true

use App\Models\User;

$user = User::create([
    'first_name' => 'Taylor',
    'last_name' => 'Otwell',
    'title' => 'Developer',
]);

$user->title = 'Painter';

$user->isDirty(); // true
$user->isDirty('title'); // true
$user->isDirty('first_name'); // false
$user->isDirty(['first_name', 'title']); // true

$user->isClean(); // false
$user->isClean('title'); // false
$user->isClean('first_name'); // true
$user->isClean(['first_name', 'title']); // false

$user->save();

$user->isDirty(); // false
$user->isClean(); // true
```

The `wasChanged` method determines if any attributes were changed when the model was last saved within the current request cycle. If needed, you may pass an attribute name to see if a particular attribute was changed:

```
 1$user = User::create([
 2    'first_name' => 'Taylor',
 3    'last_name' => 'Otwell',
 4    'title' => 'Developer',
 5]);
 6 
 7$user->title = 'Painter';
 8 
 9$user->save();
10 
11$user->wasChanged(); // true
12$user->wasChanged('title'); // true
13$user->wasChanged(['title', 'slug']); // true
14$user->wasChanged('first_name'); // false
15$user->wasChanged(['first_name', 'title']); // true

$user = User::create([
    'first_name' => 'Taylor',
    'last_name' => 'Otwell',
    'title' => 'Developer',
]);

$user->title = 'Painter';

$user->save();

$user->wasChanged(); // true
$user->wasChanged('title'); // true
$user->wasChanged(['title', 'slug']); // true
$user->wasChanged('first_name'); // false
$user->wasChanged(['first_name', 'title']); // true
```

The `getOriginal` method returns an array containing the original attributes of the model regardless of any changes to the model since it was retrieved. If needed, you may pass a specific attribute name to get the original value of a particular attribute:

```
 1$user = User::find(1);
 2 
 3$user->name; // John
 4$user->email; // [email protected]
 5 
 6$user->name = "Jack";
 7$user->name; // Jack
 8 
 9$user->getOriginal('name'); // John
10$user->getOriginal(); // Array of original attributes...

$user = User::find(1);

$user->name; // John
$user->email; // [email protected]

$user->name = "Jack";
$user->name; // Jack

$user->getOriginal('name'); // John
$user->getOriginal(); // Array of original attributes...
```

### Mass Assignment

You may use the `create` method to "save" a new model using a single PHP statement. The inserted model instance will be returned to you by the method:

```
1use App\Models\Flight;
2 
3$flight = Flight::create([
4    'name' => 'London to Paris',
5]);

use App\Models\Flight;

$flight = Flight::create([
    'name' => 'London to Paris',
]);
```

However, before using the `create` method, you will need to specify either a `fillable` or `guarded` property on your model class. These properties are required because all Eloquent models are protected against mass assignment vulnerabilities by default.

A mass assignment vulnerability occurs when a user passes an unexpected HTTP request field and that field changes a column in your database that you did not expect. For example, a malicious user might send an `is_admin` parameter through an HTTP request, which is then passed to your model's `create` method, allowing the user to escalate themselves to an administrator.

So, to get started, you should define which model attributes you want to make mass assignable. You may do this using the `$fillable` property on the model. For example, let's make the `name` attribute of our `Flight` model mass assignable:

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
10     * The attributes that are mass assignable.
11     *
12     * @var array<int, string>
13     */
14    protected $fillable = ['name'];
15}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Flight extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $fillable = ['name'];
}
```

Once you have specified which attributes are mass assignable, you may use the `create` method to insert a new record in the database. The `create` method returns the newly created model instance:

```
1$flight = Flight::create(['name' => 'London to Paris']);

$flight = Flight::create(['name' => 'London to Paris']);
```

If you already have a model instance, you may use the `fill` method to populate it with an array of attributes:

```
1$flight->fill(['name' => 'Amsterdam to Frankfurt']);

$flight->fill(['name' => 'Amsterdam to Frankfurt']);
```

#### Mass Assignment and JSON Columns

When assigning JSON columns, each column's mass assignable key must be specified in your model's `$fillable` array. For security, Laravel does not support updating nested JSON attributes when using the `guarded` property:

```
1/**
2 * The attributes that are mass assignable.
3 *
4 * @var array<int, string>
5 */
6protected $fillable = [
7    'options->enabled',
8];

/**
 * The attributes that are mass assignable.
 *
 * @var array<int, string>
 */
protected $fillable = [
    'options->enabled',
];
```

#### Allowing Mass Assignment

If you would like to make all of your attributes mass assignable, you may define your model's `$guarded` property as an empty array. If you choose to unguard your model, you should take special care to always hand-craft the arrays passed to Eloquent's `fill`, `create`, and `update` methods:

```
1/**
2 * The attributes that aren't mass assignable.
3 *
4 * @var array<string>|bool
5 */
6protected $guarded = [];

/**
 * The attributes that aren't mass assignable.
 *
 * @var array<string>|bool
 */
protected $guarded = [];
```

#### Mass Assignment Exceptions

By default, attributes that are not included in the `$fillable` array are silently discarded when performing mass-assignment operations. In production, this is expected behavior; however, during local development it can lead to confusion as to why model changes are not taking effect.

If you wish, you may instruct Laravel to throw an exception when attempting to fill an unfillable attribute by invoking the `preventSilentlyDiscardingAttributes` method. Typically, this method should be invoked in the `boot` method of your application's `AppServiceProvider` class:

```
1use Illuminate\Database\Eloquent\Model;
2 
3/**
4 * Bootstrap any application services.
5 */
6public function boot(): void
7{
8    Model::preventSilentlyDiscardingAttributes($this->app->isLocal());
9}

use Illuminate\Database\Eloquent\Model;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    Model::preventSilentlyDiscardingAttributes($this->app->isLocal());
}
```

### Upserts

Eloquent's `upsert` method may be used to update or create records in a single, atomic operation. The method's first argument consists of the values to insert or update, while the second argument lists the column(s) that uniquely identify records within the associated table. The method's third and final argument is an array of the columns that should be updated if a matching record already exists in the database. The `upsert` method will automatically set the `created_at` and `updated_at` timestamps if timestamps are enabled on the model:

```
1Flight::upsert([
2    ['departure' => 'Oakland', 'destination' => 'San Diego', 'price' => 99],
3    ['departure' => 'Chicago', 'destination' => 'New York', 'price' => 150]
4], uniqueBy: ['departure', 'destination'], update: ['price']);

Flight::upsert([
    ['departure' => 'Oakland', 'destination' => 'San Diego', 'price' => 99],
    ['departure' => 'Chicago', 'destination' => 'New York', 'price' => 150]
], uniqueBy: ['departure', 'destination'], update: ['price']);
```

All databases except SQL Server require the columns in the second argument of the `upsert` method to have a "primary" or "unique" index. In addition, the MariaDB and MySQL database drivers ignore the second argument of the `upsert` method and always use the "primary" and "unique" indexes of the table to detect existing records.


## Deleting Models

To delete a model, you may call the `delete` method on the model instance:

```
1use App\Models\Flight;
2 
3$flight = Flight::find(1);
4 
5$flight->delete();

use App\Models\Flight;

$flight = Flight::find(1);

$flight->delete();
```

#### Deleting an Existing Model by its Primary Key

In the example above, we are retrieving the model from the database before calling the `delete` method. However, if you know the primary key of the model, you may delete the model without explicitly retrieving it by calling the `destroy` method. In addition to accepting the single primary key, the `destroy` method will accept multiple primary keys, an array of primary keys, or a collection of primary keys:

```
1Flight::destroy(1);
2 
3Flight::destroy(1, 2, 3);
4 
5Flight::destroy([1, 2, 3]);
6 
7Flight::destroy(collect([1, 2, 3]));

Flight::destroy(1);

Flight::destroy(1, 2, 3);

Flight::destroy([1, 2, 3]);

Flight::destroy(collect([1, 2, 3]));
```

If you are utilizing soft deleting models, you may permanently delete models via the `forceDestroy` method:

```
1Flight::forceDestroy(1);

Flight::forceDestroy(1);
```

The `destroy` method loads each model individually and calls the `delete` method so that the `deleting` and `deleted` events are properly dispatched for each model.

#### Deleting Models Using Queries

Of course, you may build an Eloquent query to delete all models matching your query's criteria. In this example, we will delete all flights that are marked as inactive. Like mass updates, mass deletes will not dispatch model events for the models that are deleted:

```
1$deleted = Flight::where('active', 0)->delete();

$deleted = Flight::where('active', 0)->delete();
```

To delete all models in a table, you should execute a query without adding any conditions:

```
1$deleted = Flight::query()->delete();

$deleted = Flight::query()->delete();
```

When executing a mass delete statement via Eloquent, the `deleting` and `deleted` model events will not be dispatched for the deleted models. This is because the models are never actually retrieved when executing the delete statement.

### Soft Deleting

In addition to actually removing records from your database, Eloquent can also "soft delete" models. When models are soft deleted, they are not actually removed from your database. Instead, a `deleted_at` attribute is set on the model indicating the date and time at which the model was "deleted". To enable soft deletes for a model, add the `Illuminate\Database\Eloquent\SoftDeletes` trait to the model:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Model;
 6use Illuminate\Database\Eloquent\SoftDeletes;
 7 
 8class Flight extends Model
 9{
10    use SoftDeletes;
11}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Flight extends Model
{
    use SoftDeletes;
}
```

The `SoftDeletes` trait will automatically cast the `deleted_at` attribute to a `DateTime` / `Carbon` instance for you.

You should also add the `deleted_at` column to your database table. The Laravel schema builder contains a helper method to create this column:

```
 1use Illuminate\Database\Schema\Blueprint;
 2use Illuminate\Support\Facades\Schema;
 3 
 4Schema::table('flights', function (Blueprint $table) {
 5    $table->softDeletes();
 6});
 7 
 8Schema::table('flights', function (Blueprint $table) {
 9    $table->dropSoftDeletes();
10});

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

Schema::table('flights', function (Blueprint $table) {
    $table->softDeletes();
});

Schema::table('flights', function (Blueprint $table) {
    $table->dropSoftDeletes();
});
```

Now, when you call the `delete` method on the model, the `deleted_at` column will be set to the current date and time. However, the model's database record will be left in the table. When querying a model that uses soft deletes, the soft deleted models will automatically be excluded from all query results.

To determine if a given model instance has been soft deleted, you may use the `trashed` method:

```
1if ($flight->trashed()) {
2    // ...
3}

if ($flight->trashed()) {
    // ...
}
```

#### Restoring Soft Deleted Models

Sometimes you may wish to "un-delete" a soft deleted model. To restore a soft deleted model, you may call the `restore` method on a model instance. The `restore` method will set the model's `deleted_at` column to `null`:

```
1$flight->restore();

$flight->restore();
```

You may also use the `restore` method in a query to restore multiple models. Again, like other "mass" operations, this will not dispatch any model events for the models that are restored:

```
1Flight::withTrashed()
2        ->where('airline_id', 1)
3        ->restore();

Flight::withTrashed()
        ->where('airline_id', 1)
        ->restore();
```

The `restore` method may also be used when building relationship queries:

```
1$flight->history()->restore();

$flight->history()->restore();
```

#### Permanently Deleting Models

Sometimes you may need to truly remove a model from your database. You may use the `forceDelete` method to permanently remove a soft deleted model from the database table:

```
1$flight->forceDelete();

$flight->forceDelete();
```

You may also use the `forceDelete` method when building Eloquent relationship queries:

```
1$flight->history()->forceDelete();

$flight->history()->forceDelete();
```

### Querying Soft Deleted Models

#### Including Soft Deleted Models

As noted above, soft deleted models will automatically be excluded from query results. However, you may force soft deleted models to be included in a query's results by calling the `withTrashed` method on the query:

```
1use App\Models\Flight;
2 
3$flights = Flight::withTrashed()
4    ->where('account_id', 1)
5    ->get();

use App\Models\Flight;

$flights = Flight::withTrashed()
    ->where('account_id', 1)
    ->get();
```

The `withTrashed` method may also be called when building a relationship query:

```
1$flight->history()->withTrashed()->get();

$flight->history()->withTrashed()->get();
```

#### Retrieving Only Soft Deleted Models

The `onlyTrashed` method will retrieve **only** soft deleted models:

```
1$flights = Flight::onlyTrashed()
2    ->where('airline_id', 1)
3    ->get();

$flights = Flight::onlyTrashed()
    ->where('airline_id', 1)
    ->get();
```


## Pruning Models

Sometimes you may want to periodically delete models that are no longer needed. To accomplish this, you may add the `Illuminate\Database\Eloquent\Prunable` or `Illuminate\Database\Eloquent\MassPrunable` trait to the models you would like to periodically prune. After adding one of the traits to the model, implement a `prunable` method which returns an Eloquent query builder that resolves the models that are no longer needed:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Builder;
 6use Illuminate\Database\Eloquent\Model;
 7use Illuminate\Database\Eloquent\Prunable;
 8 
 9class Flight extends Model
10{
11    use Prunable;
12 
13    /**
14     * Get the prunable model query.
15     */
16    public function prunable(): Builder
17    {
18        return static::where('created_at', '<=', now()->subMonth());
19    }
20}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Prunable;

class Flight extends Model
{
    use Prunable;

    /**
     * Get the prunable model query.
     */
    public function prunable(): Builder
    {
        return static::where('created_at', '<=', now()->subMonth());
    }
}
```

When marking models as `Prunable`, you may also define a `pruning` method on the model. This method will be called before the model is deleted. This method can be useful for deleting any additional resources associated with the model, such as stored files, before the model is permanently removed from the database:

```
1/**
2 * Prepare the model for pruning.
3 */
4protected function pruning(): void
5{
6    // ...
7}

/**
 * Prepare the model for pruning.
 */
protected function pruning(): void
{
    // ...
}
```

After configuring your prunable model, you should schedule the `model:prune` Artisan command in your application's `routes/console.php` file. You are free to choose the appropriate interval at which this command should be run:

```
1use Illuminate\Support\Facades\Schedule;
2 
3Schedule::command('model:prune')->daily();

use Illuminate\Support\Facades\Schedule;

Schedule::command('model:prune')->daily();
```

Behind the scenes, the `model:prune` command will automatically detect "Prunable" models within your application's `app/Models` directory. If your models are in a different location, you may use the `--model` option to specify the model class names:

```
1Schedule::command('model:prune', [
2    '--model' => [Address::class, Flight::class],
3])->daily();

Schedule::command('model:prune', [
    '--model' => [Address::class, Flight::class],
])->daily();
```

If you wish to exclude certain models from being pruned while pruning all other detected models, you may use the `--except` option:

```
1Schedule::command('model:prune', [
2    '--except' => [Address::class, Flight::class],
3])->daily();

Schedule::command('model:prune', [
    '--except' => [Address::class, Flight::class],
])->daily();
```

You may test your `prunable` query by executing the `model:prune` command with the `--pretend` option. When pretending, the `model:prune` command will simply report how many records would be pruned if the command were to actually run:

```
1php artisan model:prune --pretend

php artisan model:prune --pretend
```

Soft deleting models will be permanently deleted (`forceDelete`) if they match the prunable query.

#### Mass Pruning

When models are marked with the `Illuminate\Database\Eloquent\MassPrunable` trait, models are deleted from the database using mass-deletion queries. Therefore, the `pruning` method will not be invoked, nor will the `deleting` and `deleted` model events be dispatched. This is because the models are never actually retrieved before deletion, thus making the pruning process much more efficient:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Builder;
 6use Illuminate\Database\Eloquent\Model;
 7use Illuminate\Database\Eloquent\MassPrunable;
 8 
 9class Flight extends Model
10{
11    use MassPrunable;
12 
13    /**
14     * Get the prunable model query.
15     */
16    public function prunable(): Builder
17    {
18        return static::where('created_at', '<=', now()->subMonth());
19    }
20}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\MassPrunable;

class Flight extends Model
{
    use MassPrunable;

    /**
     * Get the prunable model query.
     */
    public function prunable(): Builder
    {
        return static::where('created_at', '<=', now()->subMonth());
    }
}
```


## Replicating Models

You may create an unsaved copy of an existing model instance using the `replicate` method. This method is particularly useful when you have model instances that share many of the same attributes:

```
 1use App\Models\Address;
 2 
 3$shipping = Address::create([
 4    'type' => 'shipping',
 5    'line_1' => '123 Example Street',
 6    'city' => 'Victorville',
 7    'state' => 'CA',
 8    'postcode' => '90001',
 9]);
10 
11$billing = $shipping->replicate()->fill([
12    'type' => 'billing'
13]);
14 
15$billing->save();

use App\Models\Address;

$shipping = Address::create([
    'type' => 'shipping',
    'line_1' => '123 Example Street',
    'city' => 'Victorville',
    'state' => 'CA',
    'postcode' => '90001',
]);

$billing = $shipping->replicate()->fill([
    'type' => 'billing'
]);

$billing->save();
```

To exclude one or more attributes from being replicated to the new model, you may pass an array to the `replicate` method:

```
 1$flight = Flight::create([
 2    'destination' => 'LAX',
 3    'origin' => 'LHR',
 4    'last_flown' => '2020-03-04 11:00:00',
 5    'last_pilot_id' => 747,
 6]);
 7 
 8$flight = $flight->replicate([
 9    'last_flown',
10    'last_pilot_id'
11]);

$flight = Flight::create([
    'destination' => 'LAX',
    'origin' => 'LHR',
    'last_flown' => '2020-03-04 11:00:00',
    'last_pilot_id' => 747,
]);

$flight = $flight->replicate([
    'last_flown',
    'last_pilot_id'
]);
```


## Query Scopes

### Global Scopes

Global scopes allow you to add constraints to all queries for a given model. Laravel's own soft delete functionality utilizes global scopes to only retrieve "non-deleted" models from the database. Writing your own global scopes can provide a convenient, easy way to make sure every query for a given model receives certain constraints.

#### Generating Scopes

To generate a new global scope, you may invoke the `make:scope` Artisan command, which will place the generated scope in your application's `app/Models/Scopes` directory:

```
1php artisan make:scope AncientScope

php artisan make:scope AncientScope
```

#### Writing Global Scopes

Writing a global scope is simple. First, use the `make:scope` command to generate a class that implements the `Illuminate\Database\Eloquent\Scope` interface. The `Scope` interface requires you to implement one method: `apply`. The `apply` method may add `where` constraints or other types of clauses to the query as needed:

```
 1<?php
 2 
 3namespace App\Models\Scopes;
 4 
 5use Illuminate\Database\Eloquent\Builder;
 6use Illuminate\Database\Eloquent\Model;
 7use Illuminate\Database\Eloquent\Scope;
 8 
 9class AncientScope implements Scope
10{
11    /**
12     * Apply the scope to a given Eloquent query builder.
13     */
14    public function apply(Builder $builder, Model $model): void
15    {
16        $builder->where('created_at', '<', now()->subYears(2000));
17    }
18}

<?php

namespace App\Models\Scopes;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Scope;

class AncientScope implements Scope
{
    /**
     * Apply the scope to a given Eloquent query builder.
     */
    public function apply(Builder $builder, Model $model): void
    {
        $builder->where('created_at', '<', now()->subYears(2000));
    }
}
```

If your global scope is adding columns to the select clause of the query, you should use the `addSelect` method instead of `select`. This will prevent the unintentional replacement of the query's existing select clause.

#### Applying Global Scopes

To assign a global scope to a model, you may simply place the `ScopedBy` attribute on the model:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use App\Models\Scopes\AncientScope;
 6use Illuminate\Database\Eloquent\Attributes\ScopedBy;
 7 
 8#[ScopedBy([AncientScope::class])]
 9class User extends Model
10{
11    //
12}

<?php

namespace App\Models;

use App\Models\Scopes\AncientScope;
use Illuminate\Database\Eloquent\Attributes\ScopedBy;

#[ScopedBy([AncientScope::class])]
class User extends Model
{
    //
}
```

Or, you may manually register the global scope by overriding the model's `booted` method and invoke the model's `addGlobalScope` method. The `addGlobalScope` method accepts an instance of your scope as its only argument:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use App\Models\Scopes\AncientScope;
 6use Illuminate\Database\Eloquent\Model;
 7 
 8class User extends Model
 9{
10    /**
11     * The "booted" method of the model.
12     */
13    protected static function booted(): void
14    {
15        static::addGlobalScope(new AncientScope);
16    }
17}

<?php

namespace App\Models;

use App\Models\Scopes\AncientScope;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * The "booted" method of the model.
     */
    protected static function booted(): void
    {
        static::addGlobalScope(new AncientScope);
    }
}
```

After adding the scope in the example above to the `App\Models\User` model, a call to the `User::all()` method will execute the following SQL query:

```
1select * from `users` where `created_at` < 0021-02-18 00:00:00

select * from `users` where `created_at` < 0021-02-18 00:00:00
```

#### Anonymous Global Scopes

Eloquent also allows you to define global scopes using closures, which is particularly useful for simple scopes that do not warrant a separate class of their own. When defining a global scope using a closure, you should provide a scope name of your own choosing as the first argument to the `addGlobalScope` method:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Builder;
 6use Illuminate\Database\Eloquent\Model;
 7 
 8class User extends Model
 9{
10    /**
11     * The "booted" method of the model.
12     */
13    protected static function booted(): void
14    {
15        static::addGlobalScope('ancient', function (Builder $builder) {
16            $builder->where('created_at', '<', now()->subYears(2000));
17        });
18    }
19}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * The "booted" method of the model.
     */
    protected static function booted(): void
    {
        static::addGlobalScope('ancient', function (Builder $builder) {
            $builder->where('created_at', '<', now()->subYears(2000));
        });
    }
}
```

#### Removing Global Scopes

If you would like to remove a global scope for a given query, you may use the `withoutGlobalScope` method. This method accepts the class name of the global scope as its only argument:

```
1User::withoutGlobalScope(AncientScope::class)->get();

User::withoutGlobalScope(AncientScope::class)->get();
```

Or, if you defined the global scope using a closure, you should pass the string name that you assigned to the global scope:

```
1User::withoutGlobalScope('ancient')->get();

User::withoutGlobalScope('ancient')->get();
```

If you would like to remove several or even all of the query's global scopes, you may use the `withoutGlobalScopes` method:

```
1// Remove all of the global scopes...
2User::withoutGlobalScopes()->get();
3 
4// Remove some of the global scopes...
5User::withoutGlobalScopes([
6    FirstScope::class, SecondScope::class
7])->get();

// Remove all of the global scopes...
User::withoutGlobalScopes()->get();

// Remove some of the global scopes...
User::withoutGlobalScopes([
    FirstScope::class, SecondScope::class
])->get();
```

### Local Scopes

Local scopes allow you to define common sets of query constraints that you may easily re-use throughout your application. For example, you may need to frequently retrieve all users that are considered "popular". To define a scope, prefix an Eloquent model method with `scope`.

Scopes should always return the same query builder instance or `void`:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Builder;
 6use Illuminate\Database\Eloquent\Model;
 7 
 8class User extends Model
 9{
10    /**
11     * Scope a query to only include popular users.
12     */
13    public function scopePopular(Builder $query): void
14    {
15        $query->where('votes', '>', 100);
16    }
17 
18    /**
19     * Scope a query to only include active users.
20     */
21    public function scopeActive(Builder $query): void
22    {
23        $query->where('active', 1);
24    }
25}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * Scope a query to only include popular users.
     */
    public function scopePopular(Builder $query): void
    {
        $query->where('votes', '>', 100);
    }

    /**
     * Scope a query to only include active users.
     */
    public function scopeActive(Builder $query): void
    {
        $query->where('active', 1);
    }
}
```

#### Utilizing a Local Scope

Once the scope has been defined, you may call the scope methods when querying the model. However, you should not include the `scope` prefix when calling the method. You can even chain calls to various scopes:

```
1use App\Models\User;
2 
3$users = User::popular()->active()->orderBy('created_at')->get();

use App\Models\User;

$users = User::popular()->active()->orderBy('created_at')->get();
```

Combining multiple Eloquent model scopes via an `or` query operator may require the use of closures to achieve the correct logical grouping:

```
1$users = User::popular()->orWhere(function (Builder $query) {
2    $query->active();
3})->get();

$users = User::popular()->orWhere(function (Builder $query) {
    $query->active();
})->get();
```

However, since this can be cumbersome, Laravel provides a "higher order" `orWhere` method that allows you to fluently chain scopes together without the use of closures:

```
1$users = User::popular()->orWhere->active()->get();

$users = User::popular()->orWhere->active()->get();
```

#### Dynamic Scopes

Sometimes you may wish to define a scope that accepts parameters. To get started, just add your additional parameters to your scope method's signature. Scope parameters should be defined after the `$query` parameter:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Builder;
 6use Illuminate\Database\Eloquent\Model;
 7 
 8class User extends Model
 9{
10    /**
11     * Scope a query to only include users of a given type.
12     */
13    public function scopeOfType(Builder $query, string $type): void
14    {
15        $query->where('type', $type);
16    }
17}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * Scope a query to only include users of a given type.
     */
    public function scopeOfType(Builder $query, string $type): void
    {
        $query->where('type', $type);
    }
}
```

Once the expected arguments have been added to your scope method's signature, you may pass the arguments when calling the scope:

```
1$users = User::ofType('admin')->get();

$users = User::ofType('admin')->get();
```

### Pending Attributes

If you would like to use scopes to create models that have the same attributes as those used to constrain the scope, you may use the `withAttributes` method when building the scope query:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Builder;
 6use Illuminate\Database\Eloquent\Model;
 7 
 8class Post extends Model
 9{
10    /**
11     * Scope the query to only include drafts.
12     */
13    public function scopeDraft(Builder $query): void
14    {
15        $query->withAttributes([
16            'hidden' => true,
17        ]);
18    }
19}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    /**
     * Scope the query to only include drafts.
     */
    public function scopeDraft(Builder $query): void
    {
        $query->withAttributes([
            'hidden' => true,
        ]);
    }
}
```

The `withAttributes` method will add `where` clause constraints to the query using the given attributes, and it will also add the given attributes to any models created via the scope:

```
1$draft = Post::draft()->create(['title' => 'In Progress']);
2 
3$draft->hidden; // true

$draft = Post::draft()->create(['title' => 'In Progress']);

$draft->hidden; // true
```


## Comparing Models

Sometimes you may need to determine if two models are the "same" or not. The `is` and `isNot` methods may be used to quickly verify two models have the same primary key, table, and database connection or not:

```
1if ($post->is($anotherPost)) {
2    // ...
3}
4 
5if ($post->isNot($anotherPost)) {
6    // ...
7}

if ($post->is($anotherPost)) {
    // ...
}

if ($post->isNot($anotherPost)) {
    // ...
}
```

The `is` and `isNot` methods are also available when using the `belongsTo`, `hasOne`, `morphTo`, and `morphOne` relationships. This method is particularly helpful when you would like to compare a related model without issuing a query to retrieve that model:

```
1if ($post->author()->is($user)) {
2    // ...
3}

if ($post->author()->is($user)) {
    // ...
}
```
