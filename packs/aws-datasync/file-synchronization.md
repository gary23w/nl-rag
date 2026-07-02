---
title: "File synchronization"
source: https://en.wikipedia.org/wiki/File_synchronization
domain: aws-datasync
license: CC-BY-SA-4.0
tags: aws datasync, data transfer service, cloud data migration, file synchronization service
fetched: 2026-07-02
---

# File synchronization

**File synchronization** (or **syncing**) in computing is the process of ensuring that computer files in two or more locations are updated via certain rules.

In *one-way file synchronization*, also called mirroring, updated files are copied from a source location to one or more target locations, but no files are copied back to the source location. In *two-way file synchronization*, updated files are copied in both directions, usually with the purpose of keeping the two locations identical to each other. In this article, the term synchronization refers exclusively to two-way file synchronization.

File synchronization is commonly used for home backups on external hard drives or updating for transport on USB flash drives. BitTorrent Sync, Dropbox, SKYSITE, Nextcloud, OneDrive, Google Drive and iCloud are prominent products. Some backup software also supports real-time file sync. The automatic process prevents copying already identical files and thus can be faster and save much time versus a manual copy, and is less error prone. However this suffers from the limit that the synchronized files must physically fit in the portable storage device. Synchronization software that only keeps a list of files and the changed files eliminates this problem (e.g. the "snapshot" feature in Beyond Compare or the "package" feature in Synchronize It!). It is especially useful for mobile workers, or others that work on multiple computers.

It is possible to synchronize multiple locations by synchronizing them one pair at a time. The Unison Manual describes how to do this:

If you need to do this, the most reliable way to set things up is to organize the machines into a "star topology," with one machine designated as the "hub" and the rest as "spokes," and with each spoke machine synchronizing only with the hub. The big advantage of the star topology is that it eliminates the possibility of confusing "spurious conflicts" arising from the fact that a separate archive is maintained by

Unison

for every pair of hosts that it synchronizes.

## Common features

Common features of file synchronization systems include:

- Encryption for security, especially when synchronizing across the Internet.
- Compressing any data sent across a network.
- *Conflict detection* where a file has been modified on both sources, as opposed to where it has only been modified on one. Undetected conflicts can lead to overwriting copies of the file with the most recent version, causing data loss. For conflict detection, the synchronization software needs to keep a database of the synchronized files. Distributed conflict detection can be achieved by version vectors.
- *Open Files Support* ensures data integrity when copying data or application files that are in-use or database files that are exclusively locked.
- Specific support for using an intermediate storage device, such as a removable flash disc, to synchronize two machines. Most synchronizing programs can be used in this way, but providing specific support for this can reduce the amount of data stored on a device.
- The ability to preview any changes before they are made.
- The ability to view differences in individual files.
- Backup between operating systems and transfer between network computers.
- Ability to edit or use files on multiple computers or operating systems.

## Comparison to shared file access

Shared file access involves but should not be confused with file synchronization and other information synchronization. Internet-based information synchronization may, for example, use the SyncML language. Shared file access is based on server-side pushing of folder information, and is normally used over an "always on" Internet socket. File synchronization allows the user to be offline from time to time and is normally based on an agent software that polls synchronized machines at reconnect, and sometimes repeatedly with a certain time interval, to discover differences. Modern operating systems often include a local cache of remote files, allowing offline access and synchronization when reconnected.

## Possible security concerns

Consumer-grade file synchronization solutions are popular, however for business use, they create a concern of allowing corporate information to sprawl to unmanaged devices and cloud services which are uncontrolled by the organization.

When using cloud services, data privacy risks can be mitigated by using a file synchronization solution that features end-to-end encryption instead of simple transport (HTTPS) or at-rest encryption.
