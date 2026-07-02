---
title: "NixOS Manual (part 1/5)"
source: https://nixos.org/manual/nixos/stable/
domain: nixos
license: CC-BY-SA-4.0
tags: nixos distribution, declarative linux distribution, reproducible system configuration, immutable operating system
fetched: 2026-07-02
part: 1/5
---

# NixOS Manual


## Version 26.05

**List of Examples**

**1. Example partition schemes for NixOS on `/dev/sda` (MBR)**

**2. Example partition schemes for NixOS on `/dev/sda` (UEFI)**

**3. Commands for Installing NixOS on `/dev/sda`**

**4. Example: NixOS Configuration**

**5. Customize specific image variants**

**6. Gitlab Runner with `podman` and Nix Store Caching**

**7. Nix expression to build Emacs with packages (`emacs.nix`)**

**8. Querying Emacs packages**

**9. Custom Emacs in `configuration.nix`**

**10. Custom Emacs in `~/.config/nixpkgs/config.nix`**

**11. Custom Emacs build**

**12. Structure of NixOS Modules**

**13. NixOS Module for the “locate” Service**

**14. Escaping in Exec directives**

**15. `mkEnableOption` usage**

**16. Simple `mkPackageOption` usage**

**17. `mkPackageOption` with explicit default and example**

**18. `mkPackageOption` with additional description text**

**19. Extensible type placeholder in the service module**

**20. Extending `services.xserver.displayManager.enable` in the `gdm` module**

**21. Extending `services.xserver.displayManager.enable` in the `sddm` module**

**22. `types.anything`**

**23. Directly defined submodule**

**24. Submodule defined as a reference**

**25. Declaration of a list of submodules**

**26. Definition of a list of submodules**

**27. Declaration of attribute sets of submodules**

**28. Definition of attribute sets of submodules**

**29. Adding a type check**

**30. Overriding a type check**

**31. Freeform submodule**

**32. Module with conventional `settings` option**

**33. Declaring a type-checked `settings` attribute**

**34. Using extendNixOS in `passthru.tests` to make `(openssh.tests.overrideAttrs f).tests.nixos` coherent**

# Preface

This manual describes how to install, use and extend NixOS, a Linux distribution based on the purely functional package management system Nix, that is composed using modules and packages defined in the Nixpkgs project.

Additional information regarding the Nix package manager and the Nixpkgs project can be found in respectively the Nix manual and the Nixpkgs manual.

If you encounter problems, please report them on the `Discourse`, the Matrix room, or on the `#nixos` channel on Libera.Chat. Alternatively, consider contributing to this manual. Bugs should be reported in NixOS’ GitHub issue tracker.

### Note

Commands prefixed with `#` have to be run as root, either requiring to login as root user or temporarily switching to it using `sudo` for example.

# Installation

This section describes how to obtain, install, and configure NixOS for first-time use.


## Obtaining NixOS

NixOS ISO images can be downloaded from the NixOS download page. Follow the instructions in the section called “Booting from a USB flash drive” to create a bootable USB flash drive.

If you have a very old system that can’t boot from USB, you can burn the image to an empty CD. NixOS might not work very well on such systems.

As an alternative to installing NixOS yourself, you can get a running NixOS system through several other means:

- Using virtual appliances in Open Virtualization Format (OVF) that can be imported into VirtualBox. These are available from the NixOS download page.
- Using AMIs for Amazon’s EC2. To find one for your region, please refer to the download page.
- Using NixOps, the NixOS-based cloud deployment tool, which allows you to provision VirtualBox and EC2 NixOS instances from declarative specifications. Check out the NixOps homepage for details.


## Installing NixOS


## Booting from the install medium

To begin the installation, you have to boot your computer from the install drive.

1. Plug in the install drive. Then turn on or restart your computer.
2. Open the boot menu by pressing the appropriate key, which is usually shown on the display on early boot. Select the USB flash drive (the option usually contains the word “USB”). If you choose the incorrect drive, your computer will likely continue to boot as normal. In that case restart your computer and pick a different drive.NoteThe key to open the boot menu is different across computer brands and even models. It can be **F12**, but also **F1**, **F9**, **F10**, **Enter**, **Del**, **Esc** or another function key. If you are unsure and don’t see it on the early boot screen, you can search online for your computers brand, model followed by “boot from usb”. The computer might not even have that feature, so you have to go into the BIOS/UEFI settings to change the boot order. Again, search online for details about your specific computer model.For Apple computers with Intel processors press and hold the **⌥** (Option or Alt) key until you see the boot menu. On Apple silicon press and hold the power button.NoteIf your computer supports both BIOS and UEFI boot, choose the UEFI option. You will likely need to disable “Secure Boot” to use the UEFI option. The exact steps vary by device manufacturer but generally “Secure Boot” will be listed under “Boot”, “Security” or “Advanced” in the BIOS/UEFI menu.NoteIf you use a CD for the installation, the computer will probably boot from it automatically. If not, choose the option containing the word “CD” from the boot menu.
3. Shortly after selecting the appropriate boot drive, you should be presented with a menu with different installer options. Leave the default and wait (or press **Enter** to speed up).
4. The graphical images will start their corresponding desktop environment and the graphical installer, which can take some time. The minimal images will boot to a command line. You have to follow the instructions in the section called “Manual Installation” there.


## Graphical Installation

The graphical installer is recommended for desktop users and will guide you through the installation.

