---
title: "Configuration Options (part 3/4)"
source: https://rollupjs.org/configuration-options/
domain: rollup
license: CC-BY-SA-4.0 / MIT (rollupjs.org)
tags: rollup bundler, rollupjs, es module bundler, rollup tree shaking
fetched: 2026-07-02
part: 3/4
---

# Configuration Options

| Type: | `string \| ((chunk: RenderedChunk) => string \| Promise<string>)` |
|---|---|
| CLI: | `--intro`/`--outro <text>` |

Similar to `output.banner/output.footer`, except that the code goes *inside* any format-specific wrapper.

js

```js
export default {
	//...,
	output
: {
		//...,
		intro
: 'const ENVIRONMENT = "production";'
	}
};
```

### output.manualChunks 

| Type: | `{ [chunkAlias: string]: string[] } \| ((id: string, {getModuleInfo, getModuleIds}) => string \| void)` |
|---|---|

Allows the creation of custom shared common chunks. The object form can be used for an easier and safer manual chunking, and the function form can be used for a more powerful and controlled behavior.

When using the object form, each property represents a chunk that contains the listed modules and all their dependencies if they are part of the module graph unless they are already in another manual chunk. The name of the chunk will be determined by the property key. Note that it is not necessary for the listed modules themselves to be part of the module graph, which is useful if you are working with `@rollup/plugin-node-resolve` and use deep imports from packages. For instance

javascript

```javascript
manualChunks: {
	lodash: ['lodash'],
}
```

will merge all lodash modules into a manual chunk even if you are only using imports of the form `import get from 'lodash/get'`.

When using the function form, each resolved module id will be passed to the function. If a string is returned, the module and all its dependencies will be added to the manual chunk with the given name. For instance this will create a `vendor` chunk containing all dependencies inside `node_modules`:

javascript

```javascript
function manualChunks
(id
) {
	if (id
.includes
('node_modules')) {
		return 'vendor';
	}

	return null;
}
```

By default, the function form will also merge dependencies of the returned ids into the manualChunk. If you need stricter behavior, you can use output.onlyExplicitManualChunks, which will be the default in Rollup 5.

Be aware that manual chunks can change the behaviour of the application if side effects are triggered before the corresponding modules are actually used.

When using the function form, `manualChunks` will be passed an object as second parameter containing the functions `getModuleInfo` and `getModuleIds` that work the same way as `this.getModuleInfo` and `this.getModuleIds` on the plugin context.

This can be used to dynamically determine into which manual chunk a module should be placed depending on its position in the module graph. For instance consider a scenario where you have a set of components, each of which dynamically imports a set of translated strings, i.e.

js

```js
// Inside the "foo" component

function getTranslatedStrings(currentLanguage) {
	switch (currentLanguage) {
		case 'en':
			return import('./foo.strings.en.js');
		case 'de':
			return import('./foo.strings.de.js');
		// ...
	}
}
```

If a lot of such components are used together, this will result in a lot of dynamic imports of very small chunks: Even though we know that all language files of the same language that are imported by the same chunk will always be used together, Rollup does not have this information.

The following code will merge all files of the same language that are only used by a single entry point:

js

```js
function manualChunks
(id
, { getModuleInfo
 }) {
	const match
 = /.*\.strings\.(\w+)\.js/.exec
(id
);
	if (match
) {
		const language
 = match
[1]; // e.g. "en"
		const dependentEntryPoints
 = [];

		// we use a Set here so we handle each module at most once. This
		// prevents infinite loops in case of circular dependencies
		const idsToHandle
 = new Set
(getModuleInfo
(id
).dynamicImporters
);

		for (const moduleId
 of idsToHandle
) {
			const { isEntry
, dynamicImporters
, importers
 } =
				getModuleInfo
(moduleId
);
			if (isEntry
 || dynamicImporters
.length
 > 0)
				dependentEntryPoints
.push
(moduleId
);

			// The Set iterator is intelligent enough to iterate over
			// elements that are added during iteration
			for (const importerId
 of importers
) idsToHandle
.add
(importerId
);
		}

		// If there is a unique entry, we put it into a chunk based on the
		// entry name
		if (dependentEntryPoints
.length
 === 1) {
			return `${
				dependentEntryPoints
[0].split
('/').slice
(-1)[0].split
('.')[0]
			}.strings.${language
}`;
		}
		// For multiple entries, we put it into a "shared" chunk
		if (dependentEntryPoints
.length
 > 1) {
			return `shared.strings.${language
}`;
		}
	}
}
```

### output.minifyInternalExports 

| Type: | `boolean` |
|---|---|
| CLI: | `--minifyInternalExports`/`--no-minifyInternalExports` |
| Default: | `true` for formats `es` and `system` or if `output.compact` is `true`, `false` otherwise |

By default, for formats `es` and `system` or if `output.compact` is `true`, Rollup will try to export internal variables as single letter variables to allow for better minification.

**Example** Input:

js

```js
// main.js
import './lib.js';

// lib.js
import('./dynamic.js');
export const importantValue = 42;

// dynamic.js
import { importantValue } from './lib.js';
console.log(importantValue);
```

Output with `output.minifyInternalExports: true`:

js

```js
// main.js
import './main-5532def0.js';

// main-5532def0.js
import('./dynamic-402de2f0.js');
const importantValue = 42;

export { importantValue as i };

// dynamic-402de2f0.js
import { i as importantValue } from './main-5532def0.js';

console.log(importantValue);
```

