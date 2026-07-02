---
title: "NixOS Manual (part 5/5)"
source: https://nixos.org/manual/nixos/stable/
domain: nixos
license: CC-BY-SA-4.0
tags: nixos distribution, declarative linux distribution, reproducible system configuration, immutable operating system
fetched: 2026-07-02
part: 5/5
---

## Service configuration

The following configuration sets up the PostgreSQL as database backend and binds GoToSocial to `127.0.0.1:8080`, expecting to be run behind a HTTP proxy on `gotosocial.example.com`.

```
{
  services.gotosocial = {
    enable = true;
    setupPostgresqlDB = true;
    settings = {
      application-name = "My GoToSocial";
      host = "gotosocial.example.com";
      protocol = "https";
      bind-address = "127.0.0.1";
      port = 8080;
    };
  };
}
```

Please refer to the GoToSocial Documentation for additional configuration options.


## Proxy configuration

Although it is possible to expose GoToSocial directly, it is common practice to operate it behind an HTTP reverse proxy such as nginx.

```
{
  networking.firewall.allowedTCPPorts = [
    80
    443
  ];
  services.nginx = {
    enable = true;
    clientMaxBodySize = "40M";
    virtualHosts = with config.services.gotosocial.settings; {
      "${host}" = {
        enableACME = true;
        forceSSL = true;
        locations = {
          "/" = {
            recommendedProxySettings = true;
            proxyWebsockets = true;
            proxyPass = "http://${bind-address}:${toString port}";
          };
        };
      };
    };
  };
}
```

Please refer to *SSL/TLS Certificates with ACME* for details on how to provision an SSL/TLS certificate.


## User management

After the GoToSocial service is running, the `gotosocial-admin` utility can be used to manage users. In particular an administrative user can be created with

```
$ sudo gotosocial-admin account create --username <nickname> --email <email> --password <password>
$ sudo gotosocial-admin account confirm --username <nickname>
$ sudo gotosocial-admin account promote --username <nickname>
```


## Glance

Glance is a self-hosted dashboard that puts all your feeds in one place.

Visit the Glance project page to learn more about it.


## Quickstart

Check out the configuration docs to learn more. Use the following configuration to start a public instance of Glance locally:

```
{
  services.glance = {
    enable = true;
    settings = {
      pages = [
        {
          name = "Home";
          columns = [
            {
              size = "full";
              widgets = [
                { type = "calendar"; }
                {
                  type = "weather";
                  location = "Nivelles, Belgium";
                }
              ];
            }
          ];
        }
      ];
    };
    openFirewall = true;
  };
}
```


## Ente.io

Ente is a service that provides a fully open source, end-to-end encrypted platform for photos and videos.


## Quickstart

To host ente, you need the following things:

- An S3-compatible object storage server (either an external provider or a self-hosted one such as garage). From your storage provider you will need:the S3 endpoint URLa bucket namean access key ID and secret access key with read/write access to the bucket
- Several subdomains pointing to your server:accounts.example.comalbums.example.comapi.example.comcast.example.comphotos.example.com

Once you have an S3 endpoint, bucket and credentials, configure ente as follows:

```
{
  services.ente = {
    web = {
      enable = true;
      domains = {
        accounts = "accounts.example.com";
        albums = "albums.example.com";
        cast = "cast.example.com";
        photos = "photos.example.com";
      };
    };
    api = {
      enable = true;
      nginx.enable = true;
      # Create a local postgres database and set the necessary config in ente
      enableLocalDB = true;
      domain = "api.example.com";
      # You can hide secrets by setting xyz._secret = file instead of xyz = value.
      # Make sure to not include any of the secrets used here directly
      # in your config. They would be publicly readable in the nix store.
      # Use agenix, sops-nix or an equivalent secret management solution.
      settings = {
        s3 = {
          use_path_style_urls = true;
          b2-eu-cen = {
            # The S3 endpoint, bucket and credentials from your storage provider
            endpoint = "https://s3.example.com";
            # Must be us-east-1 as it is required internally by ente
            region = "us-east-1";
            bucket = "ente";
            key._secret = "/run/secrets/s3-access-key-id";
            secret._secret = "/run/secrets/s3-secret-access-key";
          };
        };
        key = {
          # generate with: openssl rand -base64 32
          encryption._secret = pkgs.writeText "encryption" "T0sn+zUVFOApdX4jJL4op6BtqqAfyQLH95fu8ASWfno=";
          # generate with: openssl rand -base64 64
          hash._secret = pkgs.writeText "hash" "g/dBZBs1zi9SXQ0EKr4RCt1TGr7ZCKkgrpjyjrQEKovWPu5/ce8dYM6YvMIPL23MMZToVuuG+Z6SGxxTbxg5NQ==";
        };
        # generate with: openssl rand -base64 32
        jwt.secret._secret = pkgs.writeText "jwt" "i2DecQmfGreG6q1vBj5tCokhlN41gcfS2cjOs9Po-u8=";
      };
    };
  };

  networking.firewall.allowedTCPPorts = [
    80
    443
  ];
  services.nginx = {
    recommendedProxySettings = true; # This is important!
    virtualHosts."accounts.${domain}".enableACME = true;
    virtualHosts."albums.${domain}".enableACME = true;
    virtualHosts."api.${domain}".enableACME = true;
    virtualHosts."cast.${domain}".enableACME = true;
    virtualHosts."photos.${domain}".enableACME = true;
  };
}
```

If you have a mail server or smtp relay, you can optionally configure `services.ente.api.settings.smtp` so ente can send you emails (registration code and possibly other events). This is optional.

Now ente should be ready to go under `https://photos.example.com`.


## Registering users

Now you can open photos.example.com and register your user(s). Beware that the first created account will be considered to be the admin account, which among some other things allows you to use `ente-cli` to increase storage limits for any user.

If you have configured smtp, you will get a mail with a verification code, otherwise you can find the code in the server logs.

```
journalctl -eu ente
[...]
ente # [  157.145165] ente[982]: INFO[0141]email.go:130 sendViaTransmail Skipping sending email to a@a.a: Verification code: 134033
```

After you have registered your users, you can set `settings.internal.disable-registration = true;` to prevent further signups.


## Increasing storage limit

By default, all users will be on the free plan which is the only plan available. While adding new plans is possible in theory, it requires some manual database operations which isn’t worthwhile. Instead, use `ente-cli` with your admin user to modify the storage limit.


## iOS background sync

On iOS, background sync is achieved via a silent notification sent by the server every 30 minutes that allows the phone to sync for about 30 seconds, enough for all but the largest videos to be synced on background (if the app is brought to foreground though, sync will resume as normal). To achieve this however, a Firebase account is needed. In the settings option, configure credentials-dir to point towards the directory where the JSON containing the Firebase credentials are stored.

```
{
  # This directory should contain your fcm-service-account.json file
  services.ente.api.settings = {
    credentials-dir = "/path/to/credentials";
    # [...]
  };
}
```


## Discourse

Discourse is a modern and open source discussion platform.


## Basic usage

A minimal configuration using Let’s Encrypt for TLS certificates looks like this:

```
{
  services.discourse = {
    enable = true;
    hostname = "discourse.example.com";
    admin = {
      email = "admin@example.com";
      username = "admin";
      fullName = "Administrator";
      passwordFile = "/path/to/password_file";
    };
    secretKeyBaseFile = "/path/to/secret_key_base_file";
  };
  security.acme.email = "me@example.com";
  security.acme.acceptTerms = true;
}
```

Provided a proper DNS setup, you’ll be able to connect to the instance at `discourse.example.com` and log in using the credentials provided in `services.discourse.admin`.


## Using a regular TLS certificate

To set up TLS using a regular certificate and key on file, use the `services.discourse.sslCertificate` and `services.discourse.sslCertificateKey` options:

```
{
  services.discourse = {
    enable = true;
    hostname = "discourse.example.com";
    sslCertificate = "/path/to/ssl_certificate";
    sslCertificateKey = "/path/to/ssl_certificate_key";
    admin = {
      email = "admin@example.com";
      username = "admin";
      fullName = "Administrator";
      passwordFile = "/path/to/password_file";
    };
    secretKeyBaseFile = "/path/to/secret_key_base_file";
  };
}
```


## Database access

Discourse uses PostgreSQL to store most of its data. A database will automatically be enabled and a database and role created unless `services.discourse.database.host` is changed from its default of `null` or `services.discourse.database.createLocally` is set to `false`.

