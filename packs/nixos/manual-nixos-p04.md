---
title: "NixOS Manual (part 4/5)"
source: https://nixos.org/manual/nixos/stable/
domain: nixos
license: CC-BY-SA-4.0
tags: nixos distribution, declarative linux distribution, reproducible system configuration, immutable operating system
fetched: 2026-07-02
part: 4/5
---

## Introduction

The **Xen Project Hypervisor** is an open-source type-1 virtual machine manager which allows multiple virtual machines, known as *domains*, to run concurrently with the host on the physical machine. This is unlike a typical type-2 hypervisor, such as QEMU, where the virtual machines run as applications on top of the host. NixOS runs as the privileged *Domain 0*, and can paravirtualise (PV Mode) or fully virtualise (HVM Mode) unprivileged domains (`domUs`).

Xen is security-supported in NixOS. All Xen Security Advisories are patched within hours of release, and generally reach the binary cache channels within a couple of days.


## Domain 0 Installation

Xen may be used as a Domain 0 since NixOS 24.11, using the `virtualisation.xen.enable` option. There are various hardware and software requirements to running a Xen Domain 0; the module is configured to prevent running Xen on a NixOS system that does not meet the software requirements. (i.e. a NixOS system that uses the legacy, scripted initial ramdisk.) The module does not yet check if the hardware requirements are met: please manually ensure that the target machine supports SLAT and IOMMU, the latter being required only for non-PV domains to be virtualised.

The boot menu on a Xen-enabled NixOS system will show duplicate entries for each generation: one boots a normal NixOS system, and the other boots into the Xen Project Hypervisor. The `systemd-boot` and Limine bootloaders are the only supported boot methods at this time.

Xen may be managed through various frontend configuration systems. `libxenlight` is one such configuration system, and is built into all Xen systems. The `xl` command is the primary command-line interface to `libxenlight`, and is capable of managing a NixOS Domain 0.


## Unprivileged Domain Installation

Known generically as guests, unprivileged domains running NixOS may import the `xen-domU.nix` profile in their configurations to automatically enable various recommended optimisations which are relevant for unprivileged domains.

Example 7. Import the Xen Unprivileged Domain profile into a NixOS configuration


## tpm2-totp with Plymouth

tpm2-totp attests the trustworthiness of a device against a human using time-based one-time passwords. This module uses a `tpm2-totp` configuration to display a TOTP at boot using Plymouth.


## Quick start

### 1. Enable modules

```
{
  boot.plymouth.tpm2-totp.enable = true;

  # Plymouth and systemd initrd/stage-1 are required:
  boot.plymouth.enable = true;
  boot.initrd.systemd.enable = true;
}
```

Switch to the new configuration before proceeding to the next step.

### 2. Configure `tpm2-totp`

Generate a new TOTP secret and save the secret in your chosen authenticator app. See `man tpm2-totp` for commands and configuration examples.

More information, including security considerations, can be found in the `README.md` in the tpm2-totp repository. Be sure to select the tag for the version of `tpm2-totp` you have installed.

### 3. Check configuration

Reboot and you should see the TOTP appear on the Plymouth boot screen. The TOTP should match the code displayed in your authenticator app (or the code immediately before/after).


## External Bootloader Backends

NixOS has support for several bootloader backends by default: systemd-boot, grub, uboot, etc. The built-in bootloader backend support is generic and supports most use cases. Some users may prefer to create advanced workflows around managing the bootloader and bootable entries.

You can replace the built-in bootloader support with your own tooling using the “external” bootloader option.

Imagine you have created a new package called FooBoot. FooBoot provides a program at `${pkgs.fooboot}/bin/fooboot-install` which takes the system closure’s path as its only argument and configures the system’s bootloader.

You can enable FooBoot like this:

```
{ pkgs, ... }:
{
  boot.loader.external = {
    enable = true;
    installHook = "${pkgs.fooboot}/bin/fooboot-install";
  };
}
```


## Developing Custom Bootloader Backends

Bootloaders should use RFC-0125’s Bootspec format and synthesis tools to identify the key properties for bootable system generations.


## Clevis

Clevis is a framework for automated decryption of resources. Clevis allows for secure unattended disk decryption during boot, using decryption policies that must be satisfied for the data to decrypt.


## Create a JWE file containing your secret

The first step is to embed your secret in a JWE file. JWE files have to be created through the clevis command line. 3 types of policies are supported:

1. TPM policies

Secrets are pinned against the presence of a TPM2 device, for example:

```
echo -n hi | clevis encrypt tpm2 '{}' > hi.jwe
```

1. Tang policies

Secrets are pinned against the presence of a Tang server, for example:

```
echo -n hi | clevis encrypt tang '{"url": "http://tang.local"}' > hi.jwe
```

1. Shamir Secret Sharing

Using Shamir’s Secret Sharing (sss), secrets are pinned using a combination of the two preceding policies. For example:

```
echo -n hi | clevis encrypt sss \
'{"t": 2, "pins": {"tpm2": {"pcr_ids": "0"}, "tang": {"url": "http://tang.local"}}}' \
> hi.jwe
```

For more complete documentation on how to generate a secret with clevis, see the clevis documentation.


## Activate unattended decryption of a resource at boot

In order to activate unattended decryption of a resource at boot, enable the `clevis` module:

```
{ boot.initrd.clevis.enable = true; }
```

Then, specify the device you want to decrypt using a given clevis secret. Clevis will automatically try to decrypt the device at boot and will fallback to interactive unlocking if the decryption policy is not fulfilled.

