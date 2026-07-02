---
title: "Tasks (part 2/2)"
source: https://docs.celeryq.dev/en/stable/userguide/tasks.html
domain: celery-tasks
license: CC-BY-SA-4.0
tags: python celery, celery task queue, distributed task python
fetched: 2026-07-02
part: 2/2
---

# OK:
class HttpError(Exception):

    def __init__(self, status_code):
        self.status_code = status_code
        Exception.__init__(self, status_code)  # <-- REQUIRED
```

So the rule is: For any exception that supports custom arguments `*args`, `Exception.__init__(self, *args)` must be used.

There’s no special support for *keyword arguments*, so if you want to preserve keyword arguments when the exception is unpickled you have to pass them as regular args:

```python
class HttpError(Exception):

    def __init__(self, status_code, headers=None, body=None):
        self.status_code = status_code
        self.headers = headers
        self.body = body

        super(HttpError, self).__init__(status_code, headers, body)
```

The worker wraps the task in a tracing function that records the final state of the task. There are a number of exceptions that can be used to signal this function to change how it treats the return of the task.

### Ignore

The task may raise `Ignore` to force the worker to ignore the task. This means that no state will be recorded for the task, but the message is still acknowledged (removed from queue).

This can be used if you want to implement custom revoke-like functionality, or manually store the result of a task.

Example keeping revoked tasks in a Redis set:

```python
from celery.exceptions import Ignore

@app.task(bind=True)
def some_task(self):
    if redis.ismember('tasks.revoked', self.request.id):
        raise Ignore()
```

Example that stores results manually:

```python
from celery import states
from celery.exceptions import Ignore

@app.task(bind=True)
def get_tweets(self, user):
    timeline = twitter.get_timeline(user)
    if not self.request.called_directly:
        self.update_state(state=states.SUCCESS, meta=timeline)
    raise Ignore()
```

### Reject

The task may raise `Reject` to reject the task message using AMQPs `basic_reject` method. This won’t have any effect unless `Task.acks_late` is enabled.

Rejecting a message has the same effect as acking it, but some brokers may implement additional functionality that can be used. For example RabbitMQ supports the concept of Dead Letter Exchanges where a queue can be configured to use a dead letter exchange that rejected messages are redelivered to.

Reject can also be used to re-queue messages, but please be very careful when using this as it can easily result in an infinite message loop.

Example using reject when a task causes an out of memory condition:

```python
import errno
from celery.exceptions import Reject

@app.task(bind=True, acks_late=True)
def render_scene(self, path):
    file = get_file(path)
    try:
        renderer.render_scene(file)

    # if the file is too big to fit in memory
    # we reject it so that it's redelivered to the dead letter exchange
    # and we can manually inspect the situation.
    except MemoryError as exc:
        raise Reject(exc, requeue=False)
    except OSError as exc:
        if exc.errno == errno.ENOMEM:
            raise Reject(exc, requeue=False)

    # For any other error we retry after 10 seconds.
    except Exception as exc:
        raise self.retry(exc, countdown=10)
```

Example re-queuing the message:

```python
from celery.exceptions import Reject

@app.task(bind=True, acks_late=True)
def requeues(self):
    if not self.request.delivery_info['redelivered']:
        raise Reject('no reason', requeue=True)
    print('received two times')
```

Consult your broker documentation for more details about the `basic_reject` method.

### Retry

The `Retry` exception is raised by the `Task.retry` method to tell the worker that the task is being retried.

All tasks inherit from the `app.Task` class. The `run()` method becomes the task body.

As an example, the following code,

```python
@app.task
def add(x, y):
    return x + y
```

will do roughly this behind the scenes:

```python
class _AddTask(app.Task):

    def run(self, x, y):
        return x + y
add = app.tasks[_AddTask.name]
```

### Instantiation

A task is **not** instantiated for every request, but is registered in the task registry as a global instance.

This means that the `__init__` constructor will only be called once per process, and that the task class is semantically closer to an Actor.

If you have a task,

```python
from celery import Task

class NaiveAuthenticateServer(Task):

    def __init__(self):
        self.users = {'george': 'password'}

    def run(self, username, password):
        try:
            return self.users[username] == password
        except KeyError:
            return False
```

And you route every request to the same process, then it will keep state between requests.

This can also be useful to cache resources, For example, a base Task class that caches a database connection:

```python
from celery import Task

class DatabaseTask(Task):
    _db = None

    @property
    def db(self):
        if self._db is None:
            self._db = Database.connect()
        return self._db
