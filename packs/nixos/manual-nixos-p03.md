---
title: "NixOS Manual (part 3/5)"
source: https://nixos.org/manual/nixos/stable/
domain: nixos
license: CC-BY-SA-4.0
tags: nixos distribution, declarative linux distribution, reproducible system configuration, immutable operating system
fetched: 2026-07-02
part: 3/5
---

## Running X without a display manager

It is possible to avoid a display manager entirely and starting the X server manually from a virtual terminal. Add to your configuration:

```
{
  services.xserver.displayManager.startx = {
    enable = true;
    generateScript = true;
  };
}
```

then you can start the X server with the `startx` command.

The second option will generate a base `xinitrc` script that will run your window manager and set up the systemd user session. You can extend the script using the extraCommands option, for example:

```
{
  services.xserver.displayManager.startx = {
    generateScript = true;
    extraCommands = ''
      xrdb -load .Xresources
      xsetroot -solid '#666661'
      xsetroot -cursor_name left_ptr
    '';
  };
}
```

or, alternatively, you can write your own from scratch in `~/.xinitrc`.

In this case, remember you’re responsible for starting the window manager, for example:

```
sxhkd &
bspwm &
```

and if you have enabled some systemd user service, you will probably want to also add these lines too:

```
# import required env variables from the current shell
systemctl --user import-environment DISPLAY XDG_SESSION_ID
# start all graphical user services
systemctl --user start nixos-fake-graphical-session.target
# start the user dbus daemon
dbus-daemon --session --address="unix:path=/run/user/$(id -u)/bus" &
```


## Intel Graphics drivers

The default and recommended driver for Intel Graphics in X.org is `modesetting` (included in the xorg-server package itself). This is a generic driver which uses the kernel mode setting (KMS) mechanism, it supports Glamor (2D graphics acceleration via OpenGL) and is actively maintained, it may perform worse in some cases (like in old chipsets).

There is a second driver, `intel` (provided by the xf86-video-intel package), specific to older Intel iGPUs from generation 2 to 9. It is not recommended by most distributions: it lacks several modern features (for example, it doesn’t support Glamor) and the package hasn’t been officially updated since 2015.

Third generation and older iGPUs (15-20+ years old) are not supported by the `modesetting` driver (X will crash upon startup). Thus, the `intel` driver is required for these chipsets. Otherwise, the results vary depending on the hardware, so you may have to try both drivers. Use the option `services.xserver.videoDrivers` to set one. The recommended configuration for modern systems is:

```
{ services.xserver.videoDrivers = [ "modesetting" ]; }
```

### Note

The `modesetting` driver doesn’t currently provide a `TearFree` option (this will become available in an upcoming X.org release), So, without using a compositor (for example, see `services.picom.enable`) you will experience screen tearing.

If you experience screen tearing no matter what, this configuration was reported to resolve the issue:

```
{
  services.xserver.videoDrivers = [ "intel" ];
  services.xserver.deviceSection = ''
    Option "DRI" "2"
    Option "TearFree" "true"
  '';
}
```

Note that this will likely downgrade the performance compared to `modesetting` or `intel` with DRI 3 (default).


## Proprietary NVIDIA drivers

NVIDIA provides a proprietary driver for its graphics cards that has better 3D performance than the X.org drivers. It is not enabled by default because it’s not free software. You can enable it as follows:

```
{ services.xserver.videoDrivers = [ "nvidia" ]; }
```

If you have an older card, you may have to use one of the legacy drivers:

```
{
  hardware.nvidia.package = config.boot.kernelPackages.nvidiaPackages.legacy_470;
  hardware.nvidia.package = config.boot.kernelPackages.nvidiaPackages.legacy_390;
  hardware.nvidia.package = config.boot.kernelPackages.nvidiaPackages.legacy_340;
}
```

You may need to reboot after enabling this driver to prevent a clash with other kernel modules.


## Touchpads

Support for Synaptics touchpads (found in many laptops such as the Dell Latitude series) can be enabled as follows:

```
{ services.libinput.enable = true; }
```

The driver has many options (see Appendix A). For instance, the following disables tap-to-click behavior:

```
{ services.libinput.touchpad.tapping = false; }
```

Note: the use of `services.xserver.synaptics` is deprecated since NixOS 17.09.


## GTK/Qt themes

GTK themes can be installed either to user profile or system-wide (via `environment.systemPackages`). To make Qt 5 applications look similar to GTK ones, you can use the following configuration:

```
{
  qt.enable = true;
  qt.platformTheme = "gtk2";
  qt.style = "gtk2";
}
```


## Custom XKB layouts

It is possible to install custom XKB keyboard layouts using the option `services.xserver.xkb.extraLayouts`.

As a first example, we are going to create a layout based on the basic US layout, with an additional layer to type some greek symbols by pressing the right-alt key.

Create a file called `us-greek` with the following content (under a directory called `symbols`; it’s an XKB peculiarity that will help with testing):

```
xkb_symbols "us-greek"
{
  include "us(basic)"            // includes the base US keys
  include "level3(ralt_switch)"  // configures right alt as a third level switch

  key <LatA> { [ a, A, Greek_alpha ] };
  key <LatB> { [ b, B, Greek_beta  ] };
  key <LatG> { [ g, G, Greek_gamma ] };
  key <LatD> { [ d, D, Greek_delta ] };
  key <LatZ> { [ z, Z, Greek_zeta  ] };
};
```

A minimal layout specification must include the following:

```
{
  services.xserver.xkb.extraLayouts.us-greek = {
    description = "US layout with alt-gr greek";
    languages = [ "eng" ];
    symbolsFile = /yourpath/symbols/us-greek;
  };
}
```

