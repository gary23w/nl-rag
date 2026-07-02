---
title: "scotty: Haskell web framework inspired by Ruby's Sinatra, using WAI and Warp"
source: https://hackage.haskell.org/package/scotty
domain: scotty-haskell
license: CC-BY-SA-4.0
tags: scotty haskell framework, haskell sinatra like, haskell microframework, warp haskell server
fetched: 2026-07-02
---

# scotty: Haskell web framework inspired by Ruby's Sinatra, using WAI and Warp

[

bsd3

,

library

,

web

] [

Propose Tags

] [

Report a vulnerability

]

A Haskell web framework inspired by Ruby's Sinatra, using WAI and Warp.

```
{-# LANGUAGE OverloadedStrings #-}

import Web.Scotty

main = scotty 3000 $
  get "/:word" $ do
    beam <- pathParam "word"
    html $ mconcat ["<h1>Scotty, ", beam, " me up!</h1>"]
```

Scotty is the cheap and cheerful way to write RESTful, declarative web applications.

- A page is as simple as defining the verb, url pattern, and Text content.
- It is template-language agnostic. Anything that returns a Text value will do.
- Conforms to WAI Application interface.
- Uses very fast Warp webserver by default.

As for the name: Sinatra + Warp = Scotty.

**WAI**

http://hackage.haskell.org/package/wai

**Warp**

http://hackage.haskell.org/package/warp

[

Skip to Readme

]

## Modules

[Index] [Quick Jump]

- *Web*
  - Web.Scotty
    - Web.Scotty.Cookie
    - *Internal*
      - Web.Scotty.Internal.Types
    - Web.Scotty.Session
    - Web.Scotty.Trans
      - Web.Scotty.Trans.Strict

## Downloads

- scotty-0.30.tar.gz [browse] (Cabal source package)
- Package description (as included in the package)

#### Maintainer's Corner

Package maintainers

- AndrewFarmer, FumiakiKinoshita, ryanglscott, ocramz, chessai, danielbrice

For package maintainers and hackage trustees

- edit package information

Candidates

- 0.30

| Versions [RSS] | 0.0.1, 0.1.0, 0.2.0, 0.3.0, 0.4.0, 0.4.1, 0.4.2, 0.4.3, 0.4.4, 0.4.5, 0.4.6, 0.5.0, 0.6.0, 0.6.1, 0.6.2, 0.7.0, 0.7.1, 0.7.2, 0.7.3, 0.8.0, 0.8.1, 0.8.2, 0.9.0, 0.9.1, 0.10.0, 0.10.1, 0.10.2, 0.11.0, 0.11.1, 0.11.2, 0.11.3, 0.11.4, 0.11.5, 0.11.6, 0.12, 0.12.1, 0.20, 0.20.1, 0.21, 0.22, **0.30** (info) |
|---|---|
| Change log | changelog.md |
| Dependencies | aeson (>=0.6.2.1 && <2.3), base (>=4.14 && <5), blaze-builder (>=0.3.3.0 && <0.5), bytestring (>=0.10.0.2), case-insensitive (>=1.0.0.1 && <1.3), containers (>=0.5 && <0.8), cookie (>=0.4), exceptions (>=0.7 && <0.11), fail, http-api-data (<0.7), http-types (>=0.9.1 && <0.13), monad-control (>=1.0.0.3 && <1.1), mtl (>=2.1.2 && <2.4), nats (>=0.1 && <2), network (>=2.6.0.2 && <3.3), random (>=1.0.0.0), regex-compat (>=0.95.1 && <0.96), resourcet, stm, text (>=0.11.3.1), time (>=1.8), transformers (>=0.3.0.0 && <0.7), transformers-base (>=0.4.1 && <0.5), unliftio (>=0.2), unordered-containers (>=0.2.10.0 && <0.3), wai (>=3.0.0 && <3.3), wai-extra (>=3.1.14), warp (>=3.0.13) [details] |
| Tested with | ghc ==8.10.7, ghc ==9.0.2, ghc ==9.2.8, ghc ==9.4.6, ghc ==9.6.4, ghc ==9.8.2 |
| License | BSD-3-Clause |
| Copyright | (c) 2012-Present, Andrew Farmer and the Scotty contributors |
| Author | Andrew Farmer <xichekolas@gmail.com> |
| Maintainer | The Scotty maintainers |
| Uploaded | by ocramz at 2026-01-07T10:12:21Z |
| Category | Web |
| Home page | https://github.com/scotty-web/scotty |
| Bug tracker | https://github.com/scotty-web/scotty/issues |
| Source repo | head: git clone git://github.com/scotty-web/scotty.git |
| Distributions | Arch:0.22, Fedora:0.22, LTSHaskell:0.22, Stackage:0.30 |
| Reverse Dependencies | 64 direct, 44 indirect [details] |
| Downloads | 66156 total (151 in the last 30 days) |
| Rating | 2.75 (votes: 7) [estimated by Bayesian average] |
| Your Rating | λ λ λ |
| Status | Docs available [build log] Last success reported on 2026-01-07 [all 1 reports] |

## Readme for scotty-0.30

[

back to package description

]

# Scotty (Hackage) (Stackage Lts) (Stackage Nightly) (CI)

A Haskell web framework inspired by Ruby's Sinatra, using WAI and Warp.

```haskell
{-# LANGUAGE OverloadedStrings #-}
import Web.Scotty

main = scotty 3000 $
    get "/:word" $ do
        beam <- pathParam "word"
        html $ mconcat ["<h1>Scotty, ", beam, " me up!</h1>"]
```

Scotty is the cheap and cheerful way to write RESTful, declarative web applications.

- A page is as simple as defining the verb, URL pattern, and Text content.
- It is template-language agnostic. Anything that returns a Text value will do.
- Conforms to the web application interface (WAI).
- Uses the very fast Warp webserver by default.

As for the name: Sinatra + Warp = Scotty.

## Examples

Run /basic.hs to see Scotty in action:

```bash
runghc examples/basic.hs
```

`Setting phasers to stun... (port 3000) (ctrl-c to quit)`

Or equivalently with `stack`:

```bash
stack exec -- scotty-basic
```

Once the server is running you can interact with it with curl or a browser:

```bash
curl localhost:3000
```

`foobar`

```bash
curl localhost:3000/foo_query?p=42
```

`<h1>42</h1>`

Additionally, the `examples` directory shows a number of concrete use cases, e.g.

- exception handling
- global state
- configuration
- cookies
- file upload
- session
- WAI middlewares (logging, header validation)
- and more

## More Information

Tutorials and related projects can be found in the Scotty wiki.

## Contributing

Feel free to ask questions or report bugs on the Github issue tracker.

Github issues are now (September 2023) labeled, so newcomers to the Haskell language can start with `easy fix` ones and gradually progress to `new feature`s, `bug`s and `R&D` :)

## Package versions

Scotty adheres to the Package Versioning Policy.

## FAQ

- Fails to compile regex-posix on Windows
  - If you are using stack, add the following parameters to `stack.yaml`:
      ```
  extra-deps:
  - regex-posix-clib-2.7
  flags:
    regex-posix:
      _regex-posix-clib: true
      ```
  - If you are using cabal, update the `constraints` section of `cabal.project.local` as follows:
      ```
constraints:
  regex-posix +_regex-posix-clib 
      ```

### Contributors

# Copyright

(c) 2012-Present, Andrew Farmer and Scotty contributors