1. In the “Welcome” screen, you can select the language of the Installer and the installed system.TipLeaving the language as “American English” will make it easier to search for error messages in a search engine or to report an issue.
2. Next you should choose your location to have the timezone set correctly. You can actually click on the map!NoteThe installer will use an online service to guess your location based on your public IP address.
3. Then you can select the keyboard layout. The default keyboard model should work well with most desktop keyboards. If you have a special keyboard or notebook, your model might be in the list. Select the language you are most comfortable typing in.
4. On the “Users” screen, you have to type in your display name, login name and password. You can also enable an option to automatically login to the desktop.
5. Then you have the option to choose a desktop environment. If you want to create a custom setup with a window manager, you can select “No desktop”.TipIf you don’t have a favorite desktop and don’t know which one to choose, you can stick to either GNOME or Plasma. They have a quite different design, so you should choose whichever you like better. They are both popular choices and well tested on NixOS.
6. You have the option to allow unfree software in the next screen.
7. The easiest option in the “Partitioning” screen is “Erase disk”, which will delete all data from the selected disk and install the system on it. Also select “Swap (with Hibernation)” in the dropdown below it. You have the option to encrypt the whole disk with LUKS.NoteAt the top left you see if the Installer was booted with BIOS or UEFI. If you know your system supports UEFI and it shows “BIOS”, reboot with the correct option.WarningMake sure you have selected the correct disk at the top and that no valuable data is still on the disk! It will be deleted when formatting the disk.
8. Check the choices you made in the “Summary” and click “Install”.NoteThe installation takes about 15 minutes. The time varies based on the selected desktop environment, internet connection speed and disk write speed.
9. When the install is complete, remove the USB flash drive and reboot into your new system!


## Manual Installation

NixOS can be installed on BIOS or UEFI systems. The procedure for a UEFI installation is broadly the same as for a BIOS installation. The differences are mentioned in the following steps.

The NixOS manual is available by running `nixos-help` in the command line or from the application menu in the desktop environment.

To have access to the command line on the graphical images, open Terminal (GNOME) or Konsole (Plasma) from the application menu.

You are logged-in automatically as `nixos`. The `nixos` user account has an empty password so you can use `sudo` without a password:

```
$ sudo -i
```

You can use `loadkeys` to switch to your preferred keyboard layout. (We even provide neo2 via `loadkeys de neo`!)

If the text is too small to be legible, try `setfont ter-v32n` to increase the font size.

To install over a serial port connect with `115200n8` (e.g. `picocom -b 115200 /dev/ttyUSB0`). When the bootloader lists boot entries, select the serial console boot entry.

### Networking in the installer

The boot process should have brought up networking (check `ip a`). Networking is necessary for the installer, since it will download lots of stuff (such as source tarballs or Nixpkgs channel binaries). It’s best if you have a DHCP server on your network. Otherwise configure networking manually using `ip`.

You can configure the network, Wi-Fi included, through NetworkManager. Using the `nmtui` program, you can do so even in a non-graphical session. If you prefer to configure the network manually, disable NetworkManager with `systemctl stop NetworkManager`.

If you would like to continue the installation from a different machine you can use activated SSH daemon. You need to copy your ssh key to either `/home/nixos/.ssh/authorized_keys` or `/root/.ssh/authorized_keys` (Tip: For installers with a modifiable filesystem such as the sd-card installer image a key can be manually placed by mounting the image on a different machine). Alternatively you must set a password for either `root` or `nixos` with `passwd` to be able to login.

### Partitioning and formatting

The NixOS installer doesn’t do any partitioning or formatting, so you need to do that yourself.

The NixOS installer ships with multiple partitioning tools. The examples below use `parted`, but also provides `fdisk`, `gdisk`, `cfdisk`, and `cgdisk`.

Use the command ‘lsblk’ to find the name of your ‘disk’ device.

The recommended partition scheme differs depending if the computer uses *Legacy Boot* or *UEFI*.

#### UEFI (GPT)

Here’s an example partition scheme for UEFI, using `/dev/sda` as the device.

### Note

You can safely ignore `parted`’s informational message about needing to update /etc/fstab.

1. Create a *GPT* partition table.
  ```
# parted /dev/sda -- mklabel gpt
  ```
2. Add the *root* partition. This will fill the disk except for the end part, where the swap will live, and the space left in front (512MiB) which will be used by the boot partition.
  ```
# parted /dev/sda -- mkpart root ext4 512MB -8GB
  ```
3. Next, add a *swap* partition. The size required will vary according to needs, here a 8GB one is created.NoteThe swap partition size rules are no different than for other Linux distributions.
  ```
# parted /dev/sda -- mkpart swap linux-swap -8GB 100%
  ```
4. Finally, the *boot* partition. NixOS by default uses the ESP (EFI system partition) as its */boot* partition. It uses the initially reserved 512MiB at the start of the disk.NoteIn case you decided to not create a swap partition, replace `3` by `2`. To be sure of the id number of ESP, run `parted --list`.
  ```
# parted /dev/sda -- mkpart ESP fat32 1MB 512MB
# parted /dev/sda -- set 3 esp on
  ```

Once complete, you can follow with the section called “Formatting”.

#### Legacy Boot (MBR)

Here’s an example partition scheme for Legacy Boot, using `/dev/sda` as the device.

### Note

You can safely ignore `parted`’s informational message about needing to update /etc/fstab.

