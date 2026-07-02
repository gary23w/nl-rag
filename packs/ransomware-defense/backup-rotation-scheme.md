---
title: "Backup rotation scheme"
source: https://en.wikipedia.org/wiki/Backup_rotation_scheme
domain: ransomware-defense
license: CC-BY-SA-4.0
tags: ransomware defense, backup and recovery, immutable backup rotation, data recovery, malware defense
fetched: 2026-07-02
---

# Backup rotation scheme

A **backup rotation scheme** is a system of backing up data to computer media (such as tapes) that minimizes, by re-use, the number of media used. It determines how and when each piece of removable storage is used for a backup job and how long it is retained after backup data is stored on it. Over time, different techniques have evolved to balance data retention and restoration needs with the cost of additional data storage media. Such a scheme can become quite complex if it incorporates incremental backups, multiple retention periods, and off-site storage.

## Schemes

### First in, first out

A first in, first out (FIFO) backup scheme saves new or modified files onto the "oldest" media in the set, i.e. the media that contain the oldest and thus least useful previously backed up data. Performing a daily backup onto a set of 14 media, the backup depth would be 14 days. Each day, the oldest media would be inserted when performing the backup. This is the simplest rotation scheme and is usually the first to come to mind.

This scheme has the advantage that it retains the longest possible tail of daily backups. It can be used when archived data is unimportant (or is retained separately from the short-term backup data) and data before the rotation period is irrelevant.

However, this scheme suffers from the possibility of data loss: suppose, an error is introduced into the data, but the problem is not identified until several generations of backups and revisions have taken place. Thus when the error is detected, all the backup files contain the error. It would then be useful to have at least one older version of the data, as it would not have the error.

### Grandfather-father-son

Grandfather-father-son backup (GFS) is a common rotation scheme for backup media, in which there are three or more backup cycles, such as daily, weekly and monthly. The daily backups are rotated on a 3-months basis using a FIFO system as above. The weekly backups are similarly rotated on a bi-yearly basis, and the monthly backup on a yearly basis. In addition, quarterly, half-yearly, and/or annual backups could also be separately retained. Often some of these backups are removed from the site for safekeeping and disaster recovery purposes.

### Tower of Hanoi

The Tower of Hanoi rotation method is more complex. It is based on the mathematics of the Tower of Hanoi puzzle, using a recursive method to optimize the back-up cycle. Every tape corresponds to a disk in the puzzle, and every disk movement to a different peg corresponds with a backup to that tape. So the first tape is used every other day (1, 3, 5, 7, 9, ...), the second tape is used every fourth day (2, 6, 10, ...), the third tape is used every eighth day (4, 12, 20, ...).

A set of *n* tapes (or other media) will allow backups for 2*n*−1 days before the last set is recycled. So, 3 tapes will give 4 days' worth of backups, and on the 4th day *Set C* will be overwritten; 4 tapes will give 8 days, and *Set D* is overwritten on the 9th day; 5 tapes will give 16 days, etc. Files can be restored from 1, 2, 4, 8, 16, ..., 2*n*−1 days ago.

The following tables show which tapes are used on which days of various cycles. A disadvantage of the method is that half the backups are overwritten after only two days.

#### Three-tape Hanoi schedule

Day of the cycle

01

02

03

04

05

06

07

08

Set

A

A

A

A

B

B

C

C

#### Four-tape Hanoi schedule

Day of the cycle

01

02

03

04

05

06

07

08

09

10

11

12

13

14

15

16

Set

A

A

A

A

A

A

A

A

B

B

B

B

C

C

D

D

#### Five-tape Hanoi schedule

Day of the cycle

01

02

03

04

05

06

07

08

09

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

Set

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

A

B

B

B

B

B

B

B

B

C

C

C

C

D

D

E

E

#### Extensions and example

Many variations are possible, and the concepts are readily extended to disc-based directories containing backups. Here are some options:

- Save a base backup as set zero.
- Save as many of the most recent backups as desired.
- Save more than one of each set number, for greater coverage.

Coverage automatically gets sparser the further back in time one goes, which approximates the likelihood of needing to do restores from past backups.

And Tower of Hanoi has the huge advantage of freeing implementers from having to deal with managing hourly, daily, weekly, monthly, quarterly or annual management strategies.

In general, backup set number *set* is used at *seq* = 2*set*−1 + j × 2*set*, *j* = 0, 1, 2, 3, 4, ..., where *seq* is the sequence or serial number of a backup (also the Tower of Hanoi move number).

Here is an example showing coverage, including set 0, keeping at least the last 4 days, and recycling:

- precious.20140515.seq.0 set 0
- precious.20150205.seq.256 set 9
- precious.20151026.seq.512 set 10
- precious.20160311.seq.640 set 8
- precious.20160516.seq.704 set 7
- precious.20160601.seq.720 set 5
- precious.20160609.seq.728 set 4
- precious.20160617.seq.736 set 6
- precious.20160618.seq.737.recycle set 1
- precious.20160619.seq.738 set 2
- precious.20160620.seq.739 set 1
- precious.20160621.seq.740 set 3
- precious.20160622.seq.741 set 1

### Weighted random distribution

An alternative arrangement is to keep generations distributed across all points in time is by deleting (or overwriting) past generations (except the oldest and the most-recent-*n* generations) when necessary in a weighted-random fashion. For each deletion, the weight assigned to each deletable generation corresponds to the probability of it being deleted.

One acceptable weight is a constant exponent (possibly the square) of the multiplicative inverse of the duration (possibly expressed in the number of days) between the dates of the generation and the generation preceding it. Using a larger exponent leads to a more uniform distribution of generations, whereas a smaller exponent leads to a distribution with more recent and fewer older generations. This technique probabilistically ensures that past generations are always distributed across all points in time as is desired.

The weighted random method only has an advantage over a more systematic approach, when backups are irregular or missed.

### Incremented media method

This method has many variations and names. A set of numbered media is used until the end of the cycle. Then the cycle is repeated using media numbered the same as the previous cycle, but incremented by one. The lowest numbered tape from the previous cycle is retired and kept permanently. Thus one has access to every backup for one cycle and to one backup per cycle before that. This method has the advantage of ensuring even media wear, but requires a schedule to be precalculated.