```

#### Per task usage

The above can be added to each task like this:

```python
from celery.app import task

@app.task(base=DatabaseTask, bind=True)
def process_rows(self: task):
    for row in self.db.table.all():
        process_row(row)
```

The `db` attribute of the `process_rows` task will then always stay the same in each process.

#### App-wide usage

You can also use your custom class in your whole Celery app by passing it as the `task_cls` argument when instantiating the app. This argument should be either a string giving the python path to your Task class or the class itself:

```python
from celery import Celery

app = Celery('tasks', task_cls='your.module.path:DatabaseTask')
```

This will make all your tasks declared using the decorator syntax within your app to use your `DatabaseTask` class and will all have a `db` attribute.

The default value is the class provided by Celery: `'celery.app.task:Task'`.

### Handlers

Task handlers are methods that execute at specific points in a task’s lifecycle. All handlers run **synchronously** within the same worker process and thread that executes the task.

#### Execution timeline

The following diagram shows the exact order of execution:

```
Worker Process Timeline
┌───────────────────────────────────────────────────────────────┐
│  1. before_start()      ← Blocks until complete               │
│  2. run()               ← Your task function                  │
│  3. [Result Backend]    ← State + return value persisted      │
│  4. on_success() OR     ← Outcome-specific handler            │
│     on_retry() OR       │                                     │
│     on_failure()        │                                     │
│  5. after_return()      ← Runs last on terminal states        │
│                       (skipped for RETRY/REJECTED/IGNORED)    │
└───────────────────────────────────────────────────────────────┘
```

Important

**Key points:**

- All handlers run in the **same worker process** as your task
- `before_start` **blocks** the task - `run()` won’t start until it completes
- Result backend is updated **before** `on_success`/`on_failure` - other clients can see the task as finished while handlers are still running
- `after_return` executes when the task reaches a terminal state. It does not run for `RETRY`, `REJECTED`, or `IGNORED`. If you need a hook that fires on every attempt, use the `task_postrun` signal.

#### Available handlers

**before_start(*self*, *task_id*, *args*, *kwargs*)**

Run by the worker before the task starts executing.

Note

This handler **blocks** the task: the `run()` method will *not* begin until `before_start` returns.

Added in version 5.2.

**Parameters:**

- **task_id** – Unique id of the task to execute.
- **args** – Original arguments for the task to execute.
- **kwargs** – Original keyword arguments for the task to execute.

The return value of this handler is ignored.

**on_success(*self*, *retval*, *task_id*, *args*, *kwargs*)**

Success handler.

Run by the worker if the task executes successfully.

Note

Invoked **after** the task result has already been persisted in the result backend. External clients may observe the task as `SUCCESS` while this handler is still running.

**Parameters:**

- **retval** – The return value of the task.
- **task_id** – Unique id of the executed task.
- **args** – Original arguments for the executed task.
- **kwargs** – Original keyword arguments for the executed task.

The return value of this handler is ignored.

**on_retry(*self*, *exc*, *task_id*, *args*, *kwargs*, *einfo*)**

Retry handler.

Run by the worker when the task is to be retried.

Note

Invoked **after** the task state has been updated to `RETRY` in the result backend but **before** the retry is scheduled.

**Parameters:**

- **exc** – The exception sent to `retry()`.
- **task_id** – Unique id of the retried task.
- **args** – Original arguments for the retried task.
- **kwargs** – Original keyword arguments for the retried task.
- **einfo** – `ExceptionInfo` instance.

The return value of this handler is ignored.

**on_failure(*self*, *exc*, *task_id*, *args*, *kwargs*, *einfo*)**

Failure handler.

Run by the worker when the task fails.

Note

Invoked **after** the task result has already been persisted in the result backend with `FAILURE` state. External clients may observe the task as failed while this handler is still running.

**Parameters:**

- **exc** – The exception raised by the task.
- **task_id** – Unique id of the failed task.
- **args** – Original arguments for the failed task.
- **kwargs** – Original keyword arguments for the failed task.
- **einfo** – `ExceptionInfo` instance.

The return value of this handler is ignored.

**after_return(*self*, *status*, *retval*, *task_id*, *args*, *kwargs*, *einfo*)**

Handler called after the task returns.

Note

Executes after the outcome-specific handler when the task reaches a terminal state.

In practice, this means it runs after `on_success` or `on_failure`. It is not executed for `RETRY`, `REJECTED`, or `IGNORED` states. If a hook is needed for every attempt, consider using the `task_postrun` signal.

**Parameters:**

- **status** – Current task state.
- **retval** – Task return value/exception.
- **task_id** – Unique id of the task.
- **args** – Original arguments for the task that returned.
- **kwargs** – Original keyword arguments for the task that returned.
- **einfo** – `ExceptionInfo` instance.

The return value of this handler is ignored.

#### Example usage

```python
import time
from celery import Task

