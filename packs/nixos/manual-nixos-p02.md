---
title: "NixOS Manual (part 2/5)"
source: https://nixos.org/manual/nixos/stable/
domain: nixos
license: CC-BY-SA-4.0
tags: nixos distribution, declarative linux distribution, reproducible system configuration, immutable operating system
fetched: 2026-07-02
part: 2/5
---

## Additional drivers or firmware

If you need additional (non-distributable) drivers or firmware in the installer, you might want to extend these configurations.

For example, to build the GNOME graphical installer ISO, but with support for certain WiFi adapters present in some MacBooks, you can create the following file at `modules/installer/cd-dvd/installation-cd-graphical-gnome-macbook.nix`:

```
{ config, ... }:

{
  imports = [ ./installation-cd-graphical-gnome.nix ];

  boot.initrd.kernelModules = [ "wl" ];

  boot.kernelModules = [
    "kvm-intel"
    "wl"
  ];
  boot.extraModulePackages = [ config.boot.kernelPackages.broadcom_sta ];
}
```

Then build it like in the example above:

```
$ git clone https://github.com/NixOS/nixpkgs.git
$ cd nixpkgs/nixos
$ export NIXPKGS_ALLOW_UNFREE=1
$ nix-build -A config.system.build.isoImage -I nixos-config=modules/installer/cd-dvd/installation-cd-graphical-gnome-macbook.nix default.nix
```


## Technical Notes

The config value enforcement is implemented via `mkImageMediaOverride = mkOverride 60;` and therefore primes over simple value assignments, but also yields to `mkForce`.

This property allows image designers to implement in semantically correct ways those configuration values upon which the correct functioning of the image depends.

For example, the iso base image overrides those file systems which it needs at a minimum for correct functioning, while the installer base image overrides the entire file system layout because there can’t be any other guarantees on a live medium than those given by the live medium itself. The latter is especially true before formatting the target block device(s). On the other hand, the netboot iso only overrides its minimum dependencies since netboot images are always made-to-target.


## Building Images with `nixos-rebuild build-image`

Nixpkgs contains a variety of modules to build custom images for different virtualization platforms and cloud providers, such as e.g. `amazon-image.nix` and `proxmox-lxc.nix`.

While those can be imported directly, `system.build.images` provides an attribute set mapping variant names to image derivations. Available variants are defined - end extendable - in `image.modules`, an attribute set mapping variant names to NixOS modules.

All of those images can be built via both, their `system.build.image` attribute and the `nixos-rebuild build-image` command.

For example, to build an Amazon image from your existing NixOS configuration, run:

```
$ nixos-rebuild build-image --image-variant amazon
[...]
Done. The disk image can be found in /nix/store/[hash]-nixos-image-amazon-25.05pre-git-x86_64-linux/nixos-image-amazon-25.05pre-git-x86_64-linux.vpc
```

To get a list of all variants available, run `nixos-rebuild build-image` without arguments.

Example 5. Customize specific image variants


## Building Images via `systemd-repart`

You can build disk images in NixOS with the `image.repart` option provided by the module image/repart.nix. This module uses `systemd-repart` to build the images and exposes it’s entire interface via the `repartConfig` option.

An example of how to build an image:

```
{ config, modulesPath, ... }:
{

  imports = [ "${modulesPath}/image/repart.nix" ];

  image.repart = {
    name = "image";
    partitions = {
      "esp" = {
        contents = {
          # ...
        };
        repartConfig = {
          Type = "esp";
          # ...
        };
      };
      "root" = {
        storePaths = [ config.system.build.toplevel ];
        repartConfig = {
          Type = "root";
          Label = "nixos";
          # ...
        };
      };
    };
  };

}
```


## Nix Store Paths

If you want to rewrite Nix store paths, e.g., to remove the `/nix/store` prefix or to nest it below a parent path, you can do that through the `nixStorePrefix` option.

### Nix Store Partition

You can define a partition that only contains the Nix store and then mount it under `/nix/store`. Because the `/nix/store` part of the paths is already determined by the mount point, you have to set `nixStorePrefix = "/"` so that `/nix/store` is stripped from the paths before copying them into the image.

```
{
  fileSystems."/nix/store".device = "/dev/disk/by-partlabel/nix-store";

  image.repart.partitions = {
    "store" = {
      storePaths = [ config.system.build.toplevel ];
      nixStorePrefix = "/";
      repartConfig = {
        Type = "linux-generic";
        Label = "nix-store";
        # ...
      };
    };
  };
}
```

### Nix Store Subvolume

Alternatively, you can create a Btrfs subvolume `/@nix-store` containing the Nix store and mount it on `/nix/store`:

```
{
  fileSystems."/" = {
    device = "/dev/disk/by-partlabel/root";
    fsType = "btrfs";
    options = [ "subvol=/@" ];
  };

  fileSystems."/nix/store" = {
    device = "/dev/disk/by-partlabel/root";
    fsType = "btrfs";
    options = [ "subvol=/@nix-store" ];
  };

  image.repart.partitions = {
    "root" = {
      storePaths = [ config.system.build.toplevel ];
      nixStorePrefix = "/@nix-store";
      repartConfig = {
        Type = "root";
        Label = "root";
        Format = "btrfs";
        Subvolumes = "/@ /@nix-store";
        MakeDirectories = "/@ /@nix-store";
        # ...
      };
    };
  };
}
```


## Appliance Image

The `image/repart.nix` module can also be used to build self-contained software appliances.

