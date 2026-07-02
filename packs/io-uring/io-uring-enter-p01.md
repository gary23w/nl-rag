---
title: "io_uring_enter(2) (part 1/2)"
source: https://man7.org/linux/man-pages/man2/io_uring_enter.2.html
domain: io-uring
license: CC-BY-SA-4.0
tags: io_uring, asynchronous i/o, linux async io
fetched: 2026-07-02
part: 1/2
---

# io_uring_enter(2) — Linux manual page

io_uring_enter(2)       Linux Programmer's Manual       io_uring_enter(2)


## NAME

io_uring_enter - initiate and/or complete asynchronous I/O


## SYNOPSIS

#include <liburing.h>

int io_uring_enter(unsigned int fd, unsigned int to_submit,
                   unsigned int min_complete, unsigned int flags,
                   sigset_t *sig);

int io_uring_enter2(unsigned int fd, unsigned int to_submit,
                    unsigned int min_complete, unsigned int flags,
                    void *arg, size_t sz);

## DESCRIPTION

io_uring_enter(2) is used to initiate and complete I/O using the
shared submission and completion queues setup by a call to
io_uring_setup(2).  A single call can both submit new I/O and wait
for completions of I/O initiated by this call or previous calls to
io_uring_enter(2).

fd is the file descriptor returned by io_uring_setup(2).
to_submit specifies the number of I/Os to submit from the
submission queue.  flags is a bitmask of the following values:

IORING_ENTER_GETEVENTS
       If this flag is set, then the system call will wait for the
       specified number of events in min_complete before
       returning. This flag can be set along with to_submit to
       both submit and complete events in a single system call.
       If this flag is set either the flag
       IORING_SETUP_DEFER_TASKRUN must not be set or the thread
       issuing the syscall must be the thread that created the
       io_uring associated with fd, or be the thread that enabled
       the ring originally created with IORING_SETUP_R_DISABLED
       via io_uring_register(2) or io_uring_enable_rings(3).

IORING_ENTER_SQ_WAKEUP
       If the ring has been created with IORING_SETUP_SQPOLL, then
       this flag asks the kernel to wakeup the SQ kernel thread to
       submit IO.

IORING_ENTER_SQ_WAIT
       If the ring has been created with IORING_SETUP_SQPOLL, then
       the application has no real insight into when the SQ kernel
       thread has consumed entries from the SQ ring. This can lead
       to a situation where the application can no longer get a
       free SQE entry to submit, without knowing when one will
       become available as the SQ kernel thread consumes them. If
       the system call is used with this flag set, then it will
       wait until at least one entry is free in the SQ ring.

IORING_ENTER_EXT_ARG
       By default, arg is a sigset_t pointer. If
       IORING_ENTER_EXT_ARG is set (supported since kernel 5.11),
       then arg is instead a pointer to a struct
       io_uring_getevents_arg and argsz must be set to the size of
       this structure. The definition is as follows:

       struct io_uring_getevents_arg {
               __u64   sigmask;
               __u32   sigmask_sz;
               __u32   pad;
               __u64   ts;
       };

       which allows passing in both a signal mask as well as
       pointer to a struct __kernel_timespec timeout value. If ts
       is set to a valid pointer, then this time value indicates
       the timeout for waiting on events. If an application is
       waiting on events and wishes to stop waiting after a
       specified amount of time, then this can be accomplished
       directly in version 5.11 and newer by using this feature.

IORING_ENTER_REGISTERED_RING
       If the ring file descriptor has been registered through use
       of IORING_REGISTER_RING_FDS, then setting this flag will
       tell the kernel that the ring_fd passed in is the
       registered ring offset rather than a normal file
       descriptor.

IORING_ENTER_ABS_TIMER

       When this flag is set, the timeout argument passed in
       struct io_uring_getevents_arg will be interpreted as an
       absolute time of the registered clock (see
       IORING_REGISTER_CLOCK) until which the waiting should end.

       Available since 6.12