class MyTask(Task):

    def before_start(self, task_id, args, kwargs):
        print(f"Task {task_id} starting with args {args}")
        # This blocks - run() won't start until this returns

    def on_success(self, retval, task_id, args, kwargs):
        print(f"Task {task_id} succeeded with result: {retval}")
        # Result is already visible to clients at this point

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(f"Task {task_id} failed: {exc}")
        # Task state is already FAILURE in backend

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        print(f"Task {task_id} finished with status: {status}")
        # Always runs last

@app.task(base=MyTask)
def my_task(x, y):
    return x + y
```

### Requests and custom requests

Upon receiving a message to run a task, the worker creates a `request` to represent such demand.

Custom task classes may override which request class to use by changing the attribute `celery.app.task.Task.Request`. You may either assign the custom request class itself, or its fully qualified name.

The request has several responsibilities. Custom request classes should cover them all – they are responsible to actually run and trace the task. We strongly recommend to inherit from `celery.worker.request.Request`.

When using the pre-forking worker, the methods `on_timeout()` and `on_failure()` are executed in the main worker process. An application may leverage such facility to detect failures which are not detected using `celery.app.task.Task.on_failure()`.

As an example, the following custom request detects and logs hard time limits, and other failures.

```python
import logging
from celery import Task
from celery.worker.request import Request

logger = logging.getLogger('my.package')

class MyRequest(Request):
    'A minimal custom request to log failures and hard time limits.'

    def on_timeout(self, soft, timeout):
        super(MyRequest, self).on_timeout(soft, timeout)
        if not soft:
           logger.warning(
               'A hard timeout was enforced for task %s',
               self.task.name
           )

    def on_failure(self, exc_info, send_failed_event=True, return_ok=False):
        super().on_failure(
            exc_info,
            send_failed_event=send_failed_event,
            return_ok=return_ok
        )
        logger.warning(
            'Failure detected for task %s',
            self.task.name
        )

class MyTask(Task):
    Request = MyRequest  # you can use a FQN 'my.package:MyRequest'

@app.task(base=MyTask)
def some_longrunning_task():
    # use your imagination
```

Here come the technical details. This part isn’t something you need to know, but you may be interested.

All defined tasks are listed in a registry. The registry contains a list of task names and their task classes. You can investigate this registry yourself:

```pycon
>>> from proj.celery import app
>>> app.tasks
{'celery.chord_unlock':
    <@task: celery.chord_unlock>,
 'celery.backend_cleanup':
    <@task: celery.backend_cleanup>,
 'celery.chord':
    <@task: celery.chord>}
```

This is the list of tasks built into Celery. Note that tasks will only be registered when the module they’re defined in is imported.

The default loader imports any modules listed in the `imports` setting.

The `app.task()` decorator is responsible for registering your task in the applications task registry.

When tasks are sent, no actual function code is sent with it, just the name of the task to execute. When the worker then receives the message it can look up the name in its task registry to find the execution code.

This means that your workers should always be updated with the same software as the client. This is a drawback, but the alternative is a technical challenge that’s yet to be solved.

### Ignore results you don’t want

If you don’t care about the results of a task, be sure to set the `ignore_result` option, as storing results wastes time and resources.

```python
@app.task(ignore_result=True)
def mytask():
    something()
```

Results can even be disabled globally using the `task_ignore_result` setting.

Results can be enabled/disabled on a per-execution basis, by passing the `ignore_result` boolean parameter, when calling `apply_async`.

```python
@app.task
def mytask(x, y):
    return x + y


# No result will be stored
result = mytask.apply_async((1, 2), ignore_result=True)
print(result.get()) # -> None


# Result will be stored
result = mytask.apply_async((1, 2), ignore_result=False)
print(result.get()) # -> 3
```

By default tasks will *not ignore results* (`ignore_result=False`) when a result backend is configured.

The option precedence order is the following:

1. Global `task_ignore_result`
2. `ignore_result` option
3. Task execution option `ignore_result`

### More optimization tips

You find additional optimization tips in the Optimizing Guide.

### Avoid launching synchronous subtasks

Having a task wait for the result of another task is really inefficient, and may even cause a deadlock if the worker pool is exhausted.

Make your design asynchronous instead, for example by using *callbacks*.

**Bad**:

```python
@app.task
def update_page_info(url):
    page = fetch_page.delay(url).get()
    info = parse_page.delay(page).get()
    store_page_info.delay(url, info)