The generation based update mechanism of NixOS is not suited for appliances. Updates of appliances are usually either performed by replacing the entire image with a new one or by updating partitions via an A/B scheme. See the Chrome OS update process for an example of how to achieve this. The appliance image built in the following example does not contain a `configuration.nix` and thus you will not be able to call `nixos-rebuild` from this system. Furthermore, it uses a Unified Kernel Image.

```
let
  pkgs = import <nixpkgs> { };
  efiArch = pkgs.stdenv.hostPlatform.efiArch;
in
(pkgs.nixos [
  (
    {
      config,
      lib,
      pkgs,
      modulesPath,
      ...
    }:
    {

      imports = [ "${modulesPath}/image/repart.nix" ];

      boot.loader.grub.enable = false;

      fileSystems."/".device = "/dev/disk/by-label/nixos";

      image.repart = {
        name = "image";
        partitions = {
          "esp" = {
            contents = {
              "/EFI/BOOT/BOOT${lib.toUpper efiArch}.EFI".source =
                "${pkgs.systemd}/lib/systemd/boot/efi/systemd-boot${efiArch}.efi";

              "/EFI/Linux/${config.system.boot.loader.ukiFile}".source =
                "${config.system.build.uki}/${config.system.boot.loader.ukiFile}";
            };
            repartConfig = {
              Type = "esp";
              Format = "vfat";
              SizeMinBytes = "96M";
            };
          };
          "root" = {
            storePaths = [ config.system.build.toplevel ];
            repartConfig = {
              Type = "root";
              Format = "ext4";
              Label = "nixos";
              Minimize = "guess";
            };
          };
        };
      };

    }
  )
]).image
```

# Configuration

This chapter describes how to configure various aspects of a NixOS machine through the configuration file `/etc/nixos/configuration.nix`. As described in *Changing the Configuration*, changes to this file only take effect after you run **nixos-rebuild**.


## Configuration Syntax

The NixOS configuration file `/etc/nixos/configuration.nix` is actually a *Nix expression*, which is the Nix package manager’s purely functional language for describing how to build packages and configurations. This means you have all the expressive power of that language at your disposal, including the ability to abstract over common patterns, which is very useful when managing complex systems. The syntax and semantics of the Nix language are fully described in the Nix manual, but here we give a short overview of the most important constructs useful in NixOS configuration files.


## NixOS Configuration File

The NixOS configuration file generally looks like this:

```
{ config, pkgs, ... }:

{
  # option definitions
}
```

The first line (`{ config, pkgs, ... }:`) denotes that this is actually a function that takes at least the two arguments `config` and `pkgs`. (These are explained later, in chapter *Writing NixOS Modules*) The function returns a *set* of option definitions (`{ ... }`). These definitions have the form `name = value`, where `name` is the name of an option and `value` is its value. For example,

```
{ config, pkgs, ... }:

{
  services.httpd.enable = true;
  services.httpd.adminAddr = "alice@example.org";
  services.httpd.virtualHosts.localhost.documentRoot = "/webroot";
}
```

defines a configuration with three option definitions that together enable the Apache HTTP Server with `/webroot` as the document root.

Sets can be nested, and in fact dots in option names are shorthand for defining a set containing another set. For instance, `services.httpd.enable` defines a set named `services` that contains a set named `httpd`, which in turn contains an option definition named `enable` with value `true`. This means that the example above can also be written as:

```
{ config, pkgs, ... }:

{
  services = {
    httpd = {
      enable = true;
      adminAddr = "alice@example.org";
      virtualHosts = {
        localhost = {
          documentRoot = "/webroot";
        };
      };
    };
  };
}
```

which may be more convenient if you have lots of option definitions that share the same prefix (such as `services.httpd`).

NixOS checks your option definitions for correctness. For instance, if you try to define an option that doesn’t exist (that is, doesn’t have a corresponding *option declaration*), `nixos-rebuild` will give an error like:

```
The option `services.httpd.enable' defined in `/etc/nixos/configuration.nix' does not exist.
```

Likewise, values in option definitions must have a correct type. For instance, `services.httpd.enable` must be a Boolean (`true` or `false`). Trying to give it a value of another type, such as a string, will cause an error:

```
The option value `services.httpd.enable' in `/etc/nixos/configuration.nix' is not a boolean.
```

Options have various types of values. The most important are:

**Strings**

Strings are enclosed in double quotes, e.g.

```
{
  networking.hostName = "dexter";
}
```

Special characters can be escaped by prefixing them with a backslash (e.g. `\"`).

Multi-line strings can be enclosed in *double single quotes*, e.g.

```
{
  networking.extraHosts =
    ''
      127.0.0.2 other-localhost
      10.0.0.1 server
    '';
}
```