Output with `output.minifyInternalExports: false`:

js

```js
// main.js
import './main-5532def0.js';

// main-5532def0.js
import('./dynamic-402de2f0.js');
const importantValue = 42;

export { importantValue };

// dynamic-402de2f0.js
import { importantValue } from './main-5532def0.js';

console.log(importantValue);
```

Even though it appears that setting this option to `true` makes the output larger, it actually makes it smaller if a minifier is used. In this case, `export { importantValue as i }` can become e.g. `export{a as i}` or even `export{i}`, while otherwise it would produce `export{ a as importantValue }` because a minifier usually will not change export signatures.

### output.paths 

| Type: | `{ [id: string]: string } \| ((id: string) => string)` |
|---|---|

Maps external module IDs to paths. External ids are ids that cannot be resolved or ids explicitly provided by the `external` option. Paths supplied by `output.paths` will be used in the generated bundle instead of the module ID, allowing you to, for example, load dependencies from a CDN:

js

```js
// app.js
import { selectAll
 } from 'd3';
selectAll
('p').style
('color', 'purple');
// ...

// rollup.config.js
export default {
	input
: 'app.js',
	external
: ['d3'],
	output
: {
		file
: 'bundle.js',
		format
: 'amd',
		paths
: {
			d3
: 'https://d3js.org/d3.v4.min'
		}
	}
};

// bundle.js
define(['https://d3js.org/d3.v4.min'], function (d3
) {
	d3
.selectAll('p').style('color', 'purple');
	// ...
});
```

### output.preserveModules 

| Type: | `boolean` |
|---|---|
| CLI: | `--preserveModules`/`--no-preserveModules` |
| Default: | `false` |

Instead of creating as few chunks as possible, this mode will create separate chunks for all modules using the original module names as file names. Requires the `output.dir` option. Tree-shaking will still be applied, suppressing files that are not used by the provided entry points or do not have side effects when executed and removing unused exports of files that are not entry points. On the other hand, if plugins (like `@rollup/plugin-commonjs`) emit additional "virtual" files to achieve certain results, those files will be emitted as actual files using a pattern `${output.virtualDirname}/fileName.js`.

It is therefore not recommended to blindly use this option to transform an entire file structure to another format if you directly want to import from those files as expected exports may be missing. In that case, you should rather designate all files explicitly as entry points by adding them to the `input` option object, see the example there for how to do that.

Note that when transforming to `cjs` or `amd` format, each file will by default be treated as an entry point with `output.exports` set to `auto`. This means that e.g. for `cjs`, a file that only contains a default export will be rendered as

js

```js
// input main.js
export default 42;

// output main.js
('use strict');

var main = 42;

module.exports = main;
```

assigning the value directly to `module.exports`. If someone imports this file, they will get access to the default export via

js

```js
const main = require('./main.js');
console.log(main); // 42
```

As with regular entry points, files that mix default and named exports will produce warnings. You can avoid the warnings by forcing all files to use named export mode via `output.exports: "named"`. In that case, the default export needs to be accessed via the `.default` property of the export:

js

```js
// input main.js
export default 42;

// output main.js
('use strict');

Object.defineProperty(exports, '__esModule', { value: true });

var main = 42;

exports.default = main;

// consuming file
const main = require('./main.js');
console.log(main.default); // 42
```

### output.preserveModulesRoot 

| Type: | `string` |
|---|---|
| CLI: | `--preserveModulesRoot <directory-name>` |

A directory path to input modules that should be stripped away from `output.dir` path while `output.preserveModules` is `true`.

For example, given the following configuration:

javascript

```javascript
export default {
	input
: ['src/module.js', `src/another/module.js`],
	output
: [
		{
			format
: 'es',
			dir
: 'dist',
			preserveModules
: true,
			preserveModulesRoot
: 'src'
		}
	]
};
```

The `preserveModulesRoot` setting ensures that the input modules will be output to the paths `dist/module.js` and `dist/another/module.js`.

This option is particularly useful while using plugins such as `@rollup/plugin-node-resolve`, which may cause changes in the output directory structure. This can happen when third-party modules are not marked `external`, or while developing in a monorepo of multiple packages that rely on one another and are not marked `external`.

### output.sourcemap 

| Type: | `boolean \| 'inline' \| 'hidden'` |
|---|---|
| CLI: | `-m`/`--sourcemap`/`--no-sourcemap` |
| Default: | `false` |

If `true`, a separate sourcemap file will be created. If `"inline"`, the sourcemap will be appended to the resulting `output` file as a data URI. `"hidden"` works like `true` except that the corresponding sourcemap comments in the bundled files are suppressed.

### output.sourcemapBaseUrl 

| Type: | `string` |
|---|---|
| CLI: | `--sourcemapBaseUrl <url>` |

By default, sourcemap files generated by Rollup uses relative URLs to reference the files they describe. By providing an absolute base URL, e.g. `https://example.com`, sourcemaps will use absolute URLs instead.

### output.sourcemapDebugIds 

| Type: | `boolean` |
|---|---|
| CLI: | `--sourcemapDebugIds`/`--no-sourcemapDebugIds` |
| Default: | `false` |

if `true`, unique ids will be emitted in source and sourcemaps which streamlines identifying sourcemaps across different builds. See the TC39 sourcemap debug ID proposal for more details.

### output.sourcemapExcludeSources 