@app.task
def fetch_page(url):
    return myhttplib.get(url)

@app.task
def parse_page(page):
    return myparser.parse_document(page)

@app.task
def store_page_info(url, info):
    return PageInfo.objects.create(url, info)
```

**Good**:

```python
def update_page_info(url):
    # fetch_page -> parse_page -> store_page
    chain = fetch_page.s(url) | parse_page.s() | store_page_info.s(url)
    chain()

@app.task()
def fetch_page(url):
    return myhttplib.get(url)

@app.task()
def parse_page(page):
    return myparser.parse_document(page)

@app.task(ignore_result=True)
def store_page_info(info, url):
    PageInfo.objects.create(url=url, info=info)
```

Here I instead created a chain of tasks by linking together different `signature()`’s. You can read about chains and other powerful constructs at Canvas: Designing Work-flows.

By default Celery will not allow you to run subtasks synchronously within a task, but in rare or extreme cases you might need to do so. **WARNING**: enabling subtasks to run synchronously is not recommended!

```python
@app.task
def update_page_info(url):
    page = fetch_page.delay(url).get(disable_sync_subtasks=False)
    info = parse_page.delay(page).get(disable_sync_subtasks=False)
    store_page_info.delay(url, info)

@app.task
def fetch_page(url):
    return myhttplib.get(url)

@app.task
def parse_page(page):
    return myparser.parse_document(page)

@app.task
def store_page_info(url, info):
    return PageInfo.objects.create(url, info)
```

### Granularity

The task granularity is the amount of computation needed by each subtask. In general it is better to split the problem up into many small tasks rather than have a few long running tasks.

With smaller tasks you can process more tasks in parallel and the tasks won’t run long enough to block the worker from processing other waiting tasks.

However, executing a task does have overhead. A message needs to be sent, data may not be local, etc. So if the tasks are too fine-grained the overhead added probably removes any benefit.

See also

The book Art of Concurrency has a section dedicated to the topic of task granularity [AOC1].

[

AOC1

]

Breshears, Clay. Section 2.2.1, “The Art of Concurrency”. O’Reilly Media, Inc. May 15, 2009. ISBN-13 978-0-596-52153-0.

### Data locality

The worker processing the task should be as close to the data as possible. The best would be to have a copy in memory, the worst would be a full transfer from another continent.

If the data is far away, you could try to run another worker at location, or if that’s not possible - cache often used data, or preload data you know is going to be used.

The easiest way to share data between workers is to use a distributed cache system, like memcached.

See also

The paper Distributed Computing Economics by Jim Gray is an excellent introduction to the topic of data locality.

### State

Since Celery is a distributed system, you can’t know which process, or on what machine the task will be executed. You can’t even know if the task will run in a timely manner.

The ancient async sayings tells us that “asserting the world is the responsibility of the task”. What this means is that the world view may have changed since the task was requested, so the task is responsible for making sure the world is how it should be; If you have a task that re-indexes a search engine, and the search engine should only be re-indexed at maximum every 5 minutes, then it must be the tasks responsibility to assert that, not the callers.

Another gotcha is Django model objects. They shouldn’t be passed on as arguments to tasks. It’s almost always better to re-fetch the object from the database when the task is running instead, as using old data may lead to race conditions.

Imagine the following scenario where you have an article and a task that automatically expands some abbreviations in it:

```python
class Article(models.Model):
    title = models.CharField()
    body = models.TextField()

@app.task
def expand_abbreviations(article):
    article.body.replace('MyCorp', 'My Corporation')
    article.save()
```

First, an author creates an article and saves it, then the author clicks on a button that initiates the abbreviation task:

```pycon
>>> article = Article.objects.get(id=102)
>>> expand_abbreviations.delay(article)
```

Now, the queue is very busy, so the task won’t be run for another 2 minutes. In the meantime another author makes changes to the article, so when the task is finally run, the body of the article is reverted to the old version because the task had the old body in its argument.

Fixing the race condition is easy, just use the article id instead, and re-fetch the article in the task body:

```python
@app.task
def expand_abbreviations(article_id):
    article = Article.objects.get(id=article_id)
    article.body.replace('MyCorp', 'My Corporation')
    article.save()
