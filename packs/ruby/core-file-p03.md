---
title: "class File (part 3/3)"
source: https://ruby-doc.org/core/File.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 3/3
---

# class File

Opens the file at the given `path` according to the given `mode`; creates and returns a new `File` object for that file.

The new `File` object is buffered mode (or non-sync mode), unless `filename` is a tty. See `IO#flush`, `IO#fsync`, `IO#fdatasync`, and `IO#sync=`.

Argument `path` must be a valid file path:

```
f = File.new('/etc/fstab')
f.close
f = File.new('t.txt')
f.close
```

Optional argument `mode` (defaults to ‘r’) must specify a valid mode; see Access Modes:

```
f = File.new('t.tmp', 'w')
f.close
f = File.new('t.tmp', File::RDONLY)
f.close
```

Optional argument `perm` (defaults to 0666) must specify valid permissions see File Permissions:

```
f = File.new('t.tmp', File::CREAT, 0644)
f.close
f = File.new('t.tmp', File::CREAT, 0444)
f.close
```

Optional keyword arguments `opts` specify:

- Open Options.
- Encoding options.

```
static VALUE
rb_file_initialize(int argc, VALUE *argv, VALUE io)
{
    if (RFILE(io)->fptr) {
        rb_raise(rb_eRuntimeError, "reinitializing File");
    }
    VALUE fname, vmode, vperm, opt;
    int posargc = rb_scan_args(argc, argv, "12:", &fname, &vmode, &vperm, &opt);
    if (posargc < 3) {          /* perm is File only */
        VALUE fd = rb_check_to_int(fname);

        if (!NIL_P(fd)) {
            return io_initialize(io, fd, vmode, opt);
        }
    }
    return rb_open_file(io, fname, vmode, vperm, opt);
}
```

open(path, mode = 'r', perm = 0666, **opts) → file

click to toggle source

open(path, mode = 'r', perm = 0666, **opts) {|f| ... } → object

Creates a new `File` object, via `File.new` with the given arguments.

With no block given, returns the `File` object.

With a block given, calls the block with the `File` object and returns the block’s value.

```
static VALUE
rb_io_s_open(int argc, VALUE *argv, VALUE klass)
{
    VALUE io = rb_class_new_instance_kw(argc, argv, klass, RB_PASS_CALLED_KEYWORDS);

    if (rb_block_given_p()) {
        return rb_ensure(rb_yield, io, io_close, io);
    }

    return io;
}
```

owned?(file_name) → true or false

click to toggle source

Returns `true` if the named file exists and the effective used id of the calling process is the owner of the file.

*file_name* can be an `IO` object.

```
static VALUE
rb_file_owned_p(VALUE obj, VALUE fname)
{
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    return RBOOL(st.st_uid == geteuid());
}
```

path(path) → string

click to toggle source

Returns the string representation of the path

```
File.path(File::NULL)           
File.path(Pathname.new("/tmp")) 
```

```
static VALUE
rb_file_s_path(VALUE klass, VALUE fname)
{
    return rb_get_path(fname);
}
```

pipe?(filepath) → true or false

click to toggle source

Returns `true` if `filepath` points to a pipe, `false` otherwise:

```
File.mkfifo('tmp/fifo')
File.pipe?('tmp/fifo') 
File.pipe?('t.txt')    
```

```
static VALUE
rb_file_pipe_p(VALUE obj, VALUE fname)
{
#ifdef S_IFIFO
#  ifndef S_ISFIFO
#    define S_ISFIFO(m) (((m) & S_IFMT) == S_IFIFO)
#  endif

    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    if (S_ISFIFO(st.st_mode)) return Qtrue;

#endif
    return Qfalse;
}
```

readable?(file_name) → true or false

click to toggle source

Returns `true` if the named file is readable by the effective user and group id of this process. See eaccess(3).

Note that some OS-level security features may cause this to return true even though the file is not readable by the effective user/group.