| Type: | `boolean` |
|---|---|
| CLI: | `--sourcemapExcludeSources`/`--no-sourcemapExcludeSources` |
| Default: | `false` |

If `true`, the actual code of the sources will not be added to the sourcemaps, making them considerably smaller.

### output.sourcemapFile 

| Type: | `string` |
|---|---|
| CLI: | `--sourcemapFile <file-name-with-path>` |

The location of the generated bundle. If this is an absolute path, all the `sources` paths in the sourcemap will be relative to it. The `map.file` property is the basename of `sourcemapFile`, as the location of the sourcemap is assumed to be adjacent to the bundle.

`sourcemapFile` is not required if `output` is specified, in which case an output filename will be inferred by adding ".map" to the output filename for the bundle.

### output.sourcemapFileNames 

| Type: | `string \| ((chunkInfo: PreRenderedChunk) => string)` |
|---|---|
| CLI: | `--sourcemapFileNames <pattern>` |

See `output.chunkFileNames` for the `PreRenderedChunk` type.

The pattern to use for sourcemaps, or a function that is called per sourcemap to return such a pattern. Patterns support the following placeholders:

- `[format]`: The rendering format defined in the output options, e.g. `es` or `cjs`.
- `[hash]`: A hash based only on the content of the final generated sourcemap. You can also set a specific hash length via e.g. `[hash:10]`. By default, it will create a base-64 hash. If you need a reduced character sets, see `output.hashCharacters`
- `[chunkhash]`: The same hash as the one used for the corresponding generated chunk (if any).
- `[name]`: The file name (without extension) of the entry point, unless the object form of input was used to define a different name.

Forward slashes `/` can be used to place files in sub-directories. When using a function, `chunkInfo` is a reduced version of the one in `generateBundle` without properties that depend on file names and no information about the rendered modules as rendering only happens after file names have been generated. You can however access a list of included `moduleIds`. See also `output.assetFileNames`, `output.chunkFileNames`.

### output.sourcemapIgnoreList 

| Type: | `boolean \| (relativeSourcePath: string, sourcemapPath: string) => boolean` |
|---|---|

A predicate to decide whether or not to ignore-list source files in a sourcemap, used to populate the `x_google_ignoreList` source map extension. `relativeSourcePath` is a relative path from the generated `.map` file to the corresponding source file while `sourcemapPath` is the fully resolved path of the generated sourcemap file.

js

```js
import path
 from 'node:path';
export default {
	input
: 'src/main',
	output
: [
		{
			file
: 'bundle.js',
			sourcemapIgnoreList
: (relativeSourcePath
, sourcemapPath
) => {
				// will ignore-list all files with node_modules in their paths
				return relativeSourcePath
.includes
('node_modules');
			},
			format
: 'es',
			sourcemap
: true
		}
	]
};
```

When you don't specify this option explicitly, by default it will put all files with `node_modules` in their path on the ignore list. You can specify `false` here to turn off the ignore-listing completely.

### output.sourcemapPathTransform 

| Type: | `(relativeSourcePath: string, sourcemapPath: string) => string` |
|---|---|

A transformation to apply to each path in a sourcemap. `relativeSourcePath` is a relative path from the generated `.map` file to the corresponding source file while `sourcemapPath` is the fully resolved path of the generated sourcemap file.

js

```js
import path
 from 'node:path';
export default {
	input
: 'src/main',
	output
: [
		{
			file
: 'bundle.js',
			sourcemapPathTransform
: (relativeSourcePath
, sourcemapPath
) => {
				// will replace relative paths with absolute paths
				return path
.resolve
(
					path
.dirname
(sourcemapPath
),
					relativeSourcePath

				);
			},
			format
: 'es',
			sourcemap
: true
		}
	]
};
```

### output.validate 

| Type: | `boolean` |
|---|---|
| CLI: | `--validate`/`--no-validate` |
| Default: | `false` |

Re-parses each generated chunk to detect if the generated code is valid JavaScript. This can be useful to debug output generated by plugins that use the `renderChunk` hook to transform code.

If the code is invalid, a warning will be issued. Note that no error is thrown so that you can still inspect the generated output. To promote this warning to an error, you can watch for it in an `onwarn` handler.

### output.virtualDirname 

| Type: | `string` |
|---|---|
| CLI: | `--virtualDirname <dirname>` |
| Default: | `_virtual` |

This option specifies the directory name for "virtual" files that might be emitted by plugins (like `@rollup/plugin-commonjs`). It is only validated when `output.preserveModules` is enabled.

### preserveEntrySignatures 

| Type: | `"strict" \| "allow-extension" \| "exports-only" \| false` |
|---|---|
| CLI: | `--preserveEntrySignatures <strict \| allow-extension>`/`--no-preserveEntrySignatures` |
| Default: | `"exports-only"` |

Controls if Rollup tries to ensure that entry chunks have the same exports as the underlying entry module.

- If set to `"strict"`, Rollup will create exactly the same exports in the entry chunk as there are in the corresponding entry module. If this is not possible because additional internal exports need to be added to a chunk, Rollup will instead create a "facade" entry chunk that reexports just the necessary bindings from other chunks but contains no code otherwise. This is the recommended setting for libraries.
- `"allow-extension"` will create all exports of the entry module in the entry chunk but may also add additional exports if necessary, avoiding a "facade" entry chunk. This setting makes sense for libraries where a strict signature is not required.
- `"exports-only"` behaves like `"strict"` if the entry module has exports, otherwise it behaves like `"allow-extension"`.
- `false` will not add any exports of an entry module to the corresponding chunk and does not even include the corresponding code unless those exports are used elsewhere in the bundle. Internal exports may be added to entry chunks, though. This is the recommended setting for web apps where the entry chunks are to be placed in script tags as it may reduce both the number of chunks and possibly the bundle size.

