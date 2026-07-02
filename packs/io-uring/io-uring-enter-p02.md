---
title: "io_uring_enter(2) (part 2/2)"
source: https://man7.org/linux/man-pages/man2/io_uring_enter.2.html
domain: io-uring
license: CC-BY-SA-4.0
tags: io_uring, asynchronous i/o, linux async io
fetched: 2026-07-02
part: 2/2
---

# io_uring_enter(2)

IORING_OP_FILES_UPDATE
       This command is an alternative to using
       IORING_REGISTER_FILES_UPDATE which then works in an async
       fashion, like the rest of the io_uring commands.  The
       arguments passed in are the same.  addr must contain a
       pointer to the array of file descriptors, len must contain
       the length of the array, and off must contain the offset at
       which to operate. Note that the array of file descriptors
       pointed to in addr must remain valid until this operation
       has completed. Available since 5.6.

IORING_OP_PROVIDE_BUFFERS
       This command allows an application to register a group of
       buffers to be used by commands that read/receive data.
       Using buffers in this manner can eliminate the need to
       separate the poll + read, which provides a convenient point
       in time to allocate a buffer for a given request. It's
       often infeasible to have as many buffers available as
       pending reads or receive. With this feature, the
       application can have its pool of buffers ready in the
       kernel, and when the file or socket is ready to
       read/receive data, a buffer can be selected for the
       operation.  fd must contain the number of buffers to
       provide, addr must contain the starting address to add
       buffers from, len must contain the length of each buffer to
       add from the range, buf_group must contain the group ID of
       this range of buffers, and off must contain the starting
       buffer ID of this range of buffers. With that set, the
       kernel adds buffers starting with the memory address in
       addr, each with a length of len.  Hence the application
       should provide len * fd worth of memory in addr.  Buffers
       are grouped by the group ID, and each buffer within this
       group will be identical in size according to the above
       arguments. This allows the application to provide different
       groups of buffers, and this is often used to have
       differently sized buffers available depending on what the
       expectations are of the individual request. When submitting
       a request that should use a provided buffer, the
       IOSQE_BUFFER_SELECT flag must be set, and buf_group must be
       set to the desired buffer group ID where the buffer should
       be selected from. Available since 5.7.

IORING_OP_REMOVE_BUFFERS
       Remove buffers previously registered with
       IORING_OP_PROVIDE_BUFFERS.  fd must contain the number of
       buffers to remove, and buf_group must contain the buffer
       group ID from which to remove the buffers. Available since
       5.7.

IORING_OP_SHUTDOWN
       Issue the equivalent of a shutdown(2) system call.  fd is
       the file descriptor to the socket being shutdown, and len
       must be set to the how argument. No no other fields should
       be set. Available since 5.11.

IORING_OP_RENAMEAT
       Issue the equivalent of a renameat2(2) system call.  fd
       should be set to the olddirfd, addr should be set to the
       oldpath, len should be set to the newdirfd, addr should be
       set to the oldpath, addr2 should be set to the newpath, and
       finally rename_flags should be set to the flags passed in
       to renameat2(2).  Available since 5.11.

IORING_OP_UNLINKAT
       Issue the equivalent of a unlinkat(2) system call.  fd
       should be set to the dirfd, addr should be set to the
       pathname, and unlink_flags should be set to the flags being
       passed in to unlinkat(2).  Available since 5.11.

IORING_OP_MKDIRAT
       Issue the equivalent of a mkdirat(2) system call.  fd
       should be set to the dirfd, addr should be set to the
       pathname, and len should be set to the mode being passed in
       to mkdirat(2).  Available since 5.15.

IORING_OP_SYMLINKAT
       Issue the equivalent of a symlinkat(2) system call.  fd
       should be set to the newdirfd, addr should be set to the
       target and addr2 should be set to the linkpath being passed
       in to symlinkat(2).  Available since 5.15.