IORING_ENTER_EXT_ARG_REG

       When this flag is set, arg is not a pointer to a
       structio_uring_getevents_arg, but merely an offset into an
       area of wait regions previously registered with
       io_uring_register(2) using the IORING_REGISTER_MEM_REGION
       operation.

       Available since 6.13

IORING_ENTER_NO_IOWAIT
       When this flag is set, the system call will not mark the
       waiting task as being in iowait if it is sleeping waiting
       on events and there are pending requests.  This is useful
       if iowait isn't expected when waiting for events. It can
       also prevent extra power usage by allowing the CPU to enter
       lower sleep states.  This flag is only available if the
       kernel supports the IORING_FEAT_NO_IOWAIT feature.

       Available since 6.15.

If the io_uring instance was configured for polling, by specifying
IORING_SETUP_IOPOLL in the call to io_uring_setup(2), then
min_complete has a slightly different meaning.  Passing a value of
0 instructs the kernel to return any events which are already
complete, without blocking.  If min_complete is a non-zero value,
the kernel will still return immediately if any completion events
are available.  If no event completions are available, then the
call will poll either until one or more completions become
available, or until the process has exceeded its scheduler time
slice.

Note that, for interrupt driven I/O (where IORING_SETUP_IOPOLL was
not specified in the call to io_uring_setup(2)), an application
may check the completion queue for event completions without
entering the kernel at all.

When the system call returns that a certain amount of SQEs have
been consumed and submitted, it's safe to reuse SQE entries in the
ring. This is true even if the actual IO submission had to be
punted to async context, which means that the SQE may in fact not
have been submitted yet. If the kernel requires later use of a
particular SQE entry, it will have made a private copy of it.

sig is a pointer to a signal mask (see sigprocmask(2)); if sig is
not NULL, io_uring_enter(2) first replaces the current signal mask
by the one pointed to by sig, then waits for events to become
available in the completion queue, and then restores the original
signal mask.  The following io_uring_enter(2) call:

    ret = io_uring_enter(fd, 0, 1, IORING_ENTER_GETEVENTS, &sig);

is equivalent to atomically executing the following calls:

    pthread_sigmask(SIG_SETMASK, &sig, &orig);
    ret = io_uring_enter(fd, 0, 1, IORING_ENTER_GETEVENTS, NULL);
    pthread_sigmask(SIG_SETMASK, &orig, NULL);

See the description of pselect(2) for an explanation of why the
sig parameter is necessary.

Submission queue entries are represented using the following data
structure:

    /*
     * IO submission data structure (Submission Queue Entry)
     */
    struct io_uring_sqe {
         __u8 opcode;        /* type of operation for this sqe */
         __u8 flags;         /* IOSQE_ flags */
         __u16     ioprio;        /* ioprio for the request */
         __s32     fd;       /* file descriptor to do IO on */
         union {
              __u64     off; /* offset into file */
              __u64     addr2;
              struct {
                   __u32     cmd_op;
                   __u32     __pad1;
              };
         };
         union {
              __u64     addr;     /* pointer to buffer or iovecs */
              __u64     splice_off_in;
              struct {
                   __u32     level;
                   __u32     optname;
              };
         };
         __u32     len;      /* buffer size or number of iovecs */
         union {
              __kernel_rwf_t rw_flags;
              __u32          fsync_flags;
              __u16          poll_events;   /* compatibility */
              __u32          poll32_events; /* word-reversed for BE */
              __u32          sync_range_flags;
              __u32          msg_flags;
              __u32          timeout_flags;
              __u32          accept_flags;
              __u32          cancel_flags;
              __u32          open_flags;
              __u32          statx_flags;
              __u32          fadvise_advice;
              __u32          splice_flags;
              __u32          rename_flags;
              __u32          unlink_flags;
              __u32          hardlink_flags;
              __u32          xattr_flags;
              __u32          msg_ring_flags;
              __u32          uring_cmd_flags;
              __u32          waitid_flags;
              __u32          futex_flags;
              __u32          install_fd_flags;
              __u32          nop_flags;
         };
         __u64     user_data;     /* data to be passed back at completion time */
         /* pack this to avoid bogus arm OABI complaints */
         union {
              /* index into fixed buffers, if used */
              __u16     buf_index;
              /* for grouped buffer selection */
              __u16     buf_group;
         } __attribute__((packed));
         /* personality to use, if used */
         __u16     personality;
         union {
              __s32     splice_fd_in;
              __u32     file_index;
              __u32     optlen;
              struct {
                   __u16     addr_len;
                   __u16     __pad3[1];
              };
         };
         union {
              struct {
                   __u64     addr3;
                   __u64     __pad2[1];
              };
              __u64     optval;
              /*
               * If the ring is initialized with IORING_SETUP_SQE128, then
               * this field is used for 80 bytes of arbitrary command data
               */
              __u8 cmd[0];
         };
    };

