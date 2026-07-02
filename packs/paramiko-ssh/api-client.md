---
title: "Client"
source: https://docs.paramiko.org/en/latest/api/client.html
domain: paramiko-ssh
license: CC-BY-SA-4.0
tags: python paramiko, paramiko ssh client, sftp python
fetched: 2026-07-02
---

# Client

SSH client & key policies

***class*paramiko.client.SSHClient**

A high-level representation of a session with an SSH server. This class wraps `Transport`, `Channel`, and `SFTPClient` to take care of most aspects of authenticating and opening channels. A typical use case is:

```
client = SSHClient()
client.load_system_host_keys()
client.connect('ssh.example.com')
stdin, stdout, stderr = client.exec_command('ls -l')
```

You may pass in explicit overrides for authentication and server host key checking. The default mechanism is to try to use local key files or an SSH agent (if one is running).

Instances of this class may be used as context managers.

New in version 1.6.

**__init__()**

Create a new SSHClient.

**load_system_host_keys(*filename=None*)**

Load host keys from a system (read-only) file. Host keys read with this method will not be saved back by `save_host_keys`.

This method can be called multiple times. Each new set of host keys will be merged with the existing set (new replacing old if there are conflicts).

If `filename` is left as `None`, an attempt will be made to read keys from the user’s local “known hosts” file, as used by OpenSSH, and no exception will be raised if the file can’t be read. This is probably only useful on posix.

**Parameters:**

**filename** (*str*) – the filename to read, or `None`

**Raises:**

`IOError` – if a filename was provided and the file could not be read

**load_host_keys(*filename*)**

Load host keys from a local host-key file. Host keys read with this method will be checked after keys loaded via `load_system_host_keys`, but will be saved back by `save_host_keys` (so they can be modified). The missing host key policy `AutoAddPolicy` adds keys to this set and saves them, when connecting to a previously-unknown server.

This method can be called multiple times. Each new set of host keys will be merged with the existing set (new replacing old if there are conflicts). When automatically saving, the last hostname is used.

**Parameters:**

**filename** (*str*) – the filename to read

**Raises:**

`IOError` – if the filename could not be read

**save_host_keys(*filename*)**

Save the host keys back to a file. Only the host keys loaded with `load_host_keys` (plus any added directly) will be saved – not any host keys loaded with `load_system_host_keys`.

**Parameters:**

**filename** (*str*) – the filename to save to

**Raises:**

`IOError` – if the file could not be written

**get_host_keys()**

Get the local `HostKeys` object. This can be used to examine the local host keys or change them.

**Returns:**

the local host keys as a `HostKeys` object.

**set_log_channel(*name*)**

Set the channel for logging. The default is `"paramiko.transport"` but it can be set to anything you want.

**Parameters:**

**name** (*str*) – new channel name for logging

**set_missing_host_key_policy(*policy*)**

Set policy to use when connecting to servers without a known host key.

Specifically:

- A **policy** is a “policy class” (or instance thereof), namely some subclass of `MissingHostKeyPolicy` such as `RejectPolicy` (the default), `AutoAddPolicy`, `WarningPolicy`, or a user-created subclass.
- A host key is **known** when it appears in the client object’s cached host keys structures (those manipulated by `load_system_host_keys` and/or `load_host_keys`).

**Parameters:**

**policy** (*.MissingHostKeyPolicy*) – the policy to use when receiving a host key from a previously-unknown server

**connect(*hostname*, *port=22*, *username=None*, *password=None*, *pkey=None*, *key_filename=None*, *timeout=None*, *allow_agent=True*, *look_for_keys=True*, *compress=False*, *sock=None*, *banner_timeout=None*, *auth_timeout=None*, *channel_timeout=None*, *passphrase=None*, *disabled_algorithms=None*, *transport_factory=None*, *auth_strategy=None*)**

Connect to an SSH server and authenticate to it. The server’s host key is checked against the system host keys (see `load_system_host_keys`) and any local host keys (`load_host_keys`). If the server’s hostname is not found in either set of host keys, the missing host key policy is used (see `set_missing_host_key_policy`). The default policy is to reject the key and raise an `SSHException`.

