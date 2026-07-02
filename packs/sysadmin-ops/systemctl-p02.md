---
title: "systemctl(1) (part 2/3)"
source: https://man7.org/linux/man-pages/man1/systemctl.1.html
domain: sysadmin-ops
license: GPL-2.0 / CC-BY-SA-4.0
tags: systemd, cron, ssh, rsync, sysadmin, devops
fetched: 2026-07-02
part: 2/3
---

# systemctl(1)

If a unit gets disabled but its triggering units are still
    active, a warning containing the names of the triggering units
    is shown.  --no-warn can be used to suppress the warning.

    When this command is used with --user, the units being
    operated on might still be enabled in global scope, and thus
    get started automatically even after a successful disablement
    in user scope. In this case, a warning about it is shown,
    which can be suppressed using --no-warn.

    This command honors --system, --user, --runtime, --global and
    --no-warn in a similar way as enable.

    Added in version 238.

reenable UNIT...
    Reenable one or more units, as specified on the command line.
    This is a combination of disable and enable and is useful to
    reset the symlinks a unit file is enabled with to the defaults
    configured in its [Install] section. This command expects a
    unit name only, it does not accept paths to unit files.

    This command implicitly reloads the system manager
    configuration after completing the operation. Note that this
    command does not implicitly restart the units that are being
    disabled. If this is desired, either combine this command with
    the --now switch, or invoke the try-restart command with
    appropriate arguments later.

    Added in version 238.

preset UNIT...
    Reset the enable/disable status of one or more unit files, as
    specified on the command line, to the defaults configured in
    the preset policy files. This has the same effect as disable
    or enable, depending how the unit is listed in the preset
    files.

    Use --preset-mode= to control whether units shall be enabled
    and disabled, or only enabled, or only disabled.

    If the unit carries no install information, it will be
    silently ignored by this command.  UNIT must be the real unit
    name, any alias names are ignored silently.

    For more information on the preset policy format, see
    systemd.preset(5).

    Added in version 238.

preset-all
    Resets all installed unit files to the defaults configured in
    the preset policy file (see above).

    Use --preset-mode= to control whether units shall be enabled
    and disabled, or only enabled, or only disabled.

    Added in version 215.