The opcode describes the operation to be performed.  It can be one
of:

IORING_OP_NOP
       Do not perform any I/O.  This is useful for testing the
       performance of the io_uring implementation itself.

IORING_OP_READV

IORING_OP_WRITEV
       Vectored read and write operations, similar to preadv2(2)
       and pwritev2(2).  If the file is not seekable, off must be
       set to zero or -1.

IORING_OP_READ_FIXED

IORING_OP_WRITE_FIXED
       Read from or write to pre-mapped buffers.  See
       io_uring_register(2) for details on how to setup a context
       for fixed reads and writes.

IORING_OP_FSYNC
       File sync.  See also fsync(2).  Optionally off and len can
       be used to specify a range within the file to be synced
       rather than syncing the entire file, which is the default
       behavior.  Note that, while I/O is initiated in the order
       in which it appears in the submission queue, completions
       are unordered.  For example, an application which places a
       write I/O followed by an fsync in the submission queue
       cannot expect the fsync to apply to the write.  The two
       operations execute in parallel, so the fsync may complete
       before the write is issued to the storage.  The same is
       also true for previously issued writes that have not
       completed prior to the fsync.  To enforce ordering one may
       utilize linked SQEs, IOSQE_IO_DRAIN or wait for the arrival
       of CQEs of requests which have to be ordered before a given
       request before submitting its SQE.

IORING_OP_POLL_ADD
       Poll the fd specified in the submission queue entry for the
       events specified in the poll_events field.  Unlike poll or
       epoll without EPOLLONESHOT, by default this interface
       always works in one shot mode.  That is, once the poll
       operation is completed, it will have to be resubmitted.

       If IORING_POLL_ADD_MULTI is set in the SQE len field, then
       the poll will work in multi shot mode instead. That means
       it'll repatedly trigger when the requested event becomes
       true, and hence multiple CQEs can be generated from this
       single SQE. The CQE flags field will have IORING_CQE_F_MORE
       set on completion if the application should expect further
       CQE entries from the original request. If this flag isn't
       set on completion, then the poll request has been
       terminated and no further events will be generated. This
       mode is available since 5.13.

       This command works like an async poll(2) and the completion
       event result is the returned mask of events.

       Without IORING_POLL_ADD_MULTI and the initial poll
       operation with IORING_POLL_ADD_MULTI the operation is level
       triggered, i.e. if there is data ready or events pending
       etc. at the time of submission a corresponding CQE will be
       posted.  Potential further completions beyond the first
       caused by a IORING_POLL_ADD_MULTI are edge triggered.

IORING_OP_POLL_REMOVE
       Remove or update an existing poll request.  If found, the
       res field of the struct io_uring_cqe will contain 0.  If
       not found, res will contain -ENOENT, or -EALREADY if the
       poll request was in the process of completing already.

       If IORING_POLL_UPDATE_EVENTS is set in the SQE len field,
       then the request will update an existing poll request with
       the mask of events passed in with this request. The lookup
       is based on the user_data field of the original SQE
       submitted, and this values is passed in the addr field of
       the SQE.  If IORING_POLL_UPDATE_USER_DATA is set in the SQE
       len field, then the request will update the user_data of an
       existing poll request based on the value passed in the off
       field. Updating an existing poll is available since 5.13.

