---
title: "Configuration Options (part 1/4)"
source: https://rollupjs.org/configuration-options/
domain: rollup
license: CC-BY-SA-4.0 / MIT (rollupjs.org)
tags: rollup bundler, rollupjs, es module bundler, rollup tree shaking
fetched: 2026-07-02
part: 1/4
---

# Configuration Options


## Core functionality 

### external 

| Type: | `(string \| RegExp)[] \| RegExp \| string \| (id: string, parentId: string, isResolved: boolean) => boolean` |
|---|---|
| CLI: | `-e`/`--external <external-id,another-external-id,...>` |

Either a function that takes an `id` and returns `true` (external) or `false` (not external), or an `Array` of module IDs, or regular expressions to match module IDs, that should remain external to the bundle. Can also be just a single ID or regular expression. The matched IDs should be either:

1. the name of an external dependency, exactly the way it is written in the import statement. I.e. to mark `import "dependency.js"` as external, use `"dependency.js"` while to mark `import "dependency"` as external, use `"dependency"`.
2. a resolved ID (like an absolute path to a file).

js

```js
// rollup.config.js
import { fileURLToPath
 } from 'node:url';

export default {
	//...,
	external
: [
		'some-externally-required-library',
		fileURLToPath
(
			new URL
(
				'src/some-local-file-that-should-not-be-bundled.js',
				import.meta.url

			)
		),
		/node_modules/
	]
};
```

Note that if you want to filter out package imports, e.g. `import {rollup} from 'rollup'`, via a `/node_modules/` regular expression, you need something like @rollup/plugin-node-resolve to resolve the imports to `node_modules` first.

When given as a command line argument, it should be a comma-separated list of IDs:

bash

```bash
rollup -i src/main.js ... -e foo,bar,baz
```

When providing a function, it is called with three parameters `(id, parent, isResolved)` that can give you more fine-grained control:

- `id` is the id of the module in question
- `parent` is the id of the module doing the import
- `isResolved` signals whether the `id` has been resolved by e.g. plugins

When creating an `iife` or `umd` bundle, you will need to provide global variable names to replace your external imports via the `output.globals` option.

Note that source phase imports (`import source x from 'y'`) are required to be external. Rollup will raise an error if a source phase import resolves to a module that is not external.

If a relative import, i.e. starting with `./` or `../`, is marked as "external", rollup will internally resolve the id to an absolute file system location so that different imports of the external module can be merged. When the resulting bundle is written, the import will again be converted to a relative import. Example:

js

```js
// input
// src/main.js (entry point)
import x from '../external.js';
import './nested/nested.js';
console.log(x);

// src/nested/nested.js
// the import would point to the same file if it existed
import x from '../../external.js';
console.log(x);

// output
// the different imports are merged
import x from '../external.js';

console.log(x);

console.log(x);
```

The conversion back to a relative import is done as if `output.file` or `output.dir` were in the same location as the entry point or the common base directory of all entry points if there is more than one.

### input 

| Type: | `string \| string [] \| { [entryName: string]: string }` |
|---|---|
| CLI: | `-i`/`--input <filename>` |

The bundle's entry point(s) (e.g. your `main.js` or `app.js` or `index.js`). If you provide an array of entry points or an object mapping names to entry points, they will be bundled to separate output chunks. Unless the `output.file` option is used, generated chunk names will follow the `output.entryFileNames` option. When using the object form, the `[name]` portion of the file name will be the name of the object property while for the array form, it will be the file name of the entry point.

Note that it is possible when using the object form to put entry points into different sub-folders by adding a `/` to the name. The following will generate at least two entry chunks with the names `entry-a.js` and `entry-b/index.js`, i.e. the file `index.js` is placed in the folder `entry-b`:

js

```js
// rollup.config.js
export default {
	// ...
	input
: {
		a
: 'src/main-a.js',
		'b/index': 'src/main-b.js'
	},
	output
: {
		// ...
		entryFileNames
: 'entry-[name].js'
	}
};
```

If you want to convert a set of files to another format while maintaining the file structure and export signatures, the recommended way—instead of using `output.preserveModules` that may tree-shake exports as well as emit virtual files created by plugins—is to turn every file into an entry point. You can do so dynamically e.g. via the `glob` package:

ts

