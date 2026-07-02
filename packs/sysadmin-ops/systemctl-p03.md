---
title: "systemctl(1) (part 3/3)"
source: https://man7.org/linux/man-pages/man1/systemctl.1.html
domain: sysadmin-ops
license: GPL-2.0 / CC-BY-SA-4.0
tags: systemd, cron, ssh, rsync, sysadmin, devops
fetched: 2026-07-02
part: 3/3
---

## OPTIONS

The following options are understood:

-t, --type=
    The argument is a comma-separated list of unit types such as
    service and socket. When units are listed with list-units,
    list-dependencies, show, or status, only units of the
    specified types will be shown. By default, units of all types
    are shown. Use --type= to reset the filter.

    As a special case, if one of the arguments is help, a list of
    allowed values will be printed and the program will exit.

--state=
    The argument is a comma-separated list of unit LOAD, SUB, or
    ACTIVE states. When listing units with list-units,
    list-dependencies, show or status, show only those in the
    specified states. Use --state=failed or --failed to show only
    failed units. Use --state= to reset the filter.

    As a special case, if one of the arguments is help, a list of
    allowed values will be printed and the program will exit.

    Added in version 206.

-p, --property=
    When showing unit/job/manager properties with the show
    command, limit display to properties specified in the
    argument. The argument should be a comma-separated list of
    property names, such as "MainPID". Unless specified, all known
    properties are shown. If specified more than once, all
    properties with the specified names are shown. Shell
    completion is implemented for property names.

    For the manager itself, systemctl show will show all available
    properties, most of which are derived or closely match the
    options described in systemd-system.conf(5).

    Properties for units vary by unit type, so showing any unit
    (even a non-existent one) is a way to list properties
    pertaining to this type. Similarly, showing any job will list
    properties pertaining to all jobs. Properties for units are
    documented in systemd.unit(5), and the pages for individual
    unit types systemd.service(5), systemd.socket(5), etc.

-P
    Equivalent to --value --property=, i.e. shows the value of the
    property without the property name or "=". Note that using -P
    once will also affect all properties listed with
    -p/--property=.

    Added in version 246.

-a, --all
    When listing units with list-units, also show inactive units
    and units which are following other units. When showing
    unit/job/manager properties, show all properties regardless
    whether they are set or not.

    To list all units installed in the file system, use the
    list-unit-files command instead.

    When listing units with list-dependencies, recursively show
    dependencies of all dependent units (by default only
    dependencies of target units are shown).

    When used with status, show journal messages in full, even if
    they include unprintable characters or are very long. By
    default, fields with unprintable characters are abbreviated as
    "blob data". (Note that the pager may escape unprintable
    characters again.)

-r, --recursive
    When listing units, also show units of local containers. Units
    of local containers will be prefixed with the container name,
    separated by a single colon character (":").

    Added in version 212.

--reverse
    Show reverse dependencies between units with
    list-dependencies, i.e. follow dependencies of type WantedBy=,
    RequiredBy=, UpheldBy=, PartOf=, BoundBy=, instead of Wants=
    and similar.

    Added in version 203.

--after
    With list-dependencies, show the units that are ordered before
    the specified unit. In other words, recursively list units
    following the After= dependency.

    Note that any After= dependency is automatically mirrored to
    create a Before= dependency. Temporal dependencies may be
    specified explicitly, but are also created implicitly for
    units which are WantedBy= targets (see systemd.target(5)), and
    as a result of other directives (for example
    RequiresMountsFor=). Both explicitly and implicitly introduced
    dependencies are shown with list-dependencies.

    When passed to the list-jobs command, for each printed job
    show which other jobs are waiting for it. May be combined with
    --before to show both the jobs waiting for each job as well as
    all jobs each job is waiting for.

    Added in version 203.

--before
    With list-dependencies, show the units that are ordered after
    the specified unit. In other words, recursively list units
    following the Before= dependency.

    When passed to the list-jobs command, for each printed job
    show which other jobs it is waiting for. May be combined with
    --after to show both the jobs waiting for each job as well as
    all jobs each job is waiting for.

    Added in version 212.