```

```pycon
>>> expand_abbreviations.delay(article_id)
```

There might even be performance benefits to this approach, as sending large messages may be expensive.

### Database transactions

Let’s have a look at another example:

```python
from django.db import transaction
from django.http import HttpResponseRedirect

@transaction.atomic
def create_article(request):
    article = Article.objects.create()
    expand_abbreviations.delay(article.pk)
    return HttpResponseRedirect('/articles/')
```

This is a Django view creating an article object in the database, then passing the primary key to a task. It uses the *transaction.atomic* decorator, that will commit the transaction when the view returns, or roll back if the view raises an exception.

There is a race condition because transactions are atomic. This means the article object is not persisted to the database until after the view function returns a response. If the asynchronous task starts executing before the transaction is committed, it may attempt to query the article object before it exists. To prevent this, we need to ensure that the transaction is committed before triggering the task.

The solution is to use `delay_on_commit()` instead:

```python
from django.db import transaction
from django.http import HttpResponseRedirect

@transaction.atomic
def create_article(request):
    article = Article.objects.create()
    expand_abbreviations.delay_on_commit(article.pk)
    return HttpResponseRedirect('/articles/')
```

This method was added in Celery 5.4. It’s a shortcut that uses Django’s `on_commit` callback to launch your Celery task once all transactions have been committed successfully.

#### With Celery <5.4

If you’re using an older version of Celery, you can replicate this behaviour using the Django callback directly as follows:

```python
import functools
from django.db import transaction
from django.http import HttpResponseRedirect

@transaction.atomic
def create_article(request):
    article = Article.objects.create()
    transaction.on_commit(
        functools.partial(expand_abbreviations.delay, article.pk)
    )
    return HttpResponseRedirect('/articles/')
```

Note

`on_commit` is available in Django 1.9 and above, if you are using a version prior to that then the django-transaction-hooks library adds support for this.

Let’s take a real world example: a blog where comments posted need to be filtered for spam. When the comment is created, the spam filter runs in the background, so the user doesn’t have to wait for it to finish.

I have a Django blog application allowing comments on blog posts. I’ll describe parts of the models/views and tasks for this application.

### `blog/models.py`

The comment model looks like this:

```python
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Comment(models.Model):
    name = models.CharField(_('name'), max_length=64)
    email_address = models.EmailField(_('email address'))
    homepage = models.URLField(_('home page'),
                               blank=True, verify_exists=False)
    comment = models.TextField(_('comment'))
    pub_date = models.DateTimeField(_('Published date'),
                                    editable=False, auto_add_now=True)
    is_spam = models.BooleanField(_('spam?'),
                                  default=False, editable=False)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
```

In the view where the comment is posted, I first write the comment to the database, then I launch the spam filter task in the background.

### `blog/views.py`

```python
from django import forms
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from blog import tasks
from blog.models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

def add_comment(request, slug, template_name='comments/create.html'):
    post = get_object_or_404(Entry, slug=slug)
    remote_addr = request.META.get('REMOTE_ADDR')

    if request.method == 'post':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            # Check spam asynchronously.
            tasks.spam_filter.delay(comment_id=comment.id,
                                    remote_addr=remote_addr)
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = CommentForm()

    context = RequestContext(request, {'form': form})
    return render_to_response(template_name, context_instance=context)
```

To filter spam in comments I use Akismet, the service used to filter spam in comments posted to the free blog platform *Wordpress*. Akismet is free for personal use, but for commercial use you need to pay. You have to sign up to their service to get an API key.

To make API calls to Akismet I use the akismet.py library written by Michael Foord.

### `blog/tasks.py`

```python
from celery import Celery

from akismet import Akismet

from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.models import Site

from blog.models import Comment

app = Celery(broker='amqp://')

@app.task
def spam_filter(comment_id, remote_addr=None):
    logger = spam_filter.get_logger()
    logger.info('Running spam filter for comment %s', comment_id)

    comment = Comment.objects.get(pk=comment_id)
    current_domain = Site.objects.get_current().domain
    akismet = Akismet(settings.AKISMET_KEY, 'http://{0}'.format(domain))
    if not akismet.verify_key():
        raise ImproperlyConfigured('Invalid AKISMET_KEY')

    is_spam = akismet.comment_check(user_ip=remote_addr,
                        comment_content=comment.comment,
                        comment_author=comment.name,
                        comment_author_email=comment.email_address)
    if is_spam:
        comment.is_spam = True
        comment.save()

    return is_spam
```