The main difference is that it strips from each line a number of spaces equal to the minimal indentation of the string as a whole (disregarding the indentation of empty lines), and that characters like `"` and `\` are not special (making it more convenient for including things like shell code). See more info about this in the Nix manual here.

**Booleans**

These can be `true` or `false`, e.g.

```
{
  networking.firewall.enable = true;
  networking.firewall.allowPing = false;
}
```

**Integers**

For example,

```
{
  boot.kernel.sysctl."net.ipv4.tcp_keepalive_time" = 60;
}
```

(Note that here the attribute name `net.ipv4.tcp_keepalive_time` is enclosed in quotes to prevent it from being interpreted as a set named `net` containing a set named `ipv4`, and so on. This is because it’s not a NixOS option but the literal name of a Linux kernel setting.)

**Sets**

Sets were introduced above. They are name/value pairs enclosed in braces, as in the option definition

```
{
  fileSystems."/boot" =
    { device = "/dev/sda1";
      fsType = "ext4";
      options = [ "rw" "data=ordered" "relatime" ];
    };
}
```

**Lists**

The important thing to note about lists is that list elements are separated by whitespace, like this:

```
{
  boot.kernelModules = [ "fuse" "kvm-intel" "coretemp" ];
}
```

List elements can be any other type, e.g. sets:

```
{
  swapDevices = [ { device = "/dev/disk/by-label/swap"; } ];
}
```

**Packages**

Usually, the packages you need are already part of the Nix Packages collection, which is a set that can be accessed through the function argument `pkgs`. Typical uses:

```
{
  environment.systemPackages =
    [ pkgs.thunderbird
      pkgs.emacs
    ];

  services.postgresql.package = pkgs.postgresql_14;
}
```

The latter option definition changes the default PostgreSQL package used by NixOS’s PostgreSQL service to 14.x. For more information on packages, including how to add new ones, see the section called “Adding Custom Packages”.


## Abstractions

If you find yourself repeating yourself over and over, it’s time to abstract. Take, for instance, this Apache HTTP Server configuration:

```
{
  services.httpd.virtualHosts = {
    "blog.example.org" = {
      documentRoot = "/webroot/blog.example.org";
      adminAddr = "alice@example.org";
      forceSSL = true;
      enableACME = true;
    };
    "wiki.example.org" = {
      documentRoot = "/webroot/wiki.example.org";
      adminAddr = "alice@example.org";
      forceSSL = true;
      enableACME = true;
    };
  };
}
```

It defines two virtual hosts with nearly identical configuration; the only difference is the document root directories. To prevent this duplication, we can use a `let`:

```
let
  commonConfig = {
    adminAddr = "alice@example.org";
    forceSSL = true;
    enableACME = true;
  };