is-enabled UNIT...
    Checks whether any of the specified unit files are enabled (as
    with enable). Returns an exit code of 0 if at least one is
    enabled, non-zero otherwise. Prints the current enable status
    (see table). To suppress this output, use --quiet. To show
    installation targets, use --full.

    Table 3.  is-enabled output
    ┌───────────────────┬─────────────────────────┬───────────┐
    │ Name              │ Description             │ Exit Code │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "enabled"         │ Enabled via             │           │
    ├───────────────────┤ .wants/,                │           │
    │ "enabled-runtime" │ .requires/ or           │           │
    │                   │ Alias= symlinks         │ 0         │
    │                   │ (permanently in         │           │
    │                   │ /etc/systemd/system/,   │           │
    │                   │ or transiently in       │           │
    │                   │ /run/systemd/system/).  │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "linked"          │ Made available through  │           │
    ├───────────────────┤ one or more symlinks    │           │
    │ "linked-runtime"  │ to the unit file        │           │
    │                   │ (permanently in         │           │
    │                   │ /etc/systemd/system/    │           │
    │                   │ or transiently in       │ > 0       │
    │                   │ /run/systemd/system/),  │           │
    │                   │ even though the unit    │           │
    │                   │ file might reside       │           │
    │                   │ outside of the unit     │           │
    │                   │ file search path.       │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "alias"           │ The name is an alias    │ 0         │
    │                   │ (symlink to another     │           │
    │                   │ unit file).             │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "masked"          │ Completely disabled,    │           │
    ├───────────────────┤ so that any start       │           │
    │ "masked-runtime"  │ operation on it fails   │           │
    │                   │ (permanently in         │ > 0       │
    │                   │ /etc/systemd/system/    │           │
    │                   │ or transiently in       │           │
    │                   │ /run/systemd/systemd/). │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "static"          │ The unit file is not    │ 0         │
    │                   │ enabled, and has no     │           │
    │                   │ provisions for enabling │           │
    │                   │ in the [Install] unit   │           │
    │                   │ file section.           │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "indirect"        │ The unit file itself is │ 0         │
    │                   │ not enabled, but it has │           │
    │                   │ a non-empty Also=       │           │
    │                   │ setting in the          │           │
    │                   │ [Install] unit file     │           │
    │                   │ section, listing other  │           │
    │                   │ unit files that might   │           │
    │                   │ be enabled, or it has   │           │
    │                   │ an alias under a        │           │
    │                   │ different name through  │           │
    │                   │ a symlink that is not   │           │
    │                   │ specified in Also=. For │           │
    │                   │ template unit files, an │           │
    │                   │ instance different than │           │
    │                   │ the one specified in    │           │
    │                   │ DefaultInstance= is     │           │
    │                   │ enabled.                │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "disabled"        │ The unit file is not    │ > 0       │
    │                   │ enabled, but contains   │           │
    │                   │ an [Install] section    │           │
    │                   │ with installation       │           │
    │                   │ instructions.           │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "generated"       │ The unit file was       │ 0         │
    │                   │ generated dynamically   │           │
    │                   │ via a generator tool.   │           │
    │                   │ See                     │           │
    │                   │ systemd.generator(7).   │           │
    │                   │ Generated unit files    │           │
    │                   │ may not be enabled,     │           │
    │                   │ they are enabled        │           │
    │                   │ implicitly by their     │           │
    │                   │ generator.              │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "transient"       │ The unit file has been  │ 0         │
    │                   │ created dynamically     │           │
    │                   │ with the runtime API.   │           │
    │                   │ Transient units may not │           │
    │                   │ be enabled.             │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "bad"             │ The unit file is        │ > 0       │
    │                   │ invalid or another      │           │
    │                   │ error occurred. Note    │           │
    │                   │ that is-enabled will    │           │
    │                   │ not actually return     │           │
    │                   │ this state, but print   │           │
    │                   │ an error message        │           │
    │                   │ instead. However, the   │           │
    │                   │ unit file listing       │           │
    │                   │ printed by              │           │
    │                   │ list-unit-files might   │           │
    │                   │ show it.                │           │
    ├───────────────────┼─────────────────────────┼───────────┤
    │ "not-found"       │ The unit file does not  │ 4         │
    │                   │ exist.                  │           │
    └───────────────────┴─────────────────────────┴───────────┘

    Added in version 238.

mask UNIT...
    Mask one or more units, as specified on the command line. This
    will link these unit files to /dev/null, making it impossible
    to start them. This is a stronger version of disable, since it
    prohibits all kinds of activation of the unit, including
    enablement and manual activation. Use this option with care.
    This honors the --runtime option to only mask temporarily
    until the next reboot of the system. The --now option may be
    used to ensure that the units are also stopped. This command
    expects valid unit names only, it does not accept unit file
    paths.

    Note that this will create a symlink under the unit's name in
    /etc/systemd/system/ (in case --runtime is not specified) or
    /run/systemd/system/ (in case --runtime is specified). If a
    matching unit file already exists under these directories this
    operation will hence fail. This means that the operation is
    primarily useful to mask units shipped by the vendor (as those
    are shipped in /usr/lib/systemd/system/ and not the
    aforementioned two directories), but typically does not work
    for units created locally (as those are typically placed
    precisely in the two aforementioned directories). Similar
    restrictions apply for --user mode, in which case the
    directories are below the user's home directory however.

    If a unit gets masked but its triggering units are still
    active, a warning containing the names of the triggering units
    is shown.  --no-warn can be used to suppress the warning.

    Added in version 238.

unmask UNIT...
    Unmask one or more unit files, as specified on the command
    line. This will undo the effect of mask. This command expects
    valid unit names only, it does not accept unit file paths.

    Added in version 238.

link PATH...
    Link a unit file that is not in the unit file search path into
    the unit file search path. This command expects an absolute
    path to a unit file. The effect of this may be undone with
    disable. The effect of this command is that a unit file is
    made available for commands such as start, even though it is
    not installed directly in the unit search path. The file
    system where the linked unit files are located must be
    accessible when systemd is started (e.g. anything underneath
    /home/ or /var/ is not allowed, unless those directories are
    located on the root file system).

    Added in version 233.