**Example** Input:

js

```js
// main.js
import { shared } from './lib.js';
export const value = `value: ${shared}`;
import('./dynamic.js');

// lib.js
export const shared = 'shared';

// dynamic.js
import { shared } from './lib.js';
console.log(shared);
```

Output for `preserveEntrySignatures: "strict"`:

js

```js
// main.js
export { v as value } from './main-50a71bb6.js';

// main-50a71bb6.js
const shared = 'shared';

const value = `value: ${shared}`;
import('./dynamic-cd23645f.js');

export { shared as s, value as v };

// dynamic-cd23645f.js
import { s as shared } from './main-50a71bb6.js';

console.log(shared);
```

Output for `preserveEntrySignatures: "allow-extension"`:

js

```js
// main.js
const shared = 'shared';

const value = `value: ${shared}`;
import('./dynamic-298476ec.js');

export { shared as s, value };

// dynamic-298476ec.js
import { s as shared } from './main.js';

console.log(shared);
```

Output for `preserveEntrySignatures: false`:

js

```js
// main.js
import('./dynamic-39821cef.js');

// dynamic-39821cef.js
const shared = 'shared';

console.log(shared);
```

At the moment, the only way to override this setting for individual entry chunks is to use the plugin API and emit those chunks via `this.emitFile` instead of using the `input` option.

### strictDeprecations 

| Type: | `boolean` |
|---|---|
| CLI: | `--strictDeprecations`/`--no-strictDeprecations` |
| Default: | `false` |

When this flag is enabled, Rollup will throw an error instead of showing a warning when a deprecated feature is used. Furthermore, features that are marked to receive a deprecation warning with the next major version will also throw an error when used.

This flag is intended to be used by e.g. plugin authors to be able to adjust their plugins for upcoming major releases as early as possible.


## Danger zone 

You probably don't need to use these options unless you know what you are doing!

### context 

| Type: | `string` |
|---|---|
| CLI: | `--context <contextVariable>` |
| Default: | `undefined` |

By default, the context of a module – i.e., the value of `this` at the top level – is `undefined`. In rare cases you might need to change this to something else, like `'window'`.

### moduleContext 

| Type: | `((id: string) => string) \| { [id: string]: string }` |
|---|---|

Same as `context`, but per-module – can either be an object of `id: context` pairs, or an `id => context` function.

### output.amd 

| Type: | `{ id?: string, autoId?: boolean, basePath?: string, define?: string }` |
|---|---|

Note `id` can only be used for single-file builds, and cannot be combined with `autoId`/`basePath`.

#### output.amd.id 

| Type: | `string` |
|---|---|
| CLI: | `--amd.id <amdId>` |

An ID to use for AMD/UMD bundles:

js

```js
// rollup.config.js
export default {
	// ...
	output
: {
		format
: 'amd',
		amd
: {
			id
: 'my-bundle'
		}
	}
};

// -> define('my-bundle', ['dependency'], ...
```

#### output.amd.autoId 

| Type: | `boolean` |
|---|---|
| CLI: | `--amd.autoId` |

Set the ID to the chunk ID (with the '.js' extension removed).

js

```js
// rollup.config.js
export default {
	// ...
	output
: {
		format
: 'amd',
		amd
: {
			autoId
: true
		}
	}
};

// -> define('main', ['dependency'], ...
// -> define('dynamic-chunk', ['dependency'], ...
```

#### output.amd.basePath 

| Type: | `string` |
|---|---|
| CLI: | `--amd.basePath` |

The path that will be prepended to the auto generated ID. This is useful if the build is going to be placed inside another AMD project, and is not at the root.

Only valid with `output.amd.autoId`.

js

```js
// rollup.config.js
export default {
	// ...
	output
: {
		format
: 'amd',
		amd
: {
			autoId
: true,
			basePath
: 'some/where'
		}
	}
};

// -> define('some/where/main', ['dependency'], ...
// -> define('some/where/dynamic-chunk', ['dependency'], ...
```

#### output.amd.define 

| Type: | `string` |
|---|---|
| CLI: | `--amd.define <defineFunctionName>` |

A function name to use instead of `define`:

js

```js
// rollup.config.js
export default {
	// ...
	output
: {
		format
: 'amd',
		amd
: {
			define
: 'def'
		}
	}
};

// -> def(['dependency'],...
```

#### output.amd.forceJsExtensionForImports 

| Type: | `boolean` |
|---|---|
| CLI: | `--amd.forceJsExtensionForImports` |
| Default: | `false` |

Add `.js` extension for imports of generated chunks and local AMD modules:

js

```js
// rollup.config.js
export default {
	// ...
	output
: {
		format
: 'amd',
		amd
: {
			forceJsExtensionForImports
: true
		}
	}
};

// -> define(['./chunk-or-local-file.js', 'dependency', 'third/dependency'],...
```

### output.esModule 

| Type: | `boolean \| "if-default-prop"` |
|---|---|
| CLI: | `--esModule`/`--no-esModule` |
| Default: | `"if-default-prop"` |

Whether to add a `__esModule: true` property when generating exports for non-ES formats. This property signifies that the exported value is the namespace of an ES module and that the default export of this module corresponds to the `.default` property of the exported object.

