---
title: "Bash Reference Manual (part 10/15)"
source: https://www.gnu.org/software/bash/manual/bash.html
domain: shell-linux
license: GFDL-1.3 (bash manual) / GPL-2.0 (man-pages)
tags: bash, shell script, linux command, posix
fetched: 2026-07-02
part: 10/15
---

## 7 Job Control

This chapter discusses what job control is, how it works, and how Bash allows you to access its facilities.

### 7.1 Job Control Basics

Job control refers to the ability to selectively stop (suspend) the execution of processes and continue (resume) their execution at a later point. A user typically employs this facility via an interactive interface supplied jointly by the operating system kernel’s terminal driver and Bash.

The shell associates a *job* with each pipeline. It keeps a table of currently executing jobs, which the `jobs` command will display. Each job has a *job number*, which `jobs` displays between brackets. Job numbers start at 1. When Bash starts a job asynchronously, it prints a line that looks like:

```
[1] 25647
```

indicating that this job is job number 1 and that the process ID of the last process in the pipeline associated with this job is 25647. All of the processes in a single pipeline are members of the same job. Bash uses the *job* abstraction as the basis for job control.

To facilitate the implementation of the user interface to job control, each process has a *process group ID*, and the operating system maintains the notion of a current terminal process group ID. This terminal process group ID is associated with the *controlling terminal*.

Processes that have the same process group ID are said to be part of the same *process group*. Members of the foreground process group (processes whose process group ID is equal to the current terminal process group ID) receive keyboard-generated signals such as `SIGINT`. Processes in the foreground process group are said to be foreground processes. Background processes are those whose process group ID differs from the controlling terminal’s; such processes are immune to keyboard-generated signals. Only foreground processes are allowed to read from or, if the user so specifies with `stty tostop`, write to the controlling terminal. The system sends a `SIGTTIN` (`SIGTTOU`) signal to background processes which attempt to read from (write to when `tostop` is in effect) the terminal, which, unless caught, suspends the process.

If the operating system on which Bash is running supports job control, Bash contains facilities to use it. Typing the *suspend* character (typically ‘^Z’, Control-Z) while a process is running stops that process and returns control to Bash. Typing the *delayed suspend* character (typically ‘^Y’, Control-Y) causes the process to stop when it attempts to read input from the terminal, and returns control to Bash. The user then manipulates the state of this job, using the `bg` command to continue it in the background, the `fg` command to continue it in the foreground, or the `kill` command to kill it. The suspend character takes effect immediately, and has the additional side effect of discarding any pending output and typeahead. If you want to force a background process to stop, or stop a process that’s not associated with your terminal session, send it the `SIGSTOP` signal using `kill`.

There are a number of ways to refer to a job in the shell. The ‘%’ character introduces a *job specification* (jobspec).

Job number `n` may be referred to as ‘%n’. A job may also be referred to using a prefix of the name used to start it, or using a substring that appears in its command line. For example, ‘%ce’ refers to a job whose command name begins with ‘ce’. Using ‘%?ce’, on the other hand, refers to any job containing the string ‘ce’ in its command line. If the prefix or substring matches more than one job, Bash reports an error.

The symbols ‘%%’ and ‘%+’ refer to the shell’s notion of the *current job*. A single ‘%’ (with no accompanying job specification) also refers to the current job. ‘%-’ refers to the *previous job*. When a job starts in the background, a job stops while in the foreground, or a job is resumed in the background, it becomes the current job. The job that was the current job becomes the previous job. When the current job terminates, the previous job becomes the current job. If there is only a single job, ‘%+’ and ‘%-’ can both be used to refer to that job. In output pertaining to jobs (e.g., the output of the `jobs` command), the current job is always marked with a ‘+’, and the previous job with a ‘-’.

Simply naming a job can be used to bring it into the foreground: ‘%1’ is a synonym for ‘fg %1’, bringing job 1 from the background into the foreground. Similarly, ‘%1 &’ resumes job 1 in the background, equivalent to ‘bg %1’.

The shell learns immediately whenever a job changes state. Normally, Bash waits until it is about to print a prompt before notifying the user about changes in a job’s status so as to not interrupt any other output, though it will notify of changes in a job’s status after a foreground command in a list completes, before executing the next command in the list. If the -b option to the `set` builtin is enabled, Bash reports status changes immediately (see The Set Builtin). Bash executes any trap on `SIGCHLD` for each child process that terminates.

When a job terminates and Bash notifies the user about it, Bash removes the job from the jobs table. It will not appear in `jobs` output, but `wait` will report its exit status, as long as it’s supplied the process ID associated with the job as an argument. When the table is empty, job numbers start over at 1.

If a user attempts to exit Bash while jobs are stopped, (or running, if the `checkjobs` option is enabled – see The Shopt Builtin), the shell prints a warning message, and if the `checkjobs` option is enabled, lists the jobs and their statuses. The `jobs` command may then be used to inspect their status. If the user immediately attempts to exit again, without an intervening command, Bash does not print another warning, and terminates any stopped jobs.

When the shell is waiting for a job or process using the `wait` builtin, and job control is enabled, `wait` will return when the job changes state. The -f option causes `wait` to wait until the job or process terminates before returning.

### 7.2 Job Control Builtins

**`bg` ¶**

```
bg [jobspec ...]
```

Resume each suspended job *jobspec* in the background, as if it had been started with ‘&’. If *jobspec* is not supplied, the shell uses its notion of the current job. `bg` returns zero unless it is run when job control is not enabled, or, when run with job control enabled, any *jobspec* was not found or specifies a job that was started without job control.