1. Create a *MBR* partition table.
  ```
# parted /dev/sda -- mklabel msdos
  ```
2. Add the *root* partition. This will fill the disk except for the end part, where the swap will live.
  ```
# parted /dev/sda -- mkpart primary 1MB -8GB
  ```
3. Set the root partition’s boot flag to on. This allows the disk to be booted from.
  ```
# parted /dev/sda -- set 1 boot on
  ```
4. Finally, add a *swap* partition. The size required will vary according to needs, here a 8GB one is created.NoteThe swap partition size rules are no different than for other Linux distributions.
  ```
# parted /dev/sda -- mkpart primary linux-swap -8GB 100%
  ```

Once complete, you can follow with the section called “Formatting”.

#### Formatting

Use the following commands:

- For initialising Ext4 partitions: `mkfs.ext4`. It is recommended that you assign a unique symbolic label to the file system using the option `-L label`, since this makes the file system configuration independent from device changes. For example:
  ```
# mkfs.ext4 -L nixos /dev/sda1
  ```
- For creating swap partitions: `mkswap`. Again it’s recommended to assign a label to the swap partition: `-L label`. For example:
  ```
# mkswap -L swap /dev/sda2
  ```
- **UEFI systems**For creating boot partitions: `mkfs.fat`. Again it’s recommended to assign a label to the boot partition: `-n label`. For example:
  ```
# mkfs.fat -F 32 -n boot /dev/sda3
  ```
- For creating LVM volumes, the LVM commands, e.g., `pvcreate`, `vgcreate`, and `lvcreate`.
- For creating software RAID devices, use `mdadm`.

### Installing

1. Mount the target file system on which NixOS should be installed on `/mnt`, e.g.
  ```
# mount /dev/disk/by-label/nixos /mnt
  ```
2. **UEFI systems**Mount the boot file system on `/mnt/boot`, e.g.
  ```
# mkdir -p /mnt/boot
# mount -o umask=077 /dev/disk/by-label/boot /mnt/boot
  ```
3. If your machine has a limited amount of memory, you may want to activate swap devices now (`swapon device`). The installer (or rather, the build actions that it may spawn) may need quite a bit of RAM, depending on your configuration.
  ```
# swapon /dev/sda2
  ```
4. You now need to create a file `/mnt/etc/nixos/configuration.nix` that specifies the intended configuration of the system. This is because NixOS has a *declarative* configuration model: you create or edit a description of the desired configuration of your system, and then NixOS takes care of making it happen. The syntax of the NixOS configuration file is described in *Configuration Syntax*, while a list of available configuration options appears in Appendix A. A minimal example is shown in Example: NixOS Configuration.This command accepts an optional `--flake` option, to also generate a `flake.nix` file, if you want to set up a flake-based configuration.The command `nixos-generate-config` can generate an initial configuration file for you:You should then edit `/mnt/etc/nixos/configuration.nix` to suit your needs:If you’re using the graphical ISO image, other editors may be available (such as `vim`). If you have network access, you can also install other editors – for instance, you can install Emacs by running `nix-env -f '<nixpkgs>' -iA emacs`.BIOS systemsYou *must* set the option `boot.loader.grub.device` to specify on which disk the GRUB boot loader is to be installed. Without it, NixOS cannot boot.If there are other operating systems running on the machine before installing NixOS, the `boot.loader.grub.useOSProber` option can be set to `true` to automatically add them to the grub menu.UEFI systemsYou must select a boot-loader, either systemd-boot or GRUB. The recommended option is systemd-boot: set the option `boot.loader.systemd-boot.enable` to `true`. `nixos-generate-config` should do this automatically for new configurations when booted in UEFI mode.You may want to look at the options starting with `boot.loader.efi` and `boot.loader.systemd-boot` as well.If you want to use GRUB, set `boot.loader.grub.device` to `nodev` and `boot.loader.grub.efiSupport` to `true`.With systemd-boot, you should not need any special configuration to detect other installed systems. With GRUB, set `boot.loader.grub.useOSProber` to `true`, but this will only detect windows partitions, not other Linux distributions. If you dual boot another Linux distribution, use systemd-boot instead.If you need to configure networking for your machine the configuration options are described in *Networking*. In particular, while wifi is supported on the installation image, it is not enabled by default in the configuration generated by `nixos-generate-config`.Another critical option is `fileSystems`, specifying the file systems that need to be mounted by NixOS. However, you typically don’t need to set it yourself, because `nixos-generate-config` sets it automatically in `/mnt/etc/nixos/hardware-configuration.nix` from your currently mounted file systems. (The configuration file `hardware-configuration.nix` is included from `configuration.nix` and will be overwritten by future invocations of `nixos-generate-config`; thus, you generally should not modify it.) Additionally, you may want to look at Hardware configuration for known-hardware at this point or after installation.NoteDepending on your hardware configuration or type of file system, you may need to set the option `boot.initrd.kernelModules` to include the kernel modules that are necessary for mounting the root file system, otherwise the installed system will not be able to boot. (If this happens, boot from the installation media again, mount the target file system on `/mnt`, fix `/mnt/etc/nixos/configuration.nix` and rerun `nixos-install`.) In most cases, `nixos-generate-config` will figure out the required modules.
  ```
# nixos-generate-config --root /mnt
  ```
  ```
# nano /mnt/etc/nixos/configuration.nix
  ```
