---
title: "Eloquent: Getting Started (part 3/3)"
source: https://laravel.com/docs/11.x/eloquent
domain: laravel
license: CC-BY-SA-4.0
tags: laravel framework, eloquent orm, php framework, blade templating
fetched: 2026-07-02
part: 3/3
---

## Events

Want to broadcast your Eloquent events directly to your client-side application? Check out Laravel's model event broadcasting.

Eloquent models dispatch several events, allowing you to hook into the following moments in a model's lifecycle: `retrieved`, `creating`, `created`, `updating`, `updated`, `saving`, `saved`, `deleting`, `deleted`, `trashed`, `forceDeleting`, `forceDeleted`, `restoring`, `restored`, and `replicating`.

The `retrieved` event will dispatch when an existing model is retrieved from the database. When a new model is saved for the first time, the `creating` and `created` events will dispatch. The `updating` / `updated` events will dispatch when an existing model is modified and the `save` method is called. The `saving` / `saved` events will dispatch when a model is created or updated - even if the model's attributes have not been changed. Event names ending with `-ing` are dispatched before any changes to the model are persisted, while events ending with `-ed` are dispatched after the changes to the model are persisted.

To start listening to model events, define a `$dispatchesEvents` property on your Eloquent model. This property maps various points of the Eloquent model's lifecycle to your own event classes. Each model event class should expect to receive an instance of the affected model via its constructor:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use App\Events\UserDeleted;
 6use App\Events\UserSaved;
 7use Illuminate\Foundation\Auth\User as Authenticatable;
 8use Illuminate\Notifications\Notifiable;
 9 
10class User extends Authenticatable
11{
12    use Notifiable;
13 
14    /**
15     * The event map for the model.
16     *
17     * @var array<string, string>
18     */
19    protected $dispatchesEvents = [
20        'saved' => UserSaved::class,
21        'deleted' => UserDeleted::class,
22    ];
23}

<?php

namespace App\Models;

use App\Events\UserDeleted;
use App\Events\UserSaved;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use Notifiable;

    /**
     * The event map for the model.
     *
     * @var array<string, string>
     */
    protected $dispatchesEvents = [
        'saved' => UserSaved::class,
        'deleted' => UserDeleted::class,
    ];
}
```

After defining and mapping your Eloquent events, you may use event listeners to handle the events.

When issuing a mass update or delete query via Eloquent, the `saved`, `updated`, `deleting`, and `deleted` model events will not be dispatched for the affected models. This is because the models are never actually retrieved when performing mass updates or deletes.

### Using Closures

Instead of using custom event classes, you may register closures that execute when various model events are dispatched. Typically, you should register these closures in the `booted` method of your model:

```
 1<?php
 2 
 3namespace App\Models;
 4 
 5use Illuminate\Database\Eloquent\Model;
 6 
 7class User extends Model
 8{
 9    /**
10     * The "booted" method of the model.
11     */
12    protected static function booted(): void
13    {
14        static::created(function (User $user) {
15            // ...
16        });
17    }
18}

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    /**
     * The "booted" method of the model.
     */
    protected static function booted(): void
    {
        static::created(function (User $user) {
            // ...
        });
    }
}
```

If needed, you may utilize queueable anonymous event listeners when registering model events. This will instruct Laravel to execute the model event listener in the background using your application's queue:

```
1use function Illuminate\Events\queueable;
2 
3static::created(queueable(function (User $user) {
4    // ...
5}));

use function Illuminate\Events\queueable;

static::created(queueable(function (User $user) {
    // ...
}));
```

### Observers

#### Defining Observers

If you are listening for many events on a given model, you may use observers to group all of your listeners into a single class. Observer classes have method names which reflect the Eloquent events you wish to listen for. Each of these methods receives the affected model as their only argument. The `make:observer` Artisan command is the easiest way to create a new observer class:

```
1php artisan make:observer UserObserver --model=User

php artisan make:observer UserObserver --model=User
```

This command will place the new observer in your `app/Observers` directory. If this directory does not exist, Artisan will create it for you. Your fresh observer will look like the following:

```
 1<?php
 2 
 3namespace App\Observers;
 4 
 5use App\Models\User;
 6 
 7class UserObserver
 8{
 9    /**
10     * Handle the User "created" event.
11     */
12    public function created(User $user): void
13    {
14        // ...
15    }
16 
17    /**
18     * Handle the User "updated" event.
19     */
20    public function updated(User $user): void
21    {
22        // ...
23    }
24 
25    /**
26     * Handle the User "deleted" event.
27     */
28    public function deleted(User $user): void
29    {
30        // ...
31    }
32 
33    /**
34     * Handle the User "restored" event.
35     */
36    public function restored(User $user): void
37    {
38        // ...
39    }
40 
41    /**
42     * Handle the User "forceDeleted" event.
43     */
44    public function forceDeleted(User $user): void
45    {
46        // ...
47    }
48}