IORING_OP_EPOLL_CTL
       Add, remove or modify entries in the interest list of
       epoll(7).  See epoll_ctl(2) for details of the system call.
       fd holds the file descriptor that represents the epoll
       instance, off holds the file descriptor to add, remove or
       modify, len holds the operation ( EPOLL_CTL_ADD,
       EPOLL_CTL_DEL, EPOLL_CTL_MOD) to perform and, addr holds a
       pointer to the epoll_event structure. Available since 5.6.

IORING_OP_SYNC_FILE_RANGE
       Issue the equivalent of a sync_file_range (2) on the file
       descriptor. The fd field is the file descriptor to sync,
       the off field holds the offset in bytes, the len field
       holds the length in bytes, and the sync_range_flags field
       holds the flags for the command. See also
       sync_file_range(2) for the general description of the
       related system call. Available since 5.2.

IORING_OP_SENDMSG
       Issue the equivalent of a sendmsg(2) system call.  fd must
       be set to the socket file descriptor, addr must contain a
       pointer to the msghdr structure, and msg_flags holds the
       flags associated with the system call. See also sendmsg(2)
       for the general description of the related system call.
       Available since 5.3.

       This command also supports the following modifiers in
       ioprio:

            IORING_RECVSEND_POLL_FIRST If set, io_uring will
            assume the socket is currently full and attempting to
            send data will be unsuccessful. For this case,
            io_uring will arm internal poll and trigger a send of
            the data when there is enough space available.  This
            initial send attempt can be wasteful for the case
            where the socket is expected to be full, setting this
            flag will bypass the initial send attempt and go
            straight to arming poll. If poll does indicate that
            data can be sent, the operation will proceed.

IORING_OP_RECVMSG
       Works just like IORING_OP_SENDMSG, except for recvmsg(2)
       instead. See the description of IORING_OP_SENDMSG.
       Available since 5.3.

       This command also supports the following modifiers in
       ioprio:

            IORING_RECVSEND_POLL_FIRST If set, io_uring will
            assume the socket is currently empty and attempting to
            receive data will be unsuccessful. For this case,
            io_uring will arm internal poll and trigger a receive
            of the data when the socket has data to be read.  This
            initial receive attempt can be wasteful for the case
            where the socket is expected to be empty, setting this
            flag will bypass the initial receive attempt and go
            straight to arming poll. If poll does indicate that
            data is ready to be received, the operation will
            proceed.

IORING_OP_SEND
       Issue the equivalent of a send(2) system call.  fd must be
       set to the socket file descriptor, addr must contain a
       pointer to the buffer, len denotes the length of the buffer
       to send, and msg_flags holds the flags associated with the
       system call. See also send(2) for the general description
       of the related system call. Available since 5.6.

       This command also supports the following modifiers in
       ioprio:

            IORING_RECVSEND_POLL_FIRST If set, io_uring will
            assume the socket is currently full and attempting to
            send data will be unsuccessful. For this case,
            io_uring will arm internal poll and trigger a send of
            the data when there is enough space available.  This
            initial send attempt can be wasteful for the case
            where the socket is expected to be full, setting this
            flag will bypass the initial send attempt and go
            straight to arming poll. If poll does indicate that
            data can be sent, the operation will proceed.