Authentication is attempted in the following order of priority:

> - The `pkey` or `key_filename` passed in (if any)
>   - `key_filename` may contain OpenSSH public certificate paths as well as regular private-key paths; when files ending in `-cert.pub` are found, they are assumed to match a private key, and both components will be loaded. (The private key itself does *not* need to be listed in `key_filename` for this to occur - *just* the certificate.)
> - Any key we can find through an SSH agent
> - Any `id_*` keys discoverable in `~/.ssh/`
>   - When OpenSSH-style public certificates exist that match an existing such private key (so e.g. one has `id_rsa` and `id_rsa-cert.pub`) the certificate will be loaded alongside the private key and used for authentication.
> - Plain username/password auth, if a password was given

If a private key requires a password to unlock it, and a password is passed in, that password will be used to attempt to unlock the key.

**Parameters:**

- **hostname** (*str*) – the server to connect to
- **port** (*int*) – the server port to connect to
- **username** (*str*) – the username to authenticate as (defaults to the current local username)
- **password** (*str*) – Used for password authentication; is also used for private key decryption if `passphrase` is not given.
- **passphrase** (*str*) – Used for decrypting private keys.
- **pkey** (*.PKey*) – an optional private key to use for authentication
- **key_filename** (*str*) – the filename, or list of filenames, of optional private key(s) and/or certs to try for authentication
- **timeout** (*float*) – an optional timeout (in seconds) for the TCP connect
- **allow_agent** (*bool*) – set to False to disable connecting to the SSH agent
- **look_for_keys** (*bool*) – set to False to disable searching for discoverable private key files in `~/.ssh/`
- **compress** (*bool*) – set to True to turn on compression
- **sock** (*socket*) – an open socket or socket-like object (such as a `Channel`) to use for communication to the target host
- **banner_timeout** (*float*) – an optional timeout (in seconds) to wait for the SSH banner to be presented.
- **auth_timeout** (*float*) – an optional timeout (in seconds) to wait for an authentication response.
- **channel_timeout** (*float*) – an optional timeout (in seconds) to wait for a channel open response.
- **disabled_algorithms** (*dict*) – an optional dict passed directly to `Transport` and its keyword argument of the same name.
- **transport_factory** – an optional callable which is handed a subset of the constructor arguments (primarily those related to the socket and algorithm selection) and generates a `Transport` instance to be used by this client. Defaults to `Transport.__init__`.
- **auth_strategy** – an optional instance of `AuthStrategy`, triggering use of this newer authentication mechanism instead of SSHClient’s legacy auth method. Warning This parameter is **incompatible** with all other authentication-related parameters (such as, but not limited to, `password`, `key_filename` and `allow_agent`) and will trigger an exception if given alongside them.

**Returns:**

`AuthResult` if `auth_strategy` is non-`None`; otherwise, returns `None`.

**Raises:**

- **BadHostKeyException** – if the server’s host key could not be verified.
- **AuthenticationException** – if authentication failed.
- **UnableToAuthenticate** – if authentication failed (when `auth_strategy` is non-`None`; and note that this is a subclass of `AuthenticationException`).
- **socket.error** – if a socket error (other than connection-refused or host-unreachable) occurred while connecting.
- **NoValidConnectionsError** – if all valid connection targets for the requested hostname (eg IPv4 and IPv6) yielded connection-refused or host-unreachable socket errors.
- **SSHException** – if there was any other error connecting or establishing an SSH session.

Changed in version 1.15: Added the `banner_timeout` argument.

Changed in version 2.4: Added the `passphrase` argument.

Changed in version 2.6: Added the `disabled_algorithms` argument.

Changed in version 2.12: Added the `transport_factory` argument.

Changed in version 3.2: Added the `auth_strategy` argument.

**close()**

Close this SSHClient and its underlying `Transport`.

This should be called anytime you are done using the client object.

Warning

Paramiko registers garbage collection hooks that will try to automatically close connections for you, but this is not presently reliable. Failure to explicitly close your client after use may lead to end-of-process hangs!

