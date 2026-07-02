---
title: "Linux Unified Key Setup"
source: https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup
domain: encryption-at-rest
license: CC-BY-SA-4.0
tags: encryption at rest, full disk encryption, data at rest, linux unified key setup, database encryption
fetched: 2026-07-02
---

# Linux Unified Key Setup

The **Linux Unified Key Setup** (**LUKS**) is a disk encryption specification created by Clemens Fruhwirth in 2004 and originally intended for Linux.

LUKS implements a platform-independent standard on-disk format for use in various tools. This facilitates compatibility and interoperability among different programs and operating systems, and assures that they all implement password management in a secure and documented manner.

## Description

LUKS is used to encrypt a block device. The contents of the encrypted device are arbitrary, and therefore any filesystem can be encrypted, including swap partitions. There is an unencrypted header at the beginning of an encrypted volume, which allows up to 8 (LUKS1) or 32 (LUKS2) encryption keys to be stored along with encryption parameters such as cipher type and key size.

The presence of this header is a major difference between LUKS and dm-crypt, since the header allows multiple different passphrases to be used, with the ability to change and remove them. If the header is lost or corrupted, the device will no longer be decryptable.

Encryption is done with a multi-layer approach. First, the block device is encrypted using a *master key.* This master key is encrypted with each active *user key*. User keys are derived from passphrases, FIDO2 security keys, TPMs or smart cards. The multi-layer approach allows users to change their passphrase without re-encrypting the whole block device. Key slots can contain information to verify user passphrases or other types of keys.

There are two versions of LUKS, with LUKS2 featuring resilience to header corruption, and using the Argon2 key derivation function by default, whereas LUKS1 uses PBKDF2. Conversion between both versions of LUKS is possible in certain situations, but some features may not be available with LUKS1 such as Argon2. LUKS2 uses JSON as a metadata format.

Available cryptographic algorithms depend on individual kernel support of the host. Libgcrypt can be used as a backend for hashing, which supports all of its algorithms. It is up to the operating system vendor to choose the default algorithm. LUKS1 makes use of an anti-forensics technique called AFsplitter, allowing for secure data erasure and protection.

### LUKS with LVM

Logical Volume Management can be used alongside LUKS.

**LVM on LUKS**

When LVM is used on an unlocked LUKS container, all underlying partitions (which are LVM logical volumes) can be encrypted with a single key. This is akin to splitting a LUKS container into multiple partitions. The LVM structure is not visible until the disk is decrypted.

**LUKS on LVM**

When LUKS is used to encrypt LVM logical volumes, an encrypted volume can span multiple devices. The underlying LVM volume group is visible without decrypting the encrypted volumes.

### Full disk encryption

A common usage of LUKS is to provide full disk encryption, which involves encrypting the root partition of an operating system installation, which protects the operating system files from being tampered with or read by unauthorized parties.