--with-dependencies
    When used with status, cat, list-units, and list-unit-files,
    those commands print all specified units and the dependencies
    of those units.

    Options --reverse, --after, --before may be used to change
    what types of dependencies are shown.

    Added in version 245.

-l, --full
    Do not ellipsize unit names, process tree entries, journal
    output, or truncate unit descriptions in the output of status,
    list-units, list-jobs, and list-timers.

    Also, show installation targets in the output of is-enabled.

--value
    When printing properties with show, only print the value, and
    skip the property name and "=". Also see option -P above.

    Added in version 230.

--show-types
    When showing sockets, show the type of the socket.

    Added in version 202.

--job-mode=
    When queuing a new job, this option controls how to deal with
    already queued jobs. It takes one of "fail", "lenient",
    "replace", "replace-irreversibly", "isolate",
    "ignore-dependencies", "ignore-requirements", "flush",
    "triggering", or "restart-dependencies". Defaults to
    "replace", except when the isolate command is used which
    implies the "isolate" job mode.

    If "fail" is specified and a requested operation on weak
    dependencies conflicts with a pending job (more specifically:
    causes an already pending start job to be reversed into a stop
    job or vice versa), cause the operation to fail.

    If "lenient" is specified and a requested operation conflicts
    with any active/activating unit, cause the operation to fail.

    If "replace" (the default) is specified, any conflicting
    pending job will be replaced, as necessary.

    If "replace-irreversibly" is specified, operate like
    "replace", but also mark the new jobs as irreversible. This
    prevents future conflicting transactions from replacing these
    jobs (or even being enqueued while the irreversible jobs are
    still pending). Irreversible jobs can still be cancelled using
    the cancel command. This job mode should be used on any
    transaction which pulls in shutdown.target.

    "isolate" is only valid for start operations and causes all
    other units to be stopped when the specified unit is started.
    This mode is always used when the isolate command is used.

    "flush" will cause all queued jobs to be canceled when the new
    job is enqueued.

    If "ignore-dependencies" is specified, then all unit
    dependencies are ignored for this new job and the operation is
    executed immediately. If passed, no required units of the unit
    passed will be pulled in, and no ordering dependencies will be
    honored. This is mostly a debugging and rescue tool for the
    administrator and should not be used by applications.

    "ignore-requirements" is similar to "ignore-dependencies", but
    only causes the requirement dependencies to be ignored, the
    ordering dependencies will still be honored.

    "triggering" may only be used with systemctl stop. In this
    mode, the specified unit and any active units that trigger it
    are stopped. See the discussion of Triggers= in
    systemd.unit(5) for more information about triggering units.

    "restart-dependencies" may only be used with systemctl start.
    In this mode, dependencies of the specified unit will receive
    restart propagation, as if a restart job had been enqueued for
    the unit.

    Added in version 209.

-T, --show-transaction
    When enqueuing a unit job (for example as effect of a
    systemctl start invocation or similar), show brief information
    about all jobs enqueued, covering both the requested job and
    any added because of unit dependencies. Note that the output
    will only include jobs immediately part of the transaction
    requested. It is possible that service start-up program code
    run as effect of the enqueued jobs might request further jobs
    to be pulled in. This means that completion of the listed jobs
    might ultimately entail more jobs than the listed ones.

    Added in version 242.

--fail
    Shorthand for --job-mode=fail.

    When used with the kill command, if no units were killed, the
    operation results in an error.

    Added in version 227.

--check-inhibitors=
    When system shutdown or sleep state is requested, this option
    controls checking of inhibitor locks. It takes one of "auto",
    "yes", and "no". Defaults to "auto", which means logind will
    perform the check and respect active inhibitor locks, but
    systemctl will only do a client-side check for interactive
    invocations (i.e. from a TTY), so that a more friendly and
    informative error can be returned to users.  "no" disables the
    checks both in systemctl and systemd-logind(8).

    Applications can establish inhibitor locks to prevent certain
    important operations (such as CD burning) from being
    interrupted by system shutdown or sleep. Any user may take
    these locks and privileged users may override these locks. If
    any locks are taken, shutdown and sleep state requests will
    normally fail (unless explicitly overridden with "no").

    Option --force provides another way to override inhibitors.

    Added in version 248.

