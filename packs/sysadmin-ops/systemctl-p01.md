---
title: "systemctl(1) (part 1/3)"
source: https://man7.org/linux/man-pages/man1/systemctl.1.html
domain: sysadmin-ops
license: GPL-2.0 / CC-BY-SA-4.0
tags: systemd, cron, ssh, rsync, sysadmin, devops
fetched: 2026-07-02
part: 1/3
---

# systemctl(1) — Linux manual page

SYSTEMCTL(1)                    systemctl                    SYSTEMCTL(1)


## NAME

systemctl - Control the systemd system and service manager


## SYNOPSIS

systemctl [OPTIONS...] COMMAND [UNIT...]


## DESCRIPTION

systemctl may be used to introspect and control the state of the
"systemd" system and service manager. Please refer to systemd(1)
for an introduction into the basic concepts and functionality this
tool manages.

## COMMANDS

The following commands are understood:

   Unit Commands (Introspection and Modification)
list-units [PATTERN...]
    List units that systemd currently has in memory. This includes
    units that are either referenced directly or through a
    dependency, units that are pinned by applications
    programmatically, or units that were active in the past and
    have failed. By default, only units which are active, have
    pending jobs, or have failed are shown; this can be changed
    with option --all. If one or more PATTERNs are specified, only
    units matching one of them are shown. The units that are shown
    are additionally filtered by --type= and --state= if those
    options are specified.

    Note that this command does not show unit templates, but only
    instances of unit templates. Units templates that are not
    instantiated are not runnable, and will thus never show up in
    the output of this command. Specifically this means that
    foo@.service will never be shown in this list — unless
    instantiated, e.g. as foo@bar.service. Use list-unit-files
    (see below) for listing installed unit template files.

    Produces output similar to

          UNIT                         LOAD   ACTIVE SUB     DESCRIPTION
          sys-module-fuse.device       loaded active plugged /sys/module/fuse
          -.mount                      loaded active mounted Root Mount
          boot-efi.mount               loaded active mounted /boot/efi
          systemd-journald.service     loaded active running Journal Service
          systemd-logind.service       loaded active running Login Service
        ● user@1000.service            loaded failed failed  User Manager for UID 1000
          ...
          systemd-tmpfiles-clean.timer loaded active waiting Daily Cleanup of Temporary Directories

        LOAD   = Reflects whether the unit definition was properly loaded.
        ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
        SUB    = The low-level unit activation state, values depend on unit type.

        123 loaded units listed. Pass --all to see loaded but inactive units, too.
        To show all installed unit files use 'systemctl list-unit-files'.

    The header and the last unit of a given type are underlined if
    the terminal supports that. A colored dot is shown next to
    services which were masked, not found, or otherwise failed.

    The LOAD column shows the load state, one of loaded,
    not-found, bad-setting, error, masked. The ACTIVE columns
    shows the general unit state, one of the following:

    Table 1. Unit ACTIVE states
    ┌──────────────┬──────────────────────────┐
    │ State        │ Description              │
    ├──────────────┼──────────────────────────┤
    │ active       │ Started, bound, plugged  │
    │              │ in, ..., depending on    │
    │              │ the unit type.           │
    ├──────────────┼──────────────────────────┤
    │ inactive     │ Stopped, unbound,        │
    │              │ unplugged, ...,          │
    │              │ depending on the unit    │
    │              │ type.                    │
    ├──────────────┼──────────────────────────┤
    │ failed       │ Similar to inactive, but │
    │              │ the unit failed in some  │
    │              │ way (process returned    │
    │              │ error code on exit,      │
    │              │ crashed, an operation    │
    │              │ timed out, or after too  │
    │              │ many restarts).          │
    ├──────────────┼──────────────────────────┤
    │ activating   │ Changing from inactive   │
    │              │ to active.               │
    ├──────────────┼──────────────────────────┤
    │ deactivating │ Changing from active to  │
    │              │ inactive.                │
    ├──────────────┼──────────────────────────┤
    │ maintenance  │ Unit is inactive and a   │
    │              │ maintenance operation is │
    │              │ in progress.             │
    ├──────────────┼──────────────────────────┤
    │ reloading    │ Unit is active and it is │
    │              │ reloading its            │
    │              │ configuration.           │
    ├──────────────┼──────────────────────────┤
    │ refreshing   │ Unit is active and a new │
    │              │ mount is being activated │
    │              │ in its namespace.        │
    └──────────────┴──────────────────────────┘

    The SUB column shows the unit-type-specific detailed state of
    the unit, possible values vary by unit type. The list of
    possible LOAD, ACTIVE, and SUB states is not constant and new
    systemd releases may both add and remove values.

        systemctl --state=help

    command may be used to display the current set of possible
    values.

    This is the default command.

