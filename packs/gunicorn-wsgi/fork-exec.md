---
title: "Fork–exec"
source: https://en.wikipedia.org/wiki/Fork%E2%80%93exec
domain: gunicorn-wsgi
license: CC-BY-SA-4.0
tags: python gunicorn, gunicorn wsgi server, wsgi worker python
fetched: 2026-07-02
---

# Fork–exec

**Fork–exec** is a commonly used technique in Unix whereby an executing process spawns a new program.

## Description

`fork()` is the name of the system call that the parent process uses to "divide" itself ("fork") into two identical processes. After calling `fork()`, the created child process is an exact copy of the parent except for the return value of the fork() call. This includes open files, register state, and all memory allocations, which includes the program's executable code. In some cases the two continue to run the same binary, but often one (usually the child) switches to running another binary executable using the `exec()` system call.

When a process forks, a complete copy of the executing program is made into the new process. This new process is a child of the parent process, and has a new process identifier (PID). The `fork()` function returns the child's PID to the parent process. The `fork()` function returns 0 to the child process. This enables the two otherwise identical processes to distinguish themselves from each other.

The parent process can either continue execution or wait for the child process to complete. The child, after discovering that it is the child, will most often then replace itself completely with another program, so that the code and address space of the original program are lost. This replacement is, however, a choice of the architecture one builds the given program on, and is therefore not an obligatory step in the child process' life.

If the parent chooses to wait for the child to die, then the parent will receive the exit code of the program that the child executed. To prevent the child becoming a zombie the parent should call wait on its children, either periodically or upon receiving the SIGCHLD signal, which indicates a child process has terminated.

One can also asynchronously wait on their children to finish, by using a signal handler for SIGCHLD, if they need to ensure everything is cleaned up. Here's an example of a signal handler that catches any incoming SIGCHLD signals and handles multiple concurrent signals received.

```mw
void cleanup(int signal) {
    while (waitpid((pid_t)(-1), 0, WNOHANG) > 0) {
        // ...
    }
}
```

When the child process calls `exec()`, all data in the original program is lost, and it is replaced with a running copy of the new program. This is known as overlaying. Although all data are replaced, the file descriptors that were open in the parent are closed only if the program has explicitly marked them *close-on-exec*. This allows for the common practice of the parent creating a pipe prior to calling `fork()` and using it to communicate with the executed program.

Microsoft Windows does not support the fork–exec model, as it does not have a system call analogous to `fork()`. The `spawn()` family of functions declared in process.h can replace it in cases where the call to `fork()` is followed directly by `exec()`.

> When a fork syscall is made on WSL, lxss.sys does some of the initial work to prepare for copying the process. It then calls internal NT APIs to create the process with the correct semantics and create a thread in the process with an identical register context. Finally, it does some additional work to complete copying the process and resumes the new process so it can begin executing.

— Jack Hammons of Microsoft