revert UNIT...
    Revert one or more unit files to their vendor versions. This
    command removes drop-in configuration files that modify the
    specified units, as well as any user-configured unit file that
    overrides a matching vendor supplied unit file. Specifically,
    for a unit "foo.service" the matching directories
    "foo.service.d/" with all their contained files are removed,
    both below the persistent and runtime configuration
    directories (i.e. below /etc/systemd/system and
    /run/systemd/system); if the unit file has a vendor-supplied
    version (i.e. a unit file located below /usr/) any matching
    persistent or runtime unit file that overrides it is removed,
    too. Note that if a unit file has no vendor-supplied version
    (i.e. is only defined below /etc/systemd/system or
    /run/systemd/system, but not in a unit file stored below
    /usr/), then it is not removed. Also, if a unit is masked, it
    is unmasked.

    Effectively, this command may be used to undo all changes made
    with systemctl edit, systemctl set-property and systemctl mask
    and puts the original unit file with its settings back in
    effect.

    Added in version 230.

add-wants TARGET UNIT..., add-requires TARGET UNIT...
    Adds "Wants=" or "Requires=" dependencies, respectively, to
    the specified TARGET for one or more units.

    This command honors --system, --user, --runtime and --global
    in a way similar to enable.

    Added in version 217.

edit UNIT...
    Edit or replace a drop-in snippet or the main unit file, to
    extend or override the definition of the specified unit.

    Depending on whether --system (the default), --user, or
    --global is specified, this command will operate on the system
    unit files, unit files for the calling user, or the unit files
    shared between all users.

    The editor (see the "Environment" section below) is invoked on
    temporary files which will be written to the real location if
    the editor exits successfully. After the editing is finished,
    configuration is reloaded, equivalent to systemctl
    daemon-reload --system or systemctl daemon-reload --user. For
    edit --global, the reload is not performed and the edits will
    take effect only for subsequent logins (or after a reload is
    requested in a different way).

    If --full is specified, a replacement for the main unit file
    will be created or edited. Otherwise, a drop-in file will be
    created or edited.

    If --drop-in= is specified, the given drop-in file name will
    be used instead of the default override.conf.

    The unit must exist, i.e. its main unit file must be present.
    If --force is specified, this requirement is ignored and a new
    unit may be created (with --full), or a drop-in for a
    nonexistent unit may be created.

    If --runtime is specified, the changes will be made
    temporarily in /run/ and they will be lost on the next reboot.

    If --stdin is specified, the new contents will be read from
    standard input. In this mode, the old contents of the file are
    discarded.

    If the temporary file is empty upon exit, the modification of
    the related unit is canceled.

    Note that this command cannot be used to remotely edit units
    and that you cannot temporarily edit units which are in /etc/,
    since they take precedence over /run/.

    Added in version 218.

get-default
    Return the default target to boot into. This returns the
    target unit name default.target is aliased (symlinked) to.

    Added in version 205.

set-default TARGET
    Set the default target to boot into. This sets (symlinks) the
    default.target alias to the given target unit.

    Added in version 205.

### Machine Commands

list-machines [PATTERN...]
    List the host and all running local containers with their
    state. If one or more PATTERNs are specified, only containers
    matching one of them are shown.

    Added in version 212.

### Job Commands

list-jobs [PATTERN...]
    List jobs that are in progress. If one or more PATTERNs are
    specified, only jobs for units matching one of them are shown.

    When combined with --after or --before the list is augmented
    with information on which other job each job is waiting for,
    and which other jobs are waiting for it, see above.

    Added in version 233.

cancel [JOB...]
    Cancel one or more jobs specified on the command line by their
    numeric job IDs. If no job ID is specified, cancel all pending
    jobs.

    Added in version 233.

### Environment Commands

systemd supports an environment block that is passed to processes
the manager spawns. The names of the variables can contain ASCII
letters, digits, and the underscore character. Variable names
cannot be empty or start with a digit. In variable values, most
characters are allowed, but the whole sequence must be valid
UTF-8. (Note that control characters like newline (NL), tab (TAB),
or the escape character (ESC), are valid ASCII and thus valid
UTF-8). The total length of the environment block is limited to
_SC_ARG_MAX value defined by sysconf(3).