IORING_OP_RECV
       Works just like IORING_OP_SEND, except for recv(2) instead.
       See the description of IORING_OP_SEND. Available since 5.6.

       This command also supports the following modifiers in
       ioprio:

            IORING_RECVSEND_POLL_FIRST If set, io_uring will
            assume the socket is currently empty and attempting to
            receive data will be unsuccessful. For this case,
            io_uring will arm internal poll and trigger a receive
            of the data when the socket has data to be read.  This
            initial receive attempt can be wasteful for the case
            where the socket is expected to be empty, setting this
            flag will bypass the initial receive attempt and go
            straight to arming poll. If poll does indicate that
            data is ready to be received, the operation will
            proceed.

IORING_OP_TIMEOUT
       This command will register a timeout operation. The addr
       field must contain a pointer to a struct __kernel_timespec
       structure, len must contain 1 to signify one
       __kernel_timespec structure, timeout_flags may contain
       IORING_TIMEOUT_ABS for an absolute timeout value, or 0 for
       a relative timeout.  off may contain a completion event
       count. A timeout will trigger a wakeup event on the
       completion ring for anyone waiting for events. A timeout
       condition is met when either the specified timeout expires,
       or the specified number of events have completed. Either
       condition will trigger the event. If set to 0, completed
       events are not counted, which effectively acts like a
       timer. io_uring timeouts use the CLOCK_MONOTONIC as the
       default clock source. The request will complete with -ETIME
       if the timeout got completed through expiration of the
       timer, or 0 if the timeout got completed through requests
       completing on their own. If the timeout was canceled before
       it expired, the request will complete with -ECANCELED.
       Available since 5.4.

       Since 5.15, this command also supports the following
       modifiers in timeout_flags:

            IORING_TIMEOUT_BOOTTIME If set, then the clocksource
            used is CLOCK_BOOTTIME instead of CLOCK_MONOTONIC.
            This clocksource differs in that it includes time
            elapsed if the system was suspend while having a
            timeout request in-flight.

            IORING_TIMEOUT_REALTIME If set, then the clocksource
            used is CLOCK_REALTIME instead of CLOCK_MONOTONIC.

       Since 5.16, IORING_TIMEOUT_ETIME_SUCCESS can be set in
       timeout_flags, which will result in the expiration of the
       timer and subsequent completion with -ETIME not being
       interpreted as an error. This is mostly relevant for linked
       SQEs, as subsequent requests in the chain would not get
       canceled by the timeout, if this flag is set. See
       IOSQE_IO_LINK for more details on linked SQEs.

       Since 6.4, IORING_TIMEOUT_MULTISHOT can be set in
       timeout_flags, which will result in the timer producing
       multiple consecutive completions like other multi shot
       operations e.g.  IORING_OP_READ_MULTISHOT or
       IORING_POLL_ADD_MULTI.  off must be set to the amount of
       desired completions.  IORING_TIMEOUT_MULTISHOT must not be
       used with IORING_TIMEOUT_ABS.

       Since kernel 7.1, IORING_TIMEOUT_IMMEDIATE_ARG can be set
       in timeout_flags, which causes the addr field to be
       interpreted as a timeout value in nanoseconds rather than a
       pointer to a struct __kernel_timespec.  This avoids the
       need to keep a timespec structure valid in user memory
       until the request is submitted.

IORING_OP_TIMEOUT_REMOVE
       If timeout_flags are zero, then it attempts to remove an
       existing timeout operation.  addr must contain the
       user_data field of the previously issued timeout operation.
       If the specified timeout request is found and canceled
       successfully, this request will terminate with a result
       value of 0 If the timeout request was found but expiration
       was already in progress, this request will terminate with a
       result value of -EBUSY If the timeout request wasn't found,
       the request will terminate with a result value of -ENOENT
       Available since 5.5.

       If timeout_flags contain IORING_TIMEOUT_UPDATE, instead of
       removing an existing operation, it updates it.  addr and
       return values are same as before.  addr2 field must contain
       a pointer to a struct __kernel_timespec structure.
       timeout_flags may also contain IORING_TIMEOUT_ABS, in which
       case the value given is an absolute one, not a relative
       one.  Available since 5.11.