list-automounts [PATTERN...]
    List automount units currently in memory, ordered by mount
    path. If one or more PATTERNs are specified, only automount
    units matching one of them are shown. Produces output similar
    to

        WHAT        WHERE                    MOUNTED IDLE TIMEOUT UNIT
        /dev/sdb1   /mnt/test                no      120s         mnt-test.automount
        binfmt_misc /proc/sys/fs/binfmt_misc yes     0            proc-sys-fs-binfmt_misc.automount

        2 automounts listed.

    Also see --show-types, --all, and --state=.

    Added in version 252.

list-paths [PATTERN...]
    List path units currently in memory, ordered by path. If one
    or more PATTERNs are specified, only path units matching one
    of them are shown. Produces output similar to

        PATH                           CONDITION         UNIT                               ACTIVATES
        /run/systemd/ask-password      DirectoryNotEmpty systemd-ask-password-plymouth.path systemd-ask-password-plymouth.service
        /run/systemd/ask-password      DirectoryNotEmpty systemd-ask-password-wall.path     systemd-ask-password-wall.service
        /var/cache/cups/org.cups.cupsd PathExists        cups.path                          cups.service

        3 paths listed.

    Also see --show-types, --all, and --state=.

    Added in version 254.

list-sockets [PATTERN...]
    List socket units currently in memory, ordered by listening
    address. If one or more PATTERNs are specified, only socket
    units matching one of them are shown. Produces output similar
    to

        LISTEN           UNIT                        ACTIVATES
        kobject-uevent 1 systemd-udevd-kernel.socket systemd-udevd.service
        /dev/rfkill      systemd-rfkill.socket       systemd-rfkill.service
        ...

        5 sockets listed.

    Note: because the addresses might contains spaces, this output
    is not suitable for programmatic consumption.

    Also see --show-types, --all, and --state=.

    Added in version 202.

list-timers [PATTERN...]
    List timer units currently in memory, ordered by the time they
    elapse next. If one or more PATTERNs are specified, only units
    matching one of them are shown. Produces output similar to

        NEXT                         LEFT          LAST                         PASSED     UNIT                         ACTIVATES
        -                            -             Thu 2017-02-23 13:40:29 EST  3 days ago ureadahead-stop.timer        ureadahead-stop.service
        Sun 2017-02-26 18:55:42 EST  1min 14s left Thu 2017-02-23 13:54:44 EST  3 days ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
        Sun 2017-02-26 20:37:16 EST  1h 42min left Sun 2017-02-26 11:56:36 EST  6h ago     apt-daily.timer              apt-daily.service
        Sun 2017-02-26 20:57:49 EST  2h 3min left  Sun 2017-02-26 11:56:36 EST  6h ago     snapd.refresh.timer          snapd.refresh.service

    NEXT shows the next time the timer will run.

    LEFT shows how long till the next time the timer runs.

    LAST shows the last time the timer ran.

    PASSED shows how long has passed since the timer last ran.

    UNIT shows the name of the timer

    ACTIVATES shows the name the service the timer activates when
    it runs.

    Also see --all and --state=.

    Added in version 209.