<?php

namespace App\Observers;

use App\Models\User;

class UserObserver
{
    /**
     * Handle the User "created" event.
     */
    public function created(User $user): void
    {
        // ...
    }

    /**
     * Handle the User "updated" event.
     */
    public function updated(User $user): void
    {
        // ...
    }

    /**
     * Handle the User "deleted" event.
     */
    public function deleted(User $user): void
    {
        // ...
    }

    /**
     * Handle the User "restored" event.
     */
    public function restored(User $user): void
    {
        // ...
    }

    /**
     * Handle the User "forceDeleted" event.
     */
    public function forceDeleted(User $user): void
    {
        // ...
    }
}
```

To register an observer, you may place the `ObservedBy` attribute on the corresponding model:

```
1use App\Observers\UserObserver;
2use Illuminate\Database\Eloquent\Attributes\ObservedBy;
3 
4#[ObservedBy([UserObserver::class])]
5class User extends Authenticatable
6{
7    //
8}

use App\Observers\UserObserver;
use Illuminate\Database\Eloquent\Attributes\ObservedBy;

#[ObservedBy([UserObserver::class])]
class User extends Authenticatable
{
    //
}
```

Or, you may manually register an observer by invoking the `observe` method on the model you wish to observe. You may register observers in the `boot` method of your application's `AppServiceProvider` class:

```
 1use App\Models\User;
 2use App\Observers\UserObserver;
 3 
 4/**
 5 * Bootstrap any application services.
 6 */
 7public function boot(): void
 8{
 9    User::observe(UserObserver::class);
10}

use App\Models\User;
use App\Observers\UserObserver;

/**
 * Bootstrap any application services.
 */
public function boot(): void
{
    User::observe(UserObserver::class);
}
```

There are additional events an observer can listen to, such as `saving` and `retrieved`. These events are described within the events documentation.

#### Observers and Database Transactions

When models are being created within a database transaction, you may want to instruct an observer to only execute its event handlers after the database transaction is committed. You may accomplish this by implementing the `ShouldHandleEventsAfterCommit` interface on your observer. If a database transaction is not in progress, the event handlers will execute immediately:

```
 1<?php
 2 
 3namespace App\Observers;
 4 
 5use App\Models\User;
 6use Illuminate\Contracts\Events\ShouldHandleEventsAfterCommit;
 7 
 8class UserObserver implements ShouldHandleEventsAfterCommit
 9{
10    /**
11     * Handle the User "created" event.
12     */
13    public function created(User $user): void
14    {
15        // ...
16    }
17}

<?php

namespace App\Observers;

use App\Models\User;
use Illuminate\Contracts\Events\ShouldHandleEventsAfterCommit;

class UserObserver implements ShouldHandleEventsAfterCommit
{
    /**
     * Handle the User "created" event.
     */
    public function created(User $user): void
    {
        // ...
    }
}
```

### Muting Events

You may occasionally need to temporarily "mute" all events fired by a model. You may achieve this using the `withoutEvents` method. The `withoutEvents` method accepts a closure as its only argument. Any code executed within this closure will not dispatch model events, and any value returned by the closure will be returned by the `withoutEvents` method:

```
1use App\Models\User;
2 
3$user = User::withoutEvents(function () {
4    User::findOrFail(1)->delete();
5 
6    return User::find(2);
7});

use App\Models\User;

$user = User::withoutEvents(function () {
    User::findOrFail(1)->delete();

    return User::find(2);
});
```

#### Saving a Single Model Without Events

Sometimes you may wish to "save" a given model without dispatching any events. You may accomplish this using the `saveQuietly` method:

```
1$user = User::findOrFail(1);
2 
3$user->name = 'Victoria Faith';
4 
5$user->saveQuietly();

$user = User::findOrFail(1);

$user->name = 'Victoria Faith';

$user->saveQuietly();
```

You may also "update", "delete", "soft delete", "restore", and "replicate" a given model without dispatching any events:

```
1$user->deleteQuietly();
2$user->forceDeleteQuietly();
3$user->restoreQuietly();

$user->deleteQuietly();
$user->forceDeleteQuietly();
$user->restoreQuietly();
```