```
static VALUE
rb_file_readable_p(VALUE obj, VALUE fname)
{
    return RBOOL(rb_eaccess(fname, R_OK) >= 0);
}
```

readable_real?(file_name) → true or false

click to toggle source

Returns `true` if the named file is readable by the real user and group id of this process. See access(3).

Note that some OS-level security features may cause this to return true even though the file is not readable by the real user/group.

```
static VALUE
rb_file_readable_real_p(VALUE obj, VALUE fname)
{
    return RBOOL(rb_access(fname, R_OK) >= 0);
}
```

readlink(link_name) → file_name

click to toggle source

Returns the name of the file referenced by the given link. Not available on all platforms.

```
File.symlink("testfile", "link2test")   
File.readlink("link2test")              
```

```
static VALUE
rb_file_s_readlink(VALUE klass, VALUE path)
{
    return rb_readlink(path, rb_filesystem_encoding());
}
```

realdirpath(pathname [, dir_string]) → real_pathname

click to toggle source

Returns the real (absolute) pathname of *pathname* in the actual filesystem. The real pathname doesn’t contain symlinks or useless dots.

If *dir_string* is given, it is used as a base directory for interpreting relative pathname instead of the current directory.

The last component of the real pathname can be nonexistent.

```
static VALUE
rb_file_s_realdirpath(int argc, VALUE *argv, VALUE klass)
{
    VALUE basedir = (rb_check_arity(argc, 1, 2) > 1) ? argv[1] : Qnil;
    VALUE path = argv[0];
    FilePathValue(path);
    return rb_realpath_internal(basedir, path, 0);
}
```

realpath(pathname [, dir_string]) → real_pathname

click to toggle source

Returns the real (absolute) pathname of *pathname* in the actual filesystem not containing symlinks or useless dots.

If *dir_string* is given, it is used as a base directory for interpreting relative pathname instead of the current directory.

All components of the pathname must exist when this method is called.

```
static VALUE
rb_file_s_realpath(int argc, VALUE *argv, VALUE klass)
{
    VALUE basedir = (rb_check_arity(argc, 1, 2) > 1) ? argv[1] : Qnil;
    VALUE path = argv[0];
    FilePathValue(path);
    return rb_realpath_internal(basedir, path, 1);
}
```

rename(old_name, new_name) → 0

click to toggle source

Renames the given file to the new name. Raises a `SystemCallError` if the file cannot be renamed.

```
File.rename("afile", "afile.bak")   
```

```
static VALUE
rb_file_s_rename(VALUE klass, VALUE from, VALUE to)
{
    struct rename_args ra;
    VALUE f, t;

    FilePathValue(from);
    FilePathValue(to);
    f = rb_str_encode_ospath(from);
    t = rb_str_encode_ospath(to);
    ra.src = StringValueCStr(f);
    ra.dst = StringValueCStr(t);
#if defined __CYGWIN__
    errno = 0;
#endif
    if (IO_WITHOUT_GVL_INT(no_gvl_rename, &ra) < 0) {
        int e = errno;
#if defined DOSISH
        switch (e) {
          case EEXIST:
            if (chmod(ra.dst, 0666) == 0 &&
                unlink(ra.dst) == 0 &&
                rename(ra.src, ra.dst) == 0)
                return INT2FIX(0);
        }
#endif
        syserr_fail2(e, from, to);
    }

    return INT2FIX(0);
}
```

setgid?(file_name) → true or false

click to toggle source

Returns `true` if the named file has the setgid bit set.

*file_name* can be an `IO` object.

```
static VALUE
rb_file_sgid_p(VALUE obj, VALUE fname)
{
#ifdef S_ISGID
    return check3rdbyte(fname, S_ISGID);
#else
    return Qfalse;
#endif
}
```

setuid?(file_name) → true or false

click to toggle source

Returns `true` if the named file has the setuid bit set.