IORING_OP_LINKAT
       Issue the equivalent of a linkat(2) system call.  fd should
       be set to the olddirfd, addr should be set to the oldpath,
       len should be set to the newdirfd, addr2 should be set to
       the newpath, and hardlink_flags should be set to the flags
       being passed in to linkat(2).  Available since 5.15.

IORING_OP_MSG_RING
       Send a message to an io_uring.  fd must be set to a file
       descriptor of a ring that the application has access to,
       len can be set to any 32-bit value that the application
       wishes to pass on, and off should be set any 64-bit value
       that the application wishes to send. On the target ring, a
       CQE will be posted with the res field matching the len set,
       and a user_data field matching the off value being passed
       in. This request type can be used to either just wake or
       interrupt anyone waiting for completions on the target
       ring, or it can be used to pass messages via the two
       fields. Available since 5.18.

IORING_OP_SOCKET
       Issue the equivalent of a socket(2) system call.  fd must
       contain the communication domain, off must contain the
       communication type, len must contain the protocol, and
       rw_flags is currently unused and must be set to zero. See
       also socket(2) for the general description of the related
       system call. Available since 5.19.

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

       Available since 5.19.

IORING_OP_URING_CMD
       Issues an asynchronous, per-file private operation, similar
       to ioctl(2).  Further information may be found in the
       dedicated man page of IORING_OP_URING_CMD.

       Available since 5.19.

IORING_OP_SEND_ZC
       Issue the zerocopy equivalent of a send(2) system call.
       Similar to IORING_OP_SEND, but tries to avoid making
       intermediate copies of data. Zerocopy execution is not
       guaranteed and may fall back to copying. The request may
       also fail with -EOPNOTSUPP, when a protocol doesn't support
       zerocopy, in which case users are recommended to use
       copying sends instead.

       The flags field of the first struct io_uring_cqe may likely
       contain IORING_CQE_F_MORE, which means that there will be a
       second completion event / notification for the request,
       with the user_data field set to the same value. The user
       must not modify the data buffer until the notification is
       posted. The first cqe follows the usual rules and so its
       res field will contain the number of bytes sent or a
       negative error code. The notification's res field will be
       set to zero and the flags field will contain
       IORING_CQE_F_NOTIF.  The two step model is needed because
       the kernel may hold on to buffers for a long time, e.g.
       waiting for a TCP ACK, and having a separate cqe for
       request completions allows userspace to push more data
       without extra delays. Note, notifications are only
       responsible for controlling the lifetime of the buffers,
       and as such don't mean anything about whether the data has
       atually been sent out or received by the other end. Even
       errored requests may generate a notification, and the user
       must check for IORING_CQE_F_MORE rather than relying on the
       result.

       fd must be set to the socket file descriptor, addr must
       contain a pointer to the buffer, len denotes the length of
       the buffer to send, and msg_flags holds the flags
       associated with the system call. When addr2 is non-zero it
       points to the address of the target with addr_len
       specifying its size, turning the request into a sendto(2)
       system call equivalent.

       Available since 6.0.

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

            IORING_RECVSEND_FIXED_BUF If set, instructs io_uring
            to use a pre-mapped buffer. The buf_index field should
            contain an index into an array of fixed buffers. See
            io_uring_register(2) for details on how to setup a
            context for fixed buffer I/O.

IORING_OP_SENDMSG_ZC
       Issue the zerocopy equivalent of a sendmsg(2) system call.
       Works just like IORING_OP_SENDMSG, but like
       IORING_OP_SEND_ZC supports IORING_RECVSEND_FIXED_BUF.  For
       additional notes regarding zero copy see IORING_OP_SEND_ZC.

       Available since 6.1

IORING_OP_WAITID
       Issue the equivalent of a waitid(2) system call.  len must
       contain the idtype being queried/waited for and fd must
       contain the 'pid' (or id) being waited for.  file_index is
       the 'options' being set (the child state changes to wait
       for).  addr2 is a pointer to siginfo_t, if any, being
       filled in. See also waitid(2) for the general description
       of the related system call. Available since 6.5.

IORING_OP_SETXATTR

IORING_OP_GETXATTR