show-environment
    Dump the systemd manager environment block. This is the
    environment block that is passed to all processes the manager
    spawns. The environment block will be dumped in
    straightforward form suitable for sourcing into most shells.
    If no special characters or whitespace is present in the
    variable values, no escaping is performed, and the assignments
    have the form "VARIABLE=value". If whitespace or characters
    which have special meaning to the shell are present,
    dollar-single-quote escaping is used, and assignments have the
    form "VARIABLE=$'value'". This syntax is known to be supported
    by bash(1), zsh(1), ksh(1), and busybox(1)'s ash(1), but not
    dash(1) or fish(1).

    Note that this shows the effective block, i.e. the combination
    of environment variables configured via configuration files,
    environment generators and via IPC (i.e. via the
    set-environment described below). At the moment a unit process
    is forked off, this combined environment block will be further
    combined with per-unit environment variables, which are not
    visible in this command.

set-environment VARIABLE=VALUE...
    Set one or more service manager environment variables, as
    specified on the command line. This command will fail if
    variable names and values do not conform to the rules listed
    above.

    Note that this operates on an environment block separate from
    the environment block configured from service manager
    configuration and environment generators. Whenever a process
    is invoked the two blocks are combined (also incorporating any
    per-service environment variables), and passed to it. The
    show-environment verb will show the combination of the blocks,
    see above.

    Added in version 233.

unset-environment VARIABLE...
    Unset one or more systemd manager environment variables. If
    only a variable name is specified, it will be removed
    regardless of its value. If a variable and a value are
    specified, the variable is only removed if it has the
    specified value.

    Note that this operates on an environment block separate from
    the environment block configured from service manager
    configuration and environment generators. Whenever a process
    is invoked the two blocks are combined (also incorporating any
    per-service environment variables), and passed to it. The
    show-environment verb will show the combination of the blocks,
    see above. Note that this means this command cannot be used to
    unset environment variables defined in the service manager
    configuration files or via generators.

    Added in version 233.

import-environment VARIABLE...
    Import all, one or more environment variables set on the
    client into the systemd manager environment block. If a list
    of environment variable names is passed, client-side values
    are then imported into the manager's environment block. If any
    names are not valid environment variable names or have invalid
    values according to the rules described above, an error is
    raised. If no arguments are passed, the entire environment
    block inherited by the systemctl process is imported. In this
    mode, any inherited invalid environment variables are quietly
    ignored.

    Importing of the full inherited environment block (calling
    this command without any arguments) is deprecated. A shell
    will set dozens of variables which only make sense locally and
    are only meant for processes which are descendants of the
    shell. Such variables in the global environment block are
    confusing to other processes.

    Added in version 209.

### Manager State Commands

daemon-reload
    Reload the systemd manager configuration. This will rerun all
    generators (see systemd.generator(7)), reload all unit files,
    and recreate the entire dependency tree. While the daemon is
    being reloaded, all sockets systemd listens on behalf of user
    configuration will stay accessible.

    This command should not be confused with the reload command.

daemon-reexec
    Reexecute the systemd manager. This will serialize the manager
    state, reexecute the process and deserialize the state again.
    This command is of little use except for debugging and package
    upgrades. Sometimes, it might be helpful as a heavy-weight
    daemon-reload. While the daemon is being reexecuted, all
    sockets systemd listening on behalf of user configuration will
    stay accessible.

log-level [LEVEL]
    If no argument is given, print the current log level of the
    manager. If an optional argument LEVEL is provided, then the
    command changes the current log level of the manager to LEVEL
    (accepts the same values as --log-level= described in
    systemd(1)).

    Added in version 244.

log-target [TARGET]
    If no argument is given, print the current log target of the
    manager. If an optional argument TARGET is provided, then the
    command changes the current log target of the manager to
    TARGET (accepts the same values as --log-target=, described in
    systemd(1)).

    Added in version 244.