### Note

The name (after `extraLayouts.`) should match the one given to the `xkb_symbols` block.

Applying this customization requires rebuilding several packages, and a broken XKB file can lead to the X session crashing at login. Therefore, you’re strongly advised to **test your layout before applying it**:

```
$ nix-shell -p xkbcomp
$ setxkbmap -I/yourpath us-greek -print | xkbcomp -I/yourpath - $DISPLAY
```

You can inspect the predefined XKB files for examples:

```
$ echo "$(nix-build --no-out-link '<nixpkgs>' -A xkeyboard-config)/etc/X11/xkb/"
```

Once the configuration is applied, and you did a logout/login cycle, the layout should be ready to use. You can try it by e.g. running `setxkbmap us-greek` and then type `<alt>+a` (it may not get applied in your terminal straight away). To change the default, the usual `services.xserver.xkb.layout` option can still be used.

A layout can have several other components besides `xkb_symbols`, for example we will define new keycodes for some multimedia key and bind these to some symbol.

Use the *xev* utility from `pkgs.xev` to find the codes of the keys of interest, then create a `media-key` file to hold the keycodes definitions

```
xkb_keycodes "media"
{
 <volUp>   = 123;
 <volDown> = 456;
}
```

Now use the newly define keycodes in `media-sym`:

```
xkb_symbols "media"
{
 key.type = "ONE_LEVEL";
 key <volUp>   { [ XF86AudioLowerVolume ] };
 key <volDown> { [ XF86AudioRaiseVolume ] };
}
```

As before, to install the layout do

```
{
  services.xserver.xkb.extraLayouts.media = {
    description = "Multimedia keys remapping";
    languages = [ "eng" ];
    symbolsFile = /path/to/media-key;
    keycodesFile = /path/to/media-sym;
  };
}
```

### Note

The function `pkgs.writeText <filename> <content>` can be useful if you prefer to keep the layout definitions inside the NixOS configuration.

Unfortunately, the Xorg server does not (currently) support setting a keymap directly but relies instead on XKB rules to select the matching components (keycodes, types, …) of a layout. This means that components other than symbols won’t be loaded by default. As a workaround, you can set the keymap using `setxkbmap` at the start of the session with:

```
{
  services.xserver.displayManager.sessionCommands = "setxkbmap -keycodes media";
}
```

If you are manually starting the X server, you should set the argument `-xkbdir /etc/X11/xkb`, otherwise X won’t find your layout files. For example with `xinit` run

```
$ xinit -- -xkbdir /etc/X11/xkb
```

To learn how to write layouts take a look at the XKB documentation . More example layouts can also be found here .


## Wayland

While X11 (see *X Window System*) is still the primary display technology on NixOS, Wayland support is steadily improving. Where X11 separates the X Server and the window manager, on Wayland those are combined: a Wayland Compositor is like an X11 window manager, but also embeds the Wayland ‘Server’ functionality. This means it is sufficient to install a Wayland Compositor such as sway without separately enabling a Wayland server:

```
{ programs.sway.enable = true; }
```

This installs the sway compositor along with some essential utilities. Now you can start sway from the TTY console.

If you are using a wlroots-based compositor, like sway, and want to be able to share your screen, make sure to configure Pipewire using `services.pipewire.enable` and related options.

For more helpful tips and tricks, see the wiki page about Sway.


## GPU acceleration

NixOS provides various APIs that benefit from GPU hardware acceleration, such as VA-API and VDPAU for video playback; OpenGL and Vulkan for 3D graphics; and OpenCL for general-purpose computing. This chapter describes how to set up GPU hardware acceleration (as far as this is not done automatically) and how to verify that hardware acceleration is indeed used.

Most of the aforementioned APIs are agnostic with regards to which display server is used. Consequently, these instructions should apply both to the X Window System and Wayland compositors.


## OpenCL

OpenCL is a general compute API. It is used by various applications such as Blender and Darktable to accelerate certain operations.

OpenCL applications load drivers through the *Installable Client Driver* (ICD) mechanism. In this mechanism, an ICD file specifies the path to the OpenCL driver for a particular GPU family. In NixOS, there are two ways to make ICD files visible to the ICD loader. The first is through the `OCL_ICD_VENDORS` environment variable. This variable can contain a directory which is scanned by the ICL loader for ICD files. For example:

```
$ export \
  OCL_ICD_VENDORS=`nix-build '<nixpkgs>' --no-out-link -A rocmPackages.clr.icd`/etc/OpenCL/vendors/
```

The second mechanism is to add the OpenCL driver package to `hardware.graphics.extraPackages`. This links the ICD file under `/run/opengl-driver`, where it will be visible to the ICD loader.

The proper installation of OpenCL drivers can be verified through the `clinfo` command of the clinfo package. This command will report the number of hardware devices that is found and give detailed information for each device:

```
$ clinfo | head -n3
Number of platforms  1
Platform Name        AMD Accelerated Parallel Processing
Platform Vendor      Advanced Micro Devices, Inc.
```

### AMD

Modern AMD Graphics Core Next (GCN) GPUs are supported through the rocmPackages.clr.icd package. Adding this package to `hardware.graphics.extraPackages` enables OpenCL support:

```
{ hardware.graphics.extraPackages = [ rocmPackages.clr.icd ]; }
```

### Intel

Intel Gen12 and later GPUs are supported by the Intel NEO OpenCL runtime that is provided by the `intel-compute-runtime` package. The previous generations (8,9 and 11), have been moved to the `intel-compute-runtime-legacy1` package. The proprietary Intel OpenCL runtime, in the `intel-ocl` package, is an alternative for Gen7 GPUs.

