---
title: "Welcome to Fabric!"
source: https://www.fabfile.org/
domain: fabric-deploy
license: CC-BY-SA-4.0
tags: python fabric, fabric deployment tool, remote execution python
fetched: 2026-07-02
---

# Welcome to Fabric!

(PyPI - Package Version) (PyPI - Python Version) (PyPI - License) (CircleCI) (Codecov)

# Welcome to Fabric!

Fabric is a high level Python (2.7, 3.4+) library designed to execute shell commands remotely over SSH, yielding useful Python objects in return. It builds on top of Invoke (subprocess command execution and command-line features) and Paramiko (SSH protocol implementation), extending their APIs to complement one another and provide additional functionality.

To find out what’s new in this version of Fabric, please see the changelog.

The project maintainer keeps a roadmap on his website.

This website covers project information for Fabric such as the changelog, contribution guidelines, and so forth. Detailed usage and API documentation can be found at our code documentation site, docs.fabfile.org.

Please see below for a high level intro, or the navigation on the left for the rest of the site content.

## What is Fabric?

Fabric is a high level Python (2.7, 3.4+) library designed to execute shell commands remotely over SSH, yielding useful Python objects in return:

```pycon3
>>> from fabric import Connection
>>> result = Connection('web1.example.com').run('uname -s', hide=True)
>>> msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
>>> print(msg.format(result))
Ran 'uname -s' on web1.example.com, got stdout:
Linux
```

It builds on top of Invoke (subprocess command execution and command-line features) and Paramiko (SSH protocol implementation), extending their APIs to complement one another and provide additional functionality.

Note

Fabric users may also be interested in two *strictly optional* libraries which implement best-practice user-level code: Invocations (Invoke-only, locally-focused CLI tasks) and Patchwork (remote-friendly, typically shell-command-focused, utility functions).

## How is it used?

Core use cases for Fabric include (but are not limited to):

- Single commands on individual hosts: >>> result = Connection('web1').run('hostname') web1 >>> result <Result cmd='hostname' exited=0>
- Single commands across multiple hosts (via varying methodologies: serial, parallel, etc): >>> from fabric import SerialGroup >>> result = SerialGroup('web1', 'web2').run('hostname') web1 web2 >>> # Sorting for consistency...it's a dict! >>> sorted(result.items()) [(<Connection host=web1>, <Result cmd='hostname' exited=0>), ...]
- Python code blocks (functions/methods) targeted at individual connections: >>> def disk_free(c): ... uname = c.run('uname -s', hide=True) ... if 'Linux' in uname.stdout: ... command = "df -h / | tail -n1 | awk '{print $5}'" ... return c.run(command, hide=True).stdout.strip() ... err = "No idea how to get disk space on {}!".format(uname) ... raise Exit(err) ... >>> print(disk_free(Connection('web1'))) 33%
- Python code blocks on multiple hosts: >>> # NOTE: Same code as above! >>> def disk_free(c): ... uname = c.run('uname -s', hide=True) ... if 'Linux' in uname.stdout: ... command = "df -h / | tail -n1 | awk '{print $5}'" ... return c.run(command, hide=True).stdout.strip() ... err = "No idea how to get disk space on {}!".format(uname) ... raise Exit(err) ... >>> for cxn in SerialGroup('web1', 'web2', 'db1'): ... print("{}: {}".format(cxn, disk_free(cxn))) <Connection host=web1>: 33% <Connection host=web2>: 17% <Connection host=db1>: 2%

In addition to these library-oriented use cases, Fabric makes it easy to integrate with Invoke’s command-line task functionality, invoking via a `fab` binary stub:

- Python functions, methods or entire objects can be used as CLI-addressable tasks, e.g. `fab deploy`;
- Tasks may indicate other tasks to be run before or after they themselves execute (pre- or post-tasks);
- Tasks are parameterized via regular GNU-style arguments, e.g. `fab deploy --env=prod -d`;
- Multiple tasks may be given in a single CLI session, e.g. `fab build deploy`;
- Much more - all other Invoke functionality is supported - see its documentation for details.

## I’m a user of Fabric 1, how do I upgrade?

We’ve packaged modern Fabric in a manner that allows installation alongside Fabric 1, so you can upgrade at whatever pace your use case requires. There are multiple possible approaches – see our detailed upgrade documentation for details.

## What is this website?

`www.fabfile.org` provides project information for Fabric such as the changelog, contribution guidelines, development roadmap, news/blog, and so forth.

Detailed conceptual and API documentation can be found at our code documentation site, docs.fabfile.org.