5. Do the installation:This will install your system based on the configuration you provided. If anything fails due to a configuration problem or any other issue (such as a network outage while downloading binaries from the NixOS binary cache), you can re-run `nixos-install` after fixing your `configuration.nix`.If you opted for a flake-based configuration, you will need to pass the `--flake` here as well and specify the name of the configuration as used in the `flake.nix` file. For the default generated flake, this is `nixos`.As the last step, `nixos-install` will ask you to set the password for the `root` user, e.g.If you have a user account declared in your `configuration.nix` and plan to log in using this user, set a password before rebooting, e.g. for the `alice` user:NoteFor unattended installations, it is possible to use `nixos-install --no-root-passwd` in order to disable the password prompt entirely.
  ```
# nixos-install
  ```
  ```
# nixos-install --flake 'path/to/flake.nix#nixos'
  ```
  ```
setting root password...
New password: ***
Retype new password: ***
  ```
  ```
# nixos-enter --root /mnt -c 'passwd alice'
  ```
6. If everything went well:
  ```
# reboot
  ```
7. You should now be able to boot into the installed NixOS. The GRUB boot menu shows a list of *available configurations* (initially just one). Every time you change the NixOS configuration (see Changing Configuration), a new item is added to the menu. This allows you to easily roll back to a previous configuration if something goes wrong.Use your declared user account to log in. If you didn’t declare one, you should still be able to log in using the `root` user.NoteSome graphical display managers such as SDDM do not allow `root` login by default, so you might need to switch to TTY. Refer to *User Management* for details on declaring user accounts.You may also want to install some software. This will be covered in *Package Management*.

### Installation summary

To summarise, Example: Commands for Installing NixOS on `/dev/sda` shows a typical sequence of commands for installing NixOS on an empty hard drive (here `/dev/sda`). Example: NixOS Configuration shows a corresponding configuration Nix expression.

Example 1. Example partition schemes for NixOS on

/dev/sda

(MBR)

Example 2. Example partition schemes for NixOS on

/dev/sda

(UEFI)

Example 3. Commands for Installing NixOS on

/dev/sda

Example 4. Example: NixOS Configuration


## Additional installation notes

### Booting from a USB flash drive

The image has to be written verbatim to the USB flash drive for it to be bootable on UEFI and BIOS systems. Here are the recommended tools to do that.

#### Creating bootable USB flash drive with a graphical tool

Etcher is a popular and user-friendly tool. It works on Linux, Windows and macOS.

Download it from balena.io, start the program, select the downloaded NixOS ISO, then select the USB flash drive and flash it.

### Warning

Etcher reports errors and usage statistics by default, which can be disabled in the settings.

An alternative is USBImager, which is very simple and does not connect to the internet. Download the version with write-only (wo) interface for your system. Start the program, select the image, select the USB flash drive and click “Write”.

#### Creating bootable USB flash drive from a Terminal on Linux

1. Plug in the USB flash drive.
2. Find the corresponding device with `lsblk`. You can distinguish them by their size.
3. Make sure all partitions on the device are properly unmounted. Replace `sdX` with your device (e.g. `sdb`).

```
sudo umount /dev/sdX*
```

1. Then use the `dd` utility to write the image to the USB flash drive.

```
sudo dd bs=4M conv=fsync oflag=direct status=progress if=<path-to-image> of=/dev/sdX
```

#### Creating bootable USB flash drive from a Terminal on macOS

1. Plug in the USB flash drive.
2. Find the corresponding device with `diskutil list`. You can distinguish them by their size.
3. Make sure all partitions on the device are properly unmounted. Replace `diskX` with your device (e.g. `disk1`).

```
diskutil unmountDisk diskX
```

1. Then use the `dd` utility to write the image to the USB flash drive.

```
sudo dd if=<path-to-image> of=/dev/rdiskX bs=4m
```

After `dd` completes, a GUI dialog “The disk you inserted was not readable by this computer” will pop up, which can be ignored.

### Note

Using the ‘raw’ `rdiskX` device instead of `diskX` with dd completes in minutes instead of hours.

1. Eject the disk when it is finished.

```
diskutil eject /dev/diskX
```

### Booting from the “netboot” media (PXE)

Advanced users may wish to install NixOS using an existing PXE or iPXE setup.

These instructions assume that you have an existing PXE or iPXE infrastructure and want to add the NixOS installer as another option. To build the necessary files from your current version of nixpkgs, you can run:

```
nix-build -A netboot.x86_64-linux '<nixpkgs/nixos/release.nix>'
```

This will create a `result` directory containing:

- `bzImage` – the Linux kernel
- `initrd` – the initrd file
- `netboot.ipxe` – an example ipxe script demonstrating the appropriate kernel command line arguments for this image

If you’re using plain PXE, configure your boot loader to use the `bzImage` and `initrd` files and have it provide the same kernel command line arguments found in `netboot.ipxe`.

If you’re using iPXE, depending on how your HTTP/FTP/etc. server is configured you may be able to use `netboot.ipxe` unmodified, or you may need to update the paths to the files to match your server’s directory layout.

In the future we may begin making these files available as build products from hydra at which point we will update this documentation with instructions on how to obtain them either for placing on a dedicated TFTP server or to boot them directly over the internet.

### “Booting” into NixOS via kexec

In some cases, your system might already be booted into/preinstalled with another Linux distribution, and booting NixOS by attaching an installation image is quite a manual process.