Both `intel-compute-runtime` packages, as well as the `intel-ocl` package can be added to `hardware.graphics.extraPackages` to enable OpenCL support. For example, for Gen12 and later GPUs, the following configuration can be used:

```
{ hardware.graphics.extraPackages = [ intel-compute-runtime ]; }
```


## Vulkan

Vulkan is a graphics and compute API for GPUs. It is used directly by games or indirectly though compatibility layers like DXVK.

By default, if `hardware.graphics.enable` is enabled, Mesa is installed and provides Vulkan for supported hardware.

Similar to OpenCL, Vulkan drivers are loaded through the *Installable Client Driver* (ICD) mechanism. ICD files for Vulkan are JSON files that specify the path to the driver library and the supported Vulkan version. All successfully loaded drivers are exposed to the application as different GPUs. In NixOS, there are two ways to make ICD files visible to Vulkan applications: an environment variable and a module option.

The way to do this is to add the Vulkan driver package to `hardware.graphics.extraPackages`. This links the ICD file under `/run/opengl-driver`, where it will be visible to the ICD loader.

The proper installation of Vulkan drivers can be verified through the `vulkaninfo` command of the vulkan-tools package. This command will report the hardware devices and drivers found, in this example output amdvlk and radv:

```
$ vulkaninfo | grep GPU
                GPU id  : 0 (Unknown AMD GPU)
                GPU id  : 1 (AMD RADV NAVI10 (LLVM 9.0.1))
     ...
GPU0:
        deviceType     = PHYSICAL_DEVICE_TYPE_DISCRETE_GPU
        deviceName     = Unknown AMD GPU
GPU1:
        deviceType     = PHYSICAL_DEVICE_TYPE_DISCRETE_GPU
```

A simple graphical application that uses Vulkan is `vkcube` from the vulkan-tools package.

### AMD

Modern AMD Graphics Core Next (GCN) GPUs are supported through the RADV driver, which is part of mesa.


## VA-API

VA-API (Video Acceleration API) is an open-source library and API specification, which provides access to graphics hardware acceleration capabilities for video processing.

VA-API drivers are loaded by `libva`. The version in nixpkgs is built to search the opengl driver path, so drivers can be installed in `hardware.graphics.extraPackages`.

VA-API can be tested using:

```
$ nix-shell -p libva-utils --run vainfo
```

### Intel

Modern Intel GPUs use the iHD driver, which can be installed with:

```
{ hardware.graphics.extraPackages = [ intel-media-driver ]; }
```

Older Intel GPUs use the i965 driver, which can be installed with:

```
{ hardware.graphics.extraPackages = [ intel-vaapi-driver ]; }
```


## Common issues

### User permissions

Except where noted explicitly, it should not be necessary to adjust user permissions to use these acceleration APIs. In the default configuration, GPU devices have world-read/write permissions (`/dev/dri/renderD*`) or are tagged as `uaccess` (`/dev/dri/card*`). The access control lists of devices with the `uaccess` tag will be updated automatically when a user logs in through `systemd-logind`. For example, if the user *alice* is logged in, the access control list should look as follows:

```
$ getfacl /dev/dri/card0
# file: dev/dri/card0
# owner: root
# group: video
user::rw-
user:alice:rw-
group::rw-
mask::rw-
other::---
```

If you disabled (this functionality of) `systemd-logind`, you may need to add the user to the `video` group and log in again.

### Mixing different versions of nixpkgs

The *Installable Client Driver* (ICD) mechanism used by OpenCL and Vulkan loads runtimes into its address space using `dlopen`. Mixing an ICD loader mechanism and runtimes from different version of nixpkgs may not work. For example, if the ICD loader uses an older version of glibc than the runtime, the runtime may not be loadable due to missing symbols. Unfortunately, the loader will generally be quiet about such issues.

If you suspect that you are running into library version mismatches between an ICL loader and a runtime, you could run an application with the `LD_DEBUG` variable set to get more diagnostic information. For example, OpenCL can be tested with `LD_DEBUG=files clinfo`, which should report missing symbols.


## Xfce Desktop Environment

To enable the Xfce Desktop Environment, set

```
{
  services.xserver.desktopManager.xfce.enable = true;
  services.displayManager.defaultSession = "xfce";
}
```

Optionally, *picom* can be enabled for nice graphical effects, some example settings:

```
{
  services.picom = {
    enable = true;
    fade = true;
    inactiveOpacity = 0.9;
    shadow = true;
    fadeDelta = 4;
  };
}
```

Some Xfce programs are not installed automatically. To install them manually (system wide), put them into your `environment.systemPackages`.


## Thunar

Thunar (the Xfce file manager) is automatically enabled when Xfce is enabled. To enable Thunar without enabling Xfce, use the configuration option `programs.thunar.enable` instead of adding `pkgs.thunar` to `environment.systemPackages`.

If you’d like to add extra plugins to Thunar, add them to `programs.thunar.plugins`. You shouldn’t just add them to `environment.systemPackages`.


## Troubleshooting

Even after enabling udisks2, volume management might not work. Thunar and/or the desktop takes time to show up. Thunar will spit out this kind of message on start (look at `journalctl --user -b`).

```
Thunar:2410): GVFS-RemoteVolumeMonitor-WARNING **: remote volume monitor with dbus name org.gtk.Private.UDisks2VolumeMonitor is not supported
```

This is caused by some needed GNOME services not running. This is all fixed by enabling “Launch GNOME services on startup” in the Advanced tab of the Session and Startup settings panel. Alternatively, you can run this command to do the same thing.