```ts
import { globSync
 } from 'glob';
import path
 from 'node:path';
import { fileURLToPath
 } from 'node:url';

export default {
	input
: Object
.fromEntries
(
		globSync
('src/**/*.js').map
(file
 => [
			// This removes `src/` as well as the file extension from each
			// file, so e.g. src/nested/foo.js becomes nested/foo
			path
.relative
(
				'src',
				file
.slice
(0, file
.length
 - path
.extname
(file
).length
)
			),
			// This expands the relative paths to absolute paths, so e.g.
			// src/nested/foo becomes /project/src/nested/foo.js
			fileURLToPath
(new URL
(file
, import.meta.url
))
		])
	),
	output
: {
		format
: 'es',
		dir
: 'dist'
	}
};
```

The option can be omitted if some plugin emits at least one chunk (using `this.emitFile`) by the end of the `buildStart` hook.

When using the command line interface, multiple inputs can be provided by using the option multiple times. When provided as the first options, it is equivalent to not prefix them with `--input`:

shell

```shell
rollup --format es --input src/entry1.js --input src/entry2.js
# is equivalent to
rollup src/entry1.js src/entry2.js --format es
```

Chunks can be named by adding an `=` to the provided value:

shell

```shell
rollup main=src/entry1.js other=src/entry2.js --format es
```

File names containing spaces can be specified by using quotes:

shell

```shell
rollup "main entry"="src/entry 1.js" "src/other entry.js" --format es
```

### jsx 

| Type: | `false \| JsxPreset \| JsxOptions` |
|---|---|
| CLI: | `--jsx <preset>`/`--no-jsx` |
| Default: | `false` |

typescript

```typescript
type JsxPreset = 'react' | 'react-jsx' | 'preserve' | 'preserve-react';

type JsxOptions =
	| {
			mode: 'preserve';
			factory: string | null;
			fragment: string | null;
			importSource: string | null;
			preset: JsxPreset | null;
	  }
	| {
			mode: 'classic';
			factory: string;
			fragment: string;
			importSource: string | null;
			preset: JsxPreset | null;
	  }
	| {
			mode: 'automatic';
			factory: string;
			importSource: string;
			jsxImportSource: string;
			preset: JsxPreset | null;
	  };
```

Allows Rollup to process JSX syntax to either preserve or transform it depending on the `jsx.mode`. If set to `false`, an error will be thrown if JSX syntax is encountered. You may also choose a preset that will set all options together:

- `"react"`: For transpiling JSX to `React.createElement` calls, where `React` is the default import from `"react"`. This is similar to setting `"jsx": "react"` in TypeScript compiler options.js`({ mode: 'classic', factory: 'React.createElement', fragment: 'React.Fragment', importSource: 'react' });`
- `"react-jsx"`: This will use the new optimized React transformation introduced with React 17 and is similar to setting `"jsx": "react-jsx"` in TypeScript compiler options.js`({ mode: 'automatic', factory: 'React.createElement', importSource: 'react', jsxImportSource: 'react/jsx-runtime' });`
- `"preserve"`: This will preserve JSX in the output. This will still tree-shake unused JSX code and may rename JSX identifiers if there are conflicts in the output.js`({ mode: 'preserve', factory: null, fragment: null, importSource: null });`
- `"preserve-react"`: This will preserve JSX in the output but ensure that the default export of `"react"` is in scope as a variable named `React`.js`({ mode: 'preserve', factory: 'React.createElement', fragment: 'React.Fragment', importSource: 'react' });`

#### jsx.mode 

| Type: | `"preserve" \| "classic" \| "automatic"` |
|---|---|
| CLI: | `--jsx.mode <mode>` |
| Default: | `"classic"` |

This will determine how JSX is processed:

- `"preserve"`: Will keep JSX syntax in the output.
- `"classic"`: This will perform a JSX transformation as it is needed by older React versions or other frameworks like for instance Preact. As an example, here is how you would configure jsx for Preact:js`({ mode: 'classic', factory: 'h', fragment: 'Fragment', importSource: 'preact' });`This would perform the following transformation:jsx`// input console.log(<div>hello</div>); // output import { h } from 'preact'; console.log(/*#__PURE__*/ h('div', null, 'hello'));`
- `"automatic"`: This will perform a JSX transformation using the new JSX transform introduced with React 17. In this mode, Rollup will try to import helpers from `jsx.jsxImportSource` to transform JSX. As there are certain edge cases, this mode may still fall back to using the classic transformations when using the `key` property together with spread attributes. To this end, you can still specify `jsx.importSource`, `jsx.factory`, and `jsx.fragment` to configure classic mode.