IORING_OP_FSETXATTR

IORING_OP_FGETXATTR
       Issue the equivalent of a setxattr(2) or getxattr(2) or
       fsetxattr(2) or fgetxattr(2) system call.  addr must
       contain a pointer to a buffer containing the name of the
       extended attribute.  addr2 must contain a pointer to a
       buffer of maximum length len, in which the value of the
       extended attribute is to be placed or is read from.
       Additional flags maybe provided in xattr_flags.  For
       setxattr(2) or getxattr(2) addr3 must contain a pointer to
       the path of the file.  For fsetxattr(2) or fgetxattr(2) fd
       must contain the file descriptor of the file.

       Available since 5.19.

IORING_OP_BIND
       Issues the equivalent of the bind(2) system call.  fd must
       contain the file descriptor of the socket, addr must
       contain a pointer to the sockaddr struct containing the
       address to assign and addr2 must contain the length of the
       address.

       Available since 6.11.

IORING_OP_LISTEN
       Issues the equivalent of the listen(2) system call.  fd
       must contain the file descriptor of the socket and len must
       contain the backlog parameter, i.e. the maximum amount of
       pending queued connections.

       Available since 6.11.

IORING_OP_FTRUNCATE
       Issues the equivalent of the ftruncate(2) system call.  fd
       must contain the file descriptor of the file to truncate
       and off must contain the length to which the file will be
       truncated.

       Available since 6.9.

IORING_OP_READ_MULTISHOT
       Like IORING_OP_READ, but similar to requests prepared with
       io_uring_prep_multishot_accept(3) additional reads and thus
       CQEs will be performed based on this single SQE once there
       is more data available.  Is restricted to pollable files
       and will fall back to single shot if the file does not
       support NOWAIT.  Like other multishot type requests, the
       application should look at the CQE flags and see if
       IORING_CQE_F_MORE is set on completion as an indication of
       whether or not the read request will generate further CQEs.
       Available since 6.7.

IORING_OP_FUTEX_WAIT
       Issues the equivalent of the futex_wait(2) system call.
       addr must hold a pointer to the futex, addr2 must hold the
       value to which the futex has to be changed so this caller
       to futex_wait(2) can be woken by a call to futex_wake(2),
       addr3 must hold the bitmask of this futex_wait(2) caller.
       For a caller of futex_wake(2) to wake a waiter additionally
       the bitmask of the waiter and waker must have at least one
       set bit in common.  fd must contain additional flags passed
       in.

       Available since 6.7.

IORING_OP_FUTEX_WAKE
       Issues the equivalent of the futex_wake(2) system call.
       addr must hold a pointer to the futex, addr2 must hold the
       maximum number of waiters waiting on this futex to wake,
       addr3 must hold the bitmask of this futex_wake(2) call.  To
       wake a waiter additionally the bitmask of the waiter and
       waker must have at least one set bit in common.  fd must
       contain additional flags passed in.

       Available since 6.7.

IORING_OP_FUTEX_WAITV
       Issues the equivalent of the futex_waitv(2) system call.
       addr must hold a pointer to the futexv struct, len must
       hold the length of the futexv struct, which may not be 0
       and must be smaller than FUTEX_WAITV_MAX (as of 6.11 ==
       128).

       Available since 6.7.

IORING_OP_FIXED_FD_INSTALL
       This operation is used to insert a registered file into the
       regular process file table.  Consequently fd must contain
       the file index and IOSQE_FIXED_FILE must be set.  The
       resulting regular fd is returned via cqe->res.  Additional
       flags may be passed in via install_fd_flags.  Currently
       supported flags are: IORING_FIXED_FD_NO_CLOEXEC, which
       overrides a potentially set O_CLOEXEC flag set on the
       initial file.

       Available since 6.8.