On a Linux system, the boot partition (`/boot`) may be encrypted if the bootloader itself supports LUKS (e.g. GRUB). This is undertaken to prevent tampering with the Linux kernel. However, the first stage bootloader or an EFI system partition cannot be encrypted (see Full disk encryption#The boot key problem).

On mobile Linux systems, postmarketOS has developed osk-sdl to allow a full disk encrypted system to be unlocked using a touch screen.

For systems running systemd, the `systemd-homed` component can be used to encrypt individual home directories.

## Operating system support

The reference implementation for LUKS operates on Linux and is based on an enhanced version of cryptsetup, using dm-crypt as the disk encryption backend. Under Microsoft Windows, LUKS-encrypted disks can be used via the Windows Subsystem for Linux. (Formerly, this was possible with LibreCrypt, which currently has fundamental security holes, and which succeeded FreeOTFE, formerly DoxBox.)

DragonFly BSD supports LUKS.

### Installer support

Several Linux distributions allow the root device to be encrypted upon OS installation. These installers include Calamares, Ubiquity, Debian-Installer, and more.

## On-disk format

LUKS headers are backward compatible; newer versions of LUKS are able to read headers of previous versions.

### LUKS1

| Offset | Data type | Description |   |
|---|---|---|---|
| 000 | 000hex | char[6] | Magic number {'L', 'U', 'K', 'S', 0xBA, 0xBE } |
| 006 | 006hex | uint16_t | LUKS Version (0x0001 for LUKS1) |
| 008 | 008hex | char[32] | Cipher Algorithm (e.g. "twofish", "aes") |
| 040 | 028hex | char[32] | Cipher mode (e.g. "cbc-essiv:sha256") |
| 072 | 048hex | char[32] | Cryptographic hash function (e.g. "sha1", "ripemd160") |
| 104 | 068hex | uint32_t | Payload offset (position of encrypted data) in 512 byte offsets |
| 108 | 06Chex | uint32_t | Number of key bytes |
| 112 | 070hex | char[20] | PBKDF2 master key checksum |
| 132 | 084hex | char[32] | PBKDF2 master key salt parameter |
| 164 | 0A4hex | uint32_t | PBKDF2 master key iterations (Default: 10) |
| 168 | 0A8hex | char[40] | UUID of the partition (e.g. "504c9fa7-d080-4acf-a829-73227b48fb89") |
| 208 | 0D0hex | (48 Bytes) | Keyslot 1 |
| … |   |   |   |
| 544 | 220hex | (48 Bytes) | Keyslot 8 |
| *592 Bytes total* |   |   |   |

| Offset | Data type | Description |
|---|---|---|
| 00 | uint32_t | State of keyslot: Active=0x00AC71F3; Disabled=0x0000DEAD |
| 04 | uint32_t | PBKDF2 iteration parameter |
| 08 | char[32] | PBKDF2 salt parameter |
| 40 | uint32_t | Start sector of key |
| 44 | uint32_t | Number of anti-forensic stripes (Default: 4000) |
| *48 Bytes total* |   |   |

### LUKS2

The LUKS2 header has a binary area and a JSON area, a second binary and JSON area, and a keyslots area. The binary and JSON areas are repeated two times with minor variations.

#### Binary area

The size of the binary areas is always 4kiB. The size of binary plus JSON area can be a power-of-two number of bytes between 16 kiB and 4 MiB, making the size of the JSON areas between 12 kiB and 4092 kiB each.

| Offset | Data type | Description |   |
|---|---|---|---|
| 1st Binary area |   |   |   |
| 00000 | 0000hex | char[6] | Magic number {'L', 'U', 'K', 'S', 0xBA, 0xBE }, allows fast detection by blkid |
| 00006 | 0006hex | uint16_t | LUKS Version (0x0002 for LUKS2) |
| 00008 | 0008hex | uint64_t | Size of binary and json area (commonly 16 kiB, 4000hex) |
| 00016 | 0010hex | uint64_t | Epoch, incremented when the header is modified |
| 00024 | 0018hex | char[48] | ASCII Partition Label, null terminated |
| 00072 | 0048hex | char[32] | String determining the checksum algorithm (commonly "sha256"), null terminated |
| 00104 | 0068hex | uint8_t[64] | Salt , unique for every binary area |
| 00168 | 00A8hex | char[40] | UUID of the device, null terminated (e.g. "02f47c64-7e74-4711-8bd4-a37613d1ecd3") |
| 00208 | 00D0hex | char[48] | Secondary "subsystem" label, null terminated |
| 00256 | 0100hex | uint64_t | offset of this LUKS area on the device (typically 0) |
| 00264 | 0108hex | _char[184] | Padding, must be zeroed |
| 00448 | 01C0hex | uint8_t[64] | Checksum of 1st binary area calculated with the checksum algorithm, zero-padded if shorter |
| 00512 | 0200hex | _char[3584] | Padding, must be zeroed |
| 1st JSON area |   |   |   |
| 04096 | 1000hex | char[12288] | LUKS JSON object, null terminated |
| 2nd Binary area |   |   |   |
| 16384 | 4000hex | char[6] | Second Magic number {'S', 'K', 'U', 'L', 0xBA, 0xBE } |
|   | Identical to 1st binary area |   |   |
| 16488 | 4068hex | uint8_t[64] | Salt, unique for every binary area |
|   | Identical to 1st binary area |   |   |
| 16640 | 4100hex | uint64_t | offset of this LUKS area on the device (typically 4000hex, 16384dec) |
| 16648 | 4108hex | _char[184] | Padding, must be zeroed |
| 16832 | 41C0hex | uint8_t[64] | Checksum of 2nd binary area calculated with the checksum algorithm, zero-padded if shorter |
| 16896 | 4200hex | _char[3584] | Padding, must be zeroed |
| 2nd JSON area |   |   |   |
|   | Identical to 1st JSON area |   |   |
| *32 kiB total* |   |   |   |

#### JSON area

The base LUKS2 JSON metadata object has 5 keys: *config*, *keyslots*, *digests*, *segments*, and *tokens*.

*Config* contains general settings and information of the LUKS header, and persistent mount options.

*Segments* describe areas on the disk than contain data and can be decrypted. They also describe the algorithm with which a segment is encrypted.

*Digests* describe what *keyslots* contain encrypted keys able to decrypt which *segments*. They contain a hash of the decrypted key of the *keyslot* that functions as a checksum and to verify correctness of the password.

*Keyslots* contain encrypted keys. The method of encryption varies, a combination of passwords, keyfiles, hardware keys, and other methods can be uses to decrypt the contained master-keys.

The *tokens* object can hold additional for external systems integrating with LUKS.

Userdata, *segments*, are encrypted with a large master-key and an efficient encryption algorithm. The master key can then be encrypted with a more expensive algorithm and potentially weaker user-provided keys, these encrypted master-keys are then stored in *Keyslots*. This slows brute-force attempts at guessing the password, and also allows changing decryption methods and passwords without having to reencrypt the entire data section, by only needing to rewrite the same master-key encrypted differently into the *keyslots*.

A typical LUKS2 JSON area, with added indentation and line-breaks:

```mw
{
	"keyslots": {
		"0": {
			"type": "luks2",
			"key_size": 64,
			"af": {
				"type": "luks1",
				"stripes": 4000,
				"hash": "sha256"
			},
			"area": {
				"type": "raw",
				"offset": "32768",
				"size": "258048",
				"encryption": "aes-xts-plain64",
				"key_size": 64
			},
			"kdf": {
				"type": "argon2id",
				"time": 4,
				"memory": 1048576,
				"cpus": 4,
				"salt": "YOvmrBmgFT7Ehm7ANZrn0quep1fUFisNCv4e+X8+CLk="
			}
		}
	},
	"tokens": {},
	"segments": {
		"0": {
			"type": "crypt",
			"offset": "16777216",
			"size": "dynamic",
			"iv_tweak": "0",
			"encryption": "aes-xts-plain64",
			"sector_size": 512
		}
	},
	"digests": {
		"0": {
			"type": "pbkdf2",
			"keyslots": [
				"0"
			],
			"segments": [
				"0"
			],
			"hash": "sha256",
			"iterations": 105703,
			"salt": "hrSZ0Sh6t3EVAyeH7XLSH1dEQrRmJwimbjHx85PLS/k=",
			"digest": "tXiDNw8fanGe8QcXewvtzF3AOTOqaIXBmhAGa8Kb42w="
		}
	},
	"config": {
		"json_size": "12288",
		"keyslots_size": "16744448",
		"flags": [
				"allow-discards"
		]
	}
}
```

#### Keyslots area

Keyslots take up the device region after the two binary and JSON areas. In the typical case shown above this starts at 32 kiB, and runs up to 4 MiB or 16 MiB. Here we will use 16MiB as an example.

Usually a device is spanned by a single *segment*, with the offset set to 16MiB and the size to dynamic. During reencryption or in unusual configuration there might be multiple segments that in total should span the device without gaps or overlap.

The *segment*(s) should each have a single associated *digest*, that each have one or more associated *keyslots*. *Keyslots* may also be unassociated with any digest and used for other purposes.

*Keyslots* themselves are mapped into the keyslots area, in the example above to a single 252kiB area starting right after the header at 32 kiB. This area is obfuscated with anti-forensic stripes in the same manner as in LUKS1.

The default algorithm for *digests*, pbkdf2, as well as the anti-forensic stripes type "luks1", are identical to LUKS1. The key derivation defaults to stronger algorithms unsupported by LUKS1, but can be set to the supported pbkdf2.

## Examples

Cryptsetup is the reference implementation of the LUKS frontend.

To encrypt a device with the path `/dev/sda1`:

```mw
# cryptsetup luksFormat /dev/sda1
```

To unlock an encrypted device, where `name` is the mapped device name:

```mw
# cryptsetup open /dev/sda1 name
```

### Re-encrypting

Re-encrypting a LUKS container can be done either with the `cryptsetup` tool itself, or with a legacy tool called `cryptsetup-reencrypt`. These tools can also be used to add encryption to an existing unencrypted filesystem, or remove encryption from a block device.

Both methods have similar syntax:

```mw
# cryptsetup reencrypt /dev/sda1
```

```mw
# cryptsetup-reencrypt /dev/sda1
```
