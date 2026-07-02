---
title: "Workflow syntax for GitHub Actions (part 4/4)"
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
domain: github-actions
license: CC-BY-4.0 (GitHub docs)
tags: github actions, github workflow, actions runner
fetched: 2026-07-02
part: 4/4
---

## Filter pattern cheat sheet

You can use special characters in path, branch, and tag filters.

- `*`: Matches zero or more characters, but does not match the `/` character. For example, `Octo*` matches `Octocat`.
- `**`: Matches zero or more of any character.
- `?`: Matches zero or one of the preceding character.
- `+`: Matches one or more of the preceding character.
- `[]` Matches one alphanumeric character listed in the brackets or included in ranges. Ranges can only include `a-z`, `A-Z`, and `0-9`. For example, the range`[0-9a-z]` matches any digit or lowercase letter. For example, `[CB]at` matches `Cat` or `Bat` and `[1-2]00` matches `100` and `200`.
- `!`: At the start of a pattern makes it negate previous positive patterns. It has no special meaning if not the first character.

The characters `*`, `[`, and `!` are special characters in YAML. If you start a pattern with `*`, `[`, or `!`, you must enclose the pattern in quotes. Also, if you use a flow sequence with a pattern containing `[` and/or `]`, the pattern must be enclosed in quotes.

```yaml
paths:
  - '**/README.md'

paths:
  - **/README.md

branches: [ main, 'release/v[0-9].[0-9]' ]

branches: [ main, release/v[0-9].[0-9] ]
```

For more information about branch, tag, and path filter syntax, see `on.<push>.<branches|tags>`, `on.<pull_request>.<branches|tags>`, and `on.<push|pull_request>.paths`.

### Patterns to match branches and tags

| Pattern | Description | Example matches |
|---|---|---|
| `feature/*` | The `*` wildcard matches any character, but does not match slash (`/`). | `feature/my-branch` `feature/your-branch` |
| `feature/**` | The `**` wildcard matches any character including slash (`/`) in branch and tag names. | `feature/beta-a/my-branch` `feature/your-branch` `feature/mona/the/octocat` |
| `main` `releases/mona-the-octocat` | Matches the exact name of a branch or tag name. | `main` `releases/mona-the-octocat` |
| `'*'` | Matches all branch and tag names that don't contain a slash (`/`). The `*` character is a special character in YAML. When you start a pattern with `*`, you must use quotes. | `main` `releases` |
| `'**'` | Matches all branch and tag names. This is the default behavior when you don't use a `branches` or `tags` filter. | `all/the/branches` `every/tag` |
| `'*feature'` | The `*` character is a special character in YAML. When you start a pattern with `*`, you must use quotes. | `mona-feature` `feature` `ver-10-feature` |
| `v2*` | Matches branch and tag names that start with `v2`. | `v2` `v2.0` `v2.9` |
| `v[12].[0-9]+.[0-9]+` | Matches all semantic versioning branches and tags with major version 1 or 2. | `v1.10.1` `v2.0.0` |

### Patterns to match file paths

Path patterns must match the whole path, and start from the repository's root.

| Pattern | Description of matches | Example matches |
|---|---|---|
| `'*'` | The `*` wildcard matches any character, but does not match slash (`/`). The `*` character is a special character in YAML. When you start a pattern with `*`, you must use quotes. | `README.md` `server.rb` |
| `'*.jsx?'` | The `?` character matches zero or one of the preceding character. | `page.js` `page.jsx` |
| `'**'` | The `**` wildcard matches any character including slash (`/`). This is the default behavior when you don't use a `path` filter. | `all/the/files.md` |
| `'*.js'` | The `*` wildcard matches any character, but does not match slash (`/`). Matches all `.js` files at the root of the repository. | `app.js` `index.js` |
| `'**.js'` | Matches all `.js` files in the repository. | `index.js` `js/index.js` `src/js/app.js` |
| `docs/*` | All files within the root of the `docs` directory only, at the root of the repository. | `docs/README.md` `docs/file.txt` |
| `docs/**` | Any files in the `docs` directory and its subdirectories at the root of the repository. | `docs/README.md` `docs/mona/octocat.txt` |
| `docs/**/*.md` | A file with a `.md` suffix anywhere in the `docs` directory. | `docs/README.md` `docs/mona/hello-world.md` `docs/a/markdown/file.md` |
| `'**/docs/**'` | Any files in a `docs` directory anywhere in the repository. | `docs/hello.md` `dir/docs/my-file.txt` `space/docs/plan/space.doc` |
| `'**/README.md'` | A README.md file anywhere in the repository. | `README.md` `js/README.md` |
| `'**/*src/**'` | Any file in a folder with a `src` suffix anywhere in the repository. | `a/src/app.js` `my-src/code/js/app.js` |
| `'**/*-post.md'` | A file with the suffix `-post.md` anywhere in the repository. | `my-post.md` `path/their-post.md` |
| `'**/migrate-*.sql'` | A file with the prefix `migrate-` and suffix `.sql` anywhere in the repository. | `migrate-10909.sql` `db/migrate-v1.0.sql` `db/sept/migrate-v1.sql` |
| `'*.md'` `'!README.md'` | Using an exclamation mark (`!`) in front of a pattern negates it. When a file matches a pattern and also matches a negative pattern defined later in the file, the file will not be included. | `hello.md` *Does not match* `README.md` `docs/hello.md` |
| `'*.md'` `'!README.md'` `README*` | Patterns are checked sequentially. A pattern that negates a previous pattern will re-include file paths. | `hello.md` `README.md` `README.doc` |