- `true` will always add the property when using named exports mode, which is similar to what other tools do.
- `"if-default-prop"` will only add the property when using named exports mode and there also is a default export. The subtle difference is that if there is no default export, consumers of the CommonJS version of your library will get all named exports as default export instead of an error or `undefined`. We chose to make this the default value as the `__esModule` property is not a standard followed by any JavaScript runtime and leads to many interop issues, so we want to limit its use to the cases where it is really needed.
- `false` on the other hand will never add the property even if the default export would become a property `.default`.

See also `output.interop`.

### output.exports 

| Type: | `"auto" \| "default" \| "named" \| "none"` |
|---|---|
| CLI: | `--exports <exportMode>` |
| Default: | `'auto'` |

What export mode to use. Defaults to `auto`, which guesses your intentions based on what the `input` module exports:

- `default` – if you are only exporting one thing using `export default ...`; note that this can cause issues when generating CommonJS output that is meant to be interchangeable with ESM output, see below
- `named` – if you are using named exports
- `none` – if you are not exporting anything (e.g. you are building an app, not a library)

As this is only an output transformation, you can only choose `default` if a default export is the only export for all entry chunks. Likewise, you can only choose `none` if there are no exports, otherwise Rollup will throw an error.

The difference between `default` and `named` affects how other people can consume your bundle. If you use `default`, a CommonJS user could do this, for example:

js

```js
// your-lib package entry
export default 'Hello world';

// a CommonJS consumer
/* require( "your-lib" ) returns "Hello World" */
const hello = require('your-lib');
```

With `named`, a user would do this instead:

js

```js
// your-lib package entry
export const hello = 'Hello world';

// a CommonJS consumer
/* require( "your-lib" ) returns {hello: "Hello World"} */
const hello = require('your-lib').hello;
/* or using destructuring */
const { hello } = require('your-lib');
```

The wrinkle is that if you use `named` exports but *also* have a `default` export, a user would have to do something like this to use the default export:

js

```js
// your-lib package entry
export default 'foo';
export const bar = 'bar';

// a CommonJS consumer
/* require( "your-lib" ) returns {default: "foo", bar: "bar"} */
const foo = require('your-lib').default;
const bar = require('your-lib').bar;
/* or using destructuring */
const { default: foo, bar } = require('your-lib');
```

Note: There are some tools such as Babel, TypeScript, Webpack, and `@rollup/plugin-commonjs` that are capable of resolving a CommonJS `require(...)` call with an ES module. If you are generating CommonJS output that is meant to be interchangeable with ESM output for those tools, you should always use `named` export mode. The reason is that most of those tools will by default return the namespace of an ES module on `require` where the default export is the `.default` property.

In other words for those tools, you cannot create a package interface where `const lib = require("your-lib")` yields the same as `import lib from "your-lib"`. With named export mode however, `const {lib} = require("your-lib")` will be equivalent to `import {lib} from "your-lib"`.

### output.externalLiveBindings 

| Type: | `boolean` |
|---|---|
| CLI: | `--externalLiveBindings`/`--no-externalLiveBindings` |
| Default: | `true` |

When set to `false`, Rollup will not generate code to support live bindings for external imports but instead assume that exports do not change over time. This will enable Rollup to generate more optimized code. Note that this can cause issues when there are circular dependencies involving an external dependency.

This will avoid most cases where Rollup generates getters in the code and can therefore be used to make code IE8 compatible in many cases.

Example:

js

```js
// input
export { x } from 'external';

// CJS output with externalLiveBindings: true
var external = require('external');

Object.defineProperty(exports, 'x', {
	enumerable: true,
	get: function () {
		return external.x;
	}
});

// CJS output with externalLiveBindings: false
var external = require('external');

exports.x = external.x;
```

### output.freeze 

| Type: | `boolean` |
|---|---|
| CLI: | `--freeze`/`--no-freeze` |
| Default: | `true` |

Whether to `Object.freeze()` namespace import objects (i.e. `import * as namespaceImportObject from...`) that are accessed dynamically.

### output.indent 

| Type: | `boolean \| string` |
|---|---|
| CLI: | `--indent`/`--no-indent` |
| Default: | `true` |

The indent string to use, for formats that require code to be indented (`amd`, `iife`, `umd`, `system`). Can also be `false` (no indent), or `true` (the default – auto-indent)

js

```js
// rollup.config.js
export default {
	// ...
	output
: {
		// ...
		indent
: false
	}
};
```

### output.noConflict 

| Type: | `boolean` |
|---|---|
| CLI: | `--noConflict`/`--no-noConflict` |
| Default: | `false` |

This will generate an additional `noConflict` export to UMD bundles. When called in an IIFE scenario, this method will return the bundle exports while restoring the corresponding global variable to its previous value.

### output.reexportProtoFromExternal 

| Type: | `boolean` |
|---|---|
| CLI: | `--reexportProtoFromExternal`/`--no-reexportProtoFromExternal` |
| Default: | `true` |

This option is only effective when `output.format` is set to one of `['amd', 'cjs', 'iife', 'umd']` and `output.externalLiveBindings` is set to false.

For maximum compatibility, Rollup reexports `__proto__` from an external module by default. However, for common use cases, it is strongly recommended to set this value to false as it effectively reduces the output size.

js

```js
// the input file
export * from 'rollup';
```

js

