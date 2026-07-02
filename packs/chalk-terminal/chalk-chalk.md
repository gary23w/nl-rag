---
title: "GitHub"
source: https://github.com/chalk/chalk
domain: chalk-terminal
license: CC-BY-SA-4.0
tags: chalk terminal, terminal string styling, ansi color output, cli text color
fetched: 2026-07-02
---

### Uh oh!

There was an error while loading. Please reload this page.

chalk

/

chalk

Public

- Uh oh! There was an error while loading. Please reload this page.
- Notifications You must be signed in to change notification settings
- Fork 1k
- Star

Branches

Tags

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
|---|---|---|---|
| Latest commit History369 Commits369 Commits |   |   |   |
| .github | .github |   |   |
| examples | examples |   |   |
| media | media |   |   |
| source | source |   |   |
| test | test |   |   |
| .editorconfig | .editorconfig |   |   |
| .gitattributes | .gitattributes |   |   |
| .gitignore | .gitignore |   |   |
| .npmrc | .npmrc |   |   |
| benchmark.js | benchmark.js |   |   |
| code-of-conduct.md | code-of-conduct.md |   |   |
| contributing.md | contributing.md |   |   |
| license | license |   |   |
| package.json | package.json |   |   |
| readme.md | readme.md |   |   |
|   |   |   |   |

## Repository files navigation

# (Chalk)

> Terminal string styling done right

(Coverage Status) (npm dependents) (Downloads)

## Info

- Why not switch to a smaller coloring package?
- See yoctocolors for a smaller alternative

## Highlights

- Expressive API
- Highly performant
- No dependencies
- Ability to nest styles
- 256/Truecolor color support
- Auto-detects color support
- Doesn't extend `String.prototype`
- Clean and focused
- Actively maintained
- Used by ~115,000 packages as of July 4, 2024

## Install

```highlight
npm install chalk
```

**IMPORTANT:** Chalk 5 is ESM. If you want to use Chalk with TypeScript or a build tool, you will probably want to use Chalk 4 for now. Read more.

## Usage

```highlight
import chalk from 'chalk';

console.log(chalk.blue('Hello world!'));
```

Chalk comes with an easy to use composable API where you just chain and nest the styles you want.

```highlight
import chalk from 'chalk';

const log = console.log;

// Combine styled and normal strings
log(chalk.blue('Hello') + ' World' + chalk.red('!'));

// Compose multiple styles using the chainable API
log(chalk.blue.bgRed.bold('Hello world!'));

// Pass in multiple arguments
log(chalk.blue('Hello', 'World!', 'Foo', 'bar', 'biz', 'baz'));

// Nest styles
log(chalk.red('Hello', chalk.underline.bgBlue('world') + '!'));

// Nest styles of the same type even (color, underline, background)
log(chalk.green(
	'I am a green line ' +
	chalk.blue.underline.bold('with a blue substring') +
	' that becomes green again!'
));

// ES2015 template literal
log(`
CPU: ${chalk.red('90%')}
RAM: ${chalk.green('40%')}
DISK: ${chalk.yellow('70%')}
`);

// Use RGB colors in terminal emulators that support it.
log(chalk.rgb(123, 45, 67).underline('Underlined reddish color'));
log(chalk.hex('#DEADED').bold('Bold gray!'));
```

Easily define your own themes:

```highlight
import chalk from 'chalk';

const error = chalk.bold.red;
const warning = chalk.hex('#FFA500'); // Orange color

console.log(error('Error!'));
console.log(warning('Warning!'));
```

Take advantage of console.log string substitution:

```highlight
import chalk from 'chalk';

const name = 'Sindre';
console.log(chalk.green('Hello %s'), name);
//=> 'Hello Sindre'
```

## API

### chalk.`<style>[.<style>...](string, [string...])`

Example: `chalk.red.bold.underline('Hello', 'world');`

Chain styles and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `chalk.red.yellow.green` is equivalent to `chalk.green`.

Multiple arguments will be separated by space.

### chalk.level

Specifies the level of color support.

Color support is automatically detected, but you can override it by setting the `level` property. You should however only do this in your own code as it applies globally to all Chalk consumers.

If you need to change this in a reusable module, create a new instance:

```highlight
import {Chalk} from 'chalk';

const customChalk = new Chalk({level: 0});
```

| Level | Description |
|---|---|
| `0` | All colors disabled |
| `1` | Basic color support (16 colors) |
| `2` | 256 color support |
| `3` | Truecolor support (16 million colors) |

### supportsColor

Detect whether the terminal supports color. Used internally and handled for you, but exposed for convenience.

Can be overridden by the user with the flags `--color` and `--no-color`. For situations where using `--color` is not possible, use the environment variable `FORCE_COLOR=1` (level 1), `FORCE_COLOR=2` (level 2), or `FORCE_COLOR=3` (level 3) to forcefully enable color, or `FORCE_COLOR=0` to forcefully disable. The use of `FORCE_COLOR` overrides all other color support checks.

Explicit 256/Truecolor mode can be enabled using the `--color=256` and `--color=16m` flags, respectively.

### chalkStderr and supportsColorStderr

`chalkStderr` contains a separate instance configured with color support detected for `stderr` stream instead of `stdout`. Override rules from `supportsColor` apply to this too. `supportsColorStderr` is exposed for convenience.

### modifierNames, foregroundColorNames, backgroundColorNames, and colorNames