IORING_OP_PIPE
       This operation is used to create a pipe, a set of file
       descriptors that can be used for communication. The pipe
       may either be created as a set of normal file descriptors,
       or it can be created as fixed/direct descriptors.  addr
       must contain a pointer to an array of two integers, where
       upon successful completion of the request, index 0 will
       contain the read side and index 1 the write side of the
       pipe.  pipe_flags may contain flags associated with pipe
       creation. Currently O_CLOEXEC | O_NONBLOCK | O_DIRECT |
       O_NOTIFICATION_PIPE are supported.  file_index may contain
       the the desired starting point for a fixed descriptor pipe
       creation. If this is set to 0, then regular file
       descriptors are used. If set to IORING_FILE_INDEX_ALLOC,
       then the kernel will allocate descriptors from the
       previously registered direct descriptor table. If set to
       any non-zero value, then it sets the exact direct
       descriptor value for index 0 of the pipe, and index 1 will
       be the following integer value.

       If used with direct descriptors rather than normal file
       descriptors, a direct descriptor table must have been
       previously registered with the kernel.

       Available since 6.16.

IORING_OP_RECV_ZC
       Receive data from a socket using zero-copy techniques.
       Unlike IORING_OP_RECV, this operation does not use a user-
       provided buffer. Instead, data is delivered through a pre-
       registered zero-copy RX interface queue.  fd must be set to
       the socket file descriptor.  zcrx_ifq_idx specifies the
       index of the registered zero-copy RX interface queue.  len
       specifies the maximum amount of data to receive.  ioprio
       can contain flags such as IORING_RECVSEND_POLL_FIRST and
       IORING_RECV_MULTISHOT.  This operation requires multishot
       mode.

       Before using this command, a zero-copy RX interface queue
       must be registered via io_uring_register(2) using
       IORING_REGISTER_ZCRX_IFQ.  Data completions are posted as
       auxiliary CQEs.

       Available since 6.15.

IORING_OP_EPOLL_WAIT
       Wait for events on an epoll instance. This is an async
       version of epoll_wait(2).  fd must be set to the epoll file
       descriptor, addr must point to an array of struct
       epoll_event to receive the events, and len must contain the
       maximum number of events to return.

       The primary use case is for legacy event loops that still
       use epoll for some file descriptors. By using io_uring to
       wait on epoll events, the application can unify its event
       handling through io_uring while maintaining backwards
       compatibility with epoll-based components.

       Available since 6.15.

IORING_OP_READV_FIXED

IORING_OP_WRITEV_FIXED
       Vectored read and write operations using pre-registered
       buffers, combining the functionality of
       IORING_OP_READV/IORING_OP_WRITEV with
       IORING_OP_READ_FIXED/IORING_OP_WRITE_FIXED.  The buf_index
       field specifies the index into the registered buffer table.
       Unlike the non-fixed vectored operations, the iovec entries
       point into the registered buffer region. This allows
       vectored I/O while still benefiting from the reduced
       overhead of pre-registered buffers.

       Available since 6.15.

IORING_OP_NOP128
       No operation, similar to IORING_OP_NOP, but explicitly uses
       a 128-byte SQE. This can be useful for testing or alignment
       purposes when using mixed 64/128-byte SQE rings
       (IORING_SETUP_SQE_MIXED).

       Available since 6.19.

IORING_OP_URING_CMD128
       Passthrough command to the underlying file, identical to
       IORING_OP_URING_CMD, but explicitly uses a 128-byte SQE.
       The extra 64 bytes provide additional space for command-
       specific data. This is useful with IORING_SETUP_SQE_MIXED
       rings where some commands need the larger SQE size while
       others do not.

       See IORING_OP_URING_CMD for general usage details.

       Available since 6.19.

The flags field is a bit mask. The supported flags are:

IOSQE_FIXED_FILE
       When this flag is specified, fd is an index into the files
       array registered with the io_uring instance (see the
       IORING_REGISTER_FILES section of the io_uring_register(2)
       man page). Note that this isn't always available for all
       commands. If used on a command that doesn't support fixed
       files, the SQE will error with -EBADF.  Available since
       5.1.

IOSQE_IO_DRAIN
       When this flag is specified, the SQE will not be started
       before previously submitted SQEs have completed, and new
       SQEs will not be started before this one completes.
       Available since 5.2.