```js
// the output file if the output.format is cjs
'use strict';

// reexportProtoFromExternal is true
var rollup = require('rollup');

Object.prototype.hasOwnProperty.call(rollup, '__proto__') &&
	!Object.prototype.hasOwnProperty.call(exports, '__proto__') &&
	Object.defineProperty(exports, '__proto__', {
		enumerable: true,
		value: rollup['__proto__']
	});

Object.keys(rollup).forEach(function (k) {
	if (k !== 'default' && !Object.prototype.hasOwnProperty.call(exports, k))
		exports[k] = rollup[k];
});

// reexportProtoFromExternal is false
var rollup = require('rollup');

Object.keys(rollup).forEach(function (k) {
	if (k !== 'default' && !Object.prototype.hasOwnProperty.call(exports, k))
		exports[k] = rollup[k];
});
```

### output.sanitizeFileName 

| Type: | `boolean \| (string) => string` |
|---|---|
| CLI: | `--sanitizeFileName`/`no-sanitizeFileName` |
| Default: | `true` |

Set to `false` to disable all chunk name sanitizations (removal of `\0`, `?` and `*` characters).

Alternatively set to a function to allow custom chunk name sanitization.

### output.strict 

| Type: | `boolean` |
|---|---|
| CLI: | `--strict`/`--no-strict` |
| Default: | `true` |

Whether to include the 'use strict' pragma at the top of generated non-ES bundles. Strictly speaking, ES modules are *always* in strict mode, so you shouldn't disable this without good reason.

### output.systemNullSetters 

| Type: | `boolean` |
|---|---|
| CLI: | `--systemNullSetters`/`--no-systemNullSetters` |
| Default: | `true` |

When outputting the `system` module format, by default, empty setter functions are replaced with `null` as an output simplification. This is incompatible with SystemJS before v6.3.3. Deactivate this option to output empty functions instead that older SystemJS versions support.

### preserveSymlinks 

| Type: | `boolean` |
|---|---|
| CLI: | `--preserveSymlinks` |
| Default: | `false` |

When set to `false`, symbolic links are followed when resolving a file. When set to `true`, instead of being followed, symbolic links are treated as if the file is where the link is. To illustrate, consider the following situation:

js

```js
// /main.js
import { x } from './linked.js';
console.log(x);

// /linked.js
// this is a symbolic link to /nested/file.js

// /nested/file.js
export { x } from './dep.js';

// /dep.js
export const x = 'next to linked';

// /nested/dep.js
export const x = 'next to original';
```

If `preserveSymlinks` is `false`, then the bundle created from `/main.js` will log "next to original" as it will use the location of the symbolically linked file to resolve its dependencies. If `preserveSymlinks` is `true`, however, it will log "next to linked" as the symbolic link will not be resolved.

### shimMissingExports 

| Type: | `boolean` |
|---|---|
| CLI: | `--shimMissingExports`/`--no-shimMissingExports` |
| Default: | `false` |

If this option is provided, bundling will not fail if bindings are imported from a file that does not define these bindings. Instead, new variables will be created for these bindings with the value `undefined`.

### treeshake 

| Type: | `boolean \| TreeshakingPreset \| TreeshakingOptions` |
|---|---|
| CLI: | `--treeshake <preset>`/`--no-treeshake` |
| Default: | `true` |

typescript

```typescript
type TreeshakingPreset = 'smallest' | 'safest' | 'recommended';

interface TreeshakingOptions {
	annotations?: boolean;
	correctVarValueBeforeDeclaration?: boolean;
	moduleSideEffects?: ModuleSideEffectsOption;
	preset?: TreeshakingPreset;
	propertyReadSideEffects?: boolean | 'always';
	tryCatchDeoptimization?: boolean;
	unknownGlobalSideEffects?: boolean;
}

type ModuleSideEffectsOption =
	| boolean
	| 'no-external'
	| string[]
	| HasModuleSideEffects;
type HasModuleSideEffects = (id: string, external: boolean) => boolean;
```

Whether to apply tree-shaking and to fine-tune the tree-shaking process. Setting this option to `false` will produce bigger bundles but may improve build performance. You may also choose one of three presets that will automatically be updated if new options are added:

- `"smallest"` will choose option values for you to minimize output size as much as possible. This should work for most code bases as long as you do not rely on certain patterns, which are currently:
  - getters with side effects will only be retained if the return value is used (`treeshake.propertyReadSideEffects: false`)
  - code from imported modules will only be retained if at least one exported value is used (`treeshake.moduleSideEffects: false`)
  - you should not bundle polyfills that rely on detecting broken builtins (`treeshake.tryCatchDeoptimization: false`)
  - some semantic issues may be swallowed (`treeshake.unknownGlobalSideEffects: false`, `treeshake.correctVarValueBeforeDeclaration: false`)
- `"recommended"` should work well for most usage patterns. Some semantic issues may be swallowed, though (`treeshake.unknownGlobalSideEffects: false`, `treeshake.correctVarValueBeforeDeclaration: false`)
- `"safest"` tries to be as spec compliant as possible while still providing some basic tree-shaking capabilities.
- `true` is equivalent to not specifying the option and will always choose the default value (see below).

If you discover a bug caused by the tree-shaking algorithm, please file an issue! Setting this option to an object implies tree-shaking is enabled and grants the following additional options:

#### treeshake.annotations 

| Type: | `boolean` |
|---|---|
| CLI: | `--treeshake.annotations`/`--no-treeshake.annotations` |
| Default: | `true` |