```
{ boot.initrd.clevis.devices."/dev/nvme0n1p1".secretFile = ./nvme0n1p1.jwe; }
```

Only `bcachefs`, `zfs` and `luks` encrypted devices are supported at this time.


## Garage

Garage is an open-source, self-hostable S3 store, simpler than MinIO, for geodistributed stores. The server setup can be automated using services.garage. A client configured to your local Garage instance is available in the global environment as `garage-manage`.


## General considerations on upgrades

Garage provides a cookbook documentation on how to upgrade: https://garagehq.deuxfleurs.fr/documentation/cookbook/upgrading/

### Warning

Garage has two types of upgrades: patch-level upgrades and minor/major version upgrades.

In all cases, you should read the changelog and ideally test the upgrade on a staging cluster.

Checking the health of your cluster can be achieved using `garage-manage repair`.

- **Straightforward upgrades (patch-level upgrades).** Upgrades must be performed one by one, i.e. for each node, stop it, upgrade it : change stateVersion or services.garage.package, restart it if it was not already by switching.
- **Multiple version upgrades.** Garage do not provide any guarantee on moving more than one major-version forward. E.g., if you’re on `0.9`, you cannot upgrade to `2.0`. You need to upgrade to `1.2` first. As long as stateVersion is declared properly, this is enforced automatically. The module will issue a warning to remind the user to upgrade to latest Garage *after* that deploy.


## Advanced upgrades (minor/major version upgrades)

Here are some baseline instructions to handle advanced upgrades in Garage, when in doubt, please refer to upstream instructions.

- Disable API and web access to Garage.
- Perform `garage-manage repair --all-nodes --yes tables` and `garage-manage repair --all-nodes --yes blocks`.
- Verify the resulting logs and check that data is synced properly between all nodes. If you have time, do additional checks (`scrub`, `block_refs`, etc.).
- Check if queues are empty by `garage-manage stats` or through monitoring tools.
- Run `systemctl stop garage` to stop the actual Garage version.
- Backup the metadata folder of ALL your nodes, e.g. for a metadata directory (the default one) in `/var/lib/garage/meta`, you can run `pushd /var/lib/garage; tar -acf meta-v0.7.tar.zst meta/; popd`.
- Run the offline migration: `nix-shell -p garage_1 --run "garage offline-repair --yes"`, this can take some time depending on how many objects are stored in your cluster.
- Bump Garage version in your NixOS configuration, either by changing stateVersion or bumping services.garage.package, this should restart Garage automatically.
- Perform `garage-manage repair --all-nodes --yes tables` and `garage-manage repair --all-nodes --yes blocks`.
- Wait for a full table sync to run.

Your upgraded cluster should be in a working state, re-enable API and web access.


## Maintainer information

As stated in the previous paragraph, we must provide a clean upgrade-path for Garage since it cannot move more than one major version forward on a single upgrade. This chapter adds some notes how Garage updates should be rolled out in the future. This is inspired from how Nextcloud does it.

While patch-level updates are no problem and can be done directly in the package-expression (and should be backported to supported stable branches after that), major-releases should be added in a new attribute (e.g. Garage `v3.0.0` should be available in `nixpkgs` as `pkgs.garage_3`). To provide simple upgrade paths it’s generally useful to backport those as well to stable branches. As long as the package-default isn’t altered, this won’t break existing setups. After that, the versioning-warning in the `garage`-module should be updated to make sure that the package-option selects the latest version on fresh setups.

If major-releases will be abandoned by upstream, we should check first if those are needed in NixOS for a safe upgrade-path before removing those. In that case we should keep those packages, but mark them as insecure in an expression like this (in `<nixpkgs/pkgs/tools/filesystem/garage/default.nix>`):

```
# ...
{
  garage_1_2_0 = generic {
    version = "1.2.0";
    sha256 = "0000000000000000000000000000000000000000000000000000";
    eol = true;
  };
}
```

Ideally we should make sure that it’s possible to jump two NixOS versions forward: i.e. the warnings and the logic in the module should guard a user to upgrade from a Garage on e.g. 22.11 to a Garage on 23.11.


## YouTrack

YouTrack is a browser-based bug tracker, issue tracking system and project management software.


## Installation

YouTrack exposes a web GUI installer on first login. You need a token to access it. You can find this token in the log of the `youtrack` service. The log line looks like

```
* JetBrains YouTrack 2023.3 Configuration Wizard will be available on [http://127.0.0.1:8090/?wizard_token=somelongtoken] after start
```


## Upgrade from 2022.3 to 2023.x

Starting with YouTrack 2023.1, JetBrains no longer distributes it as as JAR. The new distribution with the JetBrains Launcher as a ZIP changed the basic data structure and also some configuration parameters. Check out https://www.jetbrains.com/help/youtrack/server/YouTrack-Java-Start-Parameters.html for more information on the new configuration options. When upgrading to YouTrack 2023.1 or higher, a migration script will move the old state directory to `/var/lib/youtrack/2022_3` as a backup. A one-time manual update is required:

1. Before you update take a backup of your YouTrack instance!
2. Migrate the options you set in `services.youtrack.extraParams` and `services.youtrack.jvmOpts` to `services.youtrack.generalParameters` and `services.youtrack.environmentalParameters` (see the examples and the YouTrack docs)
3. To start the upgrade set `services.youtrack.package = pkgs.youtrack`
4. YouTrack then starts in upgrade mode, meaning you need to obtain the wizard token as above
5. Select you want to **Upgrade** YouTrack
6. As source you select `/var/lib/youtrack/2022_3/teamsysdata/` (adopt if you have a different state path)
7. Change the data directory location to `/var/lib/youtrack/data/`. The other paths should already be right.