-i
    Shortcut for --check-inhibitors=no.

    Added in version 198.

--dry-run
    Just print what would be done. Currently supported by verbs
    halt, poweroff, reboot, kexec, suspend, hibernate,
    hybrid-sleep, suspend-then-hibernate, default, rescue,
    emergency, and exit.

    Added in version 236.

-q, --quiet
    Suppress printing of the results of various commands and also
    the hints about truncated log lines. This does not suppress
    output of commands for which the printed output is the only
    result (like show). Errors are always printed.

-v, --verbose
    Display unit log output while executing unit operations.

    Added in version 258.

--no-warn
    Do not generate the warnings shown by default in the following
    cases:

    •   when systemctl is invoked without procfs mounted on
        /proc/,

    •   when using enable or disable on units without install
        information (i.e. do not have or have an empty [Install]
        section),

    •   when using disable combined with --user on units that are
        enabled in global scope,

    •   when a stop-ped, disable-d, or mask-ed unit still has
        active triggering units,

    •   when a unit file is changed and requires daemon-reload.

    Added in version 253.

--no-block
    Do not synchronously wait for the requested operation to
    finish. If this is not specified, the job will be verified,
    enqueued and systemctl will wait until the unit's start-up is
    completed. By passing this argument, it is only verified and
    enqueued. This option may not be combined with --wait.

--wait
    When used with start or restart, synchronously wait for
    started units to terminate again. This option may not be
    combined with --no-block. Note that this will wait forever if
    any given unit never terminates (by itself or by getting
    stopped explicitly); particularly services which use
    "RemainAfterExit=yes".

    When used with is-system-running, wait until the boot process
    is completed before returning.

    When used with kill, wait until the signalled units terminate.
    Note that this will wait forever if any given unit never
    terminates.

    Added in version 232.

--user
    Talk to the service manager of the calling user, rather than
    the service manager of the system.

--system
    Talk to the service manager of the system. This is the implied
    default.

--failed
    List units in failed state. This is equivalent to
    --state=failed.

    Added in version 233.

--no-wall
    Do not send wall message before halt, power-off and reboot.

--global
    When used with enable and disable, operate on the global user
    configuration directory, thus enabling or disabling a unit
    file globally for all future logins of all users.

--no-reload
    When used with enable, disable, preset, mask, or unmask, do
    not implicitly reload daemon configuration after executing the
    changes.

--kill-whom=
    When used with kill, choose which processes to send a UNIX
    process signal to. Must be one of main, control, cgroup or all
    to select whether to kill only the main process, the control
    process, all processes in the unit's control group or all
    processes of the unit. The main process of the unit is the one
    that defines the life-time of it. A control process of a unit
    is one that is invoked by the manager to induce state changes
    of it. For example, all processes started due to the
    ExecStartPre=, ExecStop= or ExecReload= settings of service
    units are control processes. Note that there is only one
    control process per unit at a time, as only one state change
    is executed at a time. For services of type Type=forking, the
    initial process started by the manager for ExecStart= is a
    control process, while the process ultimately forked off by
    that one is then considered the main process of the unit (if
    it can be determined). This is different for service units of
    other types, where the process forked off by the manager for
    ExecStart= is always the main process itself. A service unit
    consists of zero or one main process, zero or one control
    process plus any number of additional processes part of the
    unit's control group. Not all unit types manage processes of
    these types however. For example, for mount units, control
    processes are defined (which are the invocations of
    /usr/bin/mount and /usr/bin/umount), but no main process is
    defined. If omitted, defaults to all, except if
    --kill-subgroup= is used in which case defaults to cgroup.

    Added in version 252.