If `false`, ignore hints from annotation in comments:

##### `@__PURE__` 

Comments containing `@__PURE__` or `#__PURE__` mark a specific function call or constructor invocation as side effect free. That means that Rollup will tree-shake i.e. remove the call unless the return value is used in some code that is not tree-shaken. These annotations need to immediately precede the call invocation to take effect. The following code will be completely tree-shaken unless this option is set to `false`, in which case it will remain unchanged.

javascript

```javascript
/*@__PURE__*/ console.log('side-effect');

class Impure {
	constructor() {
		console.log('side-effect');
	}
}

/*@__PURE__ There may be additional text in the comment */ new Impure();
```

Such an annotation is considered *valid* if it directly precedes a function call or constructor invocation and is only separated from the callee by white-space or comments. The only exception are parentheses that wrap a call or invocation.

Invalid annotations are removed and Rollup emits a warning. Valid annotations remain in the code unless their function call or constructor invocation is removed as well.

##### `@__NO_SIDE_EFFECTS__` 

Comments containing `@__NO_SIDE_EFFECTS__` or `#__NO_SIDE_EFFECTS__` mark a function declaration itself as side effect free. When a function has been marked as having no side effects, all calls to that function will be considered to be side effect free. The following code will be completely tree-shaken unless this option is set to `false`, in which case it will remain unchanged.

javascript

```javascript
/*@__NO_SIDE_EFFECTS__*/
function impure() {
	console.log('side-effect');
}

/*@__NO_SIDE_EFFECTS__*/
const impureArrowFn = () => {
	console.log('side-effect');
};

impure(); // <-- call will be considered as side effect free
impureArrowFn(); // <-- call will be considered as side effect free
```

Such an annotation is considered *valid* if it directly precedes a function declaration or a constant variable declaration where the first declared variable is a function and is only separated from the declaration by white-space or comments.

Invalid annotations are removed and Rollup emits a warning. Valid annotations remain in the code unless their declaration is removed as well

#### treeshake.correctVarValueBeforeDeclaration 

| Type: | `boolean` |
|---|---|
| CLI: | `--treeshake.correctVarValueBeforeDeclaration`/`--no-treeshake.correctVarValueBeforeDeclaration` |
| Default: | `false` |

In some edge cases if a variable is accessed before its declaration assignment and is not reassigned, then Rollup may incorrectly assume that variable is constant throughout the program, as in the example below. This is not true if the variable is declared with `var`, however, as those variables can be accessed before their declaration where they will evaluate to `undefined`. Choosing `true` will make sure Rollup does not make any assumptions about the value of variables declared with `var`. Note though that this can have a noticeable negative impact on tree-shaking results.

js

```js
// everything will be tree-shaken unless treeshake.correctVarValueBeforeDeclaration === true
let logBeforeDeclaration = false;

function logIfEnabled() {
	if (logBeforeDeclaration) {
		log();
	}

	var value = true;

	function log() {
		if (!value) {
			console.log('should be retained, value is undefined');
		}
	}
}

logIfEnabled(); // could be removed
logBeforeDeclaration = true;
logIfEnabled(); // needs to be retained as it displays a log
```

#### treeshake.manualPureFunctions 

| Type: | `string[]` |
|---|---|
| CLI: | `--treeshake.manualPureFunctions <names>` |

Allows to manually define a list of function names that should always be considered "pure", i.e. they have no side effects like changing global state etc. when called. The check is performed solely by name.

This can not only help with dead code removal, but can also improve JavaScript chunk generation especially when using `output.experimentalMinChunkSize`.

Besides any functions matching that name, any properties on a pure function and any functions returned from a pure functions will also be considered pure functions, and accessing any properties is not checked for side effects.

js

```js
// rollup.config.js
export default {
	treeshake
: {
		preset
: 'smallest',
		manualPureFunctions
: ['styled', 'local']
	}
	// ...
};

// code
import styled
 from 'styled-components';
const local
 = console
.log
;

local
(); // removed
styled
.div`
	color: blue;
`; // removed
styled
?.div(); // removed
styled
()(); // removed
styled
().div(); // removed
```

WARNING

If you pass arguments to such a pure function, those arguments are still checked for direct side effects like mutating a variable or calling a global function, in which case the call to the pure function is retained. But be aware that we do not check if those arguments are called and whether such a call could have side effects.

js

```js
// rollup.config.js
export default {
	treeshake: {
		manualPureFunctions: ['lib.nested']
	}
	// ...
};

import lib from 'lib';

lib.nested(console.log('effect')); // retained
lib.nested(() => console.log('effect')); // will be removed
lib.nested.forEach(() => console.log('effect')); // will also be removed
```

#### treeshake.moduleSideEffects 

| Type: | `boolean \| "no-external" \| string[] \| (id: string, external: boolean) => boolean` |
|---|---|
| CLI: | `--treeshake.moduleSideEffects`/`--no-treeshake.moduleSideEffects`/`--treeshake.moduleSideEffects no-external` |
| Default: | `true` |

If `false`, assume modules and external dependencies from which nothing is imported do not have other side effects like mutating global variables or logging without checking. For external dependencies, this will suppress empty imports:

javascript

```javascript
// input file
import { unused } from 'external-a';
import 'external-b';
console.log(42);
```

javascript

```javascript
// output with treeshake.moduleSideEffects === true
import 'external-a';
import 'external-b';
console.log(42);
```

javascript