If you migrate a larger YouTrack instance, it might be useful to set `-Dexodus.entityStore.refactoring.forceAll=true` in `services.youtrack.generalParameters` for the first startup of YouTrack 2023.x.


## Szurubooru

An image board engine dedicated for small and medium communities.


## Configuration

By default the module will execute Szurubooru server only, the web client only contains static files that can be reached via a reverse proxy.

Here is a basic configuration:

```
{
  services.szurubooru = {
    enable = true;

    server = {
      port = 8080;

      settings = {
        domain = "https://szurubooru.domain.tld";
        secretFile = /path/to/secret/file;
      };
    };

    database = {
      passwordFile = /path/to/secret/file;
    };
  };
}
```


## Reverse proxy configuration

The preferred method to run this service is behind a reverse proxy not to expose an open port. For example, here is a minimal Nginx configuration:

```
{
  services.szurubooru = {
    enable = true;

    server = {
      port = 8080;
      # ...
    };

    # ...
  };

  services.nginx.virtualHosts."szurubooru.domain.tld" = {
    locations = {
      "/api/".proxyPass = "http://localhost:8080/";
      "/data/".root = config.services.szurubooru.dataDir;
      "/" = {
        root = config.services.szurubooru.client.package;
        tryFiles = "$uri /index.htm";
      };
    };
  };
}
```


## Extra configuration

Not all configuration options of the server are available directly in this module, but you can add them in `services.szurubooru.server.settings`:

```
{
  services.szurubooru = {
    enable = true;

    server.settings = {
      domain = "https://szurubooru.domain.tld";
      delete_source_files = "yes";
      contact_email = "example@domain.tld";
    };
  };
}
```

You can find all of the options in the default config file available here.


## Suwayomi-Server

A free and open source manga reader server that runs extensions built for Tachiyomi.


## Basic usage

By default, the module will execute Suwayomi-Server backend and web UI:

```
{ ... }:

{
  services.suwayomi-server = {
    enable = true;
  };
}
```

It runs in the systemd service named `suwayomi-server` in the data directory `/var/lib/suwayomi-server`.

You can change the default parameters with some other parameters:

```
{ ... }:

{
  services.suwayomi-server = {
    enable = true;

    dataDir = "/var/lib/suwayomi"; # Default is "/var/lib/suwayomi-server"
    openFirewall = true;

    settings = {
      server.port = 4567;
    };
  };
}
```

If you want to create a desktop icon, you can activate the system tray option:

```
{ ... }:

{
  services.suwayomi-server = {
    enable = true;

    dataDir = "/var/lib/suwayomi"; # Default is "/var/lib/suwayomi-server"
    openFirewall = true;

    settings = {
      server.port = 4567;
      server.enableSystemTray = true;
    };
  };
}
```


## Basic authentication

You can configure a basic authentication to the web interface with:

```
{ ... }:

{
  services.suwayomi-server = {
    enable = true;

    openFirewall = true;

    settings = {
      server.port = 4567;
      server = {
        basicAuthEnabled = true;
        basicAuthUsername = "username";

        # NOTE: this is not a real upstream option
        basicAuthPasswordFile = ./path/to/the/password/file;
      };
    };
  };
}
```


## Extra configuration

Not all the configuration options are available directly in this module, but you can add the other options of suwayomi-server with:

```
{ ... }:

{
  services.suwayomi-server = {
    enable = true;

    openFirewall = true;

    settings = {
      server = {
        port = 4567;
        autoDownloadNewChapters = false;
        maxSourcesInParallel = 6;
        extensionRepos = [
          "https://raw.githubusercontent.com/MY_ACCOUNT/MY_REPO/repo/index.min.json"
        ];
      };
    };
  };
}
```


## strfry

strfry is a relay for the nostr protocol.


## Basic usage

By default, the module will execute strfry:

```
{ ... }:

{
  services.strfry.enable = true;
}
```

It runs in the systemd service named `strfry`.


## Reverse Proxy

You can configure nginx as a reverse proxy with:

```
{ ... }:

{
  security.acme = {
    acceptTerms = true;
    defaults.email = "foo@bar.com";
  };

  services.nginx.enable = true;
  services.nginx.virtualHosts."strfry.example.com" = {
    addSSL = true;
    enableACME = true;
    locations."/" = {
      proxyPass = "http://127.0.0.1:${toString config.services.strfry.settings.relay.port}";
      proxyWebsockets = true; # nostr uses websockets
    };
  };

  services.strfry.enable = true;
}
```


## Plausible

Plausible is a privacy-friendly alternative to Google analytics.


## Basic Usage

At first, a secret key is needed to be generated. This can be done with e.g.

```
$ openssl rand -base64 64
```

After that, `plausible` can be deployed like this:

```
{
  services.plausible = {
    enable = true;
    server = {
      baseUrl = "http://analytics.example.org";
      # secretKeybaseFile is a path to the file which contains the secret generated
      # with openssl as described above.
      secretKeybaseFile = "/run/secrets/plausible-secret-key-base";
    };
  };
}
```


## Pi-hole Web Dashboard

The Pi-hole suite provides a web GUI for controlling and monitoring pihole-FTL.


## Configuration

Example configuration:

```
{
  services.pihole-web = {
    enable = true;
    ports = [ 80 ];
  };
}
```

