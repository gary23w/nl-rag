---
title: "envsys"
source: https://en.wikipedia.org/wiki/Sysmon
domain: osquery-endpoint
license: CC-BY-SA-4.0
tags: osquery endpoint, endpoint telemetry query, host based intrusion detection, file integrity monitoring, endpoint security
fetched: 2026-07-02
---

# envsys

(Redirected from

Sysmon

)

The **envsys** framework is a kernel-level hardware monitoring sensors framework in NetBSD. As of 4 March 2019, the framework is used by close to 85 device drivers to export various environmental monitoring sensors, as evidenced by references of the `sysmon_envsys_register` symbol within the `sys` path of NetBSD; with temperature sensors, `ENVSYS_STEMP`, being the most likely type to be exported by any given driver. Sensors are registered with the kernel through `**sysmon_envsys(9)**` API. Consumption and monitoring of sensors from the userland is performed with the help of **`envstat`** utility through `proplib(3)` through `ioctl(2)` against the **`/dev/sysmon`** pseudo-device file, the `**powerd**` power management daemon that responds to kernel events by running scripts from `/etc/powerd/scripts/`, as well as third-party tools like `symon` and GKrellM from pkgsrc.

## Features

The framework allows the user to amend the monitoring limits specified by the driver, and for the driver to perform monitoring of the sensors in kernel space, or even to programme a hardware chip to do the monitoring for the system automatically. Two levels of limits are defined: *critical* and *warning*, both of which additionally extend to an *over* and an *under* categorisation. If limit thresholds are crossed, a kernel event may be generated, which can be caught in the userland by `powerd` to execute a pre-defined user script. By comparison, in OpenBSD's hw.sensors, the monitoring of user-defined values is performed in userspace by `sensorsd`.

As of 2019, the framework itself does not facilitate computer fan control, although the drivers could still implement interfacing with the fan-controlling capabilities of their chips through other means, for example, through a driver-specific sysctl interface, which is the approach taken by the `dbcool(4)` driver. However, the drivers for the most popular Super I/O chips like `lm(4)` and `itesio(4)` do not implement any fan control at all (in fact, historically, in all of OpenBSD, NetBSD and DragonFly, these drivers don't even report the duty cycle of the fans — only the actual RPM values are reported).

## History

The framework undergone two major revisions: the first version of `envsys.h` was committed on 15 December 1999 (1999-12-15); with `envsys.4` man page following on 27 February 2000 (2000-02-27). Between 2000 and 2007, the manual page for envsys(4) in NetBSD stated that the "API is experimental", and that the "entire API should be replaced by a sysctl(8)", "should one be developed"; it can be noted that in 2003 this was the exact approach taken by OpenBSD with sysctl hw.sensors when some of the envsys(4) drivers were ported to OpenBSD.

The second revision came about on 1 July 2007 (2007-07-01). The serialisation with userland was reimplemented using property lists with the help of NetBSD's new proplib(3) library (the underlying transport layer between the kernel and userland still being done through ioctl).

The envsys framework was the precursor to OpenBSD's sysctl hw.sensors framework in 2003, and many drivers, as well as some sensor types, have been ported back and forth between NetBSD and OpenBSD. Support for sensors of `drive` type has been added to NetBSD on 1 May 2007, similar to `drive` type in OpenBSD, which was at the same time when bio(4) and bioctl were ported from OpenBSD to NetBSD.