*file_name* can be an `IO` object.

```
static VALUE
rb_file_suid_p(VALUE obj, VALUE fname)
{
#ifdef S_ISUID
    return check3rdbyte(fname, S_ISUID);
#else
    return Qfalse;
#endif
}
```

size(file_name) → integer

click to toggle source

Returns the size of `file_name`.

*file_name* can be an `IO` object.

```
static VALUE
rb_file_s_size(VALUE klass, VALUE fname)
{
    struct stat st;

    if (rb_stat(fname, &st) < 0) {
        int e = errno;
        FilePathValue(fname);
        rb_syserr_fail_path(e, fname);
    }
    return OFFT2NUM(st.st_size);
}
```

size?(file_name) → Integer or nil

click to toggle source

Returns `nil` if `file_name` doesn’t exist or has zero size, the size of the file otherwise.

*file_name* can be an `IO` object.

```
static VALUE
rb_file_size_p(VALUE obj, VALUE fname)
{
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qnil;
    if (st.st_size == 0) return Qnil;
    return OFFT2NUM(st.st_size);
}
```

socket?(filepath) → true or false

click to toggle source

Returns `true` if `filepath` points to a socket, `false` otherwise:

```
require 'socket'
File.socket?(Socket.new(:INET, :STREAM)) 
File.socket?(File.new('t.txt'))          
```

```
static VALUE
rb_file_socket_p(VALUE obj, VALUE fname)
{
#ifndef S_ISSOCK
#  ifdef _S_ISSOCK
#    define S_ISSOCK(m) _S_ISSOCK(m)
#  else
#    ifdef _S_IFSOCK
#      define S_ISSOCK(m) (((m) & S_IFMT) == _S_IFSOCK)
#    else
#      ifdef S_IFSOCK
#        define S_ISSOCK(m) (((m) & S_IFMT) == S_IFSOCK)
#      endif
#    endif
#  endif
#endif

#ifdef S_ISSOCK
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    if (S_ISSOCK(st.st_mode)) return Qtrue;
#endif

    return Qfalse;
}
```

split(file_name) → array

click to toggle source

Splits the given string into a directory and a file component and returns them in a two-element array. See also `File::dirname` and `File::basename`.

```
File.split("/home/gumby/.profile")   
```

```
static VALUE
rb_file_s_split(VALUE klass, VALUE path)
{
    FilePathStringValue(path);          /* get rid of converting twice */
    return rb_assoc_new(rb_file_dirname(path), rb_file_s_basename(1,&path,Qundef));
}
```

stat(filepath) → stat

click to toggle source

Returns a `File::Stat` object for the file at `filepath` (see `File::Stat`):

```
File.stat('t.txt').class 
```

```
static VALUE
rb_file_s_stat(VALUE klass, VALUE fname)
{
    struct stat st;

    FilePathValue(fname);
    fname = rb_str_encode_ospath(fname);
    if (stat_without_gvl(RSTRING_PTR(fname), &st) < 0) {
        rb_sys_fail_path(fname);
    }
    return rb_stat_new(&st);
}
```

sticky?(file_name) → true or false

click to toggle source

Returns `true` if the named file has the sticky bit set.

*file_name* can be an `IO` object.

```
static VALUE
rb_file_sticky_p(VALUE obj, VALUE fname)
{
#ifdef S_ISVTX
    return check3rdbyte(fname, S_ISVTX);
#else
    return Qfalse;
#endif
}
```

symlink(old_name, new_name) → 0

click to toggle source

Creates a symbolic link called *new_name* for the existing file *old_name*. Raises a NotImplemented exception on platforms that do not support symbolic links.

```
File.symlink("testfile", "link2test")   
```

```
static VALUE
rb_file_s_symlink(VALUE klass, VALUE from, VALUE to)
{
    FilePathValue(from);
    FilePathValue(to);
    from = rb_str_encode_ospath(from);
    to = rb_str_encode_ospath(to);

    if (symlink(StringValueCStr(from), StringValueCStr(to)) < 0) {
        sys_fail2(from, to);
    }
    return INT2FIX(0);
}
```