External database access can also be configured by setting `services.discourse.database.host`, `services.discourse.database.username` and `services.discourse.database.passwordFile` as appropriate. Note that you need to manually create a database called `discourse` (or the name you chose in `services.discourse.database.name`) and allow the configured database user full access to it.


## Email

In addition to the basic setup, you’ll want to configure an SMTP server Discourse can use to send user registration and password reset emails, among others. You can also optionally let Discourse receive email, which enables people to reply to threads and conversations via email.

A basic setup which assumes you want to use your configured hostname as email domain can be done like this:

```
{
  services.discourse = {
    enable = true;
    hostname = "discourse.example.com";
    sslCertificate = "/path/to/ssl_certificate";
    sslCertificateKey = "/path/to/ssl_certificate_key";
    admin = {
      email = "admin@example.com";
      username = "admin";
      fullName = "Administrator";
      passwordFile = "/path/to/password_file";
    };
    mail.outgoing = {
      serverAddress = "smtp.emailprovider.com";
      port = 587;
      username = "user@emailprovider.com";
      passwordFile = "/path/to/smtp_password_file";
    };
    mail.incoming.enable = true;
    secretKeyBaseFile = "/path/to/secret_key_base_file";
  };
}
```

This assumes you have set up an MX record for the address you’ve set in hostname and requires proper SPF, DKIM and DMARC configuration to be done for the domain you’re sending from, in order for email to be reliably delivered.

If you want to use a different domain for your outgoing email (for example `example.com` instead of `discourse.example.com`) you should set `services.discourse.mail.notificationEmailAddress` and `services.discourse.mail.contactEmailAddress` manually.

### Note

Setup of TLS for incoming email is currently only configured automatically when a regular TLS certificate is used, i.e. when `services.discourse.sslCertificate` and `services.discourse.sslCertificateKey` are set.


## Additional settings

Additional site settings and backend settings, for which no explicit NixOS options are provided, can be set in `services.discourse.siteSettings` and `services.discourse.backendSettings` respectively.

### Site settings

“Site settings” are the settings that can be changed through the Discourse UI. Their *default* values can be set using `services.discourse.siteSettings`.

Settings are expressed as a Nix attribute set which matches the structure of the configuration in config/site_settings.yml. To find a setting’s path, you only need to care about the first two levels; i.e. its category (e.g. `login`) and name (e.g. `invite_only`).

Settings containing secret data should be set to an attribute set containing the attribute `_secret` - a string pointing to a file containing the value the option should be set to. See the example.

### Backend settings

Settings are expressed as a Nix attribute set which matches the structure of the configuration in config/discourse.conf. Empty parameters can be defined by setting them to `null`.

### Example

The following example sets the title and description of the Discourse instance and enables GitHub login in the site settings, and changes a few request limits in the backend settings:

```
{
  services.discourse = {
    enable = true;
    hostname = "discourse.example.com";
    sslCertificate = "/path/to/ssl_certificate";
    sslCertificateKey = "/path/to/ssl_certificate_key";
    admin = {
      email = "admin@example.com";
      username = "admin";
      fullName = "Administrator";
      passwordFile = "/path/to/password_file";
    };
    mail.outgoing = {
      serverAddress = "smtp.emailprovider.com";
      port = 587;
      username = "user@emailprovider.com";
      passwordFile = "/path/to/smtp_password_file";
    };
    mail.incoming.enable = true;
    siteSettings = {
      required = {
        title = "My Cats";
        site_description = "Discuss My Cats (and be nice plz)";
      };
      login = {
        enable_github_logins = true;
        github_client_id = "a2f6dfe838cb3206ce20";
        github_client_secret._secret = /run/keys/discourse_github_client_secret;
      };
    };
    backendSettings = {
      max_reqs_per_ip_per_minute = 300;
      max_reqs_per_ip_per_10_seconds = 60;
      max_asset_reqs_per_ip_per_10_seconds = 250;
      max_reqs_per_ip_mode = "warn+block";
    };
    secretKeyBaseFile = "/path/to/secret_key_base_file";
  };
}
```

In the resulting site settings file, the `login.github_client_secret` key will be set to the contents of the `/run/keys/discourse_github_client_secret` file.


## Plugins