is-active PATTERN...
    Check whether any of the specified units are active (i.e.
    running). Returns an exit code 0 if at least one is active, or
    non-zero otherwise. Unless --quiet is specified, this will
    also print the current unit state to standard output.

is-failed [PATTERN...]
    Check whether any of the specified units is in the "failed"
    state. If no unit is specified, check whether there are any
    failed units or ordering cycles, which corresponds to the
    "degraded" state returned by is-system-running. Returns an
    exit code 0 if at least one has failed, non-zero otherwise.
    Unless --quiet is specified, this will also print the current
    unit or system state to standard output.

    Added in version 197.

status [PATTERN...|PID...]]
    Show runtime status information about the whole system or
    about one or more units followed by most recent log data from
    the journal. If no positional arguments are specified, and no
    unit filter is given with --type=, --state=, or --failed,
    shows the status of the whole system. If combined with --all,
    follows that with the status of all units. If positional
    arguments are specified, each positional argument is treated
    as either a unit name to show, or a glob pattern to show units
    whose names match that pattern, or a PID to show the unit
    containing that PID. When --type=, --state=, or --failed are
    used, units are additionally filtered by the TYPE and ACTIVE
    state.

    This function is intended to generate human-readable output.
    If you are looking for computer-parsable output, use show
    instead. By default, this function only shows 10 lines of
    output and ellipsizes lines to fit in the terminal window.
    This can be changed with --lines and --full, see above. In
    addition, journalctl --unit=NAME or journalctl
    --user-unit=NAME use a similar filter for messages and might
    be more convenient.

    Note that this operation only displays runtime status, i.e.
    information about the current invocation of the unit (if it is
    running) or the most recent invocation (if it is not running
    anymore, and has not been released from memory). Information
    about earlier invocations, invocations from previous system
    boots, or prior invocations that have already been released
    from memory may be retrieved via journalctl --unit=.

    systemd implicitly loads units as necessary, so just running
    the status will attempt to load a file. The command is thus
    not useful for determining if something was already loaded or
    not. The units may possibly also be quickly unloaded after the
    operation is completed if there's no reason to keep it in
    memory thereafter.

    Example 1. Example output from systemctl status

        $ systemctl status bluetooth
        ● bluetooth.service - Bluetooth service
           Loaded: loaded (/usr/lib/systemd/system/bluetooth.service; enabled; preset: enabled)
           Active: active (running) since Wed 2017-01-04 13:54:04 EST; 1 weeks 0 days ago
             Docs: man:bluetoothd(8)
         Main PID: 930 (bluetoothd)
           Status: "Running"
            Tasks: 1
           Memory: 648.0K
              CPU: 435ms
           CGroup: /system.slice/bluetooth.service
                   └─930 /usr/lib/bluetooth/bluetoothd

        Jan 12 10:46:45 example.com bluetoothd[8900]: Not enough free handles to register service
        Jan 12 10:46:45 example.com bluetoothd[8900]: Current Time Service could not be registered
        Jan 12 10:46:45 example.com bluetoothd[8900]: gatt-time-server: Input/output error (5)

    The dot ("●") uses color on supported terminals to summarize
    the unit state at a glance. Along with its color, its shape
    varies according to its state: "inactive" or "maintenance" is
    a white circle ("○"), "active" is a green dot ("●"),
    "deactivating" is a white dot, "failed" or "error" is a red
    cross ("×"), and "reloading" or "refreshing" is a green
    clockwise circle arrow ("↻").

    The "Loaded:" line in the output will show "loaded" if the
    unit has been loaded into memory. Other possible values for
    "Loaded:" include: "error" if there was a problem loading it,
    "not-found" if no unit file was found for this unit,
    "bad-setting" if an essential unit file setting could not be
    parsed and "masked" if the unit file has been masked. Along
    with showing the path to the unit file, this line will also
    show the enablement state. Enabled units are included in the
    dependency network between units, and thus are started at boot
    or via some other form of activation. See the full table of
    possible enablement states — including the definition of
    "masked" — in the documentation for the is-enabled command.

    The "Active:" line shows active state. The value is usually
    "active" or "inactive". Active could mean started, bound,
    plugged in, etc depending on the unit type. The unit could
    also be in process of changing states, reporting a state of
    "activating" or "deactivating". A special "failed" state is
    entered when the service failed in some way, such as a crash,
    exiting with an error code or timing out. If the failed state
    is entered the cause will be logged for later reference.