```
$ xfconf-query -c xfce4-session -p /compat/LaunchGNOME -s true
```

It is necessary to log out and log in again for this to take effect.


## Networking

This section describes how to configure networking components on your NixOS machine.


## NetworkManager

To facilitate network configuration, some desktop environments use NetworkManager. You can enable NetworkManager by setting:

```
{ networking.networkmanager.enable = true; }
```

some desktop managers (e.g., GNOME) enable NetworkManager automatically for you.

All users that should have permission to change network settings must belong to the `networkmanager` group:

```
{ users.users.alice.extraGroups = [ "networkmanager" ]; }
```

NetworkManager is controlled using either `nmcli` or `nmtui` (curses-based terminal user interface). See their manual pages for details on their usage. Some desktop environments (GNOME, KDE) have their own configuration tools for NetworkManager. On XFCE, there is no configuration tool for NetworkManager by default: by enabling `programs.nm-applet.enable`, the graphical applet will be installed and will launch automatically when the graphical session is started.

### Note

`networking.networkmanager` and `networking.wireless` (WPA Supplicant) can be used together if desired. To do this you need to instruct NetworkManager to ignore those interfaces like:

```
{
  networking.networkmanager.unmanaged = [
    "*"
    "except:type:wwan"
    "except:type:gsm"
  ];
}
```

Refer to the option description for the exact syntax and references to external documentation.


## Secure Shell Access

Secure shell (SSH) access to your machine can be enabled by setting:

```
{ services.openssh.enable = true; }
```

By default, root logins using a password are disallowed. They can be disabled entirely by setting `services.openssh.settings.PermitRootLogin` to `"no"`.

You can declaratively specify authorised public keys for a user as follows:

```
{
  users.users.alice.openssh.authorizedKeys.keys = [ "ssh-ed25519 AAAAB3NzaC1kc3MAAACBAPIkGWVEt4..." ];
}
```


## IPv4 Configuration

By default, NixOS uses DHCP (specifically, `dhcpcd`) to automatically configure network interfaces. However, you can configure an interface manually as follows:

```
{
  networking.interfaces.eth0.ipv4.addresses = [
    {
      address = "192.168.1.2";
      prefixLength = 24;
    }
  ];
}
```

Typically you’ll also want to set a default gateway and set of name servers:

```
{
  networking.defaultGateway = "192.168.1.1";
  networking.nameservers = [ "8.8.8.8" ];
}
```

### Note

Addresses and routes for statically configured interfaces and the default gateway are set up by systemd services named `network-addresses-<interface>.service`. The name servers configuration, instead, is performed by `network-local-commands.service` using resolvconf.

### Note

If needed, for example if addresses/routes were added/removed, you can reset the network configuration by running `systemctl restart networking-scripted.target`

The host name is set using `networking.hostName`:

```
{ networking.hostName = "cartman"; }
```

The default host name is `nixos`. Set it to the empty string (`""`) to allow the DHCP server to provide the host name.


## IPv6 Configuration

IPv6 is enabled by default. Stateless address autoconfiguration is used to automatically assign IPv6 addresses to all interfaces, and Privacy Extensions (RFC 4941) are enabled by default. You can adjust the default for this by setting `networking.tempAddresses`. This option may be overridden on a per-interface basis by `networking.interfaces.<name>.tempAddress`. You can disable IPv6 support globally by setting:

```
{ networking.enableIPv6 = false; }
```

You can disable IPv6 on a single interface using a normal sysctl (in this example, we use interface `eth0`):

```
{ boot.kernel.sysctl."net.ipv6.conf.eth0.disable_ipv6" = true; }
```

As with IPv4 networking interfaces are automatically configured via DHCPv6. You can configure an interface manually:

```
{
  networking.interfaces.eth0.ipv6.addresses = [
    {
      address = "fe00:aa:bb:cc::2";
      prefixLength = 64;
    }
  ];
}
```

For configuring a gateway, optionally with explicitly specified interface:

```
{
  networking.defaultGateway6 = {
    address = "fe00::1";
    interface = "enp0s3";
  };
}
```

See the section called “IPv4 Configuration” for similar examples and additional information.


## Firewall

NixOS has a simple stateful firewall that blocks incoming connections and other unexpected packets. The firewall applies to both IPv4 and IPv6 traffic. It is enabled by default. It can be disabled as follows:

```
{ networking.firewall.enable = false; }
```

If the firewall is enabled, you can open specific TCP ports to the outside world:

```
{
  networking.firewall.allowedTCPPorts = [
    80
    443
  ];
}
```

Note that TCP port 22 (ssh) is opened automatically if the SSH daemon is enabled (`services.openssh.enable = true`). UDP ports can be opened through `networking.firewall.allowedUDPPorts`.

To open ranges of TCP ports:

```
{
  networking.firewall.allowedTCPPortRanges = [
    {
      from = 4000;
      to = 4007;
    }
    {
      from = 8000;
      to = 8010;
    }
  ];
}
```

Similarly, UDP port ranges can be opened through `networking.firewall.allowedUDPPortRanges`.


## Wireless Networks

For a desktop installation using NetworkManager (e.g., GNOME or KDE), you should make sure the user is in the `networkmanager` group and you can just configure wireless networks from the Settings app. It is also possible to declare (some) wireless networks from the NixOS configuration with `networking.networkmanager.ensureProfiles.profiles`.

Alternatively, without NetworkManager, you can configure wireless networks using wpa_supplicant by setting

```
{ networking.wireless.enable = true; }
```

By default, wpa_supplicant will manage the first wireless interface that becomes available. It is however recommended to set the desired interface name with `networking.wireless.interfaces`, as it is more reliable.