symlink?(filepath) → true or false

click to toggle source

Returns `true` if `filepath` points to a symbolic link, `false` otherwise:

```
symlink = File.symlink('t.txt', 'symlink')
File.symlink?('symlink') 
File.symlink?('t.txt')   
```

```
static VALUE
rb_file_symlink_p(VALUE obj, VALUE fname)
{
#ifndef S_ISLNK
#  ifdef _S_ISLNK
#    define S_ISLNK(m) _S_ISLNK(m)
#  else
#    ifdef _S_IFLNK
#      define S_ISLNK(m) (((m) & S_IFMT) == _S_IFLNK)
#    else
#      ifdef S_IFLNK
#        define S_ISLNK(m) (((m) & S_IFMT) == S_IFLNK)
#      endif
#    endif
#  endif
#endif

#ifdef S_ISLNK
    struct stat st;

    FilePathValue(fname);
    fname = rb_str_encode_ospath(fname);
    if (lstat_without_gvl(StringValueCStr(fname), &st) < 0) return Qfalse;
    if (S_ISLNK(st.st_mode)) return Qtrue;
#endif

    return Qfalse;
}
```

truncate(file_name, integer) → 0

click to toggle source

Truncates the file *file_name* to be at most *integer* bytes long. Not available on all platforms.

```
f = File.new("out", "w")
f.write("1234567890")     
f.close                   
File.truncate("out", 5)   
File.size("out")          
```

```
static VALUE
rb_file_s_truncate(VALUE klass, VALUE path, VALUE len)
{
    struct truncate_arg ta;
    int r;

    ta.pos = NUM2OFFT(len);
    FilePathValue(path);
    path = rb_str_encode_ospath(path);
    ta.path = StringValueCStr(path);

    r = IO_WITHOUT_GVL_INT(nogvl_truncate, &ta);
    if (r < 0)
        rb_sys_fail_path(path);
    return INT2FIX(0);
}
```

umask() → integer

click to toggle source

umask(integer) → integer

Returns the current umask value for this process. If the optional argument is given, set the umask to that value and return the previous value. Umask values are *subtracted* from the default permissions, so a umask of `0222` would make a file read-only for everyone.

```
File.umask(0006)   
File.umask         
```

```
static VALUE
rb_file_s_umask(int argc, VALUE *argv, VALUE _)
{
    mode_t omask = 0;

    switch (argc) {
      case 0:
        omask = umask(0);
        umask(omask);
        break;
      case 1:
        omask = umask(NUM2MODET(argv[0]));
        break;
      default:
        rb_error_arity(argc, 0, 1);
    }
    return MODET2NUM(omask);
}
```

delete(file_name, ...) → integer

click to toggle source

unlink(file_name, ...) → integer

Deletes the named files, returning the number of names passed as arguments. Raises an exception on any error. Since the underlying implementation relies on the `unlink(2)` system call, the type of exception raised depends on its error type (see linux.die.net/man/2/unlink) and has the form of e.g. Errno::ENOENT.

See also `Dir::rmdir`.

```
static VALUE
rb_file_s_unlink(int argc, VALUE *argv, VALUE klass)
{
    return apply2files(unlink_internal, argc, argv, 0);
}
```

utime(atime, mtime, file_name, ...) → integer

click to toggle source

Sets the access and modification times of each named file to the first two arguments. If a file is a symlink, this method acts upon its referent rather than the link itself; for the inverse behavior see `File.lutime`. Returns the number of file names in the argument list.

```
static VALUE
rb_file_s_utime(int argc, VALUE *argv, VALUE _)
{
    return utime_internal_i(argc, argv, FALSE);
}
```

world_readable?(file_name) → integer or nil

click to toggle source