show [PATTERN...|JOB...]
    Show properties of one or more units, jobs, or the manager
    itself. If no argument is specified, properties of the manager
    will be shown. If a unit name is specified, properties of the
    unit are shown, and if a job ID is specified, properties of
    the job are shown. By default, empty properties are
    suppressed. Use --all to show those too. To select specific
    properties to show, use --property=. This command is intended
    to be used whenever computer-parsable output is required. Use
    status if you are looking for formatted human-readable output.

    Many properties shown by systemctl show map directly to
    configuration settings of the system and service manager and
    its unit files. Note that the properties shown by the command
    are generally more low-level, normalized versions of the
    original configuration settings and expose runtime state in
    addition to configuration. For example, properties shown for
    service units include the service's current main process
    identifier as "MainPID" (which is runtime state), and time
    settings are always exposed as properties ending in the
    "...USec" suffix even if a matching configuration options end
    in "...Sec", because microseconds is the normalized time unit
    used internally by the system and service manager.

    For details about many of these properties, see the
    documentation of the D-Bus interface backing these properties,
    see org.freedesktop.systemd1(5).

cat PATTERN...
    Show backing files of one or more units. Prints the "fragment"
    and "drop-ins" (source files) of units. Each file is preceded
    by a comment which includes the file name. Note that this
    shows the contents of the backing files on disk, which might
    not match the system manager's understanding of these units if
    any unit files were updated on disk and the daemon-reload
    command was not issued since.

    Added in version 209.

help PATTERN...|PID...
    Show manual pages for one or more units, if available. If a
    PID is given, the manual pages for the unit the process
    belongs to are shown.

    Added in version 185.

list-dependencies [UNIT...]
    Shows units required and wanted by the specified units. This
    recursively lists units following the Requires=, Requisite=,
    Wants=, ConsistsOf=, BindsTo=, and Upholds= dependencies. If
    no units are specified, default.target is implied.

    The units that are shown are additionally filtered by --type=
    and --state= if those options are specified. Note that we will
    not be able to use a tree structure in this case, so --plain
    is implied.

    By default, only target units are recursively expanded. When
    --all is passed, all other units are recursively expanded as
    well.

    Options --reverse, --after, --before may be used to change
    what types of dependencies are shown.

    Note that this command only lists units currently loaded into
    memory by the service manager. In particular, this command is
    not suitable to get a comprehensive list at all reverse
    dependencies on a specific unit, as it will not list the
    dependencies declared by units currently not loaded.

    Added in version 198.

start PATTERN...
    Start (activate) one or more units specified on the command
    line.

    Note that unit glob patterns expand to names of units
    currently in memory. Units which are not active and are not in
    a failed state usually are not in memory, and will not be
    matched by any pattern. In addition, in case of instantiated
    units, systemd is often unaware of the instance name until the
    instance has been started. Therefore, using glob patterns with
    start has limited usefulness. Also, secondary alias names of
    units are not considered.

    Option --all may be used to also operate on inactive units
    which are referenced by other loaded units. Note that this is
    not the same as operating on "all" possible units, because as
    the previous paragraph describes, such a list is ill-defined.
    Nevertheless, systemctl start --all GLOB may be useful if all
    the units that should match the pattern are pulled in by some
    target which is known to be loaded.

stop PATTERN...
    Stop (deactivate) one or more units specified on the command
    line.

    This command will fail if the unit does not exist or if
    stopping of the unit is prohibited (see RefuseManualStop= in
    systemd.unit(5)). It will not fail if any of the commands
    configured to stop the unit (ExecStop=, etc.) fail, because
    the manager will still forcibly terminate the unit.

    If a unit that gets stopped can still be triggered by other
    units, a warning containing the names of the triggering units
    is shown.  --no-warn can be used to suppress the warning.

