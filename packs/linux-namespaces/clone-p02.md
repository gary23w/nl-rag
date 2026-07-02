---
title: "clone(2) (part 2/2)"
source: https://man7.org/linux/man-pages/man2/clone.2.html
domain: linux-namespaces
license: CC-BY-SA-4.0
tags: linux namespaces, network namespaces, unshare, clone namespaces
fetched: 2026-07-02
part: 2/2
---

## EXAMPLES

The following program demonstrates the use of clone() to create a
child process that executes in a separate UTS namespace.  The
child changes the hostname in its UTS namespace.  Both parent and
child then display the system hostname, making it possible to see
that the hostname differs in the UTS namespaces of the parent and
child.  For an example of the use of this program, see setns(2).

Within the sample program, we allocate the memory that is to be
used for the child's stack using mmap(2) rather than malloc(3) for
the following reasons:

•  mmap(2) allocates a block of memory that starts on a page
   boundary and is a multiple of the page size.  This is useful if
   we want to establish a guard page (a page with protection
   PROT_NONE) at the end of the stack using mprotect(2).

•  We can specify the MAP_STACK flag to request a mapping that is
   suitable for a stack.  For the moment, this flag is a no-op on
   Linux, but it exists and has effect on some other systems, so
   we should include it for portability.

### Program source

#define _GNU_SOURCE
#include <err.h>
#include <sched.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/utsname.h>
#include <sys/wait.h>
#include <unistd.h>

static int              /* Start function for cloned child */
childFunc(void *arg)
{
    struct utsname uts;

    /* Change hostname in UTS namespace of child.  */

    if (sethostname(arg, strlen(arg)) == -1)
        err(EXIT_FAILURE, "sethostname");

    /* Retrieve and display hostname.  */

    if (uname(&uts) == -1)
        err(EXIT_FAILURE, "uname");
    printf("uts.nodename in child:  %s\n", uts.nodename);

    /* Keep the namespace open for a while, by sleeping.
       This allows some experimentation--for example, another
       process might join the namespace.  */

    sleep(200);

    return 0;           /* Child terminates now */
}

#define STACK_SIZE (1024 * 1024)    /* Stack size for cloned child */

int
main(int argc, char *argv[])
{
    char            *stack;         /* Start of stack buffer */
    char            *stackTop;      /* End of stack buffer */
    pid_t           pid;
    struct utsname  uts;

    if (argc < 2) {
        fprintf(stderr, "Usage: %s <child-hostname>\n", argv[0]);
        exit(EXIT_SUCCESS);
    }

    /* Allocate memory to be used for the stack of the child.  */

    stack = mmap(NULL, STACK_SIZE, PROT_READ | PROT_WRITE,
                 MAP_PRIVATE | MAP_ANONYMOUS | MAP_STACK, -1, 0);
    if (stack == MAP_FAILED)
        err(EXIT_FAILURE, "mmap");

    stackTop = stack + STACK_SIZE;  /* Assume stack grows downward */

    /* Create child that has its own UTS namespace;
       child commences execution in childFunc().  */

    pid = clone(childFunc, stackTop, CLONE_NEWUTS | SIGCHLD, argv[1]);
    if (pid == -1)
        err(EXIT_FAILURE, "clone");
    if (munmap(stack, STACK_SIZE))
        err(EXIT_FAILURE, "munmap");
    printf("clone() returned %jd\n", (intmax_t) pid);

    /* Parent falls through to here */

    sleep(1);           /* Give child time to change its hostname */

    /* Display hostname in parent's UTS namespace.  This will be
       different from hostname in child's UTS namespace.  */

    if (uname(&uts) == -1)
        err(EXIT_FAILURE, "uname");
    printf("uts.nodename in parent: %s\n", uts.nodename);

    if (waitpid(pid, NULL, 0) == -1)    /* Wait for child */
        err(EXIT_FAILURE, "waitpid");
    printf("child has terminated\n");

    exit(EXIT_SUCCESS);
}


## SEE ALSO

fork(2), futex(2), getpid(2), gettid(2), kcmp(2), mmap(2),
pidfd_open(2), set_thread_area(2), set_tid_address(2), setns(2),
tkill(2), unshare(2), wait(2), capabilities(7), namespaces(7),
pthreads(7)