service-watchdogs [yes|no]
    If no argument is given, print the current state of service
    runtime watchdogs of the manager. If an optional boolean
    argument is provided, then globally enables or disables the
    service runtime watchdogs (WatchdogSec=) and emergency actions
    (e.g.  OnFailure= or StartLimitAction=); see
    systemd.service(5). The hardware watchdog is not affected by
    this setting.

    Added in version 244.

### System Commands

is-system-running
    Checks whether the system is operational. This returns success
    (exit code 0) when the system is fully up and running,
    specifically not in startup, shutdown or maintenance mode, and
    with no failed services. Failure is returned otherwise (exit
    code non-zero). In addition, the current state is printed in a
    short string to standard output, see the table below. Use
    --quiet to suppress this output.

    Use --wait to wait until the boot process is completed before
    printing the current state and returning the appropriate error
    status. If --wait is in use, states initializing or starting
    will not be reported, instead the command will block until a
    later state (such as running or degraded) is reached.

    Table 4. is-system-running output
    ┌──────────────┬────────────────────┬───────────┐
    │ Name         │ Description        │ Exit Code │
    ├──────────────┼────────────────────┼───────────┤
    │ initializing │ Early bootup,      │ > 0       │
    │              │ before             │           │
    │              │ basic.target is    │           │
    │              │ reached or the     │           │
    │              │ maintenance state  │           │
    │              │ entered.           │           │
    ├──────────────┼────────────────────┼───────────┤
    │ starting     │ Late bootup,       │ > 0       │
    │              │ before the job     │           │
    │              │ queue becomes idle │           │
    │              │ for the first      │           │
    │              │ time, or one of    │           │
    │              │ the rescue targets │           │
    │              │ are reached.       │           │
    ├──────────────┼────────────────────┼───────────┤
    │ running      │ The system is      │ 0         │
    │              │ fully operational. │           │
    ├──────────────┼────────────────────┼───────────┤
    │ degraded     │ The system is      │ > 0       │
    │              │ operational but    │           │
    │              │ one or more units  │           │
    │              │ failed.            │           │
    ├──────────────┼────────────────────┼───────────┤
    │ maintenance  │ The rescue or      │ > 0       │
    │              │ emergency target   │           │
    │              │ is active.         │           │
    ├──────────────┼────────────────────┼───────────┤
    │ stopping     │ The manager is     │ > 0       │
    │              │ shutting down.     │           │
    ├──────────────┼────────────────────┼───────────┤
    │ offline      │ The manager is not │ > 0       │
    │              │ running.           │           │
    │              │ Specifically, this │           │
    │              │ is the operational │           │
    │              │ state if an        │           │
    │              │ incompatible       │           │
    │              │ program is running │           │
    │              │ as system manager  │           │
    │              │ (PID 1).           │           │
    ├──────────────┼────────────────────┼───────────┤
    │ unknown      │ The operational    │ > 0       │
    │              │ state could not be │           │
    │              │ determined, due to │           │
    │              │ lack of resources  │           │
    │              │ or another error   │           │
    │              │ cause.             │           │
    └──────────────┴────────────────────┴───────────┘

    Added in version 215.

default
    Enter default mode. This is equivalent to systemctl isolate
    default.target. This operation is blocking by default, use
    --no-block to request asynchronous behavior.

rescue
    Enter rescue mode. This is equivalent to systemctl isolate
    rescue.target. This operation is blocking by default, use
    --no-block to request asynchronous behavior.

emergency
    Enter emergency mode. This is equivalent to systemctl isolate
    emergency.target. This operation is blocking by default, use
    --no-block to request asynchronous behavior.

halt
    Shut down and halt the system. This is mostly equivalent to
    systemctl start halt.target --job-mode=replace-irreversibly
    --no-block, but also prints a wall message to all users. This
    command is asynchronous; it will return after the halt
    operation is enqueued, without waiting for it to complete.
    Note that this operation will simply halt the OS kernel after
    shutting down, leaving the hardware powered on. Use systemctl
    poweroff for powering off the system (see below).

    If combined with --force, shutdown of all running services is
    skipped, however all processes are killed and all file systems
    are unmounted or mounted read-only, immediately followed by
    the system halt. If --force is specified twice, the operation
    is immediately executed without terminating any processes or
    unmounting any file systems. This may result in data loss.
    Note that when --force is specified twice the halt operation
    is executed by systemctl itself, and the system manager is not
    contacted. This means the command should succeed even when the
    system manager has crashed.

    If combined with --when=, shutdown will be scheduled after the
    given timestamp. And --when=cancel will cancel the shutdown.