#### jsx.factory 

| Type: | `string \| null` |
|---|---|
| CLI: | `--jsx.factory <factory>` |
| Default: | `"React.createElement"` or `null` |

The function Rollup uses to create JSX elements in `"classic"` mode or as a fallback in `"automatic"` mode. This is usually `React.createElement` for React or `h` for other frameworks. In `"preserve"` mode, this will ensure that the factory is in scope if `jsx.importSource` is specified, or otherwise that a global variable of the same name would not be overridden by local variables. Only in `"preserve"` mode it is possible to set this value to `null`, in which case Rollup will not take care to keep any particular factory function in scope.

If the value contains a `"."` like `React.createElement` and an `jsx.importSource` is specified, Rollup will assume that the left part, e.g. `React`, refers to the default export of the `jsx.importSource`. Otherwise, Rollup assumes it is a named export.

#### jsx.fragment 

| Type: | `string \| null` |
|---|---|
| CLI: | `--jsx.fragment <fragment>` |
| Default: | `"React.Fragment"` or `null` |

The element function Rollup uses to create JSX fragments. This is usually `React.Fragment` for React or `Fragment` for other frameworks. In `"preserve"` mode, this will ensure that the fragment is in scope if `jsx.importSource` is specified, or otherwise that a global variable of the same name would not be overridden by local variables. Only in `"preserve"` mode it is possible to set this value to `null`, in which case Rollup will not take care to keep any particular fragment function in scope.

If the value contains a `"."` like `React.Fragment` and an `jsx.importSource` is specified, Rollup will assume that the left part, e.g. `React`, refers to the default export of the `jsx.importSource`. Otherwise, Rollup assumes it is a named export.

#### jsx.importSource 

| Type: | `string \| null` |
|---|---|
| CLI: | `--jsx.importSource <library>` |
| Default: | `null` |

Where to import the element factory function and/or the fragment element from. If left to `null`, Rollup will assume that `jsx.factory` and `jsx.fragment` refer to global variables and makes sure they are not shadowed by local variables.

#### jsx.jsxImportSource 

| Type: | `string` |
|---|---|
| CLI: | `--jsx.jsxImportSource <library>` |
| Default: | `"react/jsx-runtime"` |

When using `"automatic"` mode, this will specify from where to import the `jsx`, `jsxs` and `Fragment` helpers needed for that transformation. It is not possible to get those from a global variable.

#### jsx.preset 

| Type: | JsxPreset |
|---|---|
| CLI: | `--jsx.preset <value>` |

Allows choosing one of the presets listed above while overriding some options.

js

```js
export default {
	jsx
: {
		preset
: 'react',
		importSource
: 'preact',
		factory
: 'h'
	}
	// ...
};
```

### output.dir 

| Type: | `string` |
|---|---|
| CLI: | `-d`/`--dir <dirname>` |

The directory in which all generated chunks are placed. This option is required if more than one chunk is generated. Otherwise, the `file` option can be used instead.

### output.file 

| Type: | `string` |
|---|---|
| CLI: | `-o`/`--file <filename>` |

The file to write to. Will also be used to generate sourcemaps, if applicable. Can only be used if not more than one chunk is generated.

### output.format 

| Type: | `string` |
|---|---|
| CLI: | `-f`/`--format <formatspecifier>` |
| Default: | `"es"` |

Specifies the format of the generated bundle. One of the following:

- `amd` – Asynchronous Module Definition, used with module loaders like RequireJS
- `cjs` – CommonJS, suitable for Node and other bundlers (alias: `commonjs`)
- `es` – Keep the bundle as an ES module file, suitable for other bundlers and inclusion as a `<script type=module>` tag in modern browsers (alias: `esm`, `module`)
- `iife` – A self-executing function, suitable for inclusion as a `<script>` tag. (If you want to create a bundle for your application, you probably want to use this.). "iife" stands for "immediately-invoked Function Expression"
- `umd` – Universal Module Definition, works as `amd`, `cjs` and `iife` all in one
- `system` – Native format of the SystemJS loader (alias: `systemjs`)

### output.globals 

| Type: | `{ [id: string]: string } \| ((id: string) => string)` |
|---|---|
| CLI: | `-g`/`--globals <external-id:variableName,another-external-id:anotherVariableName,...>` |