reload PATTERN...
    Asks all units listed on the command line to reload their
    configuration. Note that this will reload the service-specific
    configuration, not the unit configuration file of systemd. If
    you want systemd to reload the configuration file of a unit,
    use the daemon-reload command. In other words: for the example
    case of Apache, this will reload Apache's httpd.conf in the
    web server, not the apache.service systemd unit file.

    This command should not be confused with the daemon-reload
    command.

restart PATTERN...
    Stop and then start one or more units specified on the command
    line. If the units are not running yet, they will be started.

    Note that restarting a unit with this command does not
    necessarily flush out all of the unit's resources before it is
    started again. For example, the per-service file descriptor
    storage facility (see FileDescriptorStoreMax= in
    systemd.service(5)) will remain intact as long as the unit has
    a job pending, and is only cleared when the unit is fully
    stopped and no jobs are pending anymore. If it is intended
    that the file descriptor store is flushed out, too, during a
    restart operation an explicit systemctl stop command followed
    by systemctl start should be issued.

try-restart PATTERN...
    Stop and then start one or more units specified on the command
    line if the units are running. This does nothing if units are
    not running.

enqueue-marked
    Enqueue start/stop/restart/reload jobs for all units that have
    the respective "needs-*" markers set. When a unit marked for
    reload does not support reload, restart will be queued. Those
    properties can be set using set-property Markers=....

    Unless --no-block is used, systemctl will wait for the queued
    jobs to finish.

    Added in version 260.

reload-or-restart PATTERN...
    Reload one or more units if they support it. If not, stop and
    then start them instead. If the units are not running yet,
    they will be started.

    When used in combination with --marked, it is a deprecated
    alias of enqueue-marked.

try-reload-or-restart PATTERN...
    Reload one or more units if they support it. If not, stop and
    then start them instead. This does nothing if the units are
    not running.

    Added in version 229.

isolate UNIT
    Start the unit specified on the command line and its
    dependencies and stop all others, unless they have
    IgnoreOnIsolate=yes (see systemd.unit(5)). If a unit name with
    no extension is given, an extension of ".target" will be
    assumed.

    This command is dangerous, since it will immediately stop
    processes that are not enabled in the new target, possibly
    including the graphical environment or terminal you are
    currently using.

    Note that this operation is allowed only on units where
    AllowIsolate= is enabled. See systemd.unit(5) for details.

kill PATTERN...
    Send a UNIX process signal to one or more processes of the
    unit. Use --kill-whom= to select which process to send the
    signal to. Use --signal= to select the signal to send. Combine
    with --kill-value= to enqueue a POSIX Realtime Signal with an
    associated value.

clean PATTERN...
    Remove the configuration, state, cache, logs, runtime or file
    descriptor store data of the specified units. Use --what= to
    select which kind of resource to remove. For service units
    this may be used to remove the directories configured with
    ConfigurationDirectory=, StateDirectory=, CacheDirectory=,
    LogsDirectory= and RuntimeDirectory=, see systemd.exec(5) for
    details. It may also be used to clear the file descriptor
    store as enabled via FileDescriptorStoreMax=, see
    systemd.service(5) for details. For timer units this may be
    used to clear out the persistent timestamp data if Persistent=
    is used and --what=state is selected, see systemd.timer(5).
    This command only applies to units that use either of these
    settings. If --what= is not specified, the cache and runtime
    data as well as the file descriptor store are removed (as
    these three types of resources are generally redundant and
    reproducible on the next invocation of the unit). Multiple
    values can be separated by commas. Note that the specified
    units must be stopped to invoke this operation.

    Table 2.  Possible values for --what=
    ┌─────────────────┬──────────────────────────────┐
    │ Value           │ Unit Setting                 │
    ├─────────────────┼──────────────────────────────┤
    │ "runtime"       │ RuntimeDirectory=            │
    ├─────────────────┼──────────────────────────────┤
    │ "state"         │ StateDirectory=              │
    ├─────────────────┼──────────────────────────────┤
    │ "cache"         │ CacheDirectory=              │
    ├─────────────────┼──────────────────────────────┤
    │ "logs"          │ LogsDirectory=               │
    ├─────────────────┼──────────────────────────────┤
    │ "configuration" │ ConfigurationDirectory=      │
    ├─────────────────┼──────────────────────────────┤
    │ "fdstore"       │ FileDescriptorStorePreserve= │
    ├─────────────────┼──────────────────────────────┤
    │ "all"           │ All of the above             │
    ├─────────────────┼──────────────────────────────┤
    │ "help"          │ Show the supported values    │
    │                 │ and exit                     │
    └─────────────────┴──────────────────────────────┘

    Added in version 243.