poweroff
    Shut down and power-off the system. This is mostly equivalent
    to systemctl start poweroff.target
    --job-mode=replace-irreversibly --no-block, but also prints a
    wall message to all users. This command is asynchronous; it
    will return after the power-off operation is enqueued, without
    waiting for it to complete.

    This command honors --force and --when= in a similar way as
    halt.

reboot
    Shut down and reboot the system.

    This command is mostly equivalent to systemctl start
    reboot.target --job-mode=replace-irreversibly --no-block, but
    also prints a wall message to all users. This command is
    asynchronous; it will return after the reboot operation is
    enqueued, without waiting for it to complete.

    If the switch --reboot-argument= is given, it will be passed
    as the optional argument to the reboot(2) system call.

    Options --boot-loader-entry=, --boot-loader-menu=, and
    --firmware-setup can be used to select what to do after the
    reboot. See the descriptions of those options for details.

    This command honors --force and --when= in a similar way as
    halt.

    If a new kernel has been loaded via kexec --load, a kexec will
    be performed instead of a reboot, unless
    "SYSTEMCTL_SKIP_AUTO_KEXEC=1" has been set. If a new root file
    system has been set up on "/run/nextroot/", a soft-reboot will
    be performed instead of a reboot, unless
    "SYSTEMCTL_SKIP_AUTO_SOFT_REBOOT=1" has been set.

    Added in version 246.

kexec
    Shut down and reboot the system via kexec. This command will
    load a kexec kernel if one was not loaded yet or fail. A
    kernel may be loaded earlier by a separate step, this is
    particularly useful if a custom initrd or additional kernel
    command line options are desired. The --force can be used to
    continue without a kexec kernel, i.e. to perform a normal
    reboot. The final reboot step is equivalent to systemctl start
    kexec.target --job-mode=replace-irreversibly --no-block.

    To load a kernel, an enumeration is performed following the
    UAPI.1 Boot Loader Specification[1], and the default boot
    entry is loaded. For this step to succeed, the system must be
    using UEFI and the boot loader entries must be configured
    appropriately.  bootctl list may be used to list boot entries,
    see bootctl(1).

    This command is asynchronous; it will return after the reboot
    operation is enqueued, without waiting for it to complete.

    This command honors --force and --when= similarly to halt.

    If a new kernel has been loaded via kexec --load, a kexec will
    be performed when reboot is invoked, unless
    "SYSTEMCTL_SKIP_AUTO_KEXEC=1" has been set.

soft-reboot
    Shut down and reboot userspace. This is equivalent to
    systemctl start soft-reboot.target
    --job-mode=replace-irreversibly --no-block. This command is
    asynchronous; it will return after the reboot operation is
    enqueued, without waiting for it to complete.

    This command honors --force and --when= in a similar way as
    halt.

    This operation only reboots userspace, leaving the kernel
    running. See systemd-soft-reboot.service(8) for details.

    If a new root file system has been set up on "/run/nextroot/",
    a soft-reboot will be performed when reboot is invoked, unless
    "SYSTEMCTL_SKIP_AUTO_SOFT_REBOOT=1" has been set.

    Added in version 254.

exit [EXIT_CODE]
    Ask the service manager to quit. This is only supported for
    user service managers (i.e. in conjunction with the --user
    option) or in containers and is equivalent to poweroff
    otherwise. This command is asynchronous; it will return after
    the exit operation is enqueued, without waiting for it to
    complete.

    The service manager will exit with the specified exit code, if
    EXIT_CODE is passed.

    Added in version 227.