This is particularly useful for (cloud) providers where you can’t boot a custom image, but get some Debian or Ubuntu installation.

In these cases, it might be easier to use `kexec` to “jump into NixOS” from the running system, which only assumes `bash` and `kexec` to be installed on the machine.

Note that kexec may not work correctly on some hardware, as devices are not fully re-initialized in the process. In practice, this however is rarely the case.

To build the necessary files from your current version of nixpkgs, you can run:

```
nix-build -A kexec.x86_64-linux '<nixpkgs/nixos/release.nix>'
```

This will create a `result` directory containing the following:

- `bzImage` (the Linux kernel)
- `initrd` (the initrd file)
- `kexec-boot` (a shellscript invoking `kexec`)

These three files are meant to be copied over to the other already running Linux Distribution.

Note its symlinks pointing elsewhere, so `cd` in, and use `scp * root@$destination` to copy it over, rather than rsync.

Once you finished copying, execute `kexec-boot` *on the destination*, and after some seconds, the machine should be booting into an (ephemeral) NixOS installation medium.

In case you want to describe your own system closure to kexec into, instead of the default installer image, you can build your own `configuration.nix`:

```
{ modulesPath, ... }:
{
  imports = [ (modulesPath + "/installer/netboot/netboot-minimal.nix") ];

  services.openssh.enable = true;
  users.users.root.openssh.authorizedKeys.keys = [ "my-ssh-pubkey" ];
}
```

```
nix-build '<nixpkgs/nixos>' \
  --arg configuration ./configuration.nix
  --attr config.system.build.kexecTree
```

Make sure your `configuration.nix` does still import `netboot-minimal.nix` (or `netboot-base.nix`).

### Installing in a VirtualBox guest

Installing NixOS into a VirtualBox guest is convenient for users who want to try NixOS without installing it on bare metal. If you want to set up a VirtualBox guest, follow these instructions:

1. Add a New Machine in VirtualBox with OS Type “Linux / Other Linux”
2. Base Memory Size: 768 MB or higher.
3. New Hard Disk of 10 GB or higher.
4. Mount the CD-ROM with the NixOS ISO (by clicking on CD/DVD-ROM)
5. Click on Settings / System / Processor and enable PAE/NX
6. Click on Settings / System / Acceleration and enable “VT-x/AMD-V” acceleration
7. Click on Settings / Display / Screen and select VMSVGA as Graphics Controller
8. Save the settings, start the virtual machine, and continue installation like normal

There are a few modifications you should make in configuration.nix. Enable booting:

```
{ boot.loader.grub.device = "/dev/sda"; }
```

Also remove the fsck that runs at startup. It will always fail to run, stopping your boot until you press `*`.

```
{ boot.initrd.checkJournalingFS = false; }
```

Shared folders can be given a name and a path in the host system in the VirtualBox settings (Machine / Settings / Shared Folders, then click on the “Add” icon). Add the following to the `/etc/nixos/configuration.nix` to auto-mount them. If you do not add `"nofail"`, the system will not boot properly.

```
{ config, pkgs, ... }:
{
  fileSystems."/virtualboxshare" = {
    fsType = "vboxsf";
    device = "nameofthesharedfolder";
    options = [
      "rw"
      "nofail"
    ];
  };
}
```

The folder will be available directly under the root directory.

### Installing from another Linux distribution

Because Nix (the package manager) & Nixpkgs (the Nix packages collection) can both be installed on any (most?) Linux distributions, they can be used to install NixOS in various creative ways. You can, for instance:

1. Install NixOS on another partition, from your existing Linux distribution (without the use of a USB or optical device!)
2. Install NixOS on the same partition (in place!), from your existing non-NixOS Linux distribution using `NIXOS_LUSTRATE`.
3. Install NixOS on your hard drive from the Live CD of any Linux distribution.

The first steps to all these are the same:

1. Install the Nix package manager:Short version:More details in the Nix manual
  ```
$ curl -L https://nixos.org/nix/install | sh
$ . $HOME/.nix-profile/etc/profile.d/nix.sh # …or open a fresh shell
  ```
2. Switch to the NixOS channel:If you’ve just installed Nix on a non-NixOS distribution, you will be on the `nixpkgs` channel by default.As that channel gets released without running the NixOS tests, it will be safer to use the `nixos-*` channels instead:Where `<version>` corresponds to the latest version available on channels.nixos.org.You may want to throw in a `nix-channel --update` for good measure.
  ```
$ nix-channel --list
nixpkgs https://channels.nixos.org/nixpkgs-unstable
  ```
  ```
$ nix-channel --add https://channels.nixos.org/nixos-<version> nixpkgs
  ```
3. Install the NixOS installation tools:You’ll need `nixos-generate-config` and `nixos-install`, but this also makes some man pages and `nixos-enter` available, just in case you want to chroot into your NixOS partition. NixOS installs these by default, but you don’t have NixOS yet…
  ```
$ nix-env -f '<nixpkgs>' -iA nixos-install-tools
  ```