IOSQE_IO_LINK
       When this flag is specified, the SQE forms a link with the
       next SQE in the submission ring. That next SQE will not be
       started before the previous request completes. This, in
       effect, forms a chain of SQEs, which can be arbitrarily
       long. The tail of the chain is denoted by the first SQE
       that does not have this flag set. Chains are not supported
       across submission boundaries. Even if the last SQE in a
       submission has this flag set, it will still terminate the
       current chain. This flag has no effect on previous SQE
       submissions, nor does it impact SQEs that are outside of
       the chain tail. This means that multiple chains can be
       executing in parallel, or chains and individual SQEs. Only
       members inside the chain are serialized. A chain of SQEs
       will be broken if any request in that chain ends in error.
       io_uring considers any unexpected result an error. This
       means that, eg, a short read will also terminate the
       remainder of the chain.  If a chain of SQE links is broken,
       the remaining unstarted part of the chain will be
       terminated and completed with -ECANCELED as the error code.
       Available since 5.3.

IOSQE_IO_HARDLINK
       Like IOSQE_IO_LINK, but it doesn't sever regardless of the
       completion result.  Note that the link will still sever if
       we fail submitting the parent request, hard links are only
       resilient in the presence of completion results for
       requests that did submit correctly.  IOSQE_IO_HARDLINK
       implies IOSQE_IO_LINK.  Available since 5.5.

IOSQE_ASYNC
       Normal operation for io_uring is to try and issue an sqe as
       non-blocking first, and if that fails, execute it in an
       async manner. To support more efficient overlapped
       operation of requests that the application knows/assumes
       will always (or most of the time) block, the application
       can ask for an sqe to be issued async from the start.
       Available since 5.6.

IOSQE_BUFFER_SELECT
       Used in conjunction with the IORING_OP_PROVIDE_BUFFERS
       command, which registers a pool of buffers to be used by
       commands that read or receive data. When buffers are
       registered for this use case, and this flag is set in the
       command, io_uring will grab a buffer from this pool when
       the request is ready to receive or read data. If
       successful, the resulting CQE will have IORING_CQE_F_BUFFER
       set in the flags part of the struct, and the upper
       IORING_CQE_BUFFER_SHIFT bits will contain the ID of the
       selected buffers. This allows the application to know
       exactly which buffer was selected for the operation. If no
       buffers are available and this flag is set, then the
       request will fail with -ENOBUFS as the error code. Once a
       buffer has been used, it is no longer available in the
       kernel pool. The application must re-register the given
       buffer again when it is ready to recycle it (eg has
       completed using it). Available since 5.7.

IOSQE_CQE_SKIP_SUCCESS
       Don't generate a CQE if the request completes successfully.
       If the request fails, an appropriate CQE will be posted as
       usual and if there is no IOSQE_IO_HARDLINK, CQEs for all
       linked requests will be omitted. The notion of
       failure/success is opcode specific and is the same as with
       breaking chains of IOSQE_IO_LINK.  One special case is when
       the request has a linked timeout, then the CQE generation
       for the linked timeout is decided solely by whether it has
       IOSQE_CQE_SKIP_SUCCESS set, regardless whether it timed out
       or was canceled. In other words, if a linked timeout has
       the flag set, it's guaranteed to not post a CQE.

       The semantics are chosen to accommodate several use cases.
       First, when all but the last request of a normal link
       without linked timeouts are marked with the flag, only one
       CQE per link is posted. Additionally, it enables
       suppression of CQEs in cases where the side effects of a
       successfully executed operation is enough for userspace to
       know the state of the system. One such example would be
       writing to a synchronisation file.

       This flag is incompatible with IOSQE_IO_DRAIN.  Using both
       of them in a single ring is undefined behavior, even when
       they are not used together in a single request. Currently,
       after the first request with IOSQE_CQE_SKIP_SUCCESS, all
       subsequent requests marked with drain will be failed at
       submission time.  Note that the error reporting is best
       effort only, and restrictions may change in the future.

       Available since 5.17.