Specifies `id: variableName` pairs necessary for external imports in `umd`/`iife` bundles. For example, in a case like this…

js

```js
import $ from 'jquery';
```

…we want to tell Rollup that `jquery` is external and the `jquery` module ID equates to the global `$` variable:

js

```js
// rollup.config.js
export default {
	// ...
	external
: ['jquery'],
	output
: {
		format
: 'iife',
		name
: 'MyBundle',
		globals
: {
			jquery
: '$'
		}
	}
};

/*
var MyBundle = (function ($) {
  // code goes here
}($));
*/
```

Alternatively, supply a function that will turn an external module ID into a global variable name.

When given as a command line argument, it should be a comma-separated list of `id:variableName` pairs:

shell

```shell
rollup -i src/main.js ... -g jquery:$,underscore:_
```

To tell Rollup that a local file should be replaced by a global variable, use an absolute id:

js

```js
// rollup.config.js
import { fileURLToPath
 } from 'node:url';
const externalId
 = fileURLToPath
(
	new URL
(
		'src/some-local-file-that-should-not-be-bundled.js',
		import.meta.url

	)
);

export default {
	//...,
	external
: [externalId
],
	output
: {
		format
: 'iife',
		name
: 'MyBundle',
		globals
: {
			[externalId
]: 'globalVariable'
		}
	}
};
```

### output.name 

| Type: | `string` |
|---|---|
| CLI: | `-n`/`--name <variableName>` |

Necessary for `iife`/`umd` bundles that exports values in which case it is the global variable name representing your bundle. Other scripts on the same page can use this variable name to access the exports of your bundle.

js

```js
// rollup.config.js
export default {
	// ...
	output
: {
		file
: 'bundle.js',
		format
: 'iife',
		name
: 'MyBundle'
	}
};

// var MyBundle = (function () {...
```

Namespaces are supported i.e. your name can contain dots. The resulting bundle will contain the setup necessary for the namespacing.

shell

```shell
rollup -n "a.b.c"

/* ->
this.a = this.a || {};
this.a.b = this.a.b || {};
this.a.b.c = ...
*/
```

### output.plugins 

| Type: | `MaybeArray<MaybePromise<OutputPlugin \| void>>` |
|---|---|

Adds a plugin just to this output. See Using output plugins for more information on how to use output-specific plugins and Plugins on how to write your own. For plugins imported from packages, remember to call the imported plugin function (i.e. `commonjs()`, not just `commonjs`). Falsy plugins will be ignored, which can be used to easily activate or deactivate plugins. Nested plugins will be flattened. Async plugin will be awaited and resolved.

Not every plugin can be used here. `output.plugins` is limited to plugins that only use hooks that run during `bundle.generate()` or `bundle.write()`, i.e. after Rollup's main analysis is complete. If you are a plugin author, see output generation hooks to find out which hooks can be used.

The following will add minification to one of the outputs:

js

```js
// rollup.config.js
import terser
 from '@rollup/plugin-terser';

export default {
	input
: 'main.js',
	output
: [
		{
			file
: 'bundle.js',
			format
: 'es'
		},
		{
			file
: 'bundle.min.js',
			format
: 'es',
			plugins
: [terser
()]
		}
	]
};
```

### plugins 

| Type: | `MaybeArray<MaybePromise<Plugin \| void>>` |
|---|---|

See Using plugins for more information on how to use plugins and Plugins on how to write your own (try it out, it's not as difficult as it may sound and very much extends what you can do with Rollup). For plugins imported from packages, remember to call the imported plugin function (i.e. `commonjs()`, not just `commonjs`). Falsy plugins will be ignored, which can be used to easily activate or deactivate plugins. Nested plugins will be flattened. Async plugins will be awaited and resolved.

js

```js
// rollup.config.js
import resolve
 from '@rollup/plugin-node-resolve';
import commonjs
 from '@rollup/plugin-commonjs';

const isProduction
 = process
.env
.NODE_ENV
 === 'production';

export default (async () => ({
	input
: 'main.js',
	plugins
: [
		resolve
(),
		commonjs
(),
		isProduction
 && (await import('@rollup/plugin-terser')).default
()
	],
	output
: {
		file
: 'bundle.js',
		format
: 'cjs'
	}
}))();
```

(This example also demonstrates how to use an async IIFE and dynamic imports to avoid unnecessary module loading, which can be surprisingly slow.)
