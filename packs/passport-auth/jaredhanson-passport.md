---
title: "GitHub"
source: https://github.com/jaredhanson/passport
domain: passport-auth
license: CC-BY-SA-4.0
tags: passport auth, authentication strategy, oauth login flow, node auth middleware
fetched: 2026-07-02
---

# GitHub

jaredhanson

/

passport

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 1.3k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History645 Commits645 Commits |   |   |   |
| .github | .github |   |   |
| etc | etc |   |   |
| lib | lib |   |   |
| sponsors | sponsors |   |   |
| test | test |   |   |
| .gitignore | .gitignore |   |   |
| .jshintrc | .jshintrc |   |   |
| .npmignore | .npmignore |   |   |
| .travis.yml | .travis.yml |   |   |
| CHANGELOG.md | CHANGELOG.md |   |   |
| CONTRIBUTING.md | CONTRIBUTING.md |   |   |
| LICENSE | LICENSE |   |   |
| Makefile | Makefile |   |   |
| README.md | README.md |   |   |
| SPONSORS.md | SPONSORS.md |   |   |
| package.json | package.json |   |   |
|   |   |   |   |

## Repository files navigation

(passport banner)

# Passport

Passport is Express-compatible authentication middleware for Node.js.

Passport's sole purpose is to authenticate requests, which it does through an extensible set of plugins known as *strategies*. Passport does not mount routes or assume any particular database schema, which maximizes flexibility and allows application-level decisions to be made by the developer. The API is simple: you provide Passport a request to authenticate, and Passport provides hooks for controlling what occurs when authentication succeeds or fails.

Sponsors

**Simple Authentication** Make login our problem. Not yours.

Auth0 by Okta provides a simple and customizable login page to authenticate your users. You can dynamically add new capabilities to it - including social login, multi-factor authentication, or passkeys - without making changes to your app’s code.

We help protect your app and your users from attacks - defending your application from bot attacks and detecting runtime anomalies based on suspicious IPs, breached credentials, user context, and more.

**Your app, enterprise-ready.** Start selling to enterprise customers with just a few lines of code. Add Single Sign-On (and more) in minutes instead of months.

**Drag and drop your auth** Add authentication and user management to your consumer and business apps with a few lines of code.

**Auth. Built for Devs, by Devs** Add login, registration, SSO, MFA, and a bazillion other features to your app in minutes. Integrates with any codebase and installs on any server, anywhere in the world.

**API-first AuthN, AuthZ, and Fraud Prevention** The most powerful identity platform built for developers. Easily build and secure a modern auth flow with user & org management, multi-tenant SSO, MFA, RBAC, device fingerprinting, and more.

Status: (Build) (Coverage) (Dependencies)

## Install

```
$ npm install passport
```

## Usage

#### Strategies

Passport uses the concept of strategies to authenticate requests. Strategies can range from verifying username and password credentials, delegated authentication using OAuth (for example, via Facebook or Twitter), or federated authentication using OpenID.

Before authenticating requests, the strategy (or strategies) used by an application must be configured.

```highlight
passport.use(new LocalStrategy(
  function(username, password, done) {
    User.findOne({ username: username }, function (err, user) {
      if (err) { return done(err); }
      if (!user) { return done(null, false); }
      if (!user.verifyPassword(password)) { return done(null, false); }
      return done(null, user);
    });
  }
));
```

There are 480+ strategies. Find the ones you want at: passportjs.org

#### Sessions

Passport will maintain persistent login sessions. In order for persistent sessions to work, the authenticated user must be serialized to the session, and deserialized when subsequent requests are made.

Passport does not impose any restrictions on how your user records are stored. Instead, you provide functions to Passport which implements the necessary serialization and deserialization logic. In a typical application, this will be as simple as serializing the user ID, and finding the user by ID when deserializing.

```highlight
passport.serializeUser(function(user, done) {
  done(null, user.id);
});

passport.deserializeUser(function(id, done) {
  User.findById(id, function (err, user) {
    done(err, user);
  });
});
```

#### Middleware

To use Passport in an Express or Connect-based application, configure it with the required `passport.initialize()` middleware. If your application uses persistent login sessions (recommended, but not required), `passport.session()` middleware must also be used.

```highlight
var app = express();
app.use(require('serve-static')(__dirname + '/../../public'));
app.use(require('cookie-parser')());
app.use(require('body-parser').urlencoded({ extended: true }));
app.use(require('express-session')({ secret: 'keyboard cat', resave: true, saveUninitialized: true }));
app.use(passport.initialize());
app.use(passport.session());
```

#### Authenticate Requests

Passport provides an `authenticate()` function, which is used as route middleware to authenticate requests.

```highlight
app.post('/login', 
  passport.authenticate('local', { failureRedirect: '/login' }),
  function(req, res) {
    res.redirect('/');
  });
```

## Strategies

Passport has a comprehensive set of **over 480** authentication strategies covering social networking, enterprise integration, API services, and more.

## Search all strategies

There is a **Strategy Search** at passportjs.org

The following table lists commonly used strategies:

| Strategy | Protocol | Developer |
|---|---|---|
| Local | HTML form | Jared Hanson |
| OpenID | OpenID | Jared Hanson |
| BrowserID | BrowserID | Jared Hanson |
| Facebook | OAuth 2.0 | Jared Hanson |
| Google | OpenID | Jared Hanson |
| Google | OAuth / OAuth 2.0 | Jared Hanson |
| Twitter | OAuth | Jared Hanson |
| Azure Active Directory | OAuth 2.0 / OpenID / SAML | Azure |

## Examples

- For a complete, working example, refer to the example that uses passport-local.
- **Local Strategy**: Refer to the following tutorials for setting up user authentication via LocalStrategy (`passport-local`):
  - Mongo
    - Express v3x - Tutorial / working example
    - Express v4x - Tutorial / working example
  - Postgres
    - Tutorial / working example
- **Social Authentication**: Refer to the following tutorials for setting up various social authentication strategies:
  - Express v3x - Tutorial / working example
  - Express v4x - Tutorial / working example

## Related Modules

- Locomotive — Powerful MVC web framework
- OAuthorize — OAuth service provider toolkit
- OAuth2orize — OAuth 2.0 authorization server toolkit
- connect-ensure-login — middleware to ensure login sessions

The modules page on the wiki lists other useful modules that build upon or integrate with Passport.

## License

The MIT License

Copyright (c) 2011-2021 Jared Hanson <https://www.jaredhanson.me/>