ioprio specifies the I/O priority.  See ioprio_get(2) for a
description of Linux I/O priorities.

fd specifies the file descriptor against which the operation will
be performed, with the exception noted above.

If the operation is one of IORING_OP_READ_FIXED or
IORING_OP_WRITE_FIXED, addr and len must fall within the buffer
located at buf_index in the fixed buffer array.  If the operation
is either IORING_OP_READV or IORING_OP_WRITEV, then addr points to
an iovec array of len entries.

rw_flags, specified for read and write operations, contains a
bitwise OR of per-I/O flags, as described in the preadv2(2) man
page.

The fsync_flags bit mask may contain either 0, for a normal file
integrity sync, or IORING_FSYNC_DATASYNC to provide data sync only
semantics.  See the descriptions of O_SYNC and O_DSYNC in the
open(2) manual page for more information.

The bits that may be set in poll_events are defined in <poll.h>,
and documented in poll(2).

user_data is an application-supplied value that will be copied
into the completion queue entry (see below).  buf_index is an
index into an array of fixed buffers, and is only valid if fixed
buffers were registered.  personality is the credentials id to use
for this operation. See io_uring_register(2) for how to register
personalities with io_uring. If set to 0, the current personality
of the submitting task is used.

Once the submission queue entry is initialized, I/O is submitted
by placing the index of the submission queue entry into the tail
of the submission queue.  After one or more indexes are added to
the queue, and the queue tail is advanced, the io_uring_enter(2)
system call can be invoked to initiate the I/O.

Completions use the following data structure:

    /*
     * IO completion data structure (Completion Queue Entry)
     */
    struct io_uring_cqe {
        __u64    user_data; /* sqe->data submission passed back */
        __s32    res;       /* result code for this event */
        __u32    flags;
    };

user_data is copied from the field of the same name in the
submission queue entry.  The primary use case is to store data
that the application will need to access upon completion of this
particular I/O.  The flags is used for certain commands, like
IORING_OP_POLL_ADD or in conjunction with IOSQE_BUFFER_SELECT or
IORING_OP_MSG_RING, see those entries for details.  res is the
operation-specific result, but io_uring-specific errors (e.g.
flags or opcode invalid) are returned through this field.  They
are described in section CQE ERRORS.

For read and write opcodes, the return values match errno values
documented in the preadv2(2) and pwritev2(2) man pages, with res
holding the equivalent of -errno for error cases, or the
transferred number of bytes in case the operation is successful.
Hence both error and success return can be found in that field in
the CQE. For other request types, the return values are documented
in the matching man page for that type, or in the opcodes section
above for io_uring-specific opcodes.


## RETURN VALUE

io_uring_enter(2) returns the number of I/Os successfully
consumed.  This can be zero if to_submit was zero or if the
submission queue was empty. Note that if the ring was created with
IORING_SETUP_SQPOLL specified, then the return value will
generally be the same as to_submit as submission happens outside
the context of the system call.

The errors related to a submission queue entry will be returned
through a completion queue entry (see section CQE ERRORS), rather
than through the system call itself.

Errors that occur not on behalf of a submission queue entry are
returned via the system call directly. On such an error, a
negative error code is returned. The caller should not rely on
errno variable.


## ERRORS

These are the errors returned by io_uring_enter(2) system call.

EAGAIN The kernel was unable to allocate memory for the request,
       or otherwise ran out of resources to handle it. The
       application should wait for some completions and try again.

EBADF  fd is not a valid file descriptor.

EBADFD fd is a valid file descriptor, but the io_uring ring is not
       in the right state (enabled). See io_uring_register(2) for
       details on how to enable the ring.

EBADR  At least one CQE was dropped even with the
       IORING_FEAT_NODROP feature, and there are no otherwise
       available CQEs. This clears the error state and so with no
       other changes the next call to io_uring_enter(2) will not
       have this error. This error should be extremely rare and
       indicates the machine is running critically low on memory.
       It may be reasonable for the application to terminate
       running unless it is able to safely handle any CQE being
       lost.