--kill-value=INT
    If used with the kill command, enqueues a signal along with
    the specified integer value parameter to the specified
    process(es). This operation is only available for POSIX
    Realtime Signals (i.e.  --signal=SIGRTMIN+...  or
    --signal=SIGRTMAX-...), and ensures the signals are generated
    via the sigqueue(3) system call, rather than kill(3). The
    specified value must be a 32-bit signed integer, and may be
    specified either in decimal, in hexadecimal (if prefixed with
    "0x"), octal (if prefixed with "0o") or binary (if prefixed
    with "0b")

    If this option is used the signal will only be enqueued on the
    control or main process of the unit, never on other processes
    belonging to the unit, i.e.  --kill-whom=all will only affect
    main and control processes but no other processes.

    Added in version 254.

--kill-subgroup=PATH
    Takes a control group sub-path to send signals to, for use
    with the kill command. By default the chosen signal is
    delivered to all processes of the unit's cgroups (as well as
    the main/control processes (if outside) – subject to
    --kill-whom=). But with this option a subgroup can be
    selelected instead. This functionality is only available if
    "cgroup" or "cgroup-fail" are used with --kill-whom=, and in
    fact the former is the default if --kill-subgroup= is used.

    The specified path may, but doesn't have to be prefixed with a
    slash, and its absence or presence has no effect, the path is
    either way taken relative to the unit's main control group
    path.

    This functionality is only available on units where control
    group delegation is enabled (see Delegate= in
    systemd.resource-control(5)).

    Added in version 258.

-s, --signal=
    When used with kill, choose which signal to send to selected
    processes. Must be one of the well-known signal specifiers
    such as SIGTERM, SIGINT or SIGSTOP. If omitted, defaults to
    SIGTERM.

    The special value "help" will list the known values and the
    program will exit immediately, and the special value "list"
    will list known values along with the numerical signal numbers
    and the program will exit immediately.

--what=
    Select what type of per-unit resources to remove when the
    clean command is invoked, see above. Takes one of
    configuration, state, cache, logs, runtime, fdstore to select
    the type of resource. This option may be specified more than
    once, in which case all specified resource types are removed.
    Also accepts the special value all as a shortcut for
    specifying all six resource types. If this option is not
    specified defaults to the combination of cache, runtime and
    fdstore, i.e. the three kinds of resources that are generally
    considered to be redundant and can be reconstructed on next
    invocation. The empty argument can be used to reset to this
    default.

    Note that the explicit removal of the fdstore resource type is
    only useful if the FileDescriptorStorePreserve= option is
    enabled, since the file descriptor store is otherwise cleaned
    automatically when the unit is stopped.

    Added in version 243.

-f, --force
    When used with enable, overwrite any existing conflicting
    symlinks.

    When used with edit, create all of the specified units which
    do not already exist.

    When used with suspend, hibernate, hybrid-sleep, or
    suspend-then-hibernate, the error returned by systemd-logind
    will be ignored, and the operation will be performed directly
    through starting the corresponding units.

    When used with halt, poweroff, reboot, or kexec, execute the
    selected operation without shutting down all units. However,
    all processes will be killed forcibly and all file systems are
    unmounted or remounted read-only. This is hence a drastic but
    relatively safe option to request an immediate reboot. If
    --force is specified twice for these operations (with the
    exception of kexec), they will be executed immediately,
    without terminating any processes or unmounting any file
    systems.

        Warning
        Specifying --force twice with any of these operations
        might result in data loss. Note that when --force is
        specified twice the selected operation is executed by
        systemctl itself, and the system manager is not contacted.
        This means the command should succeed even when the system
        manager has crashed.

--message=
    When used with halt, poweroff or reboot, set a short message
    explaining the reason for the operation. The message will be
    logged together with the default shutdown message.

    Added in version 225.

--now
    When used with enable, disable, mask, or reenable, also
    start/stop/try-restart the units after the specified unit file
    operations succeed.

    Added in version 220.

--root=
    When used with enable/disable/is-enabled (and related
    commands), use the specified root path when looking for unit
    files. If this option is present, systemctl will operate on
    the file system directly, instead of communicating with the
    systemd daemon to carry out changes.