If multiple interfaces are set, NixOS will create a separate systemd service for each one of them, for example:

```
{
  networking.wireless.interfaces = [
    "wlan0"
    "wlan1"
  ];
}
```

results in `wpa_supplicant-wlan0.service` and `wpa_supplicant-wlan1.service`.

### Declarative configuration

NixOS lets you specify networks declaratively:

```
{
  networking.wireless.networks = {
    # SSID with no spaces or special characters
    echelon = {
      psk = "abcdefgh";
    };
    # SSID with spaces and/or special characters
    "echelon's AP" = {
      psk = "ijklmnop";
    };
    # Hidden SSID
    echelon = {
      hidden = true;
      psk = "qrstuvwx";
    };
    free.wifi = { }; # Public wireless network
  };
}
```

If the network is using WPA2, the pre-shared key (PSK) can be also specified with the `pskRaw` option as 64 hexadecimal digits. This is useful to both obfuscate passwords and make the connection slightly faster, as the key doesn’t need to be derived every time.

The `pskRaw` values can be calculated using the `wpa_passphrase` tool:

```
$ wpa_passphrase ESSID PSK
network={
        ssid="echelon"
        #psk="abcdefgh"
        psk=dca6d6ed41f4ab5a984c9f55f6f66d4efdc720ebf66959810f4329bb391c5435
}
```

```
{
  networking.wireless.networks.echelon = {
    pskRaw = "dca6d6ed41f4ab5a984c9f55f6f66d4efdc720ebf66959810f4329bb391c5435";
  };
}
```

Other wpa_supplicant configuration can be set using the `extraConfig` option, either globally or per-network. For example:

```
{
  networking.wireless.extraConfig = ''
    # Enable MAC address randomization by default
    mac_addr=1
  '';
  networking.wireless.networks.home = {
    psk = "abcdefgh";
    extraConfig = ''
      # Use the real MAC address at home
      mac_addr=0
    '';
  };
}
```

### Note

The generated wpa_supplicant configuration file is linked to `/etc/wpa_supplicant/nixos.conf` for easier inspection.

Be aware that in the previous examples the keys would be written to the Nix store in plain text and readable to every local user. It is recommended to specify secrets (PSKs, passwords, etc.) in a safe way using `networking.wireless.secretsFile` and the `ext:` syntax. For example:

```
{
  networking.wireless.secretsFile = "/run/secrets/wireless.conf";
  networking.wireless.networks = {
    home = {
      pskRaw = "ext:psk_home";
    };
    work.auth = ''
      eap=PEAP
      identity="my-user@example.com"
      password=ext:pass_work
    '';
  };
}
```

where `/run/secrets/wireless.conf` contains

```
psk_home=mypassword
pass_work=myworkpassword
```

### Note

The secrets file should be owned and placed in a location accessible (only) by the `wpa_supplicant` user. Only certain fields support the `ext:` syntax, for example `psk`, `sae_password` and `password`, but not `ssid`.

### Imperative configuration

It can be useful to add a new network without rebuilding the NixOS configuration, particularly if you don’t yet have Internet access. Setting `networking.wireless.userControlled` to `true` will allow users of the `wpa_supplicant` group to configure wpa_supplicant imperatively.

For example, using `wpa_cli` you can add a new network and connect to it as:

```
# wpa_cli
Selected interface 'wlan0'

Interactive mode

> add_network
10
> set_network 10 ssid "echelon"
OK
> set_network 10 psk "abcdefgh"
OK
> select_network 10
OK
```

Note that these changes will be lost when wpa_supplicant is restarted. To make them persistent, the option `networking.wireless.allowAuxiliaryImperativeNetworks` can be set, which allows to use the `save` command in `wpa_cli`, or even directly editing the file `/etc/wpa_supplicant/imperative.conf`.

### Note

Remember that after manually editing `imperative.conf` the wpa_supplicant daemon needs to be restarted:

```
# systemctl restart wpa_supplicant.service
```

or

```
# systemctl restart wpa_supplicant-<interface>.service
```

if `networking.wireless.interfaces` has been set.

### Enterprise networks

Networks with more sophisticated authentication protocols can be configured using the free-form `auth` option, for example:

```
{
  networking.wireless.networks = {
    eduroam.auth = ''
      key_mgmt=WPA-EAP
      eap=PEAP
      identity="alice.smith@example.com"
      password="veryLongPassword$!3"
      ca_cert="/etc/wpa_supplicant/eduroam.pem"
    '';
  };
}
```

For examples and a list of available options, see the wpa_supplicant.conf(5) man page.

### Warning

By default, security hardening measures that limit access to files, devices and network capabilities are applied to the wpa_supplicant daemon.

Certificates and other files supplied here need to be readable by the `wpa_supplicant` user; it is therefore recommended to store them in the `/etc/wpa_supplicant` directory.

If your network authentication protocol requires write access to files, smart cards or TPM devices, you may have to disable security hardening with

```
{ networking.wireless.enableHardening = false; }
```

This setting also applies to networks configured from NetworkManager, unless the WiFi backend in use is not wpa_supplicant.


## Ad-Hoc Configuration

You can use `networking.localCommands` to specify shell commands to be run after the network interfaces have been created, but not necessarily fully configured. This is useful for doing network configuration not covered by the existing NixOS modules. For example, you can create a network namespace and a pair of virtual ethernet devices like this:

```
{
  networking.localCommands = ''
    ip netns add mynet
    ip link add name veth-in type veth peer name veth-out
    ip link set dev veth-out netns mynet
  '';
}
```

### Note