4. NoteThe following 5 steps are only for installing NixOS to another partition. For installing NixOS in place using `NIXOS_LUSTRATE`, skip ahead.Prepare your target partition:At this point it is time to prepare your target partition. Please refer to the partitioning, file-system creation, and mounting steps of *Installing NixOS*If you’re about to install NixOS in place using `NIXOS_LUSTRATE` there is nothing to do for this step.
5. Generate your NixOS configuration:You’ll probably want to edit the configuration files. Refer to the `nixos-generate-config` step in *Installing NixOS* for more information.Consider setting up the NixOS bootloader to give you the ability to boot on your existing Linux partition. For instance, if you’re using GRUB and your existing distribution is running Ubuntu, you may want to add something like this to your `configuration.nix`:(You can find the appropriate UUID for your partition in `/dev/disk/by-uuid`)
  ```
$ sudo `which nixos-generate-config` --root /mnt
  ```
  ```
{
  boot.loader.grub.extraEntries = ''
    menuentry "Ubuntu" {
      search --set=ubuntu --fs-uuid 3cc3e652-0c1f-4800-8451-033754f68e6e
      configfile "($ubuntu)/boot/grub/grub.cfg"
    }
  '';
}
  ```
6. Create the `nixbld` group and user on your original distribution:
  ```
$ sudo groupadd -g 30000 nixbld
$ sudo useradd -u 30000 -g nixbld -G nixbld nixbld
  ```
7. Download/build/install NixOS:WarningOnce you complete this step, you might no longer be able to boot on existing systems without the help of a rescue USB drive or similar.NoteOn some distributions there are separate PATHS for programs intended only for root. In order for the installation to succeed, you might have to use `PATH="$PATH:/usr/sbin:/sbin"` in the following command.Again, please refer to the `nixos-install` step in *Installing NixOS* for more information.That should be it for installation to another partition!
  ```
$ sudo PATH="$PATH" `which nixos-install` --root /mnt
  ```
8. Optionally, you may want to clean up your non-NixOS distribution:If you do not wish to keep the Nix package manager installed either, run something like `sudo rm -rv ~/.nix-* /nix` and remove the line that the Nix installer added to your `~/.profile`.
  ```
$ sudo userdel nixbld
$ sudo groupdel nixbld
  ```
9. NoteThe following steps are only for installing NixOS in place using `NIXOS_LUSTRATE`:WarningThe lustrate process will not work if the `boot.initrd.systemd.enable` option is set to `true`, which is now the default. Setting this to `false` is deprecated and scheduled for removal in NixOS 26.11, along with `NIXOS_LUSTRATE`. Other installation methods, such as the one outlined above, or installing from kexec, are recommended instead.Generate your NixOS configuration:Note that this will place the generated configuration files in `/etc/nixos`. You’ll probably want to edit the configuration files. Refer to the `nixos-generate-config` step in *Installing NixOS* for more information.NoteOn UEFI systems, check that your `/etc/nixos/hardware-configuration.nix` did the right thing with the EFI System Partition. In NixOS, by default, both systemd-boot and grub expect it to be mounted on `/boot`. However, the configuration generator bases its `fileSystems` configuration on the current mount points at the time it is run. If the current system and NixOS’s bootloader configuration don’t agree on where the EFI System Partition is to be mounted, you’ll need to manually alter the mount point in `hardware-configuration.nix` before building the system closure.You’ll likely want to set a root password for your first boot using the configuration files because you won’t have a chance to enter a password until after you reboot. You can initialize the root password to an empty one with this line: (and of course don’t forget to set one once you’ve rebooted or to lock the account with `sudo passwd -l root` if you use `sudo`)
  ```
$ sudo `which nixos-generate-config`
  ```
  ```
{ users.users.root.initialHashedPassword = ""; }
  ```
10. Build the NixOS closure and install it in the `system` profile:
  ```
$ nix-env -p /nix/var/nix/profiles/system -f '<nixpkgs/nixos>' -I nixos-config=/etc/nixos/configuration.nix -iA system
  ```
11. Change ownership of the `/nix` tree to root (since your Nix install was probably single user):
  ```
$ sudo chown -R 0:0 /nix
  ```
