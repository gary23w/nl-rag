---
title: "Block (data storage)"
source: https://en.wikipedia.org/wiki/Block_(data_storage)
domain: sqrt-block-buckets
license: CC-BY-SA-4.0
tags: square root decomposition, block decomposition, range query buckets, sqrt tree
fetched: 2026-07-02
---

# Block (data storage)

In computing (specifically data transmission and data storage), a **block**, sometimes called a **physical record**, is a sequence of bytes or bits, usually containing some whole number of records, having a fixed length; a *block size*. Data thus structured are said to be *blocked*. The process of putting data into blocks is called *blocking*, while *deblocking* is the process of extracting data from blocks. Blocked data is normally stored in a data buffer, and read or written a whole block at a time. Blocking reduces the overhead and speeds up the handling of the data stream. For some devices, such as magnetic tape and CKD disk devices, blocking reduces the amount of external storage required for the data. Blocking is almost universally employed when storing data to 9-track magnetic tape, NAND flash memory, and rotating media such as floppy disks, hard disks, and optical discs.

Most file systems are based on a block device, which is a level of abstraction for the hardware responsible for storing and retrieving specified blocks of data, though the block size in file systems may be a multiple of the physical block size. This leads to space inefficiency due to internal fragmentation, since file lengths are often not integer multiples of block size, and thus the last block of a file may remain partially empty. This will create slack space. Some newer file systems, such as Btrfs and FreeBSD UFS2, attempt to solve this through techniques called block suballocation and tail merging. Other file systems such as ZFS support variable block sizes.

Block storage is normally abstracted by a file system or database management system (DBMS) for use by applications and end users. The physical or logical volumes accessed via *block I/O* may be devices internal to a server, directly attached via SCSI or Fibre Channel, or distant devices accessed via a storage area network (SAN) using a protocol such as iSCSI, or AoE. DBMSes often use their own block I/O for improved performance and recoverability as compared to layering the DBMS on top of a file system.

On Linux the default block size for most file systems is 4096 bytes. The stat command part of GNU Core Utilities can be used to check the block size.

## In languages

### C++

In C++, a block can be read using `std::ifstream` (input file stream).

```mw
import std;

using std::array;
using std::byte;
using std::ifstream;
using std::ios;

constexpr size_t BLOCK_SIZE = 4096;

try {
    ifstream file("example.bin", ios::binary);
    file.exceptions(ios::failbit | ios::badbit);
    array<byte, BLOCK_SIZE> buf;
    file.read(reinterpret_cast<char*>(buf.data()), BLOCK_SIZE);
} catch (const ios::failure& e) {
    std::println(stderr, "I/O error: {}", e.what());
}
```

### C

In C#, a block can be read with the `FileStream` class.

```mw
using System.IO;

static const int BLOCK_SIZE = 4096;

using (FileStream stream = File.Open("example.bin", FileMode.Open))
{
    byte[] block = new byte[BLOCK_SIZE];
    await stream.ReadAsync(block, 0, BLOCK_SIZE);
}
```

### Java

In Java, a block can be read using `java.io.FileInputStream`.

```mw
import java.io.FileInputStream;
import java.io.IOException;

static final int BLOCK_SIZE = 4096;

try (FileInputStream file = new FileInputStream("example.bin")) {
    byte[] buf = new byte[BLOCK_SIZE];
    file.read(buf);
} catch (IOException e) {
    e.printStackTrace();
}
```

### Python

In Python, a block can be read with the `read` method of whatever is implementing `io.IOBase`.

```mw
BLOCK_SIZE: int = 4096

with open("example.bin", "rb") as file:
    # file is of type io.BufferedReader
    block: bytes = file.read(BLOCK_SIZE)
```

### Rust

In Rust, a block can be read with the `read_exact` method of `std::fs::File`.

```mw
use std::fs::File;

const BLOCK_SIZE: usize = 4096;

if let Ok(mut file) = File::open("example.bin")
{
    let mut buf = [0u8; BLOCK_SIZE];
    file.read_exact(&mut buf);
}
```