The commands should ideally be idempotent, so it’s recommended to perform cleanups of the state you create (e.g. virtual interfaces), or at least make sure possible failures are handled.


## Renaming network interfaces

NixOS uses the udev predictable naming scheme to assign names to network interfaces. This means that by default cards are not given the traditional names like `eth0` or `eth1`, whose order can change unpredictably across reboots. Instead, relying on physical locations and firmware information, the scheme produces names like `ens1`, `enp2s0`, etc.

These names are predictable but less memorable and not necessarily stable: for example installing new hardware or changing firmware settings can result in a name change. If this is undesirable, for example if you have a single ethernet card, you can revert to the traditional scheme by setting `networking.usePredictableInterfaceNames` to `false`.

### Assigning custom names

In case there are multiple interfaces of the same type, it’s better to assign custom names based on the device hardware address. For example, we assign the name `wan` to the interface with MAC address `52:54:00:12:01:01` using a network link unit:

```
{
  systemd.network.links."10-wan" = {
    matchConfig.PermanentMACAddress = "52:54:00:12:01:01";
    linkConfig.Name = "wan";
  };
}
```

Note that links are directly read by udev, *not networkd*, and will work even if networkd is disabled.

Alternatively, we can use a plain old udev rule:

```
{
  boot.initrd.services.udev.rules = ''
    SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", \
    ATTR{address}=="52:54:00:12:01:01", KERNEL=="eth*", NAME="wan"
  '';
}
```

### Warning

The rule must be installed in the initrd using `boot.initrd.services.udev.rules`, not the usual `services.udev.extraRules` option. This is to avoid race conditions with other programs controlling the interface.


## Linux Kernel

You can override the Linux kernel and associated packages using the option `boot.kernelPackages`. For instance, this selects the Linux 3.10 kernel:

```
{ boot.kernelPackages = pkgs.linuxKernel.packages.linux_3_10; }
```

Note that this not only replaces the kernel, but also packages that are specific to the kernel version, such as the NVIDIA video drivers. This ensures that driver packages are consistent with the kernel.

While `pkgs.linuxKernel.packages` contains all available kernel packages, you may want to use one of the unversioned `pkgs.linuxPackages_*` aliases such as `pkgs.linuxPackages_latest`, that are kept up to date with new versions.

Please note that the current convention in NixOS is to only keep actively maintained kernel versions on both unstable and the currently supported stable release(s) of NixOS. This means that a non-longterm kernel will be removed after it’s abandoned by the kernel developers, even on stable NixOS versions. If you pin your kernel onto a non-longterm version, expect your evaluation to fail as soon as the version is out of maintenance.

A kernel will be removed from nixpkgs when the first batch of stable kernels *after* the final release is published. E.g. when 6.15.11 is the final release of the 6.15 series and is released together with 6.16.3 and 6.12.43, it will be removed on the release of 6.16.4 and 6.12.44. Custom kernel variants such as linux-hardened are also affected by this.

Longterm versions of kernels will be removed before the next stable NixOS that will exceed the maintenance period of the kernel version.

The default Linux kernel configuration should be fine for most users. You can see the configuration of your current kernel with the following command:

```
zcat /proc/config.gz
```

If you want to change the kernel configuration, you can use the `packageOverrides` feature (see the section called “Customising Packages”). For instance, to enable support for the kernel debugger KGDB:

```
{
  nixpkgs.config.packageOverrides =
    pkgs:
    pkgs.lib.recursiveUpdate pkgs {
      linuxKernel.kernels.linux_5_10 = pkgs.linuxKernel.kernels.linux_5_10.override {
        extraConfig = ''
          KGDB y
        '';
      };
    };
}
```

`extraConfig` takes a list of Linux kernel configuration options, one per line. The name of the option should not include the prefix `CONFIG_`. The option value is typically `y`, `n` or `m` (to build something as a kernel module).

Kernel modules for hardware devices are generally loaded automatically by `udev`. You can force a module to be loaded via `boot.kernelModules`, e.g.

```
{
  boot.kernelModules = [
    "fuse"
    "kvm-intel"
    "coretemp"
  ];
}
```

If the module is required early during the boot (e.g. to mount the root file system), you can use `boot.initrd.kernelModules`:

```
{ boot.initrd.kernelModules = [ "cifs" ]; }
```

This causes the specified modules and their dependencies to be added to the initial ramdisk.

Kernel runtime parameters can be set through `boot.kernel.sysctl`, e.g.

```
{ boot.kernel.sysctl."net.ipv4.tcp_keepalive_time" = 120; }
```

sets the kernel’s TCP keepalive time to 120 seconds. To see the available parameters, run `sysctl -a`.


## Building a custom kernel

Please refer to the Nixpkgs manual for the various ways of building a custom kernel.

To use your custom kernel package in your NixOS configuration, set

```
{ boot.kernelPackages = pkgs.linuxPackagesFor yourCustomKernel; }
```


## Rust

The Linux kernel does not have Rust language support enabled by default. For kernel versions 6.7 or newer, experimental Rust support can be enabled. In a NixOS configuration, set:

```
{
  boot.kernelPatches = [
    {
      name = "Rust Support";
      patch = null;
      features = {
        rust = true;
      };
    }
  ];
}
```


## Developing kernel modules

This section was moved to the Nixpkgs manual.


## ZFS

It’s a common issue that the latest stable version of ZFS doesn’t support the latest available Linux kernel. It is recommended to use the latest available LTS that’s compatible with ZFS. Usually this is the default kernel provided by nixpkgs (i.e. `pkgs.linuxPackages`).


## Subversion

