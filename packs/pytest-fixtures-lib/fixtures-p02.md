---
title: "How to use fixtures (part 2/2)"
source: https://docs.pytest.org/en/stable/how-to/fixtures.html
domain: pytest-fixtures-lib
license: CC-BY-SA-4.0
tags: python pytest fixtures, pytest fixture setup, test fixture python
fetched: 2026-07-02
part: 2/2
---

## Use fixtures in classes and modules with `usefixtures`

Sometimes test functions do not directly need access to a fixture object. For example, tests may require to operate with an empty directory as the current working directory but otherwise do not care for the concrete directory. Here is how you can use the standard `tempfile` and pytest fixtures to achieve it. We separate the creation of the fixture into a `conftest.py` file:

```python
# content of conftest.py

import os
import tempfile

import pytest

@pytest.fixture
def cleandir():
    with tempfile.TemporaryDirectory() as newpath:
        old_cwd = os.getcwd()
        os.chdir(newpath)
        yield
        os.chdir(old_cwd)
```

and declare its use in a test module via a `usefixtures` marker:

```python
# content of test_setenv.py
import os

import pytest

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w", encoding="utf-8") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
```

Due to the `usefixtures` marker, the `cleandir` fixture will be required for the execution of each test method, just as if you specified a “cleandir” function argument to each of them. Let’s run it to verify our fixture is activated and the tests pass:

```pytest
$ pytest -q
..                                                                   [100%]
2 passed in 0.12s
```

You can specify multiple fixtures like this:

```python
@pytest.mark.usefixtures("cleandir", "anotherfixture")
def test(): ...
```

and you may specify fixture usage at the test module level using `pytestmark`:

```python
pytestmark = pytest.mark.usefixtures("cleandir")
```

It is also possible to put fixtures required by all tests in your project into a configuration file:

```toml
# content of pytest.toml
[pytest]
usefixtures = ["cleandir"]
```

Warning

`@pytest.mark.usefixtures` cannot be used on **fixture functions**. For example, this is an error:

```python
@pytest.mark.usefixtures("my_other_fixture")
@pytest.fixture
def my_fixture_that_sadly_wont_use_my_other_fixture(): ...
```


## Overriding fixtures on various levels

In a relatively large test suite, you may want to *override* a fixture, to augment or change its behavior inside of certain test modules or directories.

### Override a fixture on a directory (conftest) level

Given the tests file structure is:

```
tests/
    conftest.py
        # content of tests/conftest.py
        import pytest

        @pytest.fixture
        def username():
            return 'username'

    test_something.py
        # content of tests/test_something.py
        def test_username(username):
            assert username == 'username'

    subdir/
        conftest.py
            # content of tests/subdir/conftest.py
            import pytest

            @pytest.fixture
            def username(username):
                return 'overridden-' + username

        test_something_else.py
            # content of tests/subdir/test_something_else.py
            def test_username(username):
                assert username == 'overridden-username'
```

As you can see, a fixture with the same name can be overridden for a certain test directory level. Note that the `base` or `super` fixture can be accessed from the `overriding` fixture easily - used in the example above.

### Override a fixture on a test module level

Given the tests file structure is:

```
tests/
    conftest.py
        # content of tests/conftest.py
        import pytest

        @pytest.fixture
        def username():
            return 'username'

    test_something.py
        # content of tests/test_something.py
        import pytest

        @pytest.fixture
        def username(username):
            return 'overridden-' + username

        def test_username(username):
            assert username == 'overridden-username'

    test_something_else.py
        # content of tests/test_something_else.py
        import pytest

        @pytest.fixture
        def username(username):
            return 'overridden-else-' + username

        def test_username(username):
            assert username == 'overridden-else-username'
```

In the example above, a fixture with the same name can be overridden for a certain test module.

### Override a fixture with direct test parametrization

Given the tests file structure is:

```
tests/
    conftest.py
        # content of tests/conftest.py
        import pytest

        @pytest.fixture
        def username():
            return 'username'

        @pytest.fixture
        def other_username(username):
            return 'other-' + username

    test_something.py
        # content of tests/test_something.py
        import pytest

        @pytest.mark.parametrize('username', ['directly-overridden-username'])
        def test_username(username):
            assert username == 'directly-overridden-username'

        @pytest.mark.parametrize('username', ['directly-overridden-username-other'])
        def test_username_other(other_username):
            assert other_username == 'other-directly-overridden-username-other'
```

In the example above, a fixture value is overridden by the test parameter value. Note that the value of the fixture can be overridden this way even if the test doesn’t use it directly (doesn’t mention it in the function prototype).

### Override a parametrized fixture with non-parametrized one and vice versa

Given the tests file structure is:

```
tests/
    conftest.py
        # content of tests/conftest.py
        import pytest

        @pytest.fixture(params=['one', 'two', 'three'])
        def parametrized_username(request):
            return request.param

        @pytest.fixture
        def non_parametrized_username(request):
            return 'username'

    test_something.py
        # content of tests/test_something.py
        import pytest

        @pytest.fixture
        def parametrized_username():
            return 'overridden-username'

        @pytest.fixture(params=['one', 'two', 'three'])
        def non_parametrized_username(request):
            return request.param

        def test_username(parametrized_username):
            assert parametrized_username == 'overridden-username'

        def test_parametrized_username(non_parametrized_username):
            assert non_parametrized_username in ['one', 'two', 'three']

    test_something_else.py
        # content of tests/test_something_else.py
        def test_username(parametrized_username):
            assert parametrized_username in ['one', 'two', 'three']

        def test_username(non_parametrized_username):
            assert non_parametrized_username == 'username'
```

In the example above, a parametrized fixture is overridden with a non-parametrized version, and a non-parametrized fixture is overridden with a parametrized version for certain test module. The same applies for the test directory level obviously.


## Using fixtures from other projects

Usually projects that provide pytest support will use entry points, so just installing those projects into an environment will make those fixtures available for use.

In case you want to use fixtures from a project that does not use entry points, you can define `pytest_plugins` in your top `conftest.py` file to register that module as a plugin.

Suppose you have some fixtures in `mylibrary.fixtures` and you want to reuse them into your `app/tests` directory.

All you need to do is to define `pytest_plugins` in `app/tests/conftest.py` pointing to that module.

```python
pytest_plugins = "mylibrary.fixtures"
```

This effectively registers `mylibrary.fixtures` as a plugin, making all its fixtures and hooks available to tests in `app/tests`.

Note

Sometimes users will *import* fixtures from other projects for use, however this is not recommended: importing fixtures into a module will register them in pytest as *defined* in that module.

This has minor consequences, such as appearing multiple times in `pytest --help`, but it is not **recommended** because this behavior might change/stop working in future versions.