--image=image
    Takes a path to a disk image file or block device node. If
    specified, all operations are applied to file system in the
    indicated disk image. This option is similar to --root=, but
    operates on file systems stored in disk images or block
    devices. The disk image should either contain just a file
    system or a set of file systems within a GPT partition table,
    following the UAPI.2 Discoverable Partitions Specification[2].
    For further information on supported disk images, see
    systemd-nspawn(1)'s switch of the same name.

    Added in version 252.

--image-policy=policy
    Takes an image policy string as argument, as per
    systemd.image-policy(7). The policy is enforced when operating
    on the disk image specified via --image=, see above. If not
    specified, defaults to the "*" policy, i.e. all recognized
    file systems in the image are used.

--runtime
    When used with enable, disable, edit, (and related commands),
    make changes only temporarily, so that they are lost on the
    next reboot. This will have the effect that changes are not
    made in subdirectories of /etc/ but in /run/, with identical
    immediate effects, however, since the latter is lost on
    reboot, the changes are lost too.

    Similarly, when used with set-property, make changes only
    temporarily, so that they are lost on the next reboot.

--preset-mode=
    Takes one of "full" (the default), "enable-only",
    "disable-only". When used with the preset or preset-all
    commands, controls whether units shall be disabled and enabled
    according to the preset rules, or only enabled, or only
    disabled.

    Added in version 215.

-n, --lines=
    When used with status, controls the number of journal lines to
    show, counting from the most recent ones. Takes a positive
    integer argument, or 0 to disable journal output. Defaults to
    10.

-o, --output=
    When used with status, controls the formatting of the journal
    entries that are shown. For the available choices, see
    journalctl(1). Defaults to "short".

--firmware-setup
    When used with the reboot, poweroff, or halt command, indicate
    to the system's firmware to reboot into the firmware setup
    interface for the next boot. Note that this functionality is
    not available on all systems.

    Added in version 220.

--boot-loader-menu=timeout
    When used with the reboot, poweroff, or halt command, indicate
    to the system's boot loader to show the boot loader menu on
    the following boot. Takes a time value as parameter —
    indicating the menu timeout. Pass zero in order to disable the
    menu timeout. Note that not all boot loaders support this
    functionality.

    Added in version 242.

--boot-loader-entry=ID
    When used with the reboot, poweroff, or halt command, indicate
    to the system's boot loader to boot into a specific boot
    loader entry on the following boot. Takes a boot loader entry
    identifier as argument, or "help" in order to list available
    entries. Note that not all boot loaders support this
    functionality.

    Added in version 242.

--reboot-argument=
    This switch is used with reboot. The value is architecture and
    firmware specific. As an example, "recovery" might be used to
    trigger system recovery, and "fota" might be used to trigger a
    “firmware over the air” update.

    Added in version 246.

--kernel-cmdline=
    When used with kexec, append the specified string to the
    kernel command line options of the kexec kernel. The kernel
    command line is taken from the boot loader entry of the
    currently booted kernel (as selected automatically when no
    kexec kernel is preloaded, see kexec above). This string is
    appended verbatim, separated from the existing options by a
    single space.  systemctl kexec will fail if this option is
    specified when a kexec kernel is already loaded.

    Added in version 261.

--plain
    When used with list-dependencies, list-units or list-machines,
    the output is printed as a list instead of a tree, and the
    bullet circles are omitted.

    Added in version 203.

--timestamp=
    Change the format of printed timestamps. The following values
    may be used:

    pretty (this is the default)
        "Day YYYY-MM-DD HH:MM:SS TZ"

        Added in version 248.

    unix
        "@seconds-since-the-epoch"

        Added in version 251.

    us, μs
        "Day YYYY-MM-DD HH:MM:SS.UUUUUU TZ"

        Added in version 248.

    utc
        "Day YYYY-MM-DD HH:MM:SS UTC"

        Added in version 248.

    us+utc, μs+utc
        "Day YYYY-MM-DD HH:MM:SS.UUUUUU UTC"

        Added in version 248.

    Added in version 247.

--mkdir
    When used with bind, creates the destination file or directory
    before applying the bind mount. Note that even though the name
    of this option suggests that it is suitable only for
    directories, this option also creates the destination file
    node to mount over if the object to mount is not a directory,
    but a regular file, device node, socket or FIFO.

    Added in version 248.