The dashboard can be configured using `services.pihole-ftl.settings`, in particular the `webserver` subsection.


## Pict-rs

pict-rs is a a simple image hosting service.


## Quickstart

the minimum to start pict-rs is

```
{ services.pict-rs.enable = true; }
```

this will start the http server on port 8080 by default.


## Usage

pict-rs offers the following endpoints:

- `POST /image` for uploading an image. Uploaded content must be valid multipart/form-data with an image array located within the `images[]` keyThis endpoint returns the following JSON structure on success with a 201 Created status
  ```
{
    "files": [
        {
            "delete_token": "JFvFhqJA98",
            "file": "lkWZDRvugm.jpg"
        },
        {
            "delete_token": "kAYy9nk2WK",
            "file": "8qFS0QooAn.jpg"
        },
        {
            "delete_token": "OxRpM3sf0Y",
            "file": "1hJaYfGE01.jpg"
        }
    ],
    "msg": "ok"
}
  ```
- `GET /image/download?url=...` Download an image from a remote server, returning the same JSON payload as the `POST` endpoint
- `GET /image/original/{file}` for getting a full-resolution image. `file` here is the `file` key from the `/image` endpoint’s JSON
- `GET /image/details/original/{file}` for getting the details of a full-resolution image. The returned JSON is structured like so:
  ```
{
    "width": 800,
    "height": 537,
    "content_type": "image/webp",
    "created_at": [
        2020,
        345,
        67376,
        394363487
    ]
}
  ```
- `GET /image/process.{ext}?src={file}&...` get a file with transformations applied. existing transformations include`identity=true`: apply no changes`blur={float}`: apply a gaussian blur to the file`thumbnail={int}`: produce a thumbnail of the image fitting inside an `{int}` by `{int}` square using raw pixel sampling`resize={int}`: produce a thumbnail of the image fitting inside an `{int}` by `{int}` square using a Lanczos2 filter. This is slower than sampling but looks a bit better in some cases`crop={int-w}x{int-h}`: produce a cropped version of the image with an `{int-w}` by `{int-h}` aspect ratio. The resulting crop will be centered on the image. Either the width or height of the image will remain full-size, depending on the image’s aspect ratio and the requested aspect ratio. For example, a 1600x900 image cropped with a 1x1 aspect ratio will become 900x900. A 1600x1100 image cropped with a 16x9 aspect ratio will become 1600x900.Supported `ext` file extensions include `png`, `jpg`, and `webp`An example of usage could bewhich would create a 256x256px JPEG thumbnail and blur it
  ```
GET /image/process.jpg?src=asdf.png&thumbnail=256&blur=3.0
  ```
- `GET /image/details/process.{ext}?src={file}&...` for getting the details of a processed image. The returned JSON is the same format as listed for the full-resolution details endpoint.
- `DELETE /image/delete/{delete_token}/{file}` or `GET /image/delete/{delete_token}/{file}` to delete a file, where `delete_token` and `file` are from the `/image` endpoint’s JSON


## Missing

- Configuring the secure-api-key is not included yet. The envisioned basic use case is consumption on localhost by other services without exposing the service to the internet.


## OpenCloud

OpenCloud is an open-source, modern file-sync and sharing platform. It is a fork of oCIS, a ground-up rewrite of the well-known PHP-based NextCloud server.

The service can be configured using a combination of `services.opencloud.settings`, `services.opencloud.environment` and `services.opencloud.environmentFile`.


## Basic usage

OpenCloud is configured using a combination of YAML and environment variables. The full documentation can be found at OpenCloud Admin Docs.

The general flow of configuring OpenCloud is:

- configure services with `services.opencloud.settings.<service>` when possible
- configure global settings that affect multiple services via `services.opencloud.environment`
- allow NixOS to provision a default `opencloud.yaml` for you, containing default credentials for communication between the microservices
- provide additional secrets via `environmentFile`, provisioned out of band

Please note that current NixOS module for OpenCloud is configured to run in `fullstack` mode, which starts all the services for OpenCloud in a single instance, in so called supervised mode. This will start multiple OpenCloud services and listen on multiple other ports.

Current known services and their ports are as below:

| Service | Group | Port |
|---|---|---|
| gateway | api | 9142 |
| sharing | api | 9150 |
| app-registry | api | 9242 |
| ocdav | web | 45023 |
| auth-machine | api | 9166 |
| storage-system | api | 9215 |
| webdav | web | 9115 |
| webfinger | web | 46871 |
| storage-system | web | 9216 |
| web | web | 9100 |
| eventhistory | api | 33177 |
| ocs | web | 9110 |
| storage-publiclink | api | 9178 |
| settings | web | 9190 |
| ocm | api | 9282 |
| settings | api | 9191 |
| ocm | web | 9280 |
| app-provider | api | 9164 |
| storage-users | api | 9157 |
| auth-service | api | 9199 |
| thumbnails | web | 9186 |
| thumbnails | api | 9185 |
| storage-shares | api | 9154 |
| sse | sse | 46833 |
| userlog | userlog | 45363 |
| search | api | 9220 |
| proxy | web | 9200 |
| idp | web | 9130 |
| frontend | web | 9140 |
| groups | api | 9160 |
| graph | graph | 9120 |
| users | api | 9144 |
| auth-basic | api | 9146 |


## Nextcloud

Nextcloud is an open-source, self-hostable cloud platform. The server setup can be automated using services.nextcloud. A desktop client is packaged at `pkgs.nextcloud-client`.

The current default by NixOS is `nextcloud33` which is also the latest major version available.