All supported style strings are exposed as an array of strings for convenience. `colorNames` is the combination of `foregroundColorNames` and `backgroundColorNames`.

This can be useful if you wrap Chalk and need to validate input:

```highlight
import {modifierNames, foregroundColorNames} from 'chalk';

console.log(modifierNames.includes('bold'));
//=> true

console.log(foregroundColorNames.includes('pink'));
//=> false
```

## Styles

### Modifiers

- `reset` - Reset the current style.
- `bold` - Make the text bold.
- `dim` - Make the text have lower opacity.
- `italic` - Make the text italic. *(Not widely supported)*
- `underline` - Put a horizontal line below the text. *(Not widely supported)*
- `overline` - Put a horizontal line above the text. *(Not widely supported)*
- `inverse` - Invert background and foreground colors.
- `hidden` - Print the text but make it invisible.
- `strikethrough` - Puts a horizontal line through the center of the text. *(Not widely supported)*
- `visible` - Print the text only when Chalk has a color level above zero. Can be useful for things that are purely cosmetic.

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `blackBright` (alias: `gray`, `grey`)
- `redBright`
- `greenBright`
- `yellowBright`
- `blueBright`
- `magentaBright`
- `cyanBright`
- `whiteBright`

### Background colors

- `bgBlack`
- `bgRed`
- `bgGreen`
- `bgYellow`
- `bgBlue`
- `bgMagenta`
- `bgCyan`
- `bgWhite`
- `bgBlackBright` (alias: `bgGray`, `bgGrey`)
- `bgRedBright`
- `bgGreenBright`
- `bgYellowBright`
- `bgBlueBright`
- `bgMagentaBright`
- `bgCyanBright`
- `bgWhiteBright`

## 256 and Truecolor color support

Chalk supports 256 colors and Truecolor (16 million colors) on supported terminal apps.

Colors are downsampled from 16 million RGB values to an ANSI color format that is supported by the terminal emulator (or by specifying `{level: n}` as a Chalk option). For example, Chalk configured to run at level 1 (basic color support) will downsample an RGB value of #FF0000 (red) to 31 (ANSI escape for red).

Examples:

- `chalk.hex('#DEADED').underline('Hello, world!')`
- `chalk.rgb(15, 100, 204).inverse('Hello!')`

Background versions of these models are prefixed with `bg` and the first level of the module capitalized (e.g. `hex` for foreground colors and `bgHex` for background colors).

- `chalk.bgHex('#DEADED').underline('Hello, world!')`
- `chalk.bgRgb(15, 100, 204).inverse('Hello!')`

The following color models can be used:

- `rgb` - Example: `chalk.rgb(255, 136, 0).bold('Orange!')`
- `hex` - Example: `chalk.hex('#FF8800').bold('Orange!')`
- `ansi256` - Example: `chalk.bgAnsi256(194)('Honeydew, more or less')`

## Browser support

Since Chrome 69, ANSI escape codes are natively supported in the developer console.

## Windows

If you're on Windows, do yourself a favor and use Windows Terminal instead of `cmd.exe`.

## FAQ

### Why not switch to a smaller coloring package?

Chalk may be larger, but there is a reason for that. It offers a more user-friendly API, well-documented types, supports millions of colors, and covers edge cases that smaller alternatives miss. Chalk is mature, reliable, and built to last.

But beyond the technical aspects, there's something more critical: trust and long-term maintenance. I have been active in open source for over a decade, and I'm committed to keeping Chalk maintained. Smaller packages might seem appealing now, but there's no guarantee they will be around for the long term, or that they won't become malicious over time.

Chalk is also likely already in your dependency tree (since 100K+ packages depend on it), so switching won’t save space—in fact, it might increase it. npm deduplicates dependencies, so multiple Chalk instances turn into one, but adding another package alongside it will increase your overall size.

If the goal is to clean up the ecosystem, switching away from Chalk won’t even make a dent. The real problem lies with packages that have very deep dependency trees (for example, those including a lot of polyfills). Chalk has no dependencies. It's better to focus on impactful changes rather than minor optimizations.

If absolute package size is important to you, I also maintain yoctocolors, one of the smallest color packages out there.

*- Sindre*

### But the smaller coloring package has benchmarks showing it is faster

Micro-benchmarks are flawed because they measure performance in unrealistic, isolated scenarios, often giving a distorted view of real-world performance. Don't believe marketing fluff. All the coloring packages are more than fast enough.

## Related

- chalk-template - Tagged template literals support for this module
- chalk-cli - CLI for this module
- ansi-styles - ANSI escape codes for styling strings in the terminal
- supports-color - Detect whether a terminal supports color
- strip-ansi - Strip ANSI escape codes
- strip-ansi-stream - Strip ANSI escape codes from a stream
- has-ansi - Check if a string has ANSI escape codes
- ansi-regex - Regular expression for matching ANSI escape codes
- wrap-ansi - Wordwrap a string with ANSI escape codes
- slice-ansi - Slice a string with ANSI escape codes
- color-convert - Converts colors between different models
- chalk-animation - Animate strings in the terminal
- gradient-string - Apply color gradients to strings
- chalk-pipe - Create chalk style schemes with simpler style strings
- terminal-link - Create clickable links in the terminal

*(Not accepting additional entries)*

## Maintainers

- Sindre Sorhus
- Josh Junon
