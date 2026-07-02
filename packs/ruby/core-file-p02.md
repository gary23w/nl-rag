---
title: "class File (part 2/3)"
source: https://ruby-doc.org/core/File.html
domain: ruby
license: Ruby-BSD / CC-BY-SA-4.0 (Rails guides)
tags: ruby, rails, rubygem
fetched: 2026-07-02
part: 2/3
---

## What’s Here¶ ↑

First, what’s elsewhere. Class File:

- Inherits from class IO, in particular, methods for creating, reading, and writing files
- Includes module `FileTest`, which provides dozens of additional methods.

Here, class File provides methods that are useful for:

- Creating
- Querying
- Settings
- Other

### Creating¶ ↑

- `::new`: Opens the file at the given path; returns the file.
- `::open`: Same as `::new`, but when given a block will yield the file to the block, and close the file upon exiting the block.
- `::link`: Creates a new name for an existing file using a hard link.
- `::mkfifo`: Returns the FIFO file created at the given path.
- `::symlink`: Creates a symbolic link for the given file path.

### Querying¶ ↑

*Paths*

- `::absolute_path`: Returns the absolute file path for the given path.
- `::absolute_path?`: Returns whether the given path is the absolute file path.
- `::basename`: Returns the last component of the given file path.
- `::dirname`: Returns all but the last component of the given file path.
- `::expand_path`: Returns the absolute file path for the given path, expanding `~` for a home directory.
- `::extname`: Returns the file extension for the given file path.
- `::fnmatch?` (aliased as `::fnmatch`): Returns whether the given file path matches the given pattern.
- `::join`: Joins path components into a single path string.
- `::path`: Returns the string representation of the given path.
- `::readlink`: Returns the path to the file at the given symbolic link.
- `::realdirpath`: Returns the real path for the given file path, where the last component need not exist.
- `::realpath`: Returns the real path for the given file path, where all components must exist.
- `::split`: Returns an array of two strings: the directory name and basename of the file at the given path.
- `path` (aliased as `to_path`): Returns the string representation of the given path.

*Times*

- `::atime`: Returns a `Time` for the most recent access to the given file.
- `::birthtime`: Returns a `Time` for the creation of the given file.
- `::ctime`: Returns a `Time` for the metadata change of the given file.
- `::mtime`: Returns a `Time` for the most recent data modification to the content of the given file.
- `atime`: Returns a `Time` for the most recent access to `self`.
- `birthtime`: Returns a `Time` the creation for `self`.
- `ctime`: Returns a `Time` for the metadata change of `self`.
- `mtime`: Returns a `Time` for the most recent data modification to the content of `self`.

*Types*

- `::blockdev?`: Returns whether the file at the given path is a block device.
- `::chardev?`: Returns whether the file at the given path is a character device.
- `::directory?`: Returns whether the file at the given path is a directory.
- `::executable?`: Returns whether the file at the given path is executable by the effective user and group of the current process.
- `::executable_real?`: Returns whether the file at the given path is executable by the real user and group of the current process.
- `::exist?`: Returns whether the file at the given path exists.
- `::file?`: Returns whether the file at the given path is a regular file.
- `::ftype`: Returns a string giving the type of the file at the given path.
- `::grpowned?`: Returns whether the effective group of the current process owns the file at the given path.
- `::identical?`: Returns whether the files at two given paths are identical.
- `::lstat`: Returns the `File::Stat` object for the last symbolic link in the given path.
- `::owned?`: Returns whether the effective user of the current process owns the file at the given path.
- `::pipe?`: Returns whether the file at the given path is a pipe.
- `::readable?`: Returns whether the file at the given path is readable by the effective user and group of the current process.
- `::readable_real?`: Returns whether the file at the given path is readable by the real user and group of the current process.
- `::setgid?`: Returns whether the setgid bit is set for the file at the given path.
- `::setuid?`: Returns whether the setuid bit is set for the file at the given path.
- `::socket?`: Returns whether the file at the given path is a socket.
- `::stat`: Returns the `File::Stat` object for the file at the given path.
- `::sticky?`: Returns whether the file at the given path has its sticky bit set.
- `::symlink?`: Returns whether the file at the given path is a symbolic link.
- `::umask`: Returns the umask value for the current process.
- `::world_readable?`: Returns whether the file at the given path is readable by others.
- `::world_writable?`: Returns whether the file at the given path is writable by others.
- `::writable?`: Returns whether the file at the given path is writable by the effective user and group of the current process.
- `::writable_real?`: Returns whether the file at the given path is writable by the real user and group of the current process.
- `lstat`: Returns the `File::Stat` object for the last symbolic link in the path for `self`.

