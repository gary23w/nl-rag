# Sources & licenses

Every pack file carries its upstream `source:` URL and `license:` in frontmatter. The
normalized packs are redistributed under their **upstream licenses** with attribution —
nothing here relicenses upstream content. The `ragpull` tool itself is MIT (see LICENSE).

| domain | upstream sites | license |
|---|---|---|
| python | docs.pytest.org, docs.python.org | PSF-2.0 |
| rust | doc.rust-lang.org | MIT OR Apache-2.0 |
| ruby | guides.rubyonrails.org, ruby-doc.org | Ruby-BSD / CC-BY-SA-4.0 (Rails guides) |
| golang | go.dev, pkg.go.dev | BSD-3-Clause |
| javascript | developer.mozilla.org, nodejs.org | CC-BY-SA-2.5 (MDN) / MIT (Node.js) |
| web-platform | developer.mozilla.org | CC-BY-SA-2.5 |
| zig | ziglang.org | MIT |
| c-cpp | en.cppreference.com | CC-BY-SA-3.0 (cppreference) |
| http-rest | developer.mozilla.org, www.rfc-editor.org | CC-BY-SA-2.5 / IETF-Trust (RFC) |
| web-frameworks | docs.djangoproject.com, expressjs.com, flask.palletsprojects.com | BSD-3-Clause (Flask/Django) / CC-BY-SA-3.0 (Express) |
| sql-sqlite | sqlite.org | Public-Domain |
| databases | en.wikipedia.org, www.postgresql.org | CC-BY-SA-4.0 / PostgreSQL |
| data-formats | en.wikipedia.org | CC-BY-SA-4.0 |
| algorithms | en.wikipedia.org | CC-BY-SA-4.0 |
| data-structures | en.wikipedia.org | CC-BY-SA-4.0 |
| software-design | en.wikipedia.org | CC-BY-SA-4.0 |
| concurrency | en.wikipedia.org | CC-BY-SA-4.0 |
| machine-learning | en.wikipedia.org | CC-BY-SA-4.0 |
| security | cheatsheetseries.owasp.org, en.wikipedia.org | CC-BY-SA-4.0 (OWASP) / CC-BY-SA-4.0 (Wikipedia) |
| crypto | en.wikipedia.org | CC-BY-SA-4.0 |
| git | git-scm.com | GPL-2.0 |
| shell-linux | man7.org, www.gnu.org | GFDL-1.3 (bash manual) / GPL-2.0 (man-pages) |
| sysadmin-ops | en.wikipedia.org, man7.org | GPL-2.0 / CC-BY-SA-4.0 |
| docker-containers | docs.docker.com, en.wikipedia.org | Apache-2.0 |
| networking | en.wikipedia.org, man7.org | CC-BY-SA-4.0 / GPL-2.0 (man-pages) |
| build-systems | en.wikipedia.org, www.gnu.org | GFDL-1.3 / CC-BY-SA-4.0 |
| testing | en.wikipedia.org | CC-BY-SA-4.0 |
| regex | developer.mozilla.org, docs.python.org, en.wikipedia.org | CC-BY-SA-2.5 / CC-BY-SA-4.0 / PSF-2.0 |

Attribution notes:

- **Wikipedia** content is CC-BY-SA-4.0; each file's `source:` link is the attribution.
- **MDN** prose is CC-BY-SA-2.5 (code samples CC0); `source:` links attribute the page.
- **OWASP Cheat Sheet Series** is CC-BY-SA-4.0.
- **man7.org** hosts the Linux man-pages project; individual pages carry their own
  (GPL-family) licenses — see the upstream page footer.
- **Python docs** PSF-2.0; **Rust** book/std MIT OR Apache-2.0; **SQLite docs** public
  domain; **Go** BSD-3-Clause; **git docs** GPL-2.0; **GNU manuals** GFDL-1.3.

If you own an upstream source and want content removed, open an issue.