freeze PATTERN...
    Freeze one or more units specified on the command line using
    cgroup freezer

    Freezing the unit will cause all processes contained within
    the cgroup corresponding to the unit to be suspended. Being
    suspended means that unit's processes will not be scheduled to
    run on CPU until thawed. Note that this command is supported
    only on systems that use unified cgroup hierarchy. Unit is
    automatically thawed just before we execute a job against the
    unit, e.g. before the unit is stopped.

    Added in version 246.

thaw PATTERN...
    Thaw (unfreeze) one or more units specified on the command
    line.

    This is the inverse operation to the freeze command and
    resumes the execution of processes in the unit's cgroup.

    Added in version 246.

set-property UNIT PROPERTY=VALUE...
    Set the specified unit properties at runtime where this is
    supported. This allows changing configuration parameter
    properties such as resource control settings at runtime. Not
    all properties may be changed at runtime, but many resource
    control settings (primarily those in
    systemd.resource-control(5)) may. The changes are applied
    immediately, and stored on disk for future boots, unless
    --runtime is passed, in which case the settings only apply
    until the next reboot. The syntax of the property assignment
    follows closely the syntax of assignments in unit files.

    Example: systemctl set-property foobar.service CPUWeight=200

    If the specified unit appears to be inactive, the changes will
    be only stored on disk as described previously hence they will
    be effective when the unit will be started.

    Note that this command allows changing multiple properties at
    the same time, which is preferable over setting them
    individually.

    Example: systemctl set-property foobar.service CPUWeight=200
    MemoryMax=2G IPAccounting=yes

    Like with unit file configuration settings, assigning an empty
    setting usually resets a property to its defaults.

    Example: systemctl set-property avahi-daemon.service
    IPAddressDeny=

    Added in version 206.

bind UNIT PATH [PATH]
    Bind-mounts a file or directory from the host into the
    specified unit's mount namespace. The first path argument is
    the source file or directory on the host, the second path
    argument is the destination file or directory in the unit's
    mount namespace. When the latter is omitted, the destination
    path in the unit's mount namespace is the same as the source
    path on the host. When combined with the --read-only switch, a
    read-only bind mount is created. When combined with the
    --mkdir switch, the destination path is first created before
    the mount is applied.

    Note that this option is currently only supported for units
    that run within a mount namespace (e.g.: with RootImage=,
    PrivateMounts=, etc.). This command supports bind-mounting
    directories, regular files, device nodes, AF_UNIX socket
    nodes, as well as FIFOs. The bind mount is ephemeral, and it
    is undone as soon as the current unit process exists. Note
    that the namespace mentioned here, where the bind mount will
    be added to, is the one where the main service process runs.
    Other processes (those exececuted by ExecReload=,
    ExecStartPre=, etc.) run in distinct namespaces.

    If supported by the kernel, any prior mount on the selected
    target will be replaced by the new mount. If not supported,
    any prior mount will be over-mounted, but remain pinned and
    inaccessible.

    Added in version 248.

