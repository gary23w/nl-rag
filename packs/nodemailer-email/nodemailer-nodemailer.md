---
title: "GitHub"
source: https://github.com/nodemailer/nodemailer
domain: nodemailer-email
license: CC-BY-SA-4.0
tags: nodemailer email, send email node, smtp transport, mail message composition
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

nodemailer

/

nodemailer

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 1.4k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History1,213 Commits1,213 Commits |   |   |   |
| .github | .github |   |   |
| assets | assets |   |   |
| examples | examples |   |   |
| lib | lib |   |   |
| test | test |   |   |
| .c8rc.json | .c8rc.json |   |   |
| .gitattributes | .gitattributes |   |   |
| .gitignore | .gitignore |   |   |
| .ncurc.js | .ncurc.js |   |   |
| .npmignore | .npmignore |   |   |
| .prettierignore | .prettierignore |   |   |
| .prettierrc | .prettierrc |   |   |
| .prettierrc.js | .prettierrc.js |   |   |
| .release-please-config.json | .release-please-config.json |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| CLAUDE.md | CLAUDE.md |   |   |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md |   |   |
| LICENSE | LICENSE |   |   |
| README.md | README.md |   |   |
| SECURITY.md | SECURITY.md |   |   |
| SECURITY.txt | SECURITY.txt |   |   |
| eslint.config.js | eslint.config.js |   |   |
| package-lock.json | package-lock.json |   |   |
| package.json | package.json |   |   |
|   |   |   |   |

## Repository files navigation

# Nodemailer

(Nodemailer)

Send emails from Node.js – easy as cake! 🍰✉️

(NPM)

See nodemailer.com for documentation and terms.

Tip

Check out **EmailEngine** – a self-hosted email gateway that allows making **REST requests against IMAP and SMTP servers**. EmailEngine also sends webhooks whenever something changes on the registered accounts. Using the email accounts registered with EmailEngine, you can receive and send emails. EmailEngine supports OAuth2, delayed sends, opens and clicks tracking, bounce detection, etc. All on top of regular email accounts without an external MTA service.

## Having an issue?

#### First review the docs

Documentation for Nodemailer can be found at nodemailer.com.

#### Nodemailer throws a SyntaxError for "..."

You are using an older Node.js version than v6.0. Upgrade Node.js to get support for the spread operator. Nodemailer supports all Node.js versions starting from Node.js@v6.0.0.

#### I'm having issues with Gmail

Gmail either works well, or it does not work at all. It is probably easier to switch to an alternative service instead of fixing issues with Gmail. If Gmail does not work for you, then don't use it. Read more about it here.

#### I get ETIMEDOUT errors

Check your firewall settings. Timeout usually occurs when you try to open a connection to a firewalled port either on the server or on your machine. Some ISPs also block email ports to prevent spamming.

#### Nodemailer works on one machine but not in another

It's either a firewall issue, or your SMTP server blocks authentication attempts from some servers.

#### I get TLS errors

- If you are running the code on your machine, check your antivirus settings. Antiviruses often mess around with email ports usage. Node.js might not recognize the MITM cert your antivirus is using.
- Latest Node versions allow only TLS versions 1.2 and higher. Some servers might still use TLS 1.1 or lower. Check Node.js docs on how to get correct TLS support for your app. You can change this with tls.minVersion option
- You might have the wrong value for the `secure` option. This should be set to `true` only for port 465. For every other port, it should be `false`. Setting it to `false` does not mean that Nodemailer would not use TLS. Nodemailer would still try to upgrade the connection to use TLS if the server supports it.
- Older Node versions do not fully support the certificate chain of the newest Let's Encrypt certificates. Either set tls.rejectUnauthorized to `false` to skip chain verification or upgrade your Node version

```highlight
let configOptions = {
    host: 'smtp.example.com',
    port: 587,
    tls: {
        rejectUnauthorized: true,
        minVersion: 'TLSv1.2'
    }
};
```

#### I have issues with DNS / hosts file

Node.js uses c-ares to resolve domain names, not the DNS library provided by the system, so if you have some custom DNS routing set up, it might be ignored. Nodemailer runs dns.resolve4() and dns.resolve6() to resolve hostname into an IP address. If both calls fail, then Nodemailer will fall back to dns.lookup(). If this does not work for you, you can hard code the IP address into the configuration like shown below. In that case, Nodemailer would not perform any DNS lookups.

```highlight
let configOptions = {
    host: '1.2.3.4',
    port: 465,
    secure: true,
    tls: {
        // must provide server name, otherwise TLS certificate check will fail
        servername: 'example.com'
    }
};
```

#### I have an issue with TypeScript types

Nodemailer has official support for Node.js only. For anything related to TypeScript, you need to directly contact the authors of the type definitions.

#### I have a different problem

If you are having issues with Nodemailer, then the best way to find help would be Stack Overflow or revisit the docs.

### License

Nodemailer is licensed under the **MIT No Attribution license**

The Nodemailer logo was designed by Sven Kristjansen.
