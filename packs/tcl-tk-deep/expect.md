---
title: "Expect"
source: https://en.wikipedia.org/wiki/Expect
domain: tcl-tk-deep
license: CC-BY-SA-4.0
tags: tcl language, tk toolkit, john ousterhout, scripting language, glue language
fetched: 2026-07-02
---

# Expect

**Expect** is an extension to the Tcl scripting language written by Don Libes. The program automates interactions with programs that expose a text terminal interface. Expect, originally written in 1990 for the Unix platform, has since become available for Microsoft Windows and other systems.

## Basics

Expect is used to automate control of interactive applications such as Telnet, FTP, passwd, fsck, rlogin, tip, SSH, and others. Expect uses pseudo terminals (Unix) or emulates a console (Windows), starts the target program, and then communicates with it, just as a human would, via the terminal or console interface. Tk, another Tcl extension, can be used to provide a GUI.

## Usage

Expect serves as a "glue" to link existing utilities together. The general idea is to figure out how to make Expect use the system's existing tools rather than figure out how to solve a problem inside of Expect.

A key usage of Expect involves commercial software products. Many of these products provide some type of command-line interface, but these usually lack the power needed to write scripts. They were built to service the users administering the product, but the company often does not spend the resources to fully implement a robust scripting language. An Expect script can spawn a shell, look up environmental variables, perform some Unix commands to retrieve more information, and then enter into the product's command-line interface armed with the necessary information to achieve the user's goal. After retrieving information by interacting with the product via its command-line interface, the script can make intelligent decisions about what action to take, if any.

Every time an Expect operation is completed, the results are stored in a local variable called $expect_out. This allows the script to harvest information to feedback to the user, and it also allows conditional behavior of what to send next based on the circumstances.

A common use of Expect is to set up a testing suite for programs, utilities or embedded systems. DejaGnu is a testing suite written using Expect for use in testing. It has been used for testing GCC and remote targets such as embedded development.

Expect script can be automated using a tool called 'autoexpect'. This tool observes your actions and generates an Expect script using heuristics. Though generated code may be large and somewhat cryptic, one can always tweak the generated script to get the exact code.

```mw
# Assume $remote_server, $my_user_id, $my_password, and 
# $my_command were read earlier in the script.

# Open a Telnet session to a remote server, and wait 
# for a username prompt.
spawn telnet $remote_server
expect "username:"

# Send the username, and then wait for a password prompt.
send "$my_user_id\r"
expect "password:"

# Send the password, and then wait for a shell prompt.
send "$my_password\r"
expect "%"

# Send the prebuilt command, and then wait 
# for another shell prompt.
send "$my_command\r"
expect "%"

# Capture the results of the command into a variable. This 
# can be displayed, or written to disk.
set results $expect_out(buffer)

# Exit the Telnet session, and wait for a special 
# end-of-file character.
send "exit\r"
expect eof
```

Another example is a script that automates FTP:

```mw
# Set timeout parameter to a proper value.
# For example, the file size is indeed big and the network 
# speed is really one problem, you'd better set this 
# parameter a value.
set timeout -1

# Open an FTP session to a remote server, and 
# wait for a username prompt.
spawn ftp $remote_server
expect "username:"

# Send the username, and then wait for a password prompt.
send "$my_user_id\r"
expect "password:"

# Send the password, and then wait for an 'ftp' prompt.
send "$my_password\r"
expect "ftp>"

# Switch to binary mode, and then wait for an 'ftp' prompt.
send "bin\r"
expect "ftp>"

# Turn off prompting.
send "prompt\r"
expect "ftp>"

# Get all the files
send "mget *\r"
expect "ftp>"

# Exit the FTP session, and wait for a special 
# end-of-file character.
send "bye\r"
expect eof
```

Below is an example that automates SFTP (with a password):