**`fg` ¶**

```
fg [jobspec]
```

Resume the job *jobspec* in the foreground and make it the current job. If *jobspec* is not supplied, `fg` resumes the current job. The return status is that of the command placed into the foreground, or non-zero if run when job control is disabled or, when run with job control enabled, *jobspec* does not specify a valid job or *jobspec* specifies a job that was started without job control.

**`jobs` ¶**

```
jobs [-lnprs] [jobspec]
jobs -x command [arguments]
```

The first form lists the active jobs. The options have the following meanings:

**`-l`**

List process IDs in addition to the normal information.

**`-n`**

Display information only about jobs that have changed status since the user was last notified of their status.

**`-p`**

List only the process ID of the job’s process group leader.

**`-r`**

Display only running jobs.

**`-s`**

Display only stopped jobs.

If *jobspec* is supplied, `jobs` restricts output to information about that job. If *jobspec* is not supplied, `jobs` lists the status of all jobs. The return status is zero unless an invalid option is encountered or an invalid *jobspec* is supplied.

If the -x option is supplied, `jobs` replaces any *jobspec* found in *command* or *arguments* with the corresponding process group ID, and executes *command*, passing it *argument*s, returning its exit status.

**`kill` ¶**

```
kill [-s sigspec] [-n signum] [-sigspec] id [...]
kill -l|-L [exit_status]
```

Send a signal specified by *sigspec* or *signum* to the processes named by each *id*. Each *id* may be a job specification *jobspec* or process ID *pid*. *sigspec* is either a case-insensitive signal name such as `SIGINT` (with or without the `SIG` prefix) or a signal number; *signum* is a signal number. If *sigspec* and *signum* are not present, `kill` sends `SIGTERM`.

The -l option lists the signal names. If any arguments are supplied when -l is supplied, `kill` lists the names of the signals corresponding to the arguments, and the return status is zero. *exit_status* is a number specifying a signal number or the exit status of a process terminated by a signal; if it is supplied, `kill` prints the name of the signal that caused the process to terminate. `kill` assumes that process exit statuses are greater than 128; anything less than that is a signal number. The -L option is equivalent to -l.

The return status is zero if at least one signal was successfully sent, or non-zero if an error occurs or an invalid option is encountered.

**`wait` ¶**

```
wait [-fn] [-p varname] [id ...]
```

Wait until the child process specified by each *id* exits and return the exit status of the last *id*. Each *id* may be a process ID *pid* or a job specification *jobspec*; if a jobspec is supplied, `wait` waits for all processes in the job.

If no options or *id*s are supplied, `wait` waits for all running background jobs and the last-executed process substitution, if its process id is the same as *$!*, and the return status is zero.

If the -n option is supplied, `wait` waits for any one of the *id*s or, if no *id*s are supplied, any job or process substitution, to complete and returns its exit status. If none of the supplied *id*s is a child of the shell, or if no arguments are supplied and the shell has no unwaited-for children, the exit status is 127.

If the -p option is supplied, `wait` assigns the process or job identifier of the job for which the exit status is returned to the variable *varname* named by the option argument. The variable, which cannot be readonly, will be unset initially, before any assignment. This is useful only when used with the -n option.

Supplying the -f option, when job control is enabled, forces `wait` to wait for each *id* to terminate before returning its status, instead of returning when it changes status.

If none of the *id*s specify one of the shell’s an active child processes, the return status is 127. If `wait` is interrupted by a signal, any *varname* will remain unset, and the return status will be greater than 128, as described above (see Signals). Otherwise, the return status is the exit status of the last *id*.

**`disown` ¶**

```
disown [-ar] [-h] [id ...]
```

Without options, remove each *id* from the table of active jobs. Each *id* may be a job specification *jobspec* or a process ID *pid*; if *id* is a *pid*, `disown` uses the job containing *pid* as *jobspec*.

If the -h option is supplied, `disown` does not remove the jobs corresponding to each `id` from the jobs table, but rather marks them so the shell does not send `SIGHUP` to the job if the shell receives a `SIGHUP`.

If no *id* is supplied, the -a option means to remove or mark all jobs; the -r option without an *id* argument removes or marks running jobs. If no *id* is supplied, and neither the -a nor the -r option is supplied, `disown` removes or marks the current job.

The return value is 0 unless an *id* does not specify a valid job.

**`suspend` ¶**

```
suspend [-f]
```

Suspend the execution of this shell until it receives a `SIGCONT` signal. A login shell, or a shell without job control enabled, cannot be suspended; the -f option will override this and force the suspension. The return status is 0 unless the shell is a login shell or job control is not enabled and -f is not supplied.

When job control is not active, the `kill` and `wait` builtins do not accept *jobspec* arguments. They must be supplied process IDs.

### 7.3 Job Control Variables

**`auto_resume` ¶**

This variable controls how the shell interacts with the user and job control. If this variable exists then simple commands consisting of only a single word, without redirections, are treated as candidates for resumption of an existing job. There is no ambiguity allowed; if there is more than one job beginning with or containing the word, then this selects the most recently accessed job. The name of a stopped job, in this context, is the command line used to start it, as displayed by `jobs`. If this variable is set to the value ‘exact’, the word must match the name of a stopped job exactly; if set to ‘substring’, the word needs to match a substring of the name of a stopped job. The ‘substring’ value provides functionality analogous to the ‘%?string’ job ID (see Job Control Basics). If set to any other value (e.g., ‘prefix’), the word must be a prefix of a stopped job’s name; this provides functionality analogous to the ‘%string’ job ID.