If *file_name* is readable by others, returns an integer representing the file permission bits of *file_name*. Returns `nil` otherwise. The meaning of the bits is platform dependent; on Unix systems, see `stat(2)`.

*file_name* can be an `IO` object.

```
File.world_readable?("/etc/passwd")           
m = File.world_readable?("/etc/passwd")
sprintf("%o", m)                              
```

```
static VALUE
rb_file_world_readable_p(VALUE obj, VALUE fname)
{
#ifdef S_IROTH
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qnil;
    if ((st.st_mode & (S_IROTH)) == S_IROTH) {
        return UINT2NUM(st.st_mode & (S_IRUGO|S_IWUGO|S_IXUGO));
    }
#endif
    return Qnil;
}
```

world_writable?(file_name) → integer or nil

click to toggle source

If *file_name* is writable by others, returns an integer representing the file permission bits of *file_name*. Returns `nil` otherwise. The meaning of the bits is platform dependent; on Unix systems, see `stat(2)`.

*file_name* can be an `IO` object.

```
File.world_writable?("/tmp")                  
m = File.world_writable?("/tmp")
sprintf("%o", m)                              
```

```
static VALUE
rb_file_world_writable_p(VALUE obj, VALUE fname)
{
#ifdef S_IWOTH
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qnil;
    if ((st.st_mode & (S_IWOTH)) == S_IWOTH) {
        return UINT2NUM(st.st_mode & (S_IRUGO|S_IWUGO|S_IXUGO));
    }
#endif
    return Qnil;
}
```

writable?(file_name) → true or false

click to toggle source

Returns `true` if the named file is writable by the effective user and group id of this process. See eaccess(3).

Note that some OS-level security features may cause this to return true even though the file is not writable by the effective user/group.

```
static VALUE
rb_file_writable_p(VALUE obj, VALUE fname)
{
    return RBOOL(rb_eaccess(fname, W_OK) >= 0);
}
```

writable_real?(file_name) → true or false

click to toggle source

Returns `true` if the named file is writable by the real user and group id of this process. See access(3).

Note that some OS-level security features may cause this to return true even though the file is not writable by the real user/group.

```
static VALUE
rb_file_writable_real_p(VALUE obj, VALUE fname)
{
    return RBOOL(rb_access(fname, W_OK) >= 0);
}
```

zero?(file_name) → true or false

click to toggle source

Returns `true` if the named file exists and has a zero size.

*file_name* can be an `IO` object.

```
static VALUE
rb_file_zero_p(VALUE obj, VALUE fname)
{
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    return RBOOL(st.st_size == 0);
}
```

### Public Instance Methods

atime → time

click to toggle source

Returns the last access time (a `Time` object) for *file*, or epoch if *file* has not been accessed.

```
File.new("testfile").atime   
```

```
static VALUE
rb_file_atime(VALUE obj)
{
    rb_io_t *fptr;
    struct stat st;

    GetOpenFile(obj, fptr);
    if (fstat(fptr->fd, &st) == -1) {
        rb_sys_fail_path(fptr->pathv);
    }
    return stat_atime(&st);
}
```

birthtime → time

click to toggle source

Returns the birth time for *file*.

```
File.new("testfile").birthtime   
```

If the platform doesn’t have birthtime, raises `NotImplementedError`.

```
static VALUE
rb_file_birthtime(VALUE obj)
{
    rb_io_t *fptr;
    statx_data st;

    GetOpenFile(obj, fptr);
    if (fstatx_without_gvl(fptr, &st, STATX_BTIME) == -1) {
        rb_sys_fail_path(fptr->pathv);
    }
    return statx_birthtime(&st, fptr->pathv);
}
```

chmod(mode_int) → 0

click to toggle source

Changes permission bits on *file* to the bit pattern represented by *mode_int*. Actual effects are platform dependent; on Unix systems, see `chmod(2)` for details. Follows symbolic links. Also see File#lchmod.