Subversion is a centralized version-control system. It can use a variety of protocols for communication between client and server.


## Subversion inside Apache HTTP

This section focuses on configuring a web-based server on top of the Apache HTTP server, which uses WebDAV/DeltaV for communication.

For more information on the general setup, please refer to the the appropriate section of the Subversion book.

To configure, include in `/etc/nixos/configuration.nix` code to activate Apache HTTP, setting `services.httpd.adminAddr` appropriately:

```
{
  services.httpd.enable = true;
  services.httpd.adminAddr = "...";
  networking.firewall.allowedTCPPorts = [
    80
    443
  ];
}
```

For a simple Subversion server with basic authentication, configure the Subversion module for Apache as follows, setting `hostName` and `documentRoot` appropriately, and `SVNParentPath` to the parent directory of the repositories, `AuthzSVNAccessFile` to the location of the `.authz` file describing access permission, and `AuthUserFile` to the password file.

```
{
  services.httpd.extraModules = [
    # note that order is *super* important here
    {
      name = "dav_svn";
      path = "${pkgs.apacheHttpdPackages.subversion}/modules/mod_dav_svn.so";
    }
    {
      name = "authz_svn";
      path = "${pkgs.apacheHttpdPackages.subversion}/modules/mod_authz_svn.so";
    }
  ];
  services.httpd.virtualHosts = {
    "svn" = {
      hostName = HOSTNAME;
      documentRoot = DOCUMENTROOT;
      locations."/svn".extraConfig = ''
        DAV svn
        SVNParentPath REPO_PARENT
        AuthzSVNAccessFile ACCESS_FILE
        AuthName "SVN Repositories"
        AuthType Basic
        AuthUserFile PASSWORD_FILE
        Require valid-user
      '';
    };
  };
}
```

The key `"svn"` is just a symbolic name identifying the virtual host. The `"/svn"` in `locations."/svn".extraConfig` is the path underneath which the repositories will be served.

This page explains how to set up the Subversion configuration itself. This boils down to the following:

Underneath `REPO_PARENT` repositories can be set up as follows:

```
$ svn create REPO_NAME
```

Repository files need to be accessible by `wwwrun`:

```
$ chown -R wwwrun:wwwrun REPO_PARENT
```

The password file `PASSWORD_FILE` can be created as follows:

```
$ htpasswd -cs PASSWORD_FILE USER_NAME
```

Additional users can be set up similarly, omitting the `c` flag:

```
$ htpasswd -s PASSWORD_FILE USER_NAME
```

The file describing access permissions `ACCESS_FILE` will look something like the following:

```
[/]
* = r

[REPO_NAME:/]
USER_NAME = rw
```

The Subversion repositories will be accessible as `http://HOSTNAME/svn/REPO_NAME`.


## GNOME Desktop

GNOME provides a simple, yet full-featured desktop environment with a focus on productivity. Its Mutter compositor supports both Wayland and X server, and the GNOME Shell user interface is fully customizable by extensions.


## Enabling GNOME

All of the core apps, optional apps, games, and core developer tools from GNOME are available.

To enable the GNOME desktop use:

```
{
  services.desktopManager.gnome.enable = true;
  services.displayManager.gdm.enable = true;
}
```

### Note

While it is not strictly necessary to use GDM as the display manager with GNOME, it is recommended, as some features such as screen lock might not work without it.

The default applications used in NixOS are very minimal, inspired by the defaults used in gnome-build-meta.

### GNOME without the apps

If you’d like to only use the GNOME desktop and not the apps, you can disable them with:

```
{ services.gnome.core-apps.enable = false; }
```

and none of them will be installed.

If you’d only like to omit a subset of the core utilities, you can use `environment.gnome.excludePackages`. Note that this mechanism can only exclude core utilities, games and core developer tools.

### Disabling GNOME services

It is also possible to disable many of the core services. For example, if you do not need indexing files, you can disable TinySPARQL with:

```
{
  services.gnome.localsearch.enable = false;
  services.gnome.tinysparql.enable = false;
}
```

Note, however, that doing so is not supported and might break some applications. Notably, GNOME Music cannot work without TinySPARQL.

### GNOME games

You can install all of the GNOME games with:

```
{ services.gnome.games.enable = true; }
```

### GNOME core developer tools

You can install GNOME core developer tools with:

```
{ services.gnome.core-developer-tools.enable = true; }
```


## Enabling GNOME Flashback

GNOME Flashback provides a desktop environment based on the classic GNOME 2 architecture. You can enable the default GNOME Flashback session, which uses the Metacity window manager, with:

```
{ services.desktopManager.gnome.flashback.enableMetacity = true; }
```

It is also possible to create custom sessions that replace Metacity with a different window manager using `services.desktopManager.gnome.flashback.customSessions`.

The following example uses `xmonad` window manager:

```
{
  services.desktopManager.gnome.flashback.customSessions = [
    {
      wmName = "xmonad";
      wmLabel = "XMonad";
      wmCommand = "${pkgs.haskellPackages.xmonad}/bin/xmonad";
      enableGnomePanel = false;
    }
  ];
}
```


## Icons and GTK Themes

Icon themes and GTK themes don’t require any special option to install in NixOS.

You can add them to `environment.systemPackages` and switch to them with GNOME Tweaks. If you’d like to do this manually in dconf, change the values of the following keys:

```
/org/gnome/desktop/interface/gtk-theme
/org/gnome/desktop/interface/icon-theme
```

in `dconf-editor`


## Shell Extensions

Most Shell extensions are packaged under the `gnomeExtensions` attribute. Some packages that include Shell extensions, like `gpaste`, don’t have their extension decoupled under this attribute.