switch-root [ROOT [INIT]]
    Switches to a different root directory and executes a new
    system manager process below it. This is intended for use in
    the initrd, and will transition from the initrd's system
    manager process (a.k.a. "init" process, PID 1) to the main
    system manager process which is loaded from the actual host
    root files system. This call takes two arguments: the
    directory that is to become the new root directory, and the
    path to the new system manager binary below it to execute as
    PID 1. If both are omitted or the former is an empty string it
    defaults to /sysroot/. If the latter is omitted or is an empty
    string, a systemd binary will automatically be searched for
    and used as service manager. If the system manager path is
    omitted, equal to the empty string or identical to the path to
    the systemd binary, the state of the initrd's system manager
    process is passed to the main system manager, which allows
    later introspection of the state of the services involved in
    the initrd boot phase.

    Added in version 209.

sleep
    Put the system to sleep, through suspend, hibernate,
    hybrid-sleep, or suspend-then-hibernate. The sleep operation
    to use is automatically selected by systemd-logind.service(8).
    By default, suspend-then-hibernate is used, and falls back to
    suspend and then hibernate if not supported. Refer to
    SleepOperation= setting in logind.conf(5) for more details.
    This command is asynchronous, and will return after the sleep
    operation is successfully enqueued. It will not wait for the
    sleep/resume cycle to complete.

    Added in version 256.

suspend
    Suspend the system. This will trigger activation of the
    special target unit suspend.target. This command is
    asynchronous, and will return after the suspend operation is
    successfully enqueued. It will not wait for the suspend/resume
    cycle to complete.

    If --force is specified, and systemd-logind returned error for
    the operation, the error will be ignored and the operation
    will be tried again directly through starting the target unit.

hibernate
    Hibernate the system. This will trigger activation of the
    special target unit hibernate.target. This command is
    asynchronous, and will return after the hibernation operation
    is successfully enqueued. It will not wait for the
    hibernate/thaw cycle to complete.

    This command honors --force in the same way as suspend.

hybrid-sleep
    Hibernate and suspend the system. This will trigger activation
    of the special target unit hybrid-sleep.target. This command
    is asynchronous, and will return after the hybrid sleep
    operation is successfully enqueued. It will not wait for the
    sleep/wake-up cycle to complete.

    This command honors --force in the same way as suspend.

    Added in version 196.

suspend-then-hibernate
    Suspend the system and hibernate it when the battery is low,
    or when the delay specified in systemd-sleep.conf elapsed.
    This will trigger activation of the special target unit
    suspend-then-hibernate.target. This command is asynchronous,
    and will return after the hybrid sleep operation is
    successfully enqueued. It will not wait for the sleep/wake-up
    or hibernate/thaw cycle to complete.

    This command honors --force in the same way as suspend.

    Added in version 240.

### Parameter Syntax

Unit commands listed above take either a single unit name
(designated as UNIT), or multiple unit specifications (designated
as PATTERN...). In the first case, the unit name with or without a
suffix must be given. If the suffix is not specified (unit name is
"abbreviated"), systemctl will append a suitable suffix,
".service" by default, and a type-specific suffix in case of
commands which operate only on specific unit types. For example,

    # systemctl start sshd

and

    # systemctl start sshd.service

are equivalent, as are

    # systemctl isolate default

and

    # systemctl isolate default.target

Note that (absolute) paths to device nodes are automatically
converted to device unit names, and other (absolute) paths to
mount unit names.

    # systemctl status /dev/sda
    # systemctl status /home

are equivalent to:

    # systemctl status dev-sda.device
    # systemctl status home.mount

In the second case, shell-style globs will be matched against the
primary names of all units currently in memory; literal unit
names, with or without a suffix, will be treated as in the first
case. This means that literal unit names always refer to exactly
one unit, but globs may match zero units and this is not
considered an error.

Glob patterns use fnmatch(3), so normal shell-style globbing rules
are used, and "*", "?", "[]" may be used. See glob(7) for more
details. The patterns are matched against the primary names of
units currently in memory, and patterns which do not match
anything are silently skipped. For example:

    # systemctl stop "sshd@*.service"

will stop all sshd@.service instances. Note that alias names of
units, and units that are not in memory are not considered for
glob expansion.

For unit file commands, the specified UNIT should be the name of
the unit file (possibly abbreviated, see above), or the absolute
path to the unit file:

    # systemctl enable foo.service

or

    # systemctl link /path/to/foo.service