in
{
  services.httpd.virtualHosts = {
    "blog.example.org" = (commonConfig // { documentRoot = "/webroot/blog.example.org"; });
    "wiki.example.org" = (commonConfig // { documentRoot = "/webroot/wiki.example.org"; });
  };
}
```

The `let commonConfig = ...` defines a variable named `commonConfig`. The `//` operator merges two attribute sets, so the configuration of the second virtual host is the set `commonConfig` extended with the document root option.

You can write a `let` wherever an expression is allowed. Thus, you also could have written:

```
{
  services.httpd.virtualHosts =
    let
      commonConfig = {
        # ...
      };
    in
    {
      "blog.example.org" = (
        commonConfig
        // {
          # ...
        }
      );
      "wiki.example.org" = (
        commonConfig
        // {
          # ...
        }
      );
    };
}
```

but not `{ let commonConfig = ...; in ...; }` since attributes (as opposed to attribute values) are not expressions.

**Functions** provide another method of abstraction. For instance, suppose that we want to generate lots of different virtual hosts, all with identical configuration except for the document root. This can be done as follows:

```
{
  services.httpd.virtualHosts =
    let
      makeVirtualHost = webroot: {
        documentRoot = webroot;
        adminAddr = "alice@example.org";
        forceSSL = true;
        enableACME = true;
      };
    in
    {
      "example.org" = (makeVirtualHost "/webroot/example.org");
      "example.com" = (makeVirtualHost "/webroot/example.com");
      "example.gov" = (makeVirtualHost "/webroot/example.gov");
      "example.nl" = (makeVirtualHost "/webroot/example.nl");
    };
}
```

Here, `makeVirtualHost` is a function that takes a single argument `webroot` and returns the configuration for a virtual host. That function is then called for several names to produce the list of virtual host configurations.


## Modularity

The NixOS configuration mechanism is modular. If your `configuration.nix` becomes too big, you can split it into multiple files. Likewise, if you have multiple NixOS configurations (e.g. for different computers) with some commonality, you can move the common configuration into a shared file.

Modules have exactly the same syntax as `configuration.nix`. In fact, `configuration.nix` is itself a module. You can use other modules by including them from `configuration.nix`, e.g.:

```
{ config, pkgs, ... }:

{
  imports = [
    ./vpn.nix
    ./kde.nix
  ];
  services.httpd.enable = true;
  environment.systemPackages = [ pkgs.emacs ];
  # ...
}
```

Here, we include two modules from the same directory, `vpn.nix` and `kde.nix`. The latter might look like this:

```
{ config, pkgs, ... }:

{
  services.xserver.enable = true;
  services.displayManager.sddm.enable = true;
  services.desktopManager.plasma6.enable = true;
  environment.systemPackages = [ pkgs.vim ];
}
```

Note that both `configuration.nix` and `kde.nix` define the option `environment.systemPackages`. When multiple modules define an option, NixOS will try to *merge* the definitions. In the case of `environment.systemPackages` the lists of packages will be concatenated. The value in `configuration.nix` is merged last, so for list-type options, it will appear at the end of the merged list. If you want it to appear first, you can use `mkBefore`:

```
{ boot.kernelModules = mkBefore [ "kvm-intel" ]; }
```

This causes the `kvm-intel` kernel module to be loaded before any other kernel modules.

For other types of options, a merge may not be possible. For instance, if two modules define `services.httpd.adminAddr`, `nixos-rebuild` will give an error:

```
The unique option `services.httpd.adminAddr' is defined multiple times, in `/etc/nixos/httpd.nix' and `/etc/nixos/configuration.nix'.
```

When that happens, it’s possible to force one definition take precedence over the others:

```
{ services.httpd.adminAddr = pkgs.lib.mkForce "bob@example.org"; }
```

When using multiple modules, you may need to access configuration values defined in other modules. This is what the `config` function argument is for: it contains the complete, merged system configuration. That is, `config` is the result of combining the configurations returned by every module. (If you’re wondering how it’s possible that the (indirect) *result* of a function is passed as an *input* to that same function: that’s because Nix is a “lazy” language — it only computes values when they are needed. This works as long as no individual configuration value depends on itself.)

For example, here is a module that adds some packages to `environment.systemPackages` only if `services.xserver.enable` is set to `true` somewhere else:

```
{ config, pkgs, ... }:

{
  environment.systemPackages =
    if config.services.xserver.enable then
      [
        pkgs.firefox
        pkgs.thunderbird
      ]
    else
      [ ];
}
```

With multiple modules, it may not be obvious what the final value of a configuration option is. The command `nixos-option` allows you to find out:

```
$ nixos-option services.xserver.enable
true

$ nixos-option boot.kernelModules
[ "tun" "ipv6" "loop" ... ]
```

Interactive exploration of the configuration is possible using `nix repl`, a read-eval-print loop for Nix expressions. A typical use:

```
$ nix repl -f '<nixpkgs/nixos>'

nix-repl> config.networking.hostName
"mandark"

nix-repl> map (x: x.hostName) config.services.httpd.virtualHosts
[ "example.org" "example.gov" ]
```

While abstracting your configuration, you may find it useful to generate modules using code, instead of writing files. The example below would have the same effect as importing a file which sets those options.

```
{ config, pkgs, ... }:

let
  netConfig = hostName: {
    networking.hostName = hostName;
    networking.useDHCP = false;
  };

in
{
  imports = [ (netConfig "nixos.localdomain") ];
}
```


## Package Management

This section describes how to add additional packages to your system. NixOS has two distinct styles of package management:

- *Declarative*, where you declare what packages you want in your `configuration.nix`. Every time you run `nixos-rebuild`, NixOS will ensure that you get a consistent set of binaries corresponding to your specification.
- *Ad hoc*, where you install, upgrade and uninstall packages via the `nix-env` command. This style allows mixing packages from different Nixpkgs versions. It’s the only choice for non-root users.


## Declarative Package Management

With declarative package management, you specify which packages you want on your system by setting the option `environment.systemPackages`. For instance, adding the following line to `configuration.nix` enables the Mozilla Thunderbird email application:

```
{ environment.systemPackages = [ pkgs.thunderbird ]; }
```

The effect of this specification is that the Thunderbird package from Nixpkgs will be built or downloaded as part of the system when you run `nixos-rebuild switch`.

### Note

Some packages require additional global configuration such as D-Bus or systemd service registration so adding them to `environment.systemPackages` might not be sufficient. You are advised to check the list of options whether a NixOS module for the package does not exist.

You can get a list of the available packages as follows:

```
$ nix-env -qaP '*' --description
nixos.firefox   firefox-23.0   Mozilla Firefox - the browser, reloaded
...
```

The first column in the output is the *attribute name*, such as `nixos.thunderbird`.

Note: the `nixos` prefix tells us that we want to get the package from the `nixos` channel and works only in CLI tools. In declarative configuration, use `pkgs` prefix (variable).

To “uninstall” a package, remove it from `environment.systemPackages` and run `nixos-rebuild switch`.

### Customising Packages

The Nixpkgs configuration for a NixOS system is set by the `nixpkgs.config` option.

Example 6. Globally allow unfree packages

Some packages in Nixpkgs have options to enable or disable optional functionality, or change other aspects of the package.

### Warning

Unfortunately, Nixpkgs currently lacks a way to query available package configuration options.

### Note

For example, many packages come with extensions one might add. Examples include:

- `passExtensions.pass-otp`
- `python312Packages.requests`

You can use them like this:

```
{
  environment.systemPackages = with pkgs; [
    sl
    (pass.withExtensions (
      subpkgs: with subpkgs; [
        pass-audit
        pass-otp
        pass-genphrase
      ]
    ))
    (python3.withPackages (subpkgs: with subpkgs; [ requests ]))
    cowsay
  ];
}
```

Apart from high-level options, it’s possible to tweak a package in almost arbitrary ways, such as changing or disabling dependencies of a package. For instance, the Emacs package in Nixpkgs by default has a dependency on GTK 2. If you want to build it against GTK 3, you can specify that as follows:

```
{ environment.systemPackages = [ (pkgs.emacs.override { gtk = pkgs.gtk3; }) ]; }
```

The function `override` performs the call to the Nix function that produces Emacs, with the original arguments amended by the set of arguments specified by you. So here the function argument `gtk` gets the value `pkgs.gtk3`, causing Emacs to depend on GTK 3. (The parentheses are necessary because in Nix, function application binds more weakly than list construction, so without them, `environment.systemPackages` would be a list with two elements.)

Even greater customisation is possible using the function `overrideAttrs`. While the `override` mechanism above overrides the arguments of a package function, `overrideAttrs` allows changing the *attributes* passed to `mkDerivation`. This permits changing any aspect of the package, such as the source code. For instance, if you want to override the source code of Emacs, you can say:

```
{
  environment.systemPackages = [
    (pkgs.emacs.overrideAttrs (oldAttrs: {
      name = "emacs-25.0-pre";
      src = /path/to/my/emacs/tree;
    }))
  ];
}
```

Here, `overrideAttrs` takes the Nix derivation specified by `pkgs.emacs` and produces a new derivation in which the original’s `name` and `src` attribute have been replaced by the given values by re-calling `stdenv.mkDerivation`. The original attributes are accessible via the function argument, which is conventionally named `oldAttrs`.

The overrides shown above are not global. They do not affect the original package; other packages in Nixpkgs continue to depend on the original rather than the customised package. This means that if another package in your system depends on the original package, you end up with two instances of the package. If you want to have everything depend on your customised instance, you can apply a *global* override as follows:

```
{
  nixpkgs.config.packageOverrides = pkgs: {
    emacs = pkgs.emacs.override { gtk = pkgs.gtk3; };
  };
}
```

The effect of this definition is essentially equivalent to modifying the `emacs` attribute in the Nixpkgs source tree. Any package in Nixpkgs that depends on `emacs` will be passed your customised instance. (However, the value `pkgs.emacs` in `nixpkgs.config.packageOverrides` refers to the original rather than overridden instance, to prevent an infinite recursion.)

### Adding Custom Packages

It’s possible that a package you need is not available in NixOS. In that case, you can do two things. Either you can package it with Nix, or you can try to use prebuilt packages from upstream. Due to the peculiarities of NixOS, it is important to note that building software from source is often easier than using pre-built executables.

#### Building with Nix

This can be done either in-tree or out-of-tree. For an in-tree build, you can clone the Nixpkgs repository, add the package to your clone, and (optionally) submit a patch or pull request to have it accepted into the main Nixpkgs repository. This is described in detail in the Nixpkgs manual. In short, you clone Nixpkgs:

```
$ git clone https://github.com/NixOS/nixpkgs
$ cd nixpkgs
```

Then you write and test the package as described in the Nixpkgs manual. Finally, you add it to `environment.systemPackages`, e.g.

```
{ environment.systemPackages = [ pkgs.my-package ]; }
```

and you run `nixos-rebuild`, specifying your own Nixpkgs tree:

```
# nixos-rebuild switch -I nixpkgs=/path/to/my/nixpkgs
```

The second possibility is to add the package outside of the Nixpkgs tree. For instance, here is how you specify a build of the GNU Hello package directly in `configuration.nix`:

```
{
  environment.systemPackages =
    let
      my-hello =
        with pkgs;
        stdenv.mkDerivation rec {
          name = "hello-2.8";
          src = fetchurl {
            url = "mirror://gnu/hello/${name}.tar.gz";
            hash = "sha256-5rd/gffPfa761Kn1tl3myunD8TuM+66oy1O7XqVGDXM=";
          };
        };
    in
    [ my-hello ];
}
```

Of course, you can also move the definition of `my-hello` into a separate Nix expression, e.g.

```
{ environment.systemPackages = [ (import ./my-hello.nix) ]; }
```

where `my-hello.nix` contains:

```
with import <nixpkgs> { }; # bring all of Nixpkgs into scope

stdenv.mkDerivation rec {
  name = "hello-2.8";
  src = fetchurl {
    url = "mirror://gnu/hello/${name}.tar.gz";
    hash = "sha256-5rd/gffPfa761Kn1tl3myunD8TuM+66oy1O7XqVGDXM=";
  };
}
```

This allows testing the package easily:

```
$ nix-build my-hello.nix
$ ./result/bin/hello
Hello, world!
```

#### Using pre-built executables

Most pre-built executables will not work on NixOS. There are two notable exceptions: flatpaks and AppImages. For flatpaks see the dedicated section. AppImages can run “as-is” on NixOS.

First you need to enable AppImage support: add to `/etc/nixos/configuration.nix`

```
{
  programs.appimage.enable = true;
  programs.appimage.binfmt = true;
}
```

Then you can run the AppImage “as-is” or with `appimage-run foo.appimage`.

If there are shared libraries missing add them with

```
{
  programs.appimage.package = pkgs.appimage-run.override {
    extraPkgs = pkgs: [
      # missing libraries here, e.g.: `pkgs.libepoxy`
    ];
  };
}
```

To make other pre-built executables work on NixOS, you need to package them with Nix and special helpers like `autoPatchelfHook` or `buildFHSEnv`. See the Nixpkgs manual for details. This is complex and often doing a source build is easier.


## Ad-Hoc Package Management

With the command `nix-env`, you can install and uninstall packages from the command line. For instance, to install Mozilla Thunderbird:

```
$ nix-env -iA nixos.thunderbird
```

If you invoke this as root, the package is installed in the Nix profile `/nix/var/nix/profiles/default` and visible to all users of the system; otherwise, the package ends up in `/nix/var/nix/profiles/per-user/username/profile` and is not visible to other users. The `-A` flag specifies the package by its attribute name; without it, the package is installed by matching against its package name (e.g. `thunderbird`). The latter is slower because it requires matching against all available Nix packages, and is ambiguous if there are multiple matching packages.

Packages come from the NixOS channel. You typically upgrade a package by updating to the latest version of the NixOS channel:

```
$ nix-channel --update nixos
```

and then running `nix-env -i` again. Other packages in the profile are *not* affected; this is the crucial difference with the declarative style of package management, where running `nixos-rebuild switch` causes all packages to be updated to their current versions in the NixOS channel. You can however upgrade all packages for which there is a newer version by doing:

```
$ nix-env -u '*'
```

A package can be uninstalled using the `-e` flag:

```
$ nix-env -e thunderbird
```

Finally, you can roll back an undesirable `nix-env` action:

```
$ nix-env --rollback
```

`nix-env` has many more flags. For details, see the nix-env(1) manpage or the Nix manual.


## User Management

NixOS supports both declarative and imperative styles of user management. In the declarative style, users are specified in `configuration.nix`. For instance, the following states that a user account named `alice` shall exist:

```
{
  users.users.alice = {
    isNormalUser = true;
    home = "/home/alice";
    description = "Alice Foobar";
    extraGroups = [
      "wheel"
      "networkmanager"
    ];
    openssh.authorizedKeys.keys = [ "ssh-dss AAAAB3Nza... alice@foobar" ];
  };
}
```

Note that `alice` is a member of the `wheel` and `networkmanager` groups, which allows her to use `sudo` to execute commands as `root` and to configure the network, respectively. Also note the SSH public key that allows remote logins with the corresponding private key. Users created in this way do not have a password by default, so they cannot log in via mechanisms that require a password. However, you can use the `passwd` program to set a password, which is retained across invocations of `nixos-rebuild`.

If you set `users.mutableUsers` to false, then the contents of `/etc/passwd` and `/etc/group` will be congruent to your NixOS configuration. For instance, if you remove a user from `users.users` and run nixos-rebuild, the user account will cease to exist. Also, imperative commands for managing users and groups, such as useradd, are no longer available. Passwords may still be assigned by setting the user’s hashedPassword option. A hashed password can be generated using `mkpasswd`.

A user ID (uid) is assigned automatically. You can also specify a uid manually by adding

```
{ uid = 1000; }
```

to the user specification.

Groups can be specified similarly. The following states that a group named `students` shall exist:

```
{ users.groups.students.gid = 1000; }
```

As with users, the group ID (gid) is optional and will be assigned automatically if it’s missing.

In the imperative style, users and groups are managed by commands such as `useradd`, `groupmod` and so on. For instance, to create a user account named `alice`:

```
# useradd -m alice
```

To make all nix tools available to this new user use `su - USER` which opens a login shell (==shell that loads the profile) for given user. This will create the ~/.nix-defexpr symlink. So run:

```
# su - alice -c "true"
```

The flag `-m` causes the creation of a home directory for the new user, which is generally what you want. The user does not have an initial password and therefore cannot log in. A password can be set using the `passwd` utility:

```
# passwd alice
Enter new UNIX password: ***
Retype new UNIX password: ***
```

A user can be deleted using `userdel`:

```
# userdel -r alice
```

The flag `-r` deletes the user’s home directory. Accounts can be modified using `usermod`. Unix groups can be managed using `groupadd`, `groupmod` and `groupdel`.


## Create users and groups with `systemd-sysusers`

### Note

This is experimental.

Please consider using Userborn over systemd-sysusers as it’s more feature complete.

Instead of using a custom perl script to create users and groups, you can use systemd-sysusers:

```
{ systemd.sysusers.enable = true; }
```

The primary benefit of this is to remove a dependency on perl.


## Manage users and groups with `userborn`

### Note

This is experimental.

Like systemd-sysusers, Userborn doesn’t depend on Perl but offers some more advantages over systemd-sysusers:

1. It can create “normal” users (with a GID >= 1000).
2. It can update some information about users. Most notably it can update their passwords.
3. It will warn when users use an insecure or unsupported password hashing scheme.

Userborn is the recommended way to manage users if you don’t want to rely on the Perl script. It aims to eventually replace the Perl script by default.

You can enable Userborn via:

```
{ services.userborn.enable = true; }
```

You can configure Userborn to store the password files (`/etc/{group,passwd,shadow}`) outside of `/etc` and symlink them from this location to `/etc`:

```
{ services.userborn.passwordFilesLocation = "/persistent/etc"; }
```

This is useful when you store `/etc` on a `tmpfs` or if `/etc` is immutable (e.g. when using `system.etc.overlay.mutable = false;`). In the latter case the original files are by default stored in `/var/lib/nixos`.

Userborn implements immutable users by re-mounting the password files read-only. This means that unlike when using the Perl script, trying to add a new user (e.g. via `useradd`) will fail right away.


## Restrict usage time

Timekpr-nExT is a screen time managing application that helps optimizing time spent at computer for your subordinates, children or even for yourself.

You can enable it via:

```
{ services.timekpr.enable = true; }
```

This will install the `timekpr` package and start the `timekpr` service. You can then use the `timekpra` application to configure time limits for users.


## File Systems

You can define file systems using the `fileSystems` configuration option. For instance, the following definition causes NixOS to mount the Ext4 file system on device `/dev/disk/by-label/data` onto the mount point `/data`:

```
{
  fileSystems."/data" = {
    device = "/dev/disk/by-label/data";
    fsType = "ext4";
  };
}
```

This will create an entry in `/etc/fstab`, which will generate a corresponding systemd.mount unit via systemd-fstab-generator. The filesystem will be mounted automatically unless `"noauto"` is present in options. `"noauto"` filesystems can be mounted explicitly using `systemctl` e.g. `systemctl start data.mount`. Mount points are created automatically if they don’t already exist. For `device`, it’s best to use the topology-independent device aliases in `/dev/disk/by-label` and `/dev/disk/by-uuid`, as these don’t change if the topology changes (e.g. if a disk is moved to another IDE controller).

You can usually omit the file system type (`fsType`), since `mount` can usually detect the type and load the necessary kernel module automatically. However, if the file system is needed at early boot (in the initial ramdisk) and is not `ext2`, `ext3` or `ext4`, then it’s best to specify `fsType` to ensure that the kernel module is available.

### Note

System startup will fail if any of the filesystems fails to mount, dropping you to the emergency shell. You can make a mount asynchronous and non-critical by adding `options = [ "nofail" ];`.


## LUKS-Encrypted File Systems

NixOS supports file systems that are encrypted using *LUKS* (Linux Unified Key Setup). For example, here is how you create an encrypted Ext4 file system on the device `/dev/disk/by-uuid/3f6b0024-3a44-4fde-a43a-767b872abe5d`:

```
# cryptsetup luksFormat /dev/disk/by-uuid/3f6b0024-3a44-4fde-a43a-767b872abe5d

WARNING!
========
This will overwrite data on /dev/disk/by-uuid/3f6b0024-3a44-4fde-a43a-767b872abe5d irrevocably.

Are you sure? (Type uppercase yes): YES
Enter LUKS passphrase: ***
Verify passphrase: ***

# cryptsetup luksOpen /dev/disk/by-uuid/3f6b0024-3a44-4fde-a43a-767b872abe5d crypted
Enter passphrase for /dev/disk/by-uuid/3f6b0024-3a44-4fde-a43a-767b872abe5d: ***

# mkfs.ext4 /dev/mapper/crypted
```

The LUKS volume should be automatically picked up by `nixos-generate-config`, but you might want to verify that your `hardware-configuration.nix` looks correct. To manually ensure that the system is automatically mounted at boot time as `/`, add the following to `configuration.nix`:

```
{
  boot.initrd.luks.devices.crypted.device = "/dev/disk/by-uuid/3f6b0024-3a44-4fde-a43a-767b872abe5d";
  fileSystems."/".device = "/dev/mapper/crypted";
}
```

Should grub be used as bootloader, and `/boot` is located on an encrypted partition, it is necessary to add the following grub option:

```
{ boot.loader.grub.enableCryptodisk = true; }
```

### FIDO2

NixOS also supports unlocking your LUKS-Encrypted file system using a FIDO2 compatible token.

#### Without systemd in initrd

In the following example, we will create a new FIDO2 credential and add it as a new key to our existing device `/dev/sda2`:

```
# export FIDO2_LABEL="/dev/sda2 @ $HOSTNAME"
# fido2luks credential "$FIDO2_LABEL"
f1d00200108b9d6e849a8b388da457688e3dd653b4e53770012d8f28e5d3b269865038c346802f36f3da7278b13ad6a3bb6a1452e24ebeeaa24ba40eef559b1b287d2a2f80b7

# fido2luks -i add-key /dev/sda2 f1d00200108b9d6e849a8b388da457688e3dd653b4e53770012d8f28e5d3b269865038c346802f36f3da7278b13ad6a3bb6a1452e24ebeeaa24ba40eef559b1b287d2a2f80b7
Password:
Password (again):
Old password:
Old password (again):
Added to key to device /dev/sda2, slot: 2
```

To ensure that this file system is decrypted using the FIDO2 compatible key, add the following to `configuration.nix`:

```
{
  boot.initrd.luks.fido2Support = true;
  boot.initrd.luks.devices."/dev/sda2".fido2.credential =
    "f1d00200108b9d6e849a8b388da457688e3dd653b4e53770012d8f28e5d3b269865038c346802f36f3da7278b13ad6a3bb6a1452e24ebeeaa24ba40eef559b1b287d2a2f80b7";
}
```

You can also use the FIDO2 passwordless setup, but for security reasons, you might want to enable it only when your device is PIN protected, such as Trezor.

```
{ boot.initrd.luks.devices."/dev/sda2".fido2.passwordLess = true; }
```

#### systemd Stage 1

If systemd stage 1 is enabled, it handles unlocking of LUKS-encrypted volumes during boot. The following example enables systemd stage1 and adds support for unlocking the existing LUKS2 volume `root` using any enrolled FIDO2 compatible tokens.

```
{
  boot.initrd = {
    luks.devices.root = {
      crypttabExtraOpts = [ "fido2-device=auto" ];
      device = "/dev/sda2";
    };
    systemd.enable = true;
  };
}
```

All tokens that should be used for unlocking the LUKS2-encrypted volume must first be enrolled using systemd-cryptenroll. In the following example, a new key slot for the first discovered token is added to the LUKS volume.

```
# systemd-cryptenroll --fido2-device=auto /dev/sda2
```

Existing key slots are left intact, unless `--wipe-slot=` is specified. It is recommended to add a recovery key that should be stored in a secure physical location and can be entered wherever a password would be entered.

```
# systemd-cryptenroll --recovery-key /dev/sda2
```


## SSHFS File Systems

SSHFS is a FUSE filesystem that allows easy access to directories on a remote machine using the SSH File Transfer Protocol (SFTP). It means that if you have SSH access to a machine, no additional setup is needed to mount a directory.

### Interactive mounting

In NixOS, SSHFS is packaged as `sshfs`. Once installed, mounting a directory interactively is simple as running:

```
$ sshfs my-user@example.com:/my-dir /mnt/my-dir
```

Like any other FUSE file system, the directory is unmounted using:

```
$ fusermount -u /mnt/my-dir
```

### Non-interactive mounting

Mounting non-interactively requires some precautions because `sshfs` will run at boot and under a different user (root). For obvious reason, you can’t input a password, so public key authentication using an unencrypted key is needed. To create a new key without a passphrase you can do:

```
$ ssh-keygen -t ed25519 -P '' -f example-key
Generating public/private ed25519 key pair.
Your identification has been saved in example-key
Your public key has been saved in example-key.pub
The key fingerprint is:
SHA256:yjxl3UbTn31fLWeyLYTAKYJPRmzknjQZoyG8gSNEoIE my-user@workstation
```

To keep the key safe, change the ownership to `root:root` and make sure the permissions are `600`: OpenSSH normally refuses to use the key if it’s not well-protected.

The file system can be configured in NixOS via the usual fileSystems option. Here’s a typical setup:

```
{
  fileSystems."/mnt/my-dir" = {
    device = "my-user@example.com:/my-dir/";
    fsType = "sshfs";
    options = [
      # Filesystem options
      "allow_other" # for non-root access
      "_netdev" # this is a network fs
      "x-systemd.automount" # mount on demand

      # SSH options
      "reconnect" # handle connection drops
      "ServerAliveInterval=15" # keep connections alive
      "IdentityFile=/var/secrets/example-key"
    ];
  };
}
```

More options from `ssh_config(5)` can be given as well, for example you can change the default SSH port or specify a jump proxy:

```
{
  options = [
    "ProxyJump=bastion@example.com"
    "Port=22"
  ];
}
```

It’s also possible to change the `ssh` command used by SSHFS to connect to the server. For example:

```
{
  options = [
    (builtins.replaceStrings [ " " ] [ "\\040" ]
      "ssh_command=${pkgs.openssh}/bin/ssh -v -L 8080:localhost:80"
    )
  ];

}
```

### Note

The escaping of spaces is needed because every option is written to the `/etc/fstab` file, which is a space-separated table.

#### Troubleshooting

If you’re having a hard time figuring out why mounting is failing, you can add the option `"debug"`. This enables a verbose log in SSHFS that you can access via:

```
$ journalctl -u $(systemd-escape -p /mnt/my-dir/).mount
Jun 22 11:41:18 workstation mount[87790]: SSHFS version 3.7.1
Jun 22 11:41:18 workstation mount[87793]: executing <ssh> <-x> <-a> <-oClearAllForwardings=yes> <-oServerAliveInterval=15> <-oIdentityFile=/var/secrets/wrong-key> <-2> <my-user@example.com> <-s> <sftp>
Jun 22 11:41:19 workstation mount[87793]: my-user@example.com: Permission denied (publickey).
Jun 22 11:41:19 workstation mount[87790]: read: Connection reset by peer
Jun 22 11:41:19 workstation systemd[1]: mnt-my\x2ddir.mount: Mount process exited, code=exited, status=1/FAILURE
Jun 22 11:41:19 workstation systemd[1]: mnt-my\x2ddir.mount: Failed with result 'exit-code'.
Jun 22 11:41:19 workstation systemd[1]: Failed to mount /mnt/my-dir.
Jun 22 11:41:19 workstation systemd[1]: mnt-my\x2ddir.mount: Consumed 54ms CPU time, received 2.3K IP traffic, sent 2.7K IP traffic.
```

### Note

If the mount point contains special characters it needs to be escaped using `systemd-escape`. This is due to the way systemd converts paths into unit names.


## Overlayfs

NixOS offers a convenient abstraction to create both read-only as well writable overlays.

```
{
  fileSystems = {
    "/writable-overlay" = {
      overlay = {
        lowerdir = [ writableOverlayLowerdir ];
        upperdir = "/.rw-writable-overlay/upper";
        workdir = "/.rw-writable-overlay/work";
      };
      # Mount the writable overlay in the initrd.
      neededForBoot = true;
    };
    "/readonly-overlay".overlay.lowerdir = [
      writableOverlayLowerdir
      writableOverlayLowerdir2
    ];
  };
}
```

If `upperdir` and `workdir` are not null, they will be created before the overlay is mounted.

To mount an overlay as read-only, you need to provide at least two `lowerdir`s.


## X Window System

The X Window System (X11) provides the basis of NixOS’ graphical user interface. It can be enabled as follows:

```
{ services.xserver.enable = true; }
```

The X server will automatically detect and use the appropriate video driver from a set of X.org drivers (such as `vesa` and `intel`). You can also specify a driver manually, e.g.

```
{ services.xserver.videoDrivers = [ "r128" ]; }
```

to enable X.org’s `xf86-video-r128` driver.

You also need to enable at least one desktop or window manager. Otherwise, you can only log into a plain undecorated `xterm` window. Thus you should pick one or more of the following lines:

```
{
  services.desktopManager.plasma6.enable = true;
  services.xserver.desktopManager.xfce.enable = true;
  services.desktopManager.gnome.enable = true;
  services.xserver.desktopManager.mate.enable = true;
  services.xserver.windowManager.xmonad.enable = true;
  services.xserver.windowManager.twm.enable = true;
  services.xserver.windowManager.icewm.enable = true;
  services.xserver.windowManager.i3.enable = true;
  services.xserver.windowManager.herbstluftwm.enable = true;
}
```

NixOS’s default *display manager* (the program that provides a graphical login prompt and manages the X server) is LightDM. You can select an alternative one by picking one of the following lines:

```
{
  services.displayManager.sddm.enable = true;
  services.displayManager.gdm.enable = true;
}
```

You can set the keyboard layout (and optionally the layout variant):

```
{
  services.xserver.xkb.layout = "de";
  services.xserver.xkb.variant = "neo";
}
```

The X server is started automatically at boot time. If you don’t want this to happen, you can set:

```
{ services.xserver.autorun = false; }
```

The X server can then be started manually:

```
# systemctl start display-manager.service
```

On 64-bit systems, if you want OpenGL for 32-bit programs such as in Wine, you should also set the following:

```
{ hardware.graphics.enable32Bit = true; }
```


## Auto-login

The x11 login screen can be skipped entirely, automatically logging you into your window manager and desktop environment when you boot your computer.

This is especially helpful if you have disk encryption enabled. Since you already have to provide a password to decrypt your disk, entering a second password to login can be redundant.

To enable auto-login, you need to define your default window manager and desktop environment. If you wanted no desktop environment and i3 as your your window manager, you’d define:

```
{ services.displayManager.defaultSession = "none+i3"; }
```

Every display manager in NixOS supports auto-login, here is an example using lightdm for a user `alice`:

```
{
  services.xserver.displayManager.lightdm.enable = true;
  services.displayManager.autoLogin.enable = true;
  services.displayManager.autoLogin.user = "alice";
}
```