--read-only
    When used with bind, creates a read-only bind mount.

    Added in version 248.

--drop-in=NAME
    When used with edit, use NAME as the drop-in file name instead
    of override.conf.

    Added in version 253.

--when=
    When used with halt, poweroff, reboot or kexec, schedule the
    action to be performed at the given timestamp, which should
    adhere to the syntax documented in systemd.time(7) section
    "PARSING TIMESTAMPS". Specially, if "show" is given, the
    currently scheduled action will be shown, which can be
    canceled by passing an empty string or "cancel".  "auto" will
    schedule the action according to maintenance window or one
    minute in the future.

    Added in version 254.

--stdin
    When used with edit, the contents of the file will be read
    from standard input and the editor will not be launched. In
    this mode, the old contents of the file are completely
    replaced. This is useful to "edit" unit files from scripts:

        $ systemctl edit --drop-in=limits.conf --stdin some-service.service <<EOF
        [Unit]
        AllowedCPUs=7,11
        EOF

    Multiple drop-ins may be "edited" in this mode; the same
    contents will be written to all of them.

    Added in version 256.

-H, --host=
    Execute the operation remotely. Specify a hostname, or a
    username and hostname separated by "@", to connect to. The
    hostname may optionally be suffixed by a port ssh is listening
    on, separated by ":", and then a container name, separated by
    "/", which connects directly to a specific container on the
    specified host. This will use SSH to talk to the remote
    machine manager instance. Container names may be enumerated
    with machinectl -H HOST. Put IPv6 addresses in brackets.