```javascript
// output with treeshake.moduleSideEffects === false
console.log(42);
```

For non-external modules, `false` will not include any statements from a module unless at least one import from this module is included:

javascript

```javascript
// input file a.js
import { unused } from './b.js';
console.log(42);

// input file b.js
console.log('side-effect');
const ignored = 'will still be removed';
```

javascript

```javascript
// output with treeshake.moduleSideEffects === true
console.log('side-effect');

console.log(42);
```

javascript

```javascript
// output with treeshake.moduleSideEffects === false
console.log(42);
```

You can also supply a list of modules with side effects or a function to determine it for each module individually. The value `"no-external"` will only remove external imports if possible and is equivalent to the function `(id, external) => !external`;

If a module that has this flag set to `false` reexports a variable from another module and this variable is used, the question if the reexporting module is scanned for side effects depends on how the variable is reexported:

javascript

```javascript
// input file a.js
import { foo } from './b.js';
console.log(foo);

// input file b.js
// direct reexports will ignore side effects
export { foo } from './c.js';
console.log('this side-effect is ignored');

// input file c.js
// indirect reexports will include side effects
import { foo } from './d.js';
foo.mutated = true;
console.log('this side-effect and the mutation are retained');
export { foo };

// input file d.js
export const foo = 42;
```

javascript

```javascript
// output with treeshake.moduleSideEffects === false
const foo = 42;

foo.mutated = true;
console.log('this side-effect and the mutation are retained');

console.log(foo);
```

Note that despite the name, this option does not "add" side effects to modules that do not have side effects. If it is important that e.g. an empty module is "included" in the bundle because you need this for dependency tracking, the plugin interface allows you to designate modules as being excluded from tree-shaking via the `resolveId`, `load` or `transform` hook.

#### treeshake.preset 

| Type: | `"smallest" \| "safest" \| "recommended"` |
|---|---|
| CLI: | `--treeshake <value>` |

Allows choosing one of the presets listed above while overriding some options.

js

```js
export default {
	treeshake
: {
		preset
: 'smallest',
		propertyReadSideEffects
: true
	}
	// ...
};
```

#### treeshake.propertyReadSideEffects 

| Type: | `boolean \| 'always'` |
|---|---|
| CLI: | `--treeshake.propertyReadSideEffects`/`--no-treeshake.propertyReadSideEffects` |
| Default: | `true` |

If `true`, retain unused property reads that Rollup can determine to have side effects. This includes accessing properties of `null` or `undefined` or triggering explicit getters via property access. Note that this does not cover destructuring assignment or getters on objects passed as function parameters.

If `false`, assume reading a property of an object never has side effects. Depending on your code, disabling this option can significantly reduce bundle size but can potentially break functionality if you rely on getters or errors from illegal property access.

If `'always'`, assume all member property accesses, including destructuring, have side effects. This setting is recommended for code relying on getters with side effects. It typically results in larger bundle size, but smaller than disabling `treeshake` altogether.

javascript

```javascript
// Will be removed if treeshake.propertyReadSideEffects === false
const foo = {
	get bar() {
		console.log('effect');
		return 'bar';
	}
};
const result = foo.bar;
const illegalAccess = foo.quux.tooDeep;
```

#### treeshake.tryCatchDeoptimization 

| Type: | `boolean` |
|---|---|
| CLI: | `--treeshake.tryCatchDeoptimization`/`--no-treeshake.tryCatchDeoptimization` |
| Default: | `true` |

By default, Rollup assumes that many builtin globals of the runtime behave according to the latest specs when tree-shaking and do not throw unexpected errors. In order to support e.g. feature detection workflows that rely on those errors being thrown, Rollup will by default deactivate tree-shaking inside try-statements. If a function parameter is called from within a try-statement, this parameter will be deoptimized as well. Set `treeshake.tryCatchDeoptimization` to `false` if you do not need this feature and want to have tree-shaking inside try-statements.

js

```js
function otherFn() {
	// even though this function is called from a try-statement, the next line
	// will be removed as side-effect-free
	Object.create(null);
}

function test(callback) {
	try {
		// calls to otherwise side-effect-free global functions are
		// retained inside try-statements for tryCatchDeoptimization: true
		Object.create(null);

		// calls to other function are retained as well but the body of
		// this function may again be subject to tree-shaking
		otherFn();

		// if a parameter is called, then all arguments passed to that
		// function parameter will be deoptimized
		callback();
	} catch {}
}

test(() => {
	// will be ratained
	Object.create(null);
});

// call will be retained but again, otherFn is not deoptimized
test(otherFn);
```

#### treeshake.unknownGlobalSideEffects 

| Type: | `boolean` |
|---|---|
| CLI: | `--treeshake.unknownGlobalSideEffects`/`--no-treeshake.unknownGlobalSideEffects` |
| Default: | `true` |

Since accessing a non-existing global variable will throw an error, Rollup does by default retain any accesses to non-builtin global variables. Set this option to `false` to avoid this check. This is probably safe for most code-bases.

js

```js
// input
const jQuery = $;
const requestTimeout = setTimeout;
const element = angular.element;

// output with unknownGlobalSideEffects == true
const jQuery = $;
const element = angular.element;

// output with unknownGlobalSideEffects == false
const element = angular.element;
```

In the example, the last line is always retained as accessing the `element` property could also throw an error if `angular` is e.g. `null`. To avoid this check, set `treeshake.propertyReadSideEffects` to `false` as well.