IORING_OP_ACCEPT
       Issue the equivalent of an accept4(2) system call.  fd must
       be set to the socket file descriptor, addr must contain the
       pointer to the sockaddr structure, and addr2 must contain a
       pointer to the socklen_t addrlen field. Flags can be passed
       using the accept_flags field. See also accept4(2) for the
       general description of the related system call. Available
       since 5.5.

       If the file_index field is set to a positive number, the
       file won't be installed into the normal file table as usual
       but will be placed into the fixed file table at index
       file_index - 1.  In this case, instead of returning a file
       descriptor, the result will contain either 0 on success or
       an error. If the index points to a valid empty slot, the
       installation is guaranteed to not fail. If there is already
       a file in the slot, it will be replaced, similar to
       IORING_OP_FILES_UPDATE.  Please note that only io_uring has
       access to such files and no other syscall can use them. See
       IOSQE_FIXED_FILE and IORING_REGISTER_FILES.

       Available since 5.5.

IORING_OP_ASYNC_CANCEL
       Attempt to cancel an already issued request.  addr must
       contain the user_data field of the request that should be
       canceled. The cancelation request will complete with one of
       the following results codes. If found, the res field of the
       cqe will contain 0. If not found, res will contain -ENOENT.
       If found and attempted canceled, the res field will contain
       -EALREADY.  In this case, the request may or may not
       terminate. In general, requests that are interruptible
       (like socket IO) will get canceled, while disk IO requests
       cannot be canceled if already started.  Available since
       5.5.

IORING_OP_LINK_TIMEOUT
       This request must be linked with another request through
       IOSQE_IO_LINK which is described below. Unlike
       IORING_OP_TIMEOUT, IORING_OP_LINK_TIMEOUT acts on the
       linked request, not the completion queue. The format of the
       command is otherwise like IORING_OP_TIMEOUT, except there's
       no completion event count as it's tied to a specific
       request.  If used, the timeout specified in the command
       will cancel the linked command, unless the linked command
       completes before the timeout. The timeout will complete
       with -ETIME if the timer expired and the linked request was
       attempted canceled, or -ECANCELED if the timer got canceled
       because of completion of the linked request. Like
       IORING_OP_TIMEOUT the clock source used is CLOCK_MONOTONIC
       Available since 5.5.

IORING_OP_CONNECT
       Issue the equivalent of a connect(2) system call.  fd must
       be set to the socket file descriptor, addr must contain the
       const pointer to the sockaddr structure, and off must
       contain the socklen_t addrlen field. See also connect(2)
       for the general description of the related system call.
       Available since 5.5.

IORING_OP_FALLOCATE
       Issue the equivalent of a fallocate(2) system call.  fd
       must be set to the file descriptor, len must contain the
       mode associated with the operation, off must contain the
       offset on which to operate, and addr must contain the
       length. See also fallocate(2) for the general description
       of the related system call. Available since 5.6.

IORING_OP_FADVISE
       Issue the equivalent of a posix_fadvise(2) system call.  fd
       must be set to the file descriptor, off must contain the
       offset on which to operate, len must contain the length,
       and fadvise_advice must contain the advice associated with
       the operation. See also posix_fadvise(2) for the general
       description of the related system call. Available since
       5.6.

IORING_OP_MADVISE
       Issue the equivalent of a madvise(2) system call.  addr
       must contain the address to operate on, len must contain
       the length on which to operate, and fadvise_advice must
       contain the advice associated with the operation. See also
       madvise(2) for the general description of the related
       system call. Available since 5.6.

IORING_OP_OPENAT
       Issue the equivalent of a openat(2) system call.  fd is the
       dirfd argument, addr must contain a pointer to the
       *pathname argument, open_flags should contain any flags
       passed in, and len is access mode of the file. See also
       openat(2) for the general description of the related system
       call. Available since 5.6.

       If the file_index field is set to a positive number, the
       file won't be installed into the normal file table as usual
       but will be placed into the fixed file table at index
       file_index - 1.  In this case, instead of returning a file
       descriptor, the result will contain either 0 on success or
       an error. If the index points to a valid empty slot, the
       installation is guaranteed to not fail. If there is already
       a file in the slot, it will be replaced, similar to
       IORING_OP_FILES_UPDATE.  Please note that only io_uring has
       access to such files and no other syscall can use them. See
       IOSQE_FIXED_FILE and IORING_REGISTER_FILES.

       Available since 5.15.