mount-image UNIT IMAGE [PATH [PARTITION_NAME:MOUNT_OPTIONS]]
    Mounts an image from the host into the specified unit's mount
    namespace. The first path argument is the source image on the
    host, the second path argument is the destination directory in
    the unit's mount namespace (i.e. inside
    RootImage=/RootDirectory=). The following argument, if any, is
    interpreted as a colon-separated tuple of partition name and
    comma-separated list of mount options for that partition. The
    format is the same as the service MountImages= setting. When
    combined with the --read-only switch, a ready-only mount is
    created. When combined with the --mkdir switch, the
    destination path is first created before the mount is applied.

    Note that this option is currently only supported for units
    that run within a mount namespace (i.e. with RootImage=,
    PrivateMounts=, etc.). Note that the namespace mentioned here
    where the image mount will be added to, is the one where the
    main service process runs. Note that the namespace mentioned
    here, where the bind mount will be added to, is the one where
    the main service process runs. Other processes (those
    exececuted by ExecReload=, ExecStartPre=, etc.) run in
    distinct namespaces.

    If supported by the kernel, any prior mount on the selected
    target will be replaced by the new mount. If not supported,
    any prior mount will be over-mounted, but remain pinned and
    inaccessible.

    Example:

        systemctl mount-image foo.service /tmp/img.raw /var/lib/image root:ro,nosuid

        systemctl mount-image --mkdir bar.service /tmp/img.raw /var/lib/baz/img

    Added in version 248.

service-log-level SERVICE [LEVEL]
    If the LEVEL argument is not given, print the current log
    level as reported by service SERVICE.

    If the optional argument LEVEL is provided, then change the
    current log level of the service to LEVEL. The log level
    should be a typical syslog log level, i.e. a value in the
    range 0...7 or one of the strings emerg, alert, crit, err,
    warning, notice, info, debug; see syslog(3) for details.

    The service must have the appropriate BusName=destination
    property and also implement the generic
    org.freedesktop.LogControl1(5) interface. (systemctl will use
    the generic D-Bus protocol to access the
    org.freedesktop.LogControl1.LogLevel interface for the D-Bus
    name destination.)

    Added in version 247.

service-log-target SERVICE [TARGET]
    If the TARGET argument is not given, print the current log
    target as reported by service SERVICE.

    If the optional argument TARGET is provided, then change the
    current log target of the service to TARGET. The log target
    should be one of the strings console (for log output to the
    service's standard error stream), kmsg (for log output to the
    kernel log buffer), journal (for log output to
    systemd-journald.service(8) using the native journal
    protocol), syslog (for log output to the classic syslog socket
    /dev/log), null (for no log output whatsoever) or auto (for an
    automatically determined choice, typically equivalent to
    console if the service is invoked interactively, and journal
    or syslog otherwise).

    For most services, only a small subset of log targets make
    sense. In particular, most "normal" services should only
    implement console, journal, and null. Anything else is only
    appropriate for low-level services that are active in very
    early boot before proper logging is established.

    The service must have the appropriate BusName=destination
    property and also implement the generic
    org.freedesktop.LogControl1(5) interface. (systemctl will use
    the generic D-Bus protocol to access the
    org.freedesktop.LogControl1.LogLevel interface for the D-Bus
    name destination.)

    Added in version 247.

reset-failed [PATTERN...]
    Reset the "failed" state of the specified units, or if no unit
    name is passed, reset the state of all units. When a unit
    fails in some way (i.e. process exiting with non-zero error
    code, terminating abnormally or timing out), it will
    automatically enter the "failed" state and its exit code and
    status is recorded for introspection by the administrator
    until the service is stopped/re-started or reset with this
    command.

    In addition to resetting the "failed" state of a unit it also
    resets various other per-unit properties: the start rate limit
    counter of all unit types is reset to zero, as is the restart
    counter of service units. Thus, if a unit's start limit (as
    configured with StartLimitIntervalSec=/StartLimitBurst=) is
    hit and the unit refuses to be started again, use this command
    to make it startable again.

whoami [PID...]
    Returns the units the processes referenced by the given PIDs
    belong to (one per line). If no PID is specified returns the
    unit the systemctl command is invoked in.

    Added in version 254.