*Contents*

- `::empty?` (aliased as `::zero?`): Returns whether the file at the given path exists and is empty.
- `::size`: Returns the size (bytes) of the file at the given path.
- `::size?`: Returns `nil` if there is no file at the given path, or if that file is empty; otherwise returns the file size (bytes).
- `size`: Returns the size (bytes) of `self`.

### Settings¶ ↑

- `::chmod`: Changes permissions of the file at the given path.
- `::chown`: Change ownership of the file at the given path.
- `::lchmod`: Changes permissions of the last symbolic link in the given path.
- `::lchown`: Change ownership of the last symbolic in the given path.
- `::lutime`: For each given file path, sets the access time and modification time of the last symbolic link in the path.
- `::rename`: Moves the file at one given path to another given path.
- `::utime`: Sets the access time and modification time of each file at the given paths.
- `flock`: Locks or unlocks `self`.

### Other¶ ↑

- `::truncate`: Truncates the file at the given file path to the given size.
- `::unlink` (aliased as `::delete`): Deletes the file for each given file path.
- `truncate`: Truncates `self` to the given size.

### Constants

**ALT_SEPARATOR platform specific alternative separator PATH_SEPARATOR path list separator SEPARATOR separates directory parts in path Separator separates directory parts in path**

### Public Class Methods

absolute_path(file_name [, dir_string] ) → abs_file_name

click to toggle source

Converts a pathname to an absolute pathname. Relative paths are referenced from the current working directory of the process unless *dir_string* is given, in which case it will be used as the starting point. If the given pathname starts with a “`~`” it is NOT expanded, it is treated as a normal directory name.

```
File.absolute_path("~oracle/bin")       
```

```
static VALUE
s_absolute_path(int c, const VALUE * v, VALUE _)
{
    return rb_file_s_absolute_path(c, v);
}
```

absolute_path?(file_name) → true or false

click to toggle source

Returns `true` if `file_name` is an absolute path, and `false` otherwise.

```
File.absolute_path?("c:/foo")     
```

```
static VALUE
s_absolute_path_p(VALUE klass, VALUE fname)
{
    VALUE path = rb_get_path(fname);

    if (!rb_is_absolute_path(RSTRING_PTR(path))) return Qfalse;
    return Qtrue;
}
```

atime(file_name) → time

click to toggle source

Returns the last access time for the named file as a `Time` object.

*file_name* can be an `IO` object.

```
File.atime("testfile")   
```

```
static VALUE
rb_file_s_atime(VALUE klass, VALUE fname)
{
    struct stat st;

    if (rb_stat(fname, &st) < 0) {
        int e = errno;
        FilePathValue(fname);
        rb_syserr_fail_path(e, fname);
    }
    return stat_atime(&st);
}
```

basename(file_name [, suffix] ) → base_name

click to toggle source

Returns the last component of the filename given in *file_name* (after first stripping trailing separators), which can be formed using both `File::SEPARATOR` and `File::ALT_SEPARATOR` as the separator when `File::ALT_SEPARATOR` is not `nil`. If *suffix* is given and present at the end of *file_name*, it is removed. If *suffix* is “.*”, any extension will be removed.

```
File.basename("/home/gumby/work/ruby.rb")          
File.basename("/home/gumby/work/ruby.rb", ".rb")   
File.basename("/home/gumby/work/ruby.rb", ".*")    
```