-M, --machine=
    Execute operation on a local container. Specify a container
    name to connect to, optionally prefixed by a user name to
    connect as and a separating "@" character. If the special
    string ".host" is used in place of the container name, a
    connection to the local system is made (which is useful to
    connect to a specific user's user bus: "--user
    --machine=lennart@.host"). If the "@" syntax is not used, the
    connection is made as root user. If the "@" syntax is used
    either the left hand side or the right hand side may be
    omitted (but not both) in which case the local user name and
    ".host" are implied.

-C, --capsule=
    Execute operation on a capsule. Specify a capsule name to
    connect to. See capsule@.service(5) for details about
    capsules.

    Added in version 256.

--no-ask-password
    Do not query the user for authentication for privileged
    operations.

--no-pager
    Do not pipe output into a pager.

--legend=BOOL
    Enable or disable printing of the legend, i.e. column headers
    and the footer with hints. The legend is printed by default,
    unless disabled with --quiet or similar.

-h, --help
    Print a short help text and exit.

--version
    Print a short version string and exit.


## EXIT STATUS

On success, 0 is returned, a non-zero failure code otherwise.

systemctl uses the return codes defined by LSB, as defined in LSB
3.0.0[3].

Table 5. LSB return codes
┌───────┬────────────────────┬────────────────────┐
│ Value │ Description in LSB │ Use in systemd     │
├───────┼────────────────────┼────────────────────┤
│ 0     │ "program is        │ unit is active     │
│       │ running or service │                    │
│       │ is OK"             │                    │
├───────┼────────────────────┼────────────────────┤
│ 1     │ "program is dead   │ unit not failed    │
│       │ and /var/run pid   │ (used by           │
│       │ file exists"       │ is-failed)         │
├───────┼────────────────────┼────────────────────┤
│ 2     │ "program is dead   │ unused             │
│       │ and /var/lock lock │                    │
│       │ file exists"       │                    │
├───────┼────────────────────┼────────────────────┤
│ 3     │ "program is not    │ unit is not active │
│       │ running"           │                    │
├───────┼────────────────────┼────────────────────┤
│ 4     │ "program or        │ no such unit       │
│       │ service status is  │                    │
│       │ unknown"           │                    │
└───────┴────────────────────┴────────────────────┘

The mapping of LSB service states to systemd unit states is
imperfect, so it is better to not rely on those return values but
to look for specific unit states and substates instead.


## ENVIRONMENT

$SYSTEMD_EDITOR
    Editor to use when editing units; overrides $EDITOR and
    $VISUAL. If neither $SYSTEMD_EDITOR nor $EDITOR nor $VISUAL
    are present or if it is set to an empty string or if their
    execution failed, systemctl will try to execute well known
    editors in this order: editor(1), nano(1), vim(1), vi(1).

    Added in version 218.

$SYSTEMD_LOG_LEVEL
    The maximum log level of emitted messages (messages with a
    higher log level, i.e. less important ones, will be
    suppressed). Takes a comma-separated list of values. A value
    may be either one of (in order of decreasing importance)
    emerg, alert, crit, err, warning, notice, info, debug, or an
    integer in the range 0...7. See syslog(3) for more
    information. Each value may optionally be prefixed with one of
    console, syslog, kmsg or journal followed by a colon to set
    the maximum log level for that specific log target (e.g.
    SYSTEMD_LOG_LEVEL=debug,console:info specifies to log at debug
    level except when logging to the console which should be at
    info level). Note that the global maximum log level takes
    priority over any per target maximum log levels.

$SYSTEMD_LOG_COLOR
    A boolean. If true, messages written to the tty will be
    colored according to priority.

    This setting is only useful when messages are written directly
    to the terminal, because journalctl(1) and other tools that
    display logs will color messages based on the log level on
    their own.

$SYSTEMD_LOG_TIME
    A boolean. If true, console log messages will be prefixed with
    a timestamp.

    This setting is only useful when messages are written directly
    to the terminal or a file, because journalctl(1) and other
    tools that display logs will attach timestamps based on the
    entry metadata on their own.

$SYSTEMD_LOG_LOCATION
    A boolean. If true, messages will be prefixed with a filename
    and line number in the source code where the message
    originates.

    Note that the log location is often attached as metadata to
    journal entries anyway. Including it directly in the message
    text can nevertheless be convenient when debugging programs.

$SYSTEMD_LOG_TARGET
    The destination for log messages. One of console (log to the
    attached tty), console-prefixed (log to the attached tty but
    with prefixes encoding the log level and "facility", see
    syslog(3), kmsg (log to the kernel circular log buffer),
    journal (log to the journal), journal-or-kmsg (log to the
    journal if available, and to kmsg otherwise), auto (determine
    the appropriate log target automatically, the default), null
    (disable log output).

$SYSTEMD_PAGER, $PAGER
    Pager to use when --no-pager is not given.  $SYSTEMD_PAGER is
    used if set; otherwise $PAGER is used. If neither
    $SYSTEMD_PAGER nor $PAGER are set, a set of well-known pager
    implementations is tried in turn, including less(1) and
    more(1), until one is found. If no pager implementation is
    discovered, no pager is invoked. Setting those environment
    variables to an empty string or the value "cat" is equivalent
    to passing --no-pager.

    Note: if $SYSTEMD_PAGERSECURE is not set, $SYSTEMD_PAGER and
    $PAGER can only be used to disable the pager (with "cat" or
    ""), and are otherwise ignored.

$SYSTEMD_LESS
    Override the options passed to less (by default "FRSXMK").

    Users might want to change two options in particular:

    K
        This option instructs the pager to exit immediately when
        Ctrl+C is pressed. To allow less to handle Ctrl+C itself
        to switch back to the pager command prompt, unset this
        option.

        If the value of $SYSTEMD_LESS does not include "K", and
        the pager that is invoked is less, Ctrl+C will be ignored
        by the executable, and needs to be handled by the pager.

    X
        This option instructs the pager to not send termcap
        initialization and deinitialization strings to the
        terminal. It is set by default to allow command output to
        remain visible in the terminal even after the pager exits.
        Nevertheless, this prevents some pager functionality from
        working, in particular paged output cannot be scrolled
        with the mouse.

    Note that setting the regular $LESS environment variable has
    no effect for less invocations by systemd tools.

    See less(1) for more discussion.

$SYSTEMD_LESSCHARSET
    Override the charset passed to less (by default "utf-8", if
    the invoking terminal is determined to be UTF-8 compatible).

    Note that setting the regular $LESSCHARSET environment
    variable has no effect for less invocations by systemd tools.

$SYSTEMD_PAGERSECURE
    Common pager commands like less(1), in addition to "paging",
    i.e. scrolling through the output, support opening of or
    writing to other files and running arbitrary shell commands.
    When commands are invoked with elevated privileges, for
    example under sudo(8) or pkexec(1), the pager becomes a
    security boundary. Care must be taken that only programs with
    strictly limited functionality are used as pagers, and
    unintended interactive features like opening or creation of
    new files or starting of subprocesses are not allowed. "Secure
    mode" for the pager may be enabled as described below, if the
    pager supports that (most pagers are not written in a way that
    takes this into consideration). It is recommended to either
    explicitly enable "secure mode" or to completely disable the
    pager using --no-pager or PAGER=cat when allowing untrusted
    users to execute commands with elevated privileges.

    This option takes a boolean argument. When set to true, the
    "secure mode" of the pager is enabled. In "secure mode",
    LESSSECURE=1 will be set when invoking the pager, which
    instructs the pager to disable commands that open or create
    new files or start new subprocesses. Currently only less(1) is
    known to understand this variable and implement "secure mode".

    When set to false, no limitation is placed on the pager.
    Setting SYSTEMD_PAGERSECURE=0 or not removing it from the
    inherited environment may allow the user to invoke arbitrary
    commands.

    When $SYSTEMD_PAGERSECURE is not set, systemd tools attempt to
    automatically figure out if "secure mode" should be enabled
    and whether the pager supports it. "Secure mode" is enabled if
    the effective UID is not the same as the owner of the login
    session, see geteuid(2) and sd_pid_get_owner_uid(3), or when
    running under sudo(8) or similar tools ($SUDO_UID is set [4]).
    In those cases, SYSTEMD_PAGERSECURE=1 will be set and pagers
    which are not known to implement "secure mode" will not be
    used at all. Note that this autodetection only covers the most
    common mechanisms to elevate privileges and is intended as
    convenience. It is recommended to explicitly set
    $SYSTEMD_PAGERSECURE or disable the pager.

    Note that if the $SYSTEMD_PAGER or $PAGER variables are to be
    honoured, other than to disable the pager,
    $SYSTEMD_PAGERSECURE must be set too.

$SYSTEMD_COLORS
    Takes a boolean argument, or a special value. By default
    (unset), systemd and related utilities will use colors in
    their output if possible. If $COLORTERM is set to "truecolor"
    or "24bit", 24-bit colors will be enabled, 256 colors
    otherwise, unless $NO_COLOR or $TERM indicates colors are
    disabled.

    true
        Same as unset, except that $NO_COLOR is ignored.

    false
        The output will be monochrome.

    "16", "256", "24bit"
        Always use the base 16 ANSI colors, 256 colors, or 24 bit
        color, respectively.

    "auto-16", "auto-256", "auto-24bit"
        Use the given quantity of colours, subject to $TERM, and
        what the console is connected to.

$SYSTEMD_URLIFY
    The value must be a boolean. Controls whether clickable links
    should be generated in the output for terminal emulators
    supporting this. This can be specified to override the
    decision that systemd makes based on $TERM and other
    conditions.


## SEE ALSO

systemd(1), journalctl(1), loginctl(1), machinectl(1),
systemd.unit(5), systemd.resource-control(5), systemd.special(7),
wall(1), systemd.preset(5), systemd.generator(7), glob(7)


## NOTES

 1. UAPI.1 Boot Loader Specification
    https://uapi-group.org/specifications/specs/boot_loader_specification

 2. UAPI.2 Discoverable Partitions Specification
    https://uapi-group.org/specifications/specs/discoverable_partitions_specification

 3. LSB 3.0.0
    http://refspecs.linuxbase.org/LSB_3.0.0/LSB-PDA/LSB-PDA/iniscrptact.html

 4. It is recommended for other tools to set and check $SUDO_UID
    as appropriate, treating it is a common interface.