IORING_OP_OPENAT2
       Issue the equivalent of a openat2(2) system call.  fd is
       the dirfd argument, addr must contain a pointer to the
       *pathname argument, len should contain the size of the
       open_how structure, and off should be set to the address of
       the open_how structure. See also openat2(2) for the general
       description of the related system call. Available since
       5.6.

       If the file_index field is set to a positive number, the
       file won't be installed into the normal file table as usual
       but will be placed into the fixed file table at index
       file_index - 1.  In this case, instead of returning a file
       descriptor, the result will contain either 0 on success or
       an error. If the index points to a valid empty slot, the
       installation is guaranteed to not fail. If there is already
       a file in the slot, it will be replaced, similar to
       IORING_OP_FILES_UPDATE.  Please note that only io_uring has
       access to such files and no other syscall can use them. See
       IOSQE_FIXED_FILE and IORING_REGISTER_FILES.

       Available since 5.15.

IORING_OP_CLOSE
       Issue the equivalent of a close(2) system call.  fd is the
       file descriptor to be closed. See also close(2) for the
       general description of the related system call. Available
       since 5.6.  If the file_index field is set to a positive
       number, this command can be used to close files that were
       direct opened through IORING_OP_OPENAT, IORING_OP_OPENAT2,
       or IORING_OP_ACCEPT using the io_uring specific direct
       descriptors. Note that only one of the descriptor fields
       may be set. The direct close feature is available since the
       5.15 kernel, where direct descriptors were introduced.

IORING_OP_STATX
       Issue the equivalent of a statx(2) system call.  fd is the
       dirfd argument, addr must contain a pointer to the
       *pathname string, statx_flags is the flags argument, len
       should be the mask argument, and off must contain a pointer
       to the statxbuf to be filled in. See also statx(2) for the
       general description of the related system call. Available
       since 5.6.

IORING_OP_READ

IORING_OP_WRITE
       Issue the equivalent of a pread(2) or pwrite(2) system
       call.  fd is the file descriptor to be operated on, addr
       contains the buffer in question, len contains the length of
       the IO operation, and offs contains the read or write
       offset. If fd does not refer to a seekable file, off must
       be set to zero or -1. If offs is set to -1 , the offset
       will use (and advance) the file position, like the read(2)
       and write(2) system calls. These are non-vectored versions
       of the IORING_OP_READV and IORING_OP_WRITEV opcodes. See
       also read(2) and write(2) for the general description of
       the related system call. Available since 5.6.

IORING_OP_SPLICE
       Issue the equivalent of a splice(2) system call.
       splice_fd_in is the file descriptor to read from,
       splice_off_in is an offset to read from, fd is the file
       descriptor to write to, off is an offset from which to
       start writing to. A sentinel value of -1 is used to pass
       the equivalent of a NULL for the offsets to splice(2).  len
       contains the number of bytes to copy.  splice_flags
       contains a bit mask for the flag field associated with the
       system call.  Please note that one of the file descriptors
       must refer to a pipe.  See also splice(2) for the general
       description of the related system call. Available since
       5.7.

IORING_OP_TEE
       Issue the equivalent of a tee(2) system call.  splice_fd_in
       is the file descriptor to read from, fd is the file
       descriptor to write to, len contains the number of bytes to
       copy, and splice_flags contains a bit mask for the flag
       field associated with the system call.  Please note that
       both of the file descriptors must refer to a pipe.  See
       also tee(2) for the general description of the related
       system call. Available since 5.8.