```
static VALUE
rb_file_s_basename(int argc, VALUE *argv, VALUE _)
{
    VALUE fname, fext, basename;
    const char *name, *p;
    long f, n;
    rb_encoding *enc;

    fext = Qnil;
    if (rb_check_arity(argc, 1, 2) == 2) {
        fext = argv[1];
        StringValue(fext);
        enc = check_path_encoding(fext);
    }
    fname = argv[0];
    FilePathStringValue(fname);
    if (NIL_P(fext) || !(enc = rb_enc_compatible(fname, fext))) {
        enc = rb_enc_get(fname);
        fext = Qnil;
    }
    if ((n = RSTRING_LEN(fname)) == 0 || !*(name = RSTRING_PTR(fname)))
        return rb_str_new_shared(fname);

    p = ruby_enc_find_basename(name, &f, &n, enc);
    if (n >= 0) {
        if (NIL_P(fext)) {
            f = n;
        }
        else {
            const char *fp;
            fp = StringValueCStr(fext);
            if (!(f = rmext(p, f, n, fp, RSTRING_LEN(fext), enc))) {
                f = n;
            }
            RB_GC_GUARD(fext);
        }
        if (f == RSTRING_LEN(fname)) return rb_str_new_shared(fname);
    }

    basename = rb_str_new(p, f);
    rb_enc_copy(basename, fname);
    return basename;
}
```

birthtime(file_name) → time

click to toggle source

Returns the birth time for the named file.

*file_name* can be an `IO` object.

```
File.birthtime("testfile")   
```

If the platform doesn’t have birthtime, raises `NotImplementedError`.

```
VALUE
rb_file_s_birthtime(VALUE klass, VALUE fname)
{
    statx_data st;

    if (rb_statx(fname, &st, STATX_BTIME) < 0) {
        int e = errno;
        FilePathValue(fname);
        rb_syserr_fail_path(e, fname);
    }
    return statx_birthtime(&st, fname);
}
```

blockdev?(filepath) → true or false

click to toggle source

Returns `true` if `filepath` points to a block device, `false` otherwise:

```
File.blockdev?('/dev/sda1')       
File.blockdev?(File.new('t.tmp')) 
```

```
static VALUE
rb_file_blockdev_p(VALUE obj, VALUE fname)
{
#ifndef S_ISBLK
#   ifdef S_IFBLK
#       define S_ISBLK(m) (((m) & S_IFMT) == S_IFBLK)
#   else
#       define S_ISBLK(m) (0)  /* anytime false */
#   endif
#endif

#ifdef S_ISBLK
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    if (S_ISBLK(st.st_mode)) return Qtrue;

#endif
    return Qfalse;
}
```

chardev?(filepath) → true or false

click to toggle source

Returns `true` if `filepath` points to a character device, `false` otherwise.

```
File.chardev?($stdin)     
File.chardev?('t.txt')     
```

```
static VALUE
rb_file_chardev_p(VALUE obj, VALUE fname)
{
#ifndef S_ISCHR
#   define S_ISCHR(m) (((m) & S_IFMT) == S_IFCHR)
#endif

    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    if (S_ISCHR(st.st_mode)) return Qtrue;

    return Qfalse;
}
```

chmod(mode_int, file_name, ... ) → integer

click to toggle source

Changes permission bits on the named file(s) to the bit pattern represented by *mode_int*. Actual effects are operating system dependent (see the beginning of this section). On Unix systems, see `chmod(2)` for details. Returns the number of files processed.

```
File.chmod(0644, "testfile", "out")   
```

```
static VALUE
rb_file_s_chmod(int argc, VALUE *argv, VALUE _)
{
    mode_t mode;

    apply2args(1);
    mode = NUM2MODET(*argv++);

    return apply2files(chmod_internal, argc, argv, &mode);
}
```

chown(owner_int, group_int, file_name, ...) → integer

click to toggle source

Changes the owner and group of the named file(s) to the given numeric owner and group id’s. Only a process with superuser privileges may change the owner of a file. The current owner of a file may change the file’s group to any group to which the owner belongs. A `nil` or -1 owner or group id is ignored. Returns the number of files processed.

```
File.chown(nil, 100, "testfile")
```

```
static VALUE
rb_file_s_chown(int argc, VALUE *argv, VALUE _)
{
    struct chown_args arg;

    apply2args(2);
    arg.owner = to_uid(*argv++);
    arg.group = to_gid(*argv++);

    return apply2files(chown_internal, argc, argv, &arg);
}
```

ctime(file_name) → time

click to toggle source