## Basic usage

Nextcloud is a PHP-based application which requires an HTTP server (`services.nextcloud` and optionally supports `services.nginx`).

For the database, you can set `services.nextcloud.config.dbtype` to either `sqlite` (the default), `mysql`, or `pgsql`. The simplest is `sqlite`, which will be automatically created and managed by the application. For the last two, you can easily create a local database by setting `services.nextcloud.database.createLocally` to `true`, Nextcloud will automatically be configured to connect to it through socket.

A very basic configuration may look like this:

```
{ pkgs, ... }:
{
  services.nextcloud = {
    enable = true;
    hostName = "nextcloud.tld";
    database.createLocally = true;
    config = {
      dbtype = "pgsql";
      adminpassFile = "/path/to/admin-pass-file";
    };
  };

  networking.firewall.allowedTCPPorts = [
    80
    443
  ];
}
```

The `hostName` option is used internally to configure an HTTP server using `PHP-FPM` and `nginx`. The `config` attribute set is used by the imperative installer and all values are written to an additional file to ensure that changes can be applied by changing the module’s options.

In case the application serves multiple domains (those are checked with `$_SERVER['HTTP_HOST']`) it’s needed to add them to `services.nextcloud.settings.trusted_domains`.

Auto updates for Nextcloud apps can be enabled using `services.nextcloud.autoUpdateApps`.


## `nextcloud-occ`

The management command `occ` can be invoked by using the `nextcloud-occ` wrapper that’s globally available on a system with Nextcloud enabled.

It requires elevated permissions to become the `nextcloud` user. Given the way the privilege escalation is implemented, parameters passed via the environment to Nextcloud are currently ignored, except for `OC_PASS` and `NC_PASS`.

### Warning

When Polkit is enabled, the command being executed by `nextcloud-occ` might be logged into the system’s journal. Be careful to not leak secrets that way!

Custom service units that need to run `nextcloud-occ` either need elevated privileges or the systemd configuration from `nextcloud-setup.service` (recommended):

```
{ config, ... }:
{
  systemd.services.my-custom-service = {
    script = ''
      nextcloud-occ …
    '';
    serviceConfig = {
      inherit (config.systemd.services.nextcloud-cron.serviceConfig)
        User
        LoadCredential
        KillMode
        ;
    };
  };
}
```

Please note that the options required are subject to change. Please make sure to read the release notes when upgrading.


## Common problems

- **General notes.** Unfortunately Nextcloud appears to be very stateful when it comes to managing its own configuration. The config file lives in the home directory of the `nextcloud` user (by default `/var/lib/nextcloud/config/config.php`) and is also used to track several states of the application (e.g., whether installed or not).All configuration parameters are also stored in `/var/lib/nextcloud/config/override.config.php` which is generated by the module and linked from the store to ensure that all values from `config.php` can be modified by the module. However `config.php` manages the application’s state and shouldn’t be touched manually because of that.WarningDon’t delete `config.php`! This file tracks the application’s state and a deletion can cause unwanted side-effects!WarningDon’t rerun `nextcloud-occ maintenance:install`! This command tries to install the application and can cause unwanted side-effects!
- **Multiple version upgrades.** Nextcloud doesn’t allow to move more than one major-version forward. E.g., if you’re on `v16`, you cannot upgrade to `v18`, you need to upgrade to `v17` first. This is ensured automatically as long as the stateVersion is declared properly. In that case the oldest version available (one major behind the one from the previous NixOS release) will be selected by default and the module will generate a warning that reminds the user to upgrade to latest Nextcloud *after* that deploy.
- **`Error: Command "upgrade" is not defined.`** This error usually occurs if the initial installation (**nextcloud-occ maintenance:install**) has failed. After that, the application is not installed, but the upgrade is attempted to be executed. Further context can be found in NixOS/nixpkgs#111175.First of all, it makes sense to find out what went wrong by looking at the logs of the installation via **journalctl -u nextcloud-setup** and try to fix the underlying issue.If this occurs on an *existing* setup, this is most likely because the maintenance mode is active. It can be deactivated by running **nextcloud-occ maintenance:mode --off**. It’s advisable though to check the logs first on why the maintenance mode was activated.WarningOnly perform the following measures on *freshly installed instances!*A re-run of the installer can be forced by *deleting* `/var/lib/nextcloud/config/config.php`. This is the only time advisable because the fresh install doesn’t have any state that can be lost. In case that doesn’t help, an entire re-creation can be forced via **rm -rf ~nextcloud/**.
- **Server-side encryption.** Nextcloud supports server-side encryption (SSE). This is not an end-to-end encryption, but can be used to encrypt files that will be persisted to external storage such as S3.
- **Issues with file permissions / unsafe path transitions**systemd-tmpfiles(8) makes sure that the paths forconfiguration (including declarative config)dataapp storehome directory itself (usually `/var/lib/nextcloud`)are properly set up. However, `systemd-tmpfiles` will refuse to do so if it detects an unsafe path transition, i.e. creating files/directories within a directory that is neither owned by `root` nor by `nextcloud`, the owning user of the files/directories to be created.Symptoms of that include`config/override.config.php` not being updated (and the config file eventually being garbage-collected).failure to read from application data.To work around that, please make sure that all directories in question are owned by `nextcloud:nextcloud`.
- **`Failed to open stream: No such file or directory` after deploys**Symptoms are errors like this after a deployment that disappear after a few minutes:This can happen if `services.nextcloud.secretFile` or `services.nextcloud.config.dbpassFile` are managed by sops-nix.Here, `/run/secrets/nextcloud_secrets` is a symlink to `/run/secrets.d/N/nextcloud_secrets`. The `N` will be incremented when the sops-nix activation script runs, i.e. `/run/secrets.d/N` doesn’t exist anymore after a deploy, only `/run/secrets.d/N+1`.PHP maintains a cache for `realpath` that still resolves to the old path which is causing the `No such file or directory` error. Interestingly, the cache isn’t used for `file_exists` which is why this warning comes instead of the error from `nix_read_secret` in `override.config.php`.One option to work around this is to turn off the cache by setting the cache size to zero:
  ```
Warning: file_get_contents(/run/secrets/nextcloud_db_password): Failed to open stream: No such file or directory in /nix/store/lqw657xbh6h67ccv9cgv104qhcs1i2vw-nextcloud-config.php on line 11

Warning: http_response_code(): Cannot set response code - headers already sent (output started at /nix/store/lqw657xbh6h67ccv9cgv104qhcs1i2vw-nextcloud-config.php:11) in /nix/store/ikxpaq7kjdhpr4w7cgl1n28kc2gvlhg6-nextcloud-29.0.7/lib/base.php on line 639
Cannot decode /run/secrets/nextcloud_secrets, because: Syntax error
  ```
  ```
{ services.nextcloud.phpOptions."realpath_cache_size" = "0"; }
  ```