```mw
#!/usr/bin/env expect -f

# Procedure to attempt connecting; result 0 if OK, 1 otherwise
proc connect {passw} {
  expect {
    "Password:" {
      send "$passw\r"
        expect {
          "sftp*" {
            return 0
          }
        }
    }
  }
  # Timed out
  return 1
}

# Read the input parameters
set user [lindex $argv 0]
set passw [lindex $argv 1]
set host [lindex $argv 2]
set location [lindex $argv 3]
set file1 [lindex $argv 4]
set file2 [lindex $argv 5]

#puts "Argument data:\n";
#puts "user: $user";
#puts "passw: $passw";
#puts "host: $host";
#puts "location: $location";
#puts "file1: $file1";
#puts "file2: $file2";

# Check if all were provided
if { $user == "" || $passw == "" || $host == "" || $location == "" || $file1 == "" || $file2 == "" }  {
  puts "Usage: <user> <passw> <host> <location> <file1 to send> <file2 to send>\n"
  exit 1
}

# Sftp to specified host and send the files
spawn sftp $user@$host

set rez [connect $passw]
if { $rez == 0 } {
  send "cd $location\r"
  set timeout -1
  send "put $file2\r"
  send "put $file1\r"
  send "ls -l\r"
  send "quit\r"
  expect eof
  exit 0
}
puts "\nError connecting to server: $host, user: $user and password: $passw!\n"
exit 1
```

Using passwords as command-line arguments, like in this example, is a huge security hole, as any other user on the machine can read this password by running "ps". You can, however, add code that will prompt you for your password rather than giving your password as an argument. This should be more secure. See the example below.

```mw
stty -echo
send_user -- "Enter Password: "
expect_user -re "(.*)\n"
send_user "\n"
stty echo
set PASS $expect_out(1,string)
```

Another example of automated SSH login to a user machine:

```mw
# Timeout is a predefined variable in Expect which by 
# default is set to 10 seconds.
# spawn_id is another predefined variable in Expect.
# It is a good practice to close spawn_id handle 
# created by spawn command.
set timeout 60
spawn ssh $user@machine
while {1} {
  expect {

    eof                          {break}
    "The authenticity of host"   {send "yes\r"}
    "password:"                  {send "$password\r"}
    "*\]"                        {send "exit\r"}
  }
}
wait
close $spawn_id
```

## Alternatives

Various projects implement Expect-like functionality in other languages, such as C#, Java, Scala, Groovy, Perl, Python, Ruby, Shell and Go. These are generally not exact clones of the original Expect, but the concepts tend to be very similar.

### C

- Expect.NET — Expect functionality for C# (.NET)
- DotNetExpect — An Expect-inspired console automation library for .NET

### Erlang

- lux - test automation framework with Expect style execution commands.

### Go

- GoExpect - Expect-like package for the Go language
- go-expect - an Expect-like Go language library to automate control of terminal or console based programs.

### Groovy

- expect4groovy  - a Groovy DSL implementation of Expect tool.

### Java

- ExpectIt — a pure Java 1.6+ implementation of the Expect tool. It is designed to be simple, easy to use and extensible.
- expect4j — an attempt at a Java clone of the original Expect
- ExpectJ — a Java implementation of the Unix expect utility
- Expect-for-Java — pure Java implementation of the Expect tool
- expect4java  - a Java implementation of the Expect tool, but supports nested closures. There is also wrapper for Groovy language DSL.

### Perl

- Expect.pm — Perl module (newest version at metacpan.org)

### Python

- Pexpect — Python module for controlling interactive programs in a pseudo-terminal
- winpexpect — port of pexpect to the Windows platform
- paramiko-expect — A Python expect-like extension for the Paramiko SSH library which also supports tailing logs.

### Ruby

- RExpect — a drop in replacement for the expect.rb module in the standard library.
- Expect4r — Interact with Cisco IOS, IOS-XR, and Juniper JUNOS CLI

### Rust

- rexpect - pexpect-like package for the Rust language.

### Scala

- scala-expect — a Scala implementation of a very small subset of the Expect tool.

### Shell

- Empty — expect-like utility to run interactive commands in the Unix shell-scripts
- sexpect — Expect for shells. It's implemented in the client/server model which also supports attach/detach (like GNU screen).