You can install Discourse plugins using the `services.discourse.plugins` option. Pre-packaged plugins are provided in `<your_discourse_package_here>.plugins`. If you want the full suite of plugins provided through `nixpkgs`, you can also set the `services.discourse.package` option to `pkgs.discourseAllPlugins`.

Plugins can be built with the `<your_discourse_package_here>.mkDiscoursePlugin` function. Normally, it should suffice to provide a `name` and `src` attribute. If the plugin has Ruby dependencies, however, they need to be packaged in accordance with the Developing with Ruby section of the Nixpkgs manual and the appropriate gem options set in `bundlerEnvArgs` (normally `gemdir` is sufficient). A plugin’s Ruby dependencies are listed in its `plugin.rb` file as function calls to `gem`. To construct the corresponding `Gemfile` manually, run **bundle init**, then add the `gem` lines to it verbatim.

Much of the packaging can be done automatically by the `nixpkgs/pkgs/servers/web-apps/discourse/update.py` script - just add the plugin to the `plugins` list in the `update_plugins` function and run the script:

```
./update.py update-plugins
```

Some plugins provide site settings. Their defaults can be configured using `services.discourse.siteSettings`, just like regular site settings. To find the names of these settings, look in the `config/settings.yml` file of the plugin repo.

For example, to add the discourse-spoiler-alert and discourse-solved plugins, and disable `discourse-spoiler-alert` by default:

```
{
  services.discourse = {
    enable = true;
    hostname = "discourse.example.com";
    sslCertificate = "/path/to/ssl_certificate";
    sslCertificateKey = "/path/to/ssl_certificate_key";
    admin = {
      email = "admin@example.com";
      username = "admin";
      fullName = "Administrator";
      passwordFile = "/path/to/password_file";
    };
    mail.outgoing = {
      serverAddress = "smtp.emailprovider.com";
      port = 587;
      username = "user@emailprovider.com";
      passwordFile = "/path/to/smtp_password_file";
    };
    mail.incoming.enable = true;
    plugins = with config.services.discourse.package.plugins; [
      discourse-spoiler-alert
      discourse-solved
    ];
    siteSettings = {
      plugins = {
        spoiler_enabled = false;
      };
    };
    secretKeyBaseFile = "/path/to/secret_key_base_file";
  };
}
```


## Davis

Davis is a caldav and carrddav server. It has a simple, fully translatable admin interface for sabre/dav based on Symfony 5 and Bootstrap 5, initially inspired by Baïkal.


## Basic Usage

At first, an application secret is needed, this can be generated with:

```
$ cat /dev/urandom | tr -dc a-zA-Z0-9 | fold -w 48 | head -n 1
```

After that, `davis` can be deployed like this:

```
{
  services.davis = {
    enable = true;
    hostname = "davis.example.com";
    mail = {
      dsn = "smtp://username@example.com:25";
      inviteFromAddress = "davis@example.com";
    };
    adminLogin = "admin";
    adminPasswordFile = "/run/secrets/davis-admin-password";
    appSecretFile = "/run/secrets/davis-app-secret";
  };
}
```

This deploys Davis using a sqlite database running out of `/var/lib/davis`.

Logs can be found in `/var/lib/davis/var/log/`.


## Castopod

Castopod is an open-source hosting platform made for podcasters who want to engage and interact with their audience.


## Quickstart