- **Empty Files on chunked uploads**Due to a limitation of PHP-FPM, Nextcloud is unable to handle chunked uploads. See upstream issue nextcloud/server#7995 for details.A workaround is to disable chunked uploads with `nextcloud.nginx.enableFastcgiRequestBuffering`.


## Using an alternative webserver as reverse-proxy (e.g. `httpd`)

By default, `nginx` is used as reverse-proxy for `nextcloud`. However, it’s possible to use e.g. `httpd` by explicitly disabling `nginx` using `services.nginx.enable` and fixing the settings `listen.owner` & `listen.group` in the `phpfpm` pool `nextcloud`.


## Installing Apps and PHP extensions

Nextcloud apps are installed statefully through the web interface. Some apps may require extra PHP extensions to be installed. This can be configured with the `services.nextcloud.phpExtraExtensions` setting.

Alternatively, extra apps can also be declared with the `services.nextcloud.extraApps` setting. When using this setting, apps can no longer be managed statefully because this can lead to Nextcloud updating apps that are managed by Nix:

```
{ config, pkgs, ... }:
{
  services.nextcloud.extraApps = with config.services.nextcloud.package.packages.apps; {
    inherit user_oidc calendar contacts;
  };
}
```

Keep in mind that this is essentially a mirror of the apps from the appstore, but managed in nixpkgs. This is by no means a curated list of apps that receive special testing on each update.

If you want automatic updates it is recommended that you use web interface to install apps.


## Known warnings

### Logreader application only supports “file” log_type

This is because

- our module writes logs into the journal (`journalctl -t Nextcloud`)
- the Logreader application that allows reading logs in the admin panel is enabled by default and requires logs written to a file.

If you want to view logs in the admin panel, set `services.nextcloud.settings.log_type` to “file”.

If you prefer logs in the journal, disable the logreader application to shut up the “info”. We can’t really do that by default since whether apps are enabled/disabled is part of the application’s state and tracked inside the database.


## Maintainer information

As stated in the previous paragraph, we must provide a clean upgrade-path for Nextcloud since it cannot move more than one major version forward on a single upgrade. This chapter adds some notes how Nextcloud updates should be rolled out in the future.

While minor and patch-level updates are no problem and can be done directly in the package-expression (and should be backported to supported stable branches after that), major-releases should be added in a new attribute (e.g. Nextcloud `v19.0.0` should be available in `nixpkgs` as `pkgs.nextcloud19`). To provide simple upgrade paths it’s generally useful to backport those as well to stable branches. As long as the package-default isn’t altered, this won’t break existing setups. After that, the versioning-warning in the `nextcloud`-module should be updated to make sure that the package-option selects the latest version on fresh setups.

If major-releases will be abandoned by upstream, we should check first if those are needed in NixOS for a safe upgrade-path before removing those. In that case we should keep those packages, but mark them as insecure in an expression like this (in `<nixpkgs/pkgs/servers/nextcloud/default.nix>`):

```
# ...
{
  nextcloud17 = generic {
    version = "17.0.x";
    sha256 = "0000000000000000000000000000000000000000000000000000";
    eol = true;
  };
}
```

Ideally we should make sure that it’s possible to jump two NixOS versions forward: i.e. the warnings and the logic in the module should guard a user to upgrade from a Nextcloud on e.g. 19.09 to a Nextcloud on 20.09.


## Matomo

Matomo is a real-time web analytics application. This module configures php-fpm as backend for Matomo, optionally configuring an nginx vhost as well.

An automatic setup is not supported by Matomo, so you need to configure Matomo itself in the browser-based Matomo setup.


## Database Setup

You also need to configure a MariaDB or MySQL database and -user for Matomo yourself, and enter those credentials in your browser. You can use passwordless database authentication via the UNIX_SOCKET authentication plugin with the following SQL commands:

```
# For MariaDB
INSTALL PLUGIN unix_socket SONAME 'auth_socket';
CREATE DATABASE matomo;
CREATE USER 'matomo'@'localhost' IDENTIFIED WITH unix_socket;
GRANT ALL PRIVILEGES ON matomo.* TO 'matomo'@'localhost';

# For MySQL
INSTALL PLUGIN auth_socket SONAME 'auth_socket.so';
CREATE DATABASE matomo;
CREATE USER 'matomo'@'localhost' IDENTIFIED WITH auth_socket;
GRANT ALL PRIVILEGES ON matomo.* TO 'matomo'@'localhost';
```