Returns the change time for the named file (the time at which directory information about the file was changed, not the file itself).

*file_name* can be an `IO` object.

Note that on Windows (NTFS), returns creation time (birth time).

```
File.ctime("testfile")   
```

```
static VALUE
rb_file_s_ctime(VALUE klass, VALUE fname)
{
    struct stat st;

    if (rb_stat(fname, &st) < 0) {
        int e = errno;
        FilePathValue(fname);
        rb_syserr_fail_path(e, fname);
    }
    return stat_ctime(&st);
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

directory?(path) → true or false

click to toggle source

With string `object` given, returns `true` if `path` is a string path leading to a directory, or to a symbolic link to a directory; `false` otherwise:

```
File.directory?('.')              
File.directory?('foo')            
File.symlink('.', 'dirlink')      
File.directory?('dirlink')        
File.symlink('t,txt', 'filelink') 
File.directory?('filelink')       
```

Argument `path` can be an `IO` object.

```
VALUE
rb_file_directory_p(VALUE obj, VALUE fname)
{
#ifndef S_ISDIR
#   define S_ISDIR(m) (((m) & S_IFMT) == S_IFDIR)
#endif

    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    if (S_ISDIR(st.st_mode)) return Qtrue;
    return Qfalse;
}
```

dirname(file_name, level = 1) → dir_name

click to toggle source

Returns all components of the filename given in *file_name* except the last one (after first stripping trailing separators). The filename can be formed using both `File::SEPARATOR` and `File::ALT_SEPARATOR` as the separator when `File::ALT_SEPARATOR` is not `nil`.

```
File.dirname("/home/gumby/work/ruby.rb")   
```

If `level` is given, removes the last `level` components, not only one.

```
File.dirname("/home/gumby/work/ruby.rb", 2) 
File.dirname("/home/gumby/work/ruby.rb", 4) 
```

```
static VALUE
rb_file_s_dirname(int argc, VALUE *argv, VALUE klass)
{
    int n = 1;
    if ((argc = rb_check_arity(argc, 1, 2)) > 1) {
        n = NUM2INT(argv[1]);
    }
    return rb_file_dirname_n(argv[0], n);
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

executable?(file_name) → true or false

click to toggle source

Returns `true` if the named file is executable by the effective user and group id of this process. See eaccess(3).

Windows does not support execute permissions separately from read permissions. On Windows, a file is only considered executable if it ends in .bat, .cmd, .com, or .exe.

Note that some OS-level security features may cause this to return true even though the file is not executable by the effective user/group.

```
static VALUE
rb_file_executable_p(VALUE obj, VALUE fname)
{
    return RBOOL(rb_eaccess(fname, X_OK) >= 0);
}
```

executable_real?(file_name) → true or false

click to toggle source

Returns `true` if the named file is executable by the real user and group id of this process. See access(3).

Windows does not support execute permissions separately from read permissions. On Windows, a file is only considered executable if it ends in .bat, .cmd, .com, or .exe.

Note that some OS-level security features may cause this to return true even though the file is not executable by the real user/group.

```
static VALUE
rb_file_executable_real_p(VALUE obj, VALUE fname)
{
    return RBOOL(rb_access(fname, X_OK) >= 0);
}
```

exist?(file_name) → true or false

click to toggle source

Return `true` if the named file exists.

*file_name* can be an `IO` object.

“file exists” means that stat() or fstat() system call is successful.

```
static VALUE
rb_file_exist_p(VALUE obj, VALUE fname)
{
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    return Qtrue;
}
```

expand_path(file_name [, dir_string] ) → abs_file_name

click to toggle source

Converts a pathname to an absolute pathname. Relative paths are referenced from the current working directory of the process unless `dir_string` is given, in which case it will be used as the starting point. The given pathname may start with a “`~`”, which expands to the process owner’s home directory (the environment variable `HOME` must be set correctly). “`~`*user*” expands to the named user’s home directory.

```
File.expand_path("~oracle/bin")           
```

A simple example of using `dir_string` is as follows.

```
File.expand_path("ruby", "/usr/bin")      
```

A more complex example which also resolves parent directory is as follows. Suppose we are in bin/mygem and want the absolute path of lib/mygem.rb.

```
File.expand_path("../../lib/mygem.rb", __FILE__)
```

So first it resolves the parent of __FILE__, that is bin/, then go to the parent, the root of the project and appends `lib/mygem.rb`.

```
static VALUE
s_expand_path(int c, const VALUE * v, VALUE _)
{
    return rb_file_s_expand_path(c, v);
}
```

extname(path) → string

click to toggle source

Returns the extension (the portion of file name in `path` starting from the last period).

If `path` is a dotfile, or starts with a period, then the starting dot is not dealt with the start of the extension.

An empty string will also be returned when the period is the last character in `path`.

On Windows, trailing dots are truncated.

```
File.extname("test.rb")         
File.extname("a/b/d/test.rb")   
File.extname(".a/b/d/test.rb")  
File.extname("foo.")            
File.extname("foo.")            
File.extname("test")            
File.extname(".profile")        
File.extname(".profile.sh")     
```

```
static VALUE
rb_file_s_extname(VALUE klass, VALUE fname)
{
    const char *name, *e;
    long len;
    VALUE extname;

    FilePathStringValue(fname);
    name = StringValueCStr(fname);
    len = RSTRING_LEN(fname);
    e = ruby_enc_find_extname(name, &len, rb_enc_get(fname));
    if (len < 1)
        return rb_str_new(0, 0);
    extname = rb_str_subseq(fname, e - name, len); /* keep the dot, too! */
    return extname;
}
```

file?(file) → true or false

click to toggle source

Returns `true` if the named `file` exists and is a regular file.

`file` can be an `IO` object.

If the `file` argument is a symbolic link, it will resolve the symbolic link and use the file referenced by the link.

```
static VALUE
rb_file_file_p(VALUE obj, VALUE fname)
{
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    return RBOOL(S_ISREG(st.st_mode));
}
```

fnmatch( pattern, path, [flags] ) → (true or false)

click to toggle source

Returns true if `path` matches against `pattern`. The pattern is not a regular expression; instead it follows rules similar to shell filename globbing. It may contain the following metacharacters:

**`*` Matches any file. Can be restricted by other values in the glob. Equivalent to `/.*/x` in regexp. `*` Matches all regular files `c*` Matches all files beginning with `c` `*c` Matches all files ending with `c` `*c*` Matches all files that have `c` in them (including at the beginning or end). To match hidden files (that start with a `.`) set the File::FNM_DOTMATCH flag.**

**`**` Matches directories recursively or files expansively.**

**`?` Matches any one character. Equivalent to `/.{1}/` in regexp.**

**`[set]` Matches any one character in `set`. Behaves exactly like character sets in `Regexp`, including set negation (`[^a-z]`).**

**`\` Escapes the next metacharacter.**

**`{a,b}` Matches pattern a and pattern b if File::FNM_EXTGLOB flag is enabled. Behaves like a `Regexp` union (`(?:a|b)`).**

`flags` is a bitwise OR of the `FNM_XXX` constants. The same glob pattern and flags are used by `Dir::glob`.

Examples:

```
File.fnmatch('cat',       'cat')        
File.fnmatch('cat',       'category')   

File.fnmatch('c{at,ub}s', 'cats')                    
File.fnmatch('c{at,ub}s', 'cats', File::FNM_EXTGLOB) 

File.fnmatch('c?t',     'cat')          
File.fnmatch('c??t',    'cat')          
File.fnmatch('c*',      'cats')         
File.fnmatch('c*t',     'c/a/b/t')      
File.fnmatch('ca[a-z]', 'cat')          
File.fnmatch('ca[^t]',  'cat')          

File.fnmatch('cat', 'CAT')                     
File.fnmatch('cat', 'CAT', File::FNM_CASEFOLD) 
File.fnmatch('cat', 'CAT', File::FNM_SYSCASE)  

File.fnmatch('?',   '/', File::FNM_PATHNAME)  
File.fnmatch('*',   '/', File::FNM_PATHNAME)  
File.fnmatch('[/]', '/', File::FNM_PATHNAME)  

File.fnmatch('\?',   '?')                       
File.fnmatch('\a',   'a')                       
File.fnmatch('\a',   '\a', File::FNM_NOESCAPE)  
File.fnmatch('[\?]', '?')                       

File.fnmatch('*',   '.profile')                      
File.fnmatch('*',   '.profile', File::FNM_DOTMATCH)  
File.fnmatch('.*',  '.profile')                      

File.fnmatch('**/*.rb', 'main.rb')                  
File.fnmatch('**/*.rb', './main.rb')                
File.fnmatch('**/*.rb', 'lib/song.rb')              
File.fnmatch('**.rb', 'main.rb')                    
File.fnmatch('**.rb', './main.rb')                  
File.fnmatch('**.rb', 'lib/song.rb')                
File.fnmatch('*',     'dave/.profile')              

File.fnmatch('**/foo', 'a/b/c/foo', File::FNM_PATHNAME)     
File.fnmatch('**/foo', '/a/b/c/foo', File::FNM_PATHNAME)    
File.fnmatch('**/foo', 'c:/a/b/c/foo', File::FNM_PATHNAME)  
File.fnmatch('**/foo', 'a/.b/c/foo', File::FNM_PATHNAME)    
File.fnmatch('**/foo', 'a/.b/c/foo', File::FNM_PATHNAME | File::FNM_DOTMATCH) 
```

```
def fnmatch(pattern, path, flags = 0)
end
```

Also aliased as:

fnmatch?

fnmatch?

(pattern, path, flags = 0)

Alias for:

fnmatch

ftype(file_name) → string

click to toggle source

Identifies the type of the named file; the return string is one of “`file`”, “`directory`”, “`characterSpecial`”, “`blockSpecial`”, “`fifo`”, “`link`”, “`socket`”, or “`unknown`”.

```
File.ftype("testfile")            
File.ftype("/dev/tty")            
File.ftype("/tmp/.X11-unix/X0")   
```

```
static VALUE
rb_file_s_ftype(VALUE klass, VALUE fname)
{
    struct stat st;

    FilePathValue(fname);
    fname = rb_str_encode_ospath(fname);
    if (lstat_without_gvl(StringValueCStr(fname), &st) == -1) {
        rb_sys_fail_path(fname);
    }

    return rb_file_ftype(&st);
}
```

grpowned?(file_name) → true or false

click to toggle source

Returns `true` if the named file exists and the effective group id of the calling process is the owner of the file. Returns `false` on Windows.

*file_name* can be an `IO` object.

```
static VALUE
rb_file_grpowned_p(VALUE obj, VALUE fname)
{
#ifndef _WIN32
    struct stat st;

    if (rb_stat(fname, &st) < 0) return Qfalse;
    if (rb_group_member(st.st_gid)) return Qtrue;
#endif
    return Qfalse;
}
```

identical?(file_1, file_2) → true or false

click to toggle source

Returns `true` if the named files are identical.

*file_1* and *file_2* can be an `IO` object.

```
open("a", "w") {}
p File.identical?("a", "a")      
p File.identical?("a", "./a")    
File.link("a", "b")
p File.identical?("a", "b")      
File.symlink("a", "c")
p File.identical?("a", "c")      
open("d", "w") {}
p File.identical?("a", "d")      
```

```
static VALUE
rb_file_identical_p(VALUE obj, VALUE fname1, VALUE fname2)
{
#ifndef _WIN32
    struct stat st1, st2;

    if (rb_stat(fname1, &st1) < 0) return Qfalse;
    if (rb_stat(fname2, &st2) < 0) return Qfalse;
    if (st1.st_dev != st2.st_dev) return Qfalse;
    if (st1.st_ino != st2.st_ino) return Qfalse;
    return Qtrue;
#else
    extern VALUE rb_w32_file_identical_p(VALUE, VALUE);
    return rb_w32_file_identical_p(fname1, fname2);
#endif
}
```

join(string, ...) → string

click to toggle source

Returns a new string formed by joining the strings using `"/"`.

```
File.join("usr", "mail", "gumby")   
```

```
static VALUE
rb_file_s_join(VALUE klass, VALUE args)
{
    return rb_file_join(args);
}
```

lchmod(mode_int, file_name, ...) → integer

click to toggle source

Equivalent to `File::chmod`, but does not follow symbolic links (so it will change the permissions associated with the link, not the file referenced by the link). Often not available.

```
static VALUE
rb_file_s_lchmod(int argc, VALUE *argv, VALUE _)
{
    mode_t mode;

    apply2args(1);
    mode = NUM2MODET(*argv++);

    return apply2files(lchmod_internal, argc, argv, &mode);
}
```

lchown(owner_int, group_int, file_name,..) → integer

click to toggle source

Equivalent to `File::chown`, but does not follow symbolic links (so it will change the owner associated with the link, not the file referenced by the link). Often not available. Returns number of files in the argument list.

```
static VALUE
rb_file_s_lchown(int argc, VALUE *argv, VALUE _)
{
    struct chown_args arg;

    apply2args(2);
    arg.owner = to_uid(*argv++);
    arg.group = to_gid(*argv++);

    return apply2files(lchown_internal, argc, argv, &arg);
}
```

link(old_name, new_name) → 0

click to toggle source

Creates a new name for an existing file using a hard link. Will not overwrite *new_name* if it already exists (raising a subclass of `SystemCallError`). Not available on all platforms.

```
File.link("testfile", ".testfile")   
IO.readlines(".testfile")[0]         
```

```
static VALUE
rb_file_s_link(VALUE klass, VALUE from, VALUE to)
{
    FilePathValue(from);
    FilePathValue(to);
    from = rb_str_encode_ospath(from);
    to = rb_str_encode_ospath(to);

    if (link(StringValueCStr(from), StringValueCStr(to)) < 0) {
        sys_fail2(from, to);
    }
    return INT2FIX(0);
}
```

lstat(filepath) → stat

click to toggle source

Like `File::stat`, but does not follow the last symbolic link; instead, returns a `File::Stat` object for the link itself.

```
File.symlink('t.txt', 'symlink')
File.stat('symlink').size  
File.lstat('symlink').size 
```

```
static VALUE
rb_file_s_lstat(VALUE klass, VALUE fname)
{
#ifdef HAVE_LSTAT
    struct stat st;

    FilePathValue(fname);
    fname = rb_str_encode_ospath(fname);
    if (lstat_without_gvl(StringValueCStr(fname), &st) == -1) {
        rb_sys_fail_path(fname);
    }
    return rb_stat_new(&st);
#else
    return rb_file_s_stat(klass, fname);
#endif
}
```

lutime(atime, mtime, file_name, ...) → integer

click to toggle source

Sets the access and modification times of each named file to the first two arguments. If a file is a symlink, this method acts upon the link itself as opposed to its referent; for the inverse behavior, see `File.utime`. Returns the number of file names in the argument list.

```
static VALUE
rb_file_s_lutime(int argc, VALUE *argv, VALUE _)
{
    return utime_internal_i(argc, argv, TRUE);
}
```

mkfifo(file_name, mode=0666) → 0

click to toggle source

Creates a FIFO special file with name *file_name*. *mode* specifies the FIFO’s permissions. It is modified by the process’s umask in the usual way: the permissions of the created file are (mode & ~umask).

```
static VALUE
rb_file_s_mkfifo(int argc, VALUE *argv, VALUE _)
{
    VALUE path;
    struct mkfifo_arg ma;

    ma.mode = 0666;
    rb_check_arity(argc, 1, 2);
    if (argc > 1) {
        ma.mode = NUM2MODET(argv[1]);
    }
    path = argv[0];
    FilePathValue(path);
    path = rb_str_encode_ospath(path);
    ma.path = RSTRING_PTR(path);
    if (IO_WITHOUT_GVL(nogvl_mkfifo, &ma)) {
        rb_sys_fail_path(path);
    }
    return INT2FIX(0);
}
```

mtime(file_name) → time

click to toggle source

Returns the modification time for the named file as a `Time` object.

*file_name* can be an `IO` object.

```
File.mtime("testfile")   
```

```
static VALUE
rb_file_s_mtime(VALUE klass, VALUE fname)
{
    struct stat st;

    if (rb_stat(fname, &st) < 0) {
        int e = errno;
        FilePathValue(fname);
        rb_syserr_fail_path(e, fname);
    }
    return stat_mtime(&st);
}
```

new(path, mode = 'r', perm = 0666, **opts) → file

click to toggle source