You can install them like any other package:

```
{
  environment.systemPackages = [
    pkgs.gnomeExtensions.dash-to-dock
    pkgs.gnomeExtensions.gsconnect
    pkgs.gnomeExtensions.mpris-indicator-button
  ];
}
```

Unfortunately, we lack a way for these to be managed in a completely declarative way. So you have to enable them manually with an Extensions application. It is possible to use a GSettings override for this on `org.gnome.shell.enabled-extensions`, but that will only influence the default value.


## GSettings Overrides

Majority of software building on the GNOME platform use GLib’s GSettings system to manage runtime configuration. For our purposes, the system consists of XML schemas describing the individual configuration options, stored in the package, and a settings backend, where the values of the settings are stored. On NixOS, like on most Linux distributions, dconf database is used as the backend.

GSettings vendor overrides can be used to adjust the default values for settings of the GNOME desktop and apps by replacing the default values specified in the XML schemas. Using overrides will allow you to pre-seed user settings before you even start the session.

### Warning

Overrides really only change the default values for GSettings keys so if you or an application changes the setting value, the value set by the override will be ignored. Until NixOS’s dconf module implements changing values, you will either need to keep that in mind and clear the setting from the backend using `dconf reset` command when that happens, or use the module from home-manager.

You can override the default GSettings values using the `services.desktopManager.gnome.extraGSettingsOverrides` option.

Take note that whatever packages you want to override GSettings for, you need to add them to `services.desktopManager.gnome.extraGSettingsOverridePackages`.

You can use `dconf-editor` tool to explore which GSettings you can set.

### Example

```
{
  services.desktopManager.gnome = {
    extraGSettingsOverrides = ''
      # Change default background
      [org.gnome.desktop.background]
      picture-uri='file://${pkgs.nixos-artwork.wallpapers.mosaic-blue.gnomeFilePath}'

      # Favorite apps in gnome-shell
      [org.gnome.shell]
      favorite-apps=['org.gnome.Console.desktop', 'org.gnome.Nautilus.desktop']
    '';

    extraGSettingsOverridePackages = [
      pkgs.gsettings-desktop-schemas # for org.gnome.desktop
      pkgs.gnome-shell # for org.gnome.shell
    ];
  };
}
```


## Frequently Asked Questions

### Can I use LightDM with GNOME?

Yes you can, and any other display-manager in NixOS.

However, it doesn’t work correctly for the Wayland session of GNOME Shell yet, and won’t be able to lock your screen.

See this issue.


## Pantheon Desktop

Pantheon is the desktop environment created for the elementary OS distribution. It is written from scratch in Vala, utilizing GNOME technologies with GTK and Granite.


## Enabling Pantheon

All of Pantheon is working in NixOS and the applications should be available, aside from a few exceptions. To enable Pantheon, set

```
{ services.desktopManager.pantheon.enable = true; }
```

This automatically enables LightDM and Pantheon’s LightDM greeter. If you’d like to disable this, set

```
{
  services.xserver.displayManager.lightdm.greeters.pantheon.enable = false;
  services.xserver.displayManager.lightdm.enable = false;
}
```

but please be aware using Pantheon without LightDM as a display manager will break screenlocking from the UI. The NixOS module for Pantheon installs all of Pantheon’s default applications. If you’d like to not install Pantheon’s apps, set

```
{ services.pantheon.apps.enable = false; }
```

You can also use `environment.pantheon.excludePackages` to remove any other app (like `elementary-mail`).


## Wingpanel and Switchboard plugins

Wingpanel and Switchboard work differently than they do in other distributions, as far as using plugins. You cannot install a plugin globally (like with `environment.systemPackages`) to start using it. You should instead be using the following options:

- `services.desktopManager.pantheon.extraWingpanelIndicators`
- `services.desktopManager.pantheon.extraSwitchboardPlugs`

to configure the programs with plugs or indicators.

The difference in NixOS is both these programs are patched to load plugins from a directory that is the value of an environment variable. All of which is controlled in Nix. If you need to configure the particular packages manually you can override the packages like:

```
wingpanel-with-indicators.override {
  indicators = [ pkgs.some-special-indicator ];
}
```

```
switchboard-with-plugs.override { plugs = [ pkgs.some-special-plug ]; }
```

please note that, like how the NixOS options describe these as extra plugins, this would only add to the default plugins included with the programs. If for some reason you’d like to configure which plugins to use exactly, both packages have an argument for this:

```
wingpanel-with-indicators.override {
  useDefaultIndicators = false;
  indicators = specialListOfIndicators;
}
```

```
switchboard-with-plugs.override {
  useDefaultPlugs = false;
  plugs = specialListOfPlugs;
}
```

this could be most useful for testing a particular plug-in in isolation.


## FAQ

**I have switched from a different desktop and Pantheon’s theming looks messed up.**

Open Switchboard and go to: Administration → About → Restore Default Settings → Restore Settings. This will reset any dconf settings to their Pantheon defaults. Note this could reset certain GNOME specific preferences if that desktop was used prior.

**I cannot enable both GNOME and Pantheon.**

This is a known issue and there is no known workaround.

**Does AppCenter work, or is it available?**

AppCenter is available and the Flatpak backend should work so you can install some Flatpak applications using it. However, due to missing appstream metadata, the Packagekit backend does not function currently. See this issue.

If you are using Pantheon, AppCenter should be installed by default if you have Flatpak support enabled. If you also wish to add the `appcenter` Flatpak remote:

```
$ flatpak remote-add --if-not-exists appcenter https://flatpak.elementary.io/repo.flatpakrepo
```


## Xen Project Hypervisor