Then fill in `matomo` as database user and database name, and leave the password field blank. This authentication works by allowing only the `matomo` unix user to authenticate as the `matomo` database user (without needing a password), but no other users. For more information on passwordless login, see https://mariadb.com/kb/en/mariadb/unix_socket-authentication-plugin/.

Of course, you can use password based authentication as well, e.g. when the database is not on the same host.


## Archive Processing

This module comes with the systemd service `matomo-archive-processing.service` and a timer that automatically triggers archive processing every hour. This means that you can safely disable browser triggers for Matomo archiving at `Administration > System > General Settings`.

With automatic archive processing, you can now also enable to delete old visitor logs at `Administration > System > Privacy`, but make sure that you run `systemctl start matomo-archive-processing.service` at least once without errors if you have already collected data before, so that the reports get archived before the source data gets deleted.


## Backup

You only need to take backups of your MySQL database and the `/var/lib/matomo/config/config.ini.php` file. Use a user in the `matomo` group or root to access the file. For more information, see https://matomo.org/faq/how-to-install/faq_138/.


## Issues

- Matomo will warn you that the JavaScript tracker is not writable. This is because it’s located in the read-only nix store. You can safely ignore this, unless you need a plugin that needs JavaScript tracker access.


## Using other Web Servers than nginx

You can use other web servers by forwarding calls for `index.php` and `piwik.php` to the `services.phpfpm.pools.<name>.socket` fastcgi unix socket. You can use the nginx configuration in the module code as a reference to what else should be configured.


## Lemmy

Lemmy is a federated alternative to reddit in rust.


## Quickstart

The minimum to start lemmy is

```
{
  services.lemmy = {
    enable = true;
    settings = {
      hostname = "lemmy.union.rocks";
      database.createLocally = true;
    };
    caddy.enable = true;
  };
}
```

This will start the backend on port 8536 and the frontend on port 1234. It will expose your instance with a caddy reverse proxy to the hostname you’ve provided. Postgres will be initialized on that same instance automatically.


## Usage

On first connection you will be asked to define an admin user.


## Missing

- Exposing with nginx is not implemented yet.
- This has been tested using a local database with a unix socket connection. Using different database settings will likely require modifications


## Keycloak

Keycloak is an open source identity and access management server with support for OpenID Connect, OAUTH 2.0 and SAML 2.0.


## Administration

An administrative user with the username `admin` is automatically created in the `master` realm. Its initial password can be configured by setting `services.keycloak.initialAdminPassword` and defaults to `changeme`. The password is not stored safely and should be changed immediately in the admin panel.

Refer to the Keycloak Server Administration Guide for information on how to administer your Keycloak instance.


## Database access

Keycloak can be used with either PostgreSQL, MariaDB or MySQL. Which one is used can be configured in `services.keycloak.database.type`. The selected database will automatically be enabled and a database and role created unless `services.keycloak.database.host` is changed from its default of `localhost` or `services.keycloak.database.createLocally` is set to `false`.

External database access can also be configured by setting `services.keycloak.database.host`, `services.keycloak.database.name`, `services.keycloak.database.username`, `services.keycloak.database.useSSL` and `services.keycloak.database.caCert` as appropriate. Note that you need to manually create the database and allow the configured database user full access to it.

`services.keycloak.database.passwordFile` must be set to the path to a file containing the password used to log in to the database. If `services.keycloak.database.host` and `services.keycloak.database.createLocally` are kept at their defaults, the database role `keycloak` with that password is provisioned on the local database instance.

### Warning

The path should be provided as a string, not a Nix path, since Nix paths are copied into the world readable Nix store.


## Unix socket authentication

For PostgreSQL, Keycloak can connect via Unix socket using peer authentication, avoiding the need for a database password.

To use Unix sockets, set `services.keycloak.database.host` to the PostgreSQL socket directory (e.g., `/run/postgresql`) and add the required junixsocket plugins:

```
{
  services.keycloak = {
    database.host = "/run/postgresql";
    plugins = with pkgs.keycloak.plugins; [
      junixsocket-common
      junixsocket-native-common
    ];
  };
}
```

### Note

Unix socket authentication is only supported for PostgreSQL.


## Hostname

The hostname is used to build the public URL used as base for all frontend requests and must be configured through `services.keycloak.settings.hostname`.

### Note

If you’re migrating an old Wildfly based Keycloak instance and want to keep compatibility with your current clients, you’ll likely want to set `services.keycloak.settings.http-relative-path` to `/auth`. See the option description for more details.

`services.keycloak.settings.hostname-backchannel-dynamic` Keycloak has the capability to offer a separate URL for backchannel requests, enabling internal communication while maintaining the use of a public URL for frontchannel requests. Moreover, the backchannel is dynamically resolved based on incoming headers endpoint.

For more information on hostname configuration, see the Hostname section of the Keycloak Server Installation and Configuration Guide.


## Setting up TLS/SSL

By default, Keycloak won’t accept unsecured HTTP connections originating from outside its local network.

HTTPS support requires a TLS/SSL certificate and a private key, both PEM formatted. Their paths should be set through `services.keycloak.sslCertificate` and `services.keycloak.sslCertificateKey`.

### Warning