Configure ACME (https://nixos.org/manual/nixos/unstable/#module-security-acme). Use the following configuration to start a public instance of Castopod on `castopod.example.com` domain:

```
{
  networking.firewall.allowedTCPPorts = [
    80
    443
  ];
  services.castopod = {
    enable = true;
    database.createLocally = true;
    nginx.virtualHost = {
      serverName = "castopod.example.com";
      enableACME = true;
      forceSSL = true;
    };
  };
}
```

Go to `https://castopod.example.com/cp-install` to create superadmin account after applying the above configuration.


## c2FmZQ

c2FmZQ is an application that can securely encrypt, store, and share files, including but not limited to pictures and videos.

The service `c2fmzq-server` can be enabled by setting

```
{ services.c2fmzq-server.enable = true; }
```

This will spin up an instance of the server which is API-compatible with Stingle Photos and an experimental Progressive Web App (PWA) to interact with the storage via the browser.

In principle the server can be exposed directly on a public interface and there are command line options to manage HTTPS certificates directly, but the module is designed to be served behind a reverse proxy or only accessed via localhost.

```
{
  services.c2fmzq-server = {
    enable = true;
    bindIP = "127.0.0.1"; # default
    port = 8080; # default
  };

  services.nginx = {
    enable = true;
    recommendedProxySettings = true;
    virtualHosts."example.com" = {
      enableACME = true;
      forceSSL = true;
      locations."/" = {
        proxyPass = "http://127.0.0.1:8080";
      };
    };
  };
}
```

For more information, see https://github.com/c2FmZQ/c2FmZQ/.


## Akkoma

Akkoma is a lightweight ActivityPub microblogging server forked from Pleroma.


## Service configuration

The Elixir configuration file required by Akkoma is generated automatically from `services.akkoma.config`. Secrets must be included from external files outside of the Nix store by setting the configuration option to an attribute set containing the attribute `_secret` – a string pointing to the file containing the actual value of the option.

For the mandatory configuration settings these secrets will be generated automatically if the referenced file does not exist during startup, unless disabled through `services.akkoma.initSecrets`.

The following configuration binds Akkoma to the Unix socket `/run/akkoma/socket`, expecting to be run behind a HTTP proxy on `fediverse.example.com`.

```
{
  services.akkoma.enable = true;
  services.akkoma.config = {
    ":pleroma" = {
      ":instance" = {
        name = "My Akkoma instance";
        description = "More detailed description";
        email = "admin@example.com";
        registration_open = false;
      };

      "Pleroma.Web.Endpoint" = {
        url.host = "fediverse.example.com";
      };
    };
  };
}
```

Please refer to the configuration cheat sheet for additional configuration options.


## User management

After the Akkoma service is running, the administration utility can be used to manage users. In particular an administrative user can be created with

```
$ pleroma_ctl user new <nickname> <email> --admin --moderator --password <password>
```


## Proxy configuration

Although it is possible to expose Akkoma directly, it is common practice to operate it behind an HTTP reverse proxy such as nginx.

```
{
  services.akkoma.nginx = {
    enableACME = true;
    forceSSL = true;
  };

  services.nginx = {
    enable = true;

    clientMaxBodySize = "16m";
    recommendedTlsSettings = true;
    recommendedOptimisation = true;
    recommendedGzipSettings = true;
  };
}
```

Please refer to *SSL/TLS Certificates with ACME* for details on how to provision an SSL/TLS certificate.

### Media proxy

Without the media proxy function, Akkoma does not store any remote media like pictures or video locally, and clients have to fetch them directly from the source server.

```
{
  # Enable nginx slice module distributed with Tengine
  services.nginx.package = pkgs.tengine;

  # Enable media proxy
  services.akkoma.config.":pleroma".":media_proxy" = {
    enabled = true;
    proxy_opts.redirect_on_failure = true;
  };

  # Adjust the persistent cache size as needed:
  #  Assuming an average object size of 128 KiB, around 1 MiB
  #  of memory is required for the key zone per GiB of cache.
  # Ensure that the cache directory exists and is writable by nginx.
  services.nginx.commonHttpConfig = ''
    proxy_cache_path /var/cache/nginx/cache/akkoma-media-cache
      levels= keys_zone=akkoma_media_cache:16m max_size=16g
      inactive=1y use_temp_path=off;
  '';

  services.akkoma.nginx = {
    locations."/proxy" = {
      proxyPass = "http://unix:/run/akkoma/socket";

      extraConfig = ''
        proxy_cache akkoma_media_cache;

        # Cache objects in slices of 1 MiB
        slice 1m;
        proxy_cache_key $host$uri$is_args$args$slice_range;
        proxy_set_header Range $slice_range;

        # Decouple proxy and upstream responses
        proxy_buffering on;
        proxy_cache_lock on;
        proxy_ignore_client_abort on;

        # Default cache times for various responses
        proxy_cache_valid 200 1y;
        proxy_cache_valid 206 301 304 1h;

        # Allow serving of stale items
        proxy_cache_use_stale error timeout invalid_header updating;
      '';
    };
  };
}
```

#### Prefetch remote media

The following example enables the `MediaProxyWarmingPolicy` MRF policy which automatically fetches all media associated with a post through the media proxy, as soon as the post is received by the instance.

```
{
  services.akkoma.config.":pleroma".":mrf".policies = map (pkgs.formats.elixirConf { }).lib.mkRaw [
    "Pleroma.Web.ActivityPub.MRF.MediaProxyWarmingPolicy"
  ];
}
```

#### Media previews

Akkoma can generate previews for media.

```
{
  services.akkoma.config.":pleroma".":media_preview_proxy" = {
    enabled = true;
    thumbnail_max_width = 1920;
    thumbnail_max_height = 1080;
  };
}
```


## Frontend management

Akkoma will be deployed with the `akkoma-fe` and `admin-fe` frontends by default. These can be modified by setting `services.akkoma.frontends`.

The following example overrides the primary frontend’s default configuration using a custom derivation.

```
{
  services.akkoma.frontends.primary.package =
    pkgs.runCommand "akkoma-fe"
      {
        config = builtins.toJSON {
          expertLevel = 1;
          collapseMessageWithSubject = false;
          stopGifs = false;
          replyVisibility = "following";
          webPushHideIfCW = true;
          hideScopeNotice = true;
          renderMisskeyMarkdown = false;
          hideSiteFavicon = true;
          postContentType = "text/markdown";
          showNavShortcuts = false;
        };
        nativeBuildInputs = with pkgs; [
          jq
          lndir
        ];
        passAsFile = [ "config" ];
      }
      ''
        mkdir $out
        lndir ${pkgs.akkoma-frontends.akkoma-fe} $out

        rm $out/static/config.json
        jq -s add ${pkgs.akkoma-frontends.akkoma-fe}/static/config.json ${config} \
          >$out/static/config.json
      '';
}
```


## Federation policies

Akkoma comes with a number of modules to police federation with other ActivityPub instances. The most valuable for typical users is the `:mrf_simple` module which allows limiting federation based on instance hostnames.

This configuration snippet provides an example on how these can be used. Choosing an adequate federation policy is not trivial and entails finding a balance between connectivity to the rest of the fediverse and providing a pleasant experience to the users of an instance.

```
{
  services.akkoma.config.":pleroma" = with (pkgs.formats.elixirConf { }).lib; {
    ":mrf".policies = map mkRaw [ "Pleroma.Web.ActivityPub.MRF.SimplePolicy" ];

    ":mrf_simple" = {
      # Tag all media as sensitive
      media_nsfw = mkMap { "nsfw.weird.kinky" = "Untagged NSFW content"; };

      # Reject all activities except deletes
      reject = mkMap {
        "kiwifarms.cc" = "Persistent harassment of users, no moderation";
      };

      # Force posts to be visible by followers only
      followers_only = mkMap {
        "beta.birdsite.live" = "Avoid polluting timelines with Twitter posts";
      };
    };
  };
}
```


## Upload filters

This example strips GPS and location metadata from uploads, deduplicates them and anonymises the the file name.

```
{
  services.akkoma.config.":pleroma"."Pleroma.Upload".filters =
    map (pkgs.formats.elixirConf { }).lib.mkRaw
      [
        "Pleroma.Upload.Filter.Exiftool"
        "Pleroma.Upload.Filter.Dedupe"
        "Pleroma.Upload.Filter.AnonymizeFilename"
      ];
}
```


## Migration from Pleroma

Pleroma instances can be migrated to Akkoma either by copying the database and upload data or by pointing Akkoma to the existing data. The necessary database migrations are run automatically during startup of the service.

The configuration has to be copy‐edited manually.

Depending on the size of the database, the initial migration may take a long time and exceed the startup timeout of the system manager. To work around this issue one may adjust the startup timeout `systemd.services.akkoma.serviceConfig.TimeoutStartSec` or simply run the migrations manually:

```
pleroma_ctl migrate
```

### Copying data

Copying the Pleroma data instead of re‐using it in place may permit easier reversion to Pleroma, but allows the two data sets to diverge.

First disable Pleroma and then copy its database and upload data:

```
# Create a copy of the database
nix-shell -p postgresql --run 'createdb -T pleroma akkoma'

# Copy upload data
mkdir /var/lib/akkoma
cp -R --reflink=auto /var/lib/pleroma/uploads /var/lib/akkoma/
```

After the data has been copied, enable the Akkoma service and verify that the migration has been successful. If no longer required, the original data may then be deleted:

```
# Delete original database
nix-shell -p postgresql --run 'dropdb pleroma'

# Delete original Pleroma state
rm -r /var/lib/pleroma
```

### Re‐using data

To re‐use the Pleroma data in place, disable Pleroma and enable Akkoma, pointing it to the Pleroma database and upload directory.

```
{
  # Adjust these settings according to the database name and upload directory path used by Pleroma
  services.akkoma.config.":pleroma"."Pleroma.Repo".database = "pleroma";
  services.akkoma.config.":pleroma".":instance".upload_dir = "/var/lib/pleroma/uploads";
}
```

Please keep in mind that after the Akkoma service has been started, any migrations applied by Akkoma have to be rolled back before the database can be used again with Pleroma. This can be achieved through `pleroma_ctl ecto.rollback`. Refer to the Ecto SQL documentation for details.


## Advanced deployment options

### Confinement

The Akkoma systemd service may be confined to a chroot with

```
{ services.systemd.akkoma.confinement.enable = true; }
```

Confinement of services is not generally supported in NixOS and therefore disabled by default. Depending on the Akkoma configuration, the default confinement settings may be insufficient and lead to subtle errors at run time, requiring adjustment:

Use `services.systemd.akkoma.confinement.packages` to make packages available in the chroot.

`services.systemd.akkoma.serviceConfig.BindPaths` and `services.systemd.akkoma.serviceConfig.BindReadOnlyPaths` permit access to outside paths through bind mounts. Refer to `BindPaths=` of systemd.exec(5) for details.

### Distributed deployment

Being an Elixir application, Akkoma can be deployed in a distributed fashion.

This requires setting `services.akkoma.dist.address` and `services.akkoma.dist.cookie`. The specifics depend strongly on the deployment environment. For more information please check the relevant Erlang documentation.


## systemd-lock-handler

The `systemd-lock-handler` module provides a service that bridges D-Bus events from `logind` to user-level systemd targets:

- `lock.target` started by `loginctl lock-session`,
- `unlock.target` started by `loginctl unlock-session` and
- `sleep.target` started by `systemctl suspend`.

You can create a user service that starts with any of these targets.

For example, to create a service for `swaylock`:

```
{
  services.systemd-lock-handler.enable = true;

  systemd.user.services.swaylock = {
    description = "Screen locker for Wayland";
    documentation = [ "man:swaylock(1)" ];

    # If swaylock exits cleanly, unlock the session:
    onSuccess = [ "unlock.target" ];

    # When lock.target is stopped, stops this too:
    partOf = [ "lock.target" ];

    # Delay lock.target until this service is ready:
    before = [ "lock.target" ];
    wantedBy = [ "lock.target" ];

    serviceConfig = {
      # systemd will consider this service started when swaylock forks...
      Type = "forking";

      # ... and swaylock will fork only after it has locked the screen.
      ExecStart = "${lib.getExe pkgs.swaylock} -f";

      # If swaylock crashes, always restart it immediately:
      Restart = "on-failure";
      RestartSec = 0;
    };
  };
}
```

See upstream documentation for more information.


## kerberos_server

Kerberos is a computer-network authentication protocol that works on the basis of tickets to allow nodes communicating over a non-secure network to prove their identity to one another in a secure manner.

This module provides both the MIT and Heimdal implementations of the a Kerberos server.


## Usage

To enable a Kerberos server:

```
{
  security.krb5 = {
    # Here you can choose between the MIT and Heimdal implementations.
    package = pkgs.krb5;
    # package = pkgs.heimdal;

    # Optionally set up a client on the same machine as the server
    enable = true;
    settings = {
      libdefaults.default_realm = "EXAMPLE.COM";
      realms."EXAMPLE.COM" = {
        kdc = "kerberos.example.com";
        admin_server = "kerberos.example.com";
      };
    };
  };

  services.kerberos-server = {
    enable = true;
    settings = {
      realms."EXAMPLE.COM" = {
        acl = [
          {
            principal = "adminuser";
            access = [
              "add"
              "cpw"
            ];
          }
        ];
      };
    };
  };
}
```