EBUSY  If the IORING_FEAT_NODROP feature flag is set, then EBUSY
       will be returned if there were overflow entries,
       IORING_ENTER_GETEVENTS flag is set and not all of the
       overflow entries were able to be flushed to the CQ ring.

       Without IORING_FEAT_NODROP the application is attempting to
       overcommit the number of requests it can have pending. The
       application should wait for some completions and try again.
       May occur if the application tries to queue more requests
       than we have room for in the CQ ring, or if the application
       attempts to wait for more events without having reaped the
       ones already present in the CQ ring.

EEXIST The thread submitting the work is invalid. This may occur
       if IORING_ENTER_GETEVENTS and IORING_SETUP_DEFER_TASKRUN is
       set, but the submitting thread is not the thread that
       initially created or enabled the io_uring associated with
       fd.

EINVAL Some bits in the flags argument are invalid.

EFAULT An invalid user space address was specified for the sig
       argument.

ENXIO  The io_uring instance is in the process of being torn down.

EOPNOTSUPP
       fd does not refer to an io_uring instance.

EINTR  The operation was interrupted by a delivery of a signal
       before it could complete; see signal(7).  Can happen while
       waiting for events with IORING_ENTER_GETEVENTS.

EOWNERDEAD
       The ring has been setup with IORING_SETUP_SQPOLL and the sq
       poll kernel thread has been killed.


## CQE ERRORS

These io_uring-specific errors are returned as a negative value in
the res field of the completion queue entry.

EACCES The flags field or opcode in a submission queue entry is
       not allowed due to registered restrictions.  See
       io_uring_register(2) for details on how restrictions work.

EBADF  The fd field in the submission queue entry is invalid, or
       the IOSQE_FIXED_FILE flag was set in the submission queue
       entry, but no files were registered with the io_uring
       instance.

EFAULT buffer is outside of the process' accessible address space

EFAULT IORING_OP_READ_FIXED or IORING_OP_WRITE_FIXED was specified
       in the opcode field of the submission queue entry, but
       either buffers were not registered for this io_uring
       instance, or the address range described by addr and len
       does not fit within the buffer registered at buf_index.

EINVAL The flags field or opcode in a submission queue entry is
       invalid.

EINVAL The buf_index member of the submission queue entry is
       invalid.

EINVAL The personality field in a submission queue entry is
       invalid.

EINVAL IORING_OP_READV or IORING_OP_WRITEV was specified in the
       submission queue entry, but the io_uring instance has fixed
       buffers registered.

EINVAL IORING_OP_READ_FIXED or IORING_OP_WRITE_FIXED was specified
       in the submission queue entry, and the buf_index is
       invalid.

EINVAL IORING_OP_READV, IORING_OP_WRITEV, IORING_OP_READ_FIXED,
       IORING_OP_WRITE_FIXED or IORING_OP_FSYNC was specified in
       the submission queue entry, but the io_uring instance was
       configured for IOPOLLing, or any of addr, ioprio, off, len,
       or buf_index was set in the submission queue entry.

EINVAL IORING_OP_POLL_ADD or IORING_OP_POLL_REMOVE was specified
       in the opcode field of the submission queue entry, but the
       io_uring instance was configured for busy-wait polling
       (IORING_SETUP_IOPOLL), or any of ioprio, off, len, or
       buf_index was non-zero in the submission queue entry.

EINVAL IORING_OP_POLL_ADD was specified in the opcode field of the
       submission queue entry, and the addr field was non-zero.

EOPNOTSUPP
       opcode is valid, but not supported by this kernel.

EOPNOTSUPP
       IOSQE_BUFFER_SELECT was set in the flags field of the
       submission queue entry, but the opcode doesn't support
       buffer selection.

EINVAL IORING_OP_TIMEOUT was specified, but timeout_flags
       specified more than one clock source or
       IORING_TIMEOUT_MULTISHOT was set alongside
       IORING_TIMEOUT_ABS.