### Unit File Commands

list-unit-files [PATTERN...]
    List unit files installed on the system, in combination with
    their enablement state (as reported by is-enabled). If one or
    more PATTERNs are specified, only unit files whose name
    matches one of them are shown (patterns matching unit file
    system paths are not supported).

    Unlike list-units this command will list template units in
    addition to explicitly instantiated units.

    Added in version 233.

enable UNIT..., enable PATH...
    Enable one or more units or unit instances. This will create a
    set of symlinks, as encoded in the [Install] sections of the
    indicated unit files. After the symlinks have been created,
    the system manager configuration is reloaded (in a way
    equivalent to daemon-reload), in order to ensure the changes
    are taken into account immediately. Note that this does not
    have the effect of also starting any of the units being
    enabled. If this is desired, combine this command with the
    --now switch, or invoke start with appropriate arguments
    later. Note that in case of unit instance enablement (i.e.
    enablement of units of the form foo@bar.service), symlinks
    named the same as instances are created in the unit
    configuration directory, however they point to the single
    template unit file they are instantiated from.

    This command expects either valid unit names (in which case
    various unit file directories are automatically searched for
    unit files with appropriate names), or absolute paths to unit
    files (in which case these files are read directly). If a
    specified unit file is located outside of the usual unit file
    directories, an additional symlink is created, linking it into
    the unit configuration path, thus ensuring it is found when
    requested by commands such as start. The file system where the
    linked unit files are located must be accessible when systemd
    is started (e.g. anything underneath /home/ or /var/ is not
    allowed, unless those directories are located on the root file
    system).

    This command will print the file system operations executed.
    This output may be suppressed by passing --quiet.

    Note that this operation creates only the symlinks suggested
    in the [Install] section of the unit files. While this command
    is the recommended way to manipulate the unit configuration
    directory, the administrator is free to make additional
    changes manually by placing or removing symlinks below this
    directory. This is particularly useful to create
    configurations that deviate from the suggested default
    installation. In this case, the administrator must make sure
    to invoke daemon-reload manually as necessary, in order to
    ensure the changes are taken into account.

    When using this operation on units without install
    information, a warning about it is shown.  --no-warn can be
    used to suppress the warning.

    Enabling units should not be confused with starting
    (activating) units, as done by the start command. Enabling and
    starting units is orthogonal: units may be enabled without
    being started and started without being enabled. Enabling
    simply hooks the unit into various suggested places (for
    example, so that the unit is automatically started on boot or
    when a particular kind of hardware is plugged in). Starting
    actually spawns the daemon process (in case of service units),
    or binds the socket (in case of socket units), and so on.

    Depending on whether --system, --user, --runtime, or --global
    is specified, this enables the unit for the system, for the
    calling user only, for only this boot of the system, or for
    all future logins of all users. Note that in the last case, no
    systemd daemon configuration is reloaded.

    Using enable on masked units is not supported and results in
    an error.

disable UNIT...
    Disables one or more units. This removes all symlinks to the
    unit files backing the specified units from the unit
    configuration directory, and hence undoes any changes made by
    enable or link. Note that this removes all symlinks to
    matching unit files, including manually created symlinks, and
    not just those actually created by enable or link. Note that
    while disable undoes the effect of enable, the two commands
    are otherwise not symmetric, as disable may remove more
    symlinks than a prior enable invocation of the same unit
    created.

    This command expects valid unit names only, it does not accept
    paths to unit files.

    In addition to the units specified as arguments, all units are
    disabled that are listed in the Also= setting contained in the
    [Install] section of any of the unit files being operated on.

    This command implicitly reloads the system manager
    configuration after completing the operation. Note that this
    command does not implicitly stop the units that are being
    disabled. If this is desired, either combine this command with
    the --now switch, or invoke the stop command with appropriate
    arguments later.

    This command will print information about the file system
    operations (symlink removals) executed. This output may be
    suppressed by passing --quiet.