The paths should be provided as a strings, not a Nix paths, since Nix paths are copied into the world readable Nix store.


## Themes

You can package custom themes and make them visible to Keycloak through `services.keycloak.themes`. See the Themes section of the Keycloak Server Development Guide and the description of the aforementioned NixOS option for more information.


## Configuration file settings

Keycloak server configuration parameters can be set in `services.keycloak.settings`. These correspond directly to options in `conf/keycloak.conf`. Some of the most important parameters are documented as suboptions, the rest can be found in the All configuration section of the Keycloak Server Installation and Configuration Guide.

Options containing secret data should be set to an attribute set containing the attribute `_secret` - a string pointing to a file containing the value the option should be set to. See the description of `services.keycloak.settings` for an example.


## Example configuration

A basic configuration with some custom settings could look like this:

```
{
  services.keycloak = {
    enable = true;
    settings = {
      hostname = "keycloak.example.com";
      hostname-strict-backchannel = true;
    };
    initialAdminPassword = "e6Wcm0RrtegMEHl"; # change on first login
    sslCertificate = "/run/keys/ssl_cert";
    sslCertificateKey = "/run/keys/ssl_key";
    database.passwordFile = "/run/keys/db_password";
  };
}
```


## Jitsi Meet

With Jitsi Meet on NixOS you can quickly configure a complete, private, self-hosted video conferencing solution.


## Basic usage

A minimal configuration using Let’s Encrypt for TLS certificates looks like this:

```
{
  services.jitsi-meet = {
    enable = true;
    hostName = "jitsi.example.com";
  };
  services.jitsi-videobridge.openFirewall = true;
  networking.firewall.allowedTCPPorts = [
    80
    443
  ];
  security.acme.email = "me@example.com";
  security.acme.acceptTerms = true;
}
```

Jitsi Meet depends on the Prosody XMPP server only for message passing from the web browser while the default Prosody configuration is intended for use with standalone XMPP clients and XMPP federation. If you only use Prosody as a backend for Jitsi Meet it is therefore recommended to also enable `services.jitsi-meet.prosody.lockdown` option to disable unnecessary Prosody features such as federation or the file proxy.


## Configuration

Here is the minimal configuration with additional configurations:

```
{
  services.jitsi-meet = {
    enable = true;
    hostName = "jitsi.example.com";
    prosody.lockdown = true;
    config = {
      enableWelcomePage = false;
      prejoinPageEnabled = true;
      defaultLang = "fi";
    };
    interfaceConfig = {
      SHOW_JITSI_WATERMARK = false;
      SHOW_WATERMARK_FOR_GUESTS = false;
    };
  };
  services.jitsi-videobridge.openFirewall = true;
  networking.firewall.allowedTCPPorts = [
    80
    443
  ];
  security.acme.email = "me@example.com";
  security.acme.acceptTerms = true;
}
```


## Honk

With Honk on NixOS you can quickly configure a complete ActivityPub server with minimal setup and support costs.


## Basic usage

A minimal configuration looks like this:

```
{
  services.honk = {
    enable = true;
    host = "0.0.0.0";
    port = 8080;
    username = "username";
    passwordFile = "/etc/honk/password.txt";
    servername = "honk.example.com";
  };

  networking.firewall.allowedTCPPorts = [ 8080 ];
}
```


## Hatsu

Hatsu is an fully-automated ActivityPub bridge for static sites.


## Quickstart

The minimum configuration to start hatsu server would look like this:

```
{
  services.hatsu = {
    enable = true;
    settings = {
      HATSU_DOMAIN = "hatsu.local";
      HATSU_PRIMARY_ACCOUNT = "example.com";
    };
  };
}
```

this will start the hatsu server on port 3939 and save the database in `/var/lib/hatsu/hatsu.sqlite3`.

Please refer to the Hatsu Documentation for additional configuration options.


## Grocy

Grocy is a web-based self-hosted groceries & household management solution for your home.


## Basic usage

A very basic configuration may look like this:

```
{ pkgs, ... }:
{
  services.grocy = {
    enable = true;
    hostName = "grocy.tld";
  };
}
```

This configures a simple vhost using nginx which listens to `grocy.tld` with fully configured ACME/LE (this can be disabled by setting services.grocy.nginx.enableSSL to `false`). After the initial setup the credentials `admin:admin` can be used to login.

The application’s state is persisted at `/var/lib/grocy/grocy.db` in a `sqlite3` database. The migration is applied when requesting the `/`-route of the application.


## Settings

The configuration for `grocy` is located at `/etc/grocy/config.php`. By default, the following settings can be defined in the NixOS-configuration:

```
{ pkgs, ... }:
{
  services.grocy.settings = {
    # The default currency in the system for invoices etc.
    # Please note that exchange rates aren't taken into account, this
    # is just the setting for what's shown in the frontend.
    currency = "EUR";

    # The display language (and locale configuration) for grocy.
    culture = "de";

    calendar = {
      # Whether or not to show the week-numbers
      # in the calendar.
      showWeekNumber = true;

      # Index of the first day to be shown in the calendar (0=Sunday, 1=Monday,
      # 2=Tuesday and so on).
      firstDayOfWeek = 2;
    };
  };
}
```

If you want to alter the configuration file on your own, you can do this manually with an expression like this:

```
{ lib, ... }:
{
  environment.etc."grocy/config.php".text = lib.mkAfter ''
    // Arbitrary PHP code in grocy's configuration file
  '';
}
```


## GoToSocial

GoToSocial is an ActivityPub social network server, written in Golang.