**exec_command(*command*, *bufsize=-1*, *timeout=None*, *get_pty=False*, *environment=None*)**

Execute a command on the SSH server. A new `Channel` is opened and the requested command is executed. The command’s input and output streams are returned as Python `file`-like objects representing stdin, stdout, and stderr.

**Parameters:**

- **command** (*str*) – the command to execute
- **bufsize** (*int*) – interpreted the same way as by the built-in `file()` function in Python
- **timeout** (*int*) – set command’s channel timeout. See `Channel.settimeout`
- **get_pty** (*bool*) – Request a pseudo-terminal from the server (default `False`). See `Channel.get_pty`
- **environment** (*dict*) – a dict of shell environment variables, to be merged into the default environment that the remote command executes within. Warning Servers may silently reject some environment variables; see the warning in `Channel.set_environment_variable` for details.

**Returns:**

the stdin, stdout, and stderr of the executing command, as a 3-tuple

**Raises:**

`SSHException` – if the server fails to execute the command

Changed in version 1.10: Added the `get_pty` kwarg.

**invoke_shell(*term='vt100'*, *width=80*, *height=24*, *width_pixels=0*, *height_pixels=0*, *environment=None*)**

Start an interactive shell session on the SSH server. A new `Channel` is opened and connected to a pseudo-terminal using the requested terminal type and size.

**Parameters:**

- **term** (*str*) – the terminal type to emulate (for example, `"vt100"`)
- **width** (*int*) – the width (in characters) of the terminal window
- **height** (*int*) – the height (in characters) of the terminal window
- **width_pixels** (*int*) – the width (in pixels) of the terminal window
- **height_pixels** (*int*) – the height (in pixels) of the terminal window
- **environment** (*dict*) – the command’s environment

**Returns:**

a new `Channel` connected to the remote shell

**Raises:**

`SSHException` – if the server fails to invoke a shell

**open_sftp()**

Open an SFTP session on the SSH server.

**Returns:**

a new `SFTPClient` session object

**get_transport()**

Return the underlying `Transport` object for this SSH connection. This can be used to perform lower-level tasks, like opening specific kinds of channels.

**Returns:**

the `Transport` for this connection

***class*paramiko.client.MissingHostKeyPolicy**

Interface for defining the policy that `SSHClient` should use when the SSH server’s hostname is not in either the system host keys or the application’s keys. Pre-made classes implement policies for automatically adding the key to the application’s `HostKeys` object (`AutoAddPolicy`), and for automatically rejecting the key (`RejectPolicy`).

This function may be used to ask the user to verify the key, for example.

**missing_host_key(*client*, *hostname*, *key*)**

Called when an `SSHClient` receives a server key for a server that isn’t in either the system or local `HostKeys` object. To accept the key, simply return. To reject, raised an exception (which will be passed to the calling application).

**__weakref__**

list of weak references to the object (if defined)

***class*paramiko.client.AutoAddPolicy**

Policy for automatically adding the hostname and new host key to the local `HostKeys` object, and saving it. This is used by `SSHClient`.

**missing_host_key(*client*, *hostname*, *key*)**

Called when an `SSHClient` receives a server key for a server that isn’t in either the system or local `HostKeys` object. To accept the key, simply return. To reject, raised an exception (which will be passed to the calling application).

***class*paramiko.client.RejectPolicy**

Policy for automatically rejecting the unknown hostname & key. This is used by `SSHClient`.

**missing_host_key(*client*, *hostname*, *key*)**

Called when an `SSHClient` receives a server key for a server that isn’t in either the system or local `HostKeys` object. To accept the key, simply return. To reject, raised an exception (which will be passed to the calling application).

***class*paramiko.client.WarningPolicy**

Policy for logging a Python-style warning for an unknown host key, but accepting it. This is used by `SSHClient`.

**missing_host_key(*client*, *hostname*, *key*)**

Called when an `SSHClient` receives a server key for a server that isn’t in either the system or local `HostKeys` object. To accept the key, simply return. To reject, raised an exception (which will be passed to the calling application).