```
f = File.new("out", "w");
f.chmod(0644)   
```

```
static VALUE
rb_file_chmod(VALUE obj, VALUE vmode)
{
    rb_io_t *fptr;
    mode_t mode;
#if !defined HAVE_FCHMOD || !HAVE_FCHMOD
    VALUE path;
#endif

    mode = NUM2MODET(vmode);

    GetOpenFile(obj, fptr);
#ifdef HAVE_FCHMOD
    if (rb_fchmod(fptr->fd, mode) == -1) {
        if (HAVE_FCHMOD || errno != ENOSYS)
            rb_sys_fail_path(fptr->pathv);
    }
    else {
        if (!HAVE_FCHMOD) return INT2FIX(0);
    }
#endif
#if !defined HAVE_FCHMOD || !HAVE_FCHMOD
    if (NIL_P(fptr->pathv)) return Qnil;
    path = rb_str_encode_ospath(fptr->pathv);
    if (rb_chmod(RSTRING_PTR(path), mode) == -1)
        rb_sys_fail_path(fptr->pathv);
#endif

    return INT2FIX(0);
}
```

chown(owner_int, group_int ) → 0

click to toggle source

Changes the owner and group of *file* to the given numeric owner and group id’s. Only a process with superuser privileges may change the owner of a file. The current owner of a file may change the file’s group to any group to which the owner belongs. A `nil` or -1 owner or group id is ignored. Follows symbolic links. See also File#lchown.

```
File.new("testfile").chown(502, 1000)
```

```
static VALUE
rb_file_chown(VALUE obj, VALUE owner, VALUE group)
{
    rb_io_t *fptr;
    rb_uid_t o;
    rb_gid_t g;
#ifndef HAVE_FCHOWN
    VALUE path;
#endif

    o = to_uid(owner);
    g = to_gid(group);
    GetOpenFile(obj, fptr);
#ifndef HAVE_FCHOWN
    if (NIL_P(fptr->pathv)) return Qnil;
    path = rb_str_encode_ospath(fptr->pathv);
    if (rb_chown(RSTRING_PTR(path), o, g) == -1)
        rb_sys_fail_path(fptr->pathv);
#else
    if (rb_fchown(fptr->fd, o, g) == -1)
        rb_sys_fail_path(fptr->pathv);
#endif

    return INT2FIX(0);
}
```

ctime → time

click to toggle source

Returns the change time for *file* (that is, the time directory information about the file was changed, not the file itself).

Note that on Windows (NTFS), returns creation time (birth time).

```
File.new("testfile").ctime   
```

```
static VALUE
rb_file_ctime(VALUE obj)
{
    rb_io_t *fptr;
    struct stat st;

    GetOpenFile(obj, fptr);
    if (fstat(fptr->fd, &st) == -1) {
        rb_sys_fail_path(fptr->pathv);
    }
    return stat_ctime(&st);
}
```

flock(locking_constant) → 0 or false

click to toggle source

Locks or unlocks file `self` according to the given `locking_constant`, a bitwise OR of the values in the table below.

Not available on all platforms.

Returns `false` if `File::LOCK_NB` is specified and the operation would have blocked; otherwise returns `0`.

| Constant | Lock | Effect |—————–|————–|—————————————————————————————————————–| | `File::LOCK_EX` | Exclusive | Only one process may hold an exclusive lock for `self` at a time. | | `File::LOCK_NB` | Non-blocking | No blocking; may be combined with `File::LOCK_SH` or `File::LOCK_EX` using the bitwise OR operator `|`. | | `File::LOCK_SH` | Shared | Multiple processes may each hold a shared lock for `self` at the same time. | | `File::LOCK_UN` | Unlock | Remove an existing lock held by this process. |

Example:

```
File.open('counter', File::RDWR | File::CREAT, 0644) do |f|
  f.flock(File::LOCK_EX)
  value = f.read.to_i + 1
  f.rewind
  f.write("#{value}\n")
  f.flush
  f.truncate(f.pos)
end

File.open('counter', 'r') do |f|
  f.flock(File::LOCK_SH)
  f.read
end
```

```
static VALUE
rb_file_flock(VALUE obj, VALUE operation)
{
    rb_io_t *fptr;
    int op[2], op1;
    struct timeval time;

    op[1] = op1 = NUM2INT(operation);
    GetOpenFile(obj, fptr);
    op[0] = fptr->fd;

    if (fptr->mode & FMODE_WRITABLE) {
        rb_io_flush_raw(obj, 0);
    }
    while ((int)rb_io_blocking_region(fptr, rb_thread_flock, op) < 0) {
        int e = errno;
        switch (e) {
          case EAGAIN:
          case EACCES:
#if defined(EWOULDBLOCK) && EWOULDBLOCK != EAGAIN
          case EWOULDBLOCK:
#endif
            if (op1 & LOCK_NB) return Qfalse;

            time.tv_sec = 0;
            time.tv_usec = 100 * 1000;  /* 0.1 sec */
            rb_thread_wait_for(time);
            rb_io_check_closed(fptr);
            continue;

          case EINTR:
#if defined(ERESTART)
          case ERESTART:
#endif
            break;

          default:
            rb_syserr_fail_path(e, fptr->pathv);
        }
    }
    return INT2FIX(0);
}
```

lstat → stat

click to toggle source

Like `File#stat`, but does not follow the last symbolic link; instead, returns a `File::Stat` object for the link itself:

```
File.symlink('t.txt', 'symlink')
f = File.new('symlink')
f.stat.size  
f.lstat.size 
```

```
static VALUE
rb_file_lstat(VALUE obj)
{
#ifdef HAVE_LSTAT
    rb_io_t *fptr;
    struct stat st;
    VALUE path;

    GetOpenFile(obj, fptr);
    if (NIL_P(fptr->pathv)) return Qnil;
    path = rb_str_encode_ospath(fptr->pathv);
    if (lstat_without_gvl(RSTRING_PTR(path), &st) == -1) {
        rb_sys_fail_path(fptr->pathv);
    }
    return rb_stat_new(&st);
#else
    return rb_io_stat(obj);
#endif
}
```

mtime → time

click to toggle source

Returns the modification time for *file*.

```
File.new("testfile").mtime   
```

```
static VALUE
rb_file_mtime(VALUE obj)
{
    rb_io_t *fptr;
    struct stat st;

    GetOpenFile(obj, fptr);
    if (fstat(fptr->fd, &st) == -1) {
        rb_sys_fail_path(fptr->pathv);
    }
    return stat_mtime(&st);
}
```

size → integer

click to toggle source

Returns the size of *file* in bytes.

```
File.new("testfile").size   
```

```
static VALUE
file_size(VALUE self)
{
    return OFFT2NUM(rb_file_size(self));
}
```

truncate(integer) → 0

click to toggle source

Truncates *file* to at most *integer* bytes. The file must be opened for writing. Not available on all platforms.

```
f = File.new("out", "w")
f.syswrite("1234567890")   
f.truncate(5)              
f.close()                  
File.size("out")           
```

```
static VALUE
rb_file_truncate(VALUE obj, VALUE len)
{
    rb_io_t *fptr;
    struct ftruncate_arg fa;

    fa.pos = NUM2OFFT(len);
    GetOpenFile(obj, fptr);
    if (!(fptr->mode & FMODE_WRITABLE)) {
        rb_raise(rb_eIOError, "not opened for writing");
    }
    rb_io_flush_raw(obj, 0);
    fa.fd = fptr->fd;
    if ((int)rb_io_blocking_region(fptr, nogvl_ftruncate, &fa) < 0) {
        rb_sys_fail_path(fptr->pathv);
    }
    return INT2FIX(0);
}
```