12. Set up the `/etc/NIXOS` and `/etc/NIXOS_LUSTRATE` files:`/etc/NIXOS` officializes that this is now a NixOS partition (the bootup scripts require its presence).`/etc/NIXOS_LUSTRATE` tells the NixOS bootup scripts to move *everything* that’s in the root partition to `/old-root`. This will move your existing distribution out of the way in the very early stages of the NixOS bootup. There are exceptions (we do need to keep NixOS there after all), so the NixOS lustrate process will not touch:The `/nix` directoryThe `/boot` directoryAny file or directory listed in `/etc/NIXOS_LUSTRATE` (one per line)NoteThe act of “lustrating” refers to the wiping of the existing distribution. Creating `/etc/NIXOS_LUSTRATE` can also be used on NixOS to remove all mutable files from your root partition (anything that’s not in `/nix` or `/boot` gets “lustrated” on the next boot.lustrate /ˈlʌstreɪt/ verb.purify by expiatory sacrifice, ceremonial washing, or some other ritual action.Let’s create the files:Let’s also make sure the NixOS configuration files are kept once we reboot on NixOS:
  ```
$ sudo touch /etc/NIXOS
$ sudo touch /etc/NIXOS_LUSTRATE
  ```
  ```
$ echo etc/nixos | sudo tee -a /etc/NIXOS_LUSTRATE
  ```
13. Finally, install NixOS’s boot system, backing up the current boot system’s files in the process.The details of this step can vary depending on the bootloader configuration in NixOS and the bootloader in use by the current system.The commands below should work for:BIOS systems.UEFI systems where both the current system and NixOS mount the EFI System Partition on `/boot`. Both systemd-boot and grub expect this by default in NixOS, but other distributions vary.WarningOnce you complete this step, your current distribution will no longer be bootable! If you didn’t get all the NixOS configuration right, especially those settings pertaining to boot loading and root partition, NixOS may not be bootable either. Have a USB rescue device ready in case this happens.WarningOn UEFI systems, anything on the EFI System Partition will be removed by these commands, such as other coexisting OS’s bootloaders.Cross your fingers, reboot, hopefully you should get a NixOS prompt!In other cases, most commonly where the EFI System Partition of the current system is instead mounted on `/boot/efi`, the goal is to:Make sure `/boot` (and the EFI System Partition, if mounted elsewhere) are mounted how the NixOS configuration would mount them.Clear them of files related to the current system, backing them up outside of `/boot`. NixOS will move the backups into `/old-root` along with everything else when it first boots.Instruct the NixOS closure built earlier to install its bootloader with:`sudo NIXOS_INSTALL_BOOTLOADER=1 /nix/var/nix/profiles/system/bin/switch-to-configuration boot`
  ```
$ sudo mkdir /boot.bak && sudo mv /boot/* /boot.bak &&
sudo NIXOS_INSTALL_BOOTLOADER=1 /nix/var/nix/profiles/system/bin/switch-to-configuration boot
  ```
14. If for some reason you want to revert to the old distribution, you’ll need to boot on a USB rescue disk and do something along these lines:This may work as is or you might also need to reinstall the boot loader.And of course, if you’re happy with NixOS and no longer need the old distribution:
  ```
# mkdir root
# mount /dev/sdaX root
# mkdir root/nixos-root
# mv -v root/* root/nixos-root/
# mv -v root/nixos-root/old-root/* root/
# mv -v root/boot.bak root/boot  # We had renamed this by hand earlier
# umount root
# reboot
  ```
  ```
sudo rm -rf /old-root
  ```
15. It’s also worth noting that this whole process can be automated. This is especially useful for Cloud VMs, where provider do not provide NixOS. For instance, nixos-infect uses the lustrate process to convert Digital Ocean droplets to NixOS from other distributions automatically.

### Installing behind a proxy

To install NixOS behind a proxy, do the following before running `nixos-install`.

1. Update proxy configuration in `/mnt/etc/nixos/configuration.nix` to keep the internet accessible after reboot.
  ```
{
  networking.proxy.default = "http://user:password@proxy:port/";
  networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";
}
  ```
2. Setup the proxy environment variables in the shell where you are running `nixos-install`.
  ```
# proxy_url="http://user:password@proxy:port/"
# export http_proxy="$proxy_url"
# export HTTP_PROXY="$proxy_url"
# export https_proxy="$proxy_url"
# export HTTPS_PROXY="$proxy_url"
  ```

### Note

If you are switching networks with different proxy configurations, use the `specialisation` option in `configuration.nix` to switch proxies at runtime. Refer to Appendix A for more information.


## Changing the Configuration

The file `/etc/nixos/configuration.nix` contains the current configuration of your machine. Whenever you’ve changed something in that file, you should do

```
# nixos-rebuild switch
```

to build the new configuration, make it the default configuration for booting, and try to realise the configuration in the running system (e.g., by restarting system services).

### Warning

This command doesn’t start/stop user services automatically. `nixos-rebuild` only runs a `daemon-reload` for each user with running user services.

### Warning

These commands must be executed as root, so you should either run them from a root shell or by prefixing them with `sudo -i`.

You can also do

```
# nixos-rebuild test
```

to build the configuration and switch the running system to it, but without making it the boot default. So if (say) the configuration locks up your machine, you can just reboot to get back to a working configuration.

There is also

```
# nixos-rebuild boot
```

to build the configuration and make it the boot default, but not switch to it now (so it will only take effect after the next reboot).

You can make your configuration show up in a different submenu of the GRUB 2 boot screen by giving it a different *profile name*, e.g.

```
# nixos-rebuild switch -p test
```

which causes the new configuration (and previous ones created using `-p test`) to show up in the GRUB submenu “NixOS - Profile ‘test’”. This can be useful to separate test configurations from “stable” configurations.

A repl, or read-eval-print loop, is also available. You can inspect your configuration and use the Nix language with

```
# nixos-rebuild repl
```

Your configuration is loaded into the `config` variable. Use tab for autocompletion, use the `:r` command to reload the configuration files. See `:?` or `nix repl` in the Nix manual to learn more.

Finally, you can do

```
$ nixos-rebuild build
```

to build the configuration but nothing more. This is useful to see whether everything compiles cleanly.

If you have a machine that supports hardware virtualisation, you can also test the new configuration in a sandbox by building and running a QEMU *virtual machine* that contains the desired configuration. Just do

```
$ nixos-rebuild build-vm
$ ./result/bin/run-*-vm
```

The VM does not have any data from your host system, so your existing user accounts and home directories will not be available unless you have set `mutableUsers = false`. Another way is to temporarily add the following to your configuration:

```
{ users.users.your-user.initialHashedPassword = "test"; }
```

*Important:* delete the $hostname.qcow2 file if you have started the virtual machine at least once without the right users, otherwise the changes will not get picked up. You can forward ports on the host to the guest. For instance, the following will forward host port 2222 to guest port 22 (SSH):

```
$ QEMU_NET_OPTS="hostfwd=tcp:127.0.0.1:2222-:22" ./result/bin/run-*-vm
```

allowing you to log in via SSH (assuming you have set the appropriate passwords or SSH authorized keys):

```
$ ssh -p 2222 localhost
```

Such port forwardings connect via the VM’s virtual network interface. Thus they cannot connect to ports that are only bound to the VM’s loopback interface (`127.0.0.1`), and the VM’s NixOS firewall must be configured to allow these connections.


## Upgrading NixOS

The best way to keep your NixOS installation up to date is to use one of the NixOS *channels*. A channel is a Nix mechanism for distributing Nix expressions and associated binaries. The NixOS channels are updated automatically from NixOS’s Git repository after certain tests have passed and a selection of packages has been built successfully (see `nixos/release-combined.nix` and `nixos/release-small.nix`). These channels are:

- *Stable channels*, such as `nixos-26.05`. These only get conservative bug fixes and package upgrades. For instance, a channel update may cause the Linux kernel on your system to be upgraded from 4.19.34 to 4.19.38 (a minor bug fix), but not from 4.19.x to 4.20.x (a major change that has the potential to break things). Stable channels are generally maintained until the next stable branch is created.
- The *unstable channel*, `nixos-unstable`. This corresponds to NixOS’s main development branch, and may thus see radical changes between channel updates. It’s not recommended for production systems.
- *Small channels*, such as `nixos-26.05-small` or `nixos-unstable-small`. These are identical to the stable and unstable channels described above, except that they contain fewer binary packages. This means they get updated faster than the regular channels (for instance, when a critical security patch is committed to NixOS’s source tree), but may require more packages to be built from source than usual. They’re mostly intended for server environments and as such contain few GUI applications.

To see what channels are available, go to https://channels.nixos.org. (Note that the URIs of the various channels redirect to a directory that contains the channel’s latest version and includes ISO images and VirtualBox appliances.) Please note that during the release process, channels that are not yet released will be present here as well. See the Getting NixOS page https://nixos.org/download/ to find the newest supported stable release.

When you first install NixOS, you’re automatically subscribed to the NixOS channel that corresponds to your installation source. For instance, if you installed from a 26.05 ISO, you will be subscribed to the `nixos-26.05` channel. To see which NixOS channel you’re subscribed to, run the following as root:

```
# nix-channel --list | grep nixos
nixos https://channels.nixos.org/nixos-unstable
```

To switch to a different NixOS channel, do

```
# nix-channel --add https://channels.nixos.org/channel-name nixos
```

(Be sure to include the `nixos` parameter at the end.) For instance, to use the NixOS 26.05 stable channel:

```
# nix-channel --add https://channels.nixos.org/nixos-26.05 nixos
```

If you have a server, you may want to use the “small” channel instead:

```
# nix-channel --add https://channels.nixos.org/nixos-26.05-small nixos
```

And if you want to live on the bleeding edge:

```
# nix-channel --add https://channels.nixos.org/nixos-unstable nixos
```

You can then upgrade NixOS to the latest version in your chosen channel by running

```
# nixos-rebuild switch --upgrade
```

which is equivalent to the more verbose `nix-channel --update nixos; nixos-rebuild switch`.

### Note

Channels are set per user. This means that running `nix-channel --add` as a non root user (or without sudo) will not affect configuration in `/etc/nixos/configuration.nix`

### Warning

It is generally safe to switch back and forth between channels. The only exception is that a newer NixOS may also have a newer Nix version, which may involve an upgrade of Nix’s database schema. This cannot be undone easily, so in that case you will not be able to go back to your original channel.


## Automatic Upgrades

You can keep a NixOS system up-to-date automatically by adding the following to `configuration.nix`:

```
{
  system.autoUpgrade.enable = true;
  system.autoUpgrade.allowReboot = true;
}
```

This enables a periodically executed systemd service named `nixos-upgrade.service`. If the `allowReboot` option is `false`, it runs `nixos-rebuild switch --upgrade` to upgrade NixOS to the latest version in the current channel. (To see when the service runs, see `systemctl list-timers`.) If `allowReboot` is `true`, then the system will automatically reboot if the new generation contains a different kernel, initrd or kernel modules. You can also specify a channel explicitly, e.g.

```
{ system.autoUpgrade.channel = "https://channels.nixos.org/nixos-26.05"; }
```


## Building a NixOS (Live) ISO

Default live installer configurations are available inside `nixos/modules/installer/cd-dvd`. For building other system images, see Building Images with `nixos-rebuild build-image`.

You have two options:

- Use any of those default configurations as is
- Combine them with (any of) your host config(s)

System images, such as the live installer ones, know how to enforce configuration settings on which they immediately depend in order to work correctly.

However, if you are confident, you can opt to override those enforced values with `mkForce`.


## Practical Instructions

To build an ISO image for the channel `nixos-unstable`:

```
$ git clone https://github.com/NixOS/nixpkgs.git
$ cd nixpkgs/nixos
$ git switch nixos-unstable
$ nix-build -A config.system.build.isoImage -I nixos-config=modules/installer/cd-dvd/installation-cd-minimal.nix default.nix
```

To check the content of an ISO image, mount it like so:

```
# mount -o loop -t iso9660 ./result/iso/nixos-image-25.05pre-git-x86_64-linux.iso /mnt/iso
```
