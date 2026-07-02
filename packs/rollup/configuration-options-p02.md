---
title: "Configuration Options (part 2/4)"
source: https://rollupjs.org/configuration-options/
domain: rollup
license: CC-BY-SA-4.0 / MIT (rollupjs.org)
tags: rollup bundler, rollupjs, es module bundler, rollup tree shaking
fetched: 2026-07-02
part: 2/4
---

## Advanced functionality 

### cache 

| Type: | `RollupCache \| boolean` |
|---|---|
| Default: | `true` |

The `cache` property of a previous bundle. Use it to speed up subsequent builds in watch mode — Rollup will only reanalyse the modules that have changed. Setting this option explicitly to `false` will prevent generating the `cache` property on the bundle and also deactivate caching for plugins.

js

```js
const rollup
 = require
('rollup');
let cache
;

async function buildWithCache
() {
	const bundle
 = await rollup
.rollup
({
		cache
 // is ignored if falsy
		// ... other input options
	});
	cache
 = bundle
.cache
; // store the cache object of the previous build
	return bundle
;
}

buildWithCache
()
	.then
(bundle
 => {
		// ... do something with the bundle
	})
	.then
(() => buildWithCache
()) // will use the cache of the previous build
	.then
(bundle
 => {
		// ... do something with the bundle
	});
```

### logLevel 

| Type: | `LogLevel \| "silent"` |
|---|---|
| CLI: | `--logLevel <level>` |
| Default: | `"info"` |

Determine which logs to process. See `onLog` for the available log levels. The default `logLevel` of `"info"` means that info and warnings logs will be processed while debug logs will be swallowed, which means that they are neither passed to plugin `onLog` hooks nor the `onLog` option or printed to the console.

When using the CLI, errors will still be printed to the console as they are not processed via the logging system. See the `--silent` flag for how to suppress error logs.

### makeAbsoluteExternalsRelative 

| Type: | `boolean \| "ifRelativeSource"` |
|---|---|
| CLI: | `--makeAbsoluteExternalsRelative`/`--no-makeAbsoluteExternalsRelative` |
| Default: | `"ifRelativeSource"` |

Determines if absolute external paths should be converted to relative paths in the output. This does not only apply to paths that are absolute in the source but also to paths that are resolved to an absolute path by either a plugin or Rollup core.

For `true`, an external import like `import "/Users/Rollup/project/relative.js"` would be converted to a relative path. When converting an absolute path to a relative path, Rollup does *not* take the `file` or `dir` options into account, because those may not be present e.g. for builds using the JavaScript API. Instead, it assumes that the root of the generated bundle is located at the common shared parent directory of all modules that were included in the bundle. Assuming that the common parent directory of all modules is `"/Users/Rollup/project"`, the import from above would likely be converted to `import "./relative.js"` in the output. If the output chunk is itself nested in a subdirectory by choosing e.g. `chunkFileNames: "chunks/[name].js"`, the import would be `"../relative.js"`.

As stated before, this would also apply to originally relative imports like `import "./relative.js"` that are resolved to an absolute path before they are marked as external by the `external` option.

One common problem is that this mechanism will also apply to imports like `import "/absolute.js'"`, resulting in unexpected relative paths in the output.

For this case, `"ifRelativeSource"` checks if the original import was a relative import and only then convert it to a relative import in the output. Choosing `false` will keep all paths as absolute paths in the output.

Note that when a relative path is directly marked as "external" using the `external` option, then it will be the same relative path in the output. When it is resolved first via a plugin or Rollup core and then marked as external, the above logic will apply.

### maxParallelFileOps 

| Type: | `number` |
|---|---|
| CLI: | `--maxParallelFileOps <number>` |
| Default: | 1000 |

Limits the number of files rollup will open in parallel when reading modules or writing chunks. Without a limit or with a high enough value, builds can fail with an "EMFILE: too many open files". This depends on how many open file handles the operating system allows. If you set the limit too low and use plugins that rely on the `this.load` context function, such as the `commonjs` plugin, then it can happen that builds stall without an error message as it limits the number of parallel `load` calls.

### onLog 

| Type: | `(level: LogLevel, log: RollupLog, defaultHandler: LogOrStringHandler) => void;` |
|---|---|

typescript

```typescript
type LogLevel = 'warn' | 'info' | 'debug';

type LogOrStringHandler = (
	level: LogLevel | 'error',
	log: string | RollupLog
) => void;

// All possible properties, actual properties depend on log
interface RollupLog {
	binding?: string;
	cause?: Error;
	code?: string;
	exporter?: string;
	frame?: string; // always printed by the CLI
	hook?: string;
	id?: string; // always printed by the CLI
	ids?: string[];
	loc?: {
		column: number;
		file?: string;
		line: number;
	}; // always printed by the CLI if id is present
	message: string; // the actual message, always printed by the CLI
	meta?: any; // add custom plugin properties to logs
	names?: string[];
	plugin?: string; // added by Rollup for plugin logs, only printed for warnings
	pluginCode?: string; // added by Rollup for plugin logs that contain a code
	pos?: number;
	reexporter?: string;
	stack?: string; // url for additional information, always printed by the CLI
	url?: string;
}
```

A function that intercepts log messages. If not supplied, logs are printed to the console, whereby Rollup CLI aggregates certain `"warn"` logs and prints consolidated warnings after the build to reduce noise. This handler is also triggered when using the `--silent` CLI option.

The function receives three arguments: the log level, the log object and the default handler. Log objects have, at a minimum, a `code` and a `message` property, allowing you to control how different kinds of logs are handled. Other properties are added depending on the type of log. See `utils/logs.ts` for a complete list of built-in errors and logs together with their codes and properties.

If the default handler is not invoked, the log will not be printed to the console. Moreover, you can change the log level by invoking the default handler with a different level. Using the additional level `"error"` will turn the log into a thrown error that has all properties of the log attached.

js

```js
// rollup.config.js
export default {
	//...
	onLog
(level
, log
, handler
) {
		if (log
.code
 === 'CIRCULAR_DEPENDENCY') {
			return; // Ignore circular dependency warnings
		}
		if (level
 === 'warn') {
			handler
('error', log
); // turn other warnings into errors
		} else {
			handler
(level
, log
); // otherwise, just print the log
		}
	}
};
```

This handler will not be invoked if logs are filtered out by the `logLevel` option. I.e. by default, `"debug"` logs will be swallowed.

Some logs also have a `loc` property and a `frame` allowing you to locate the source of the log:

js

```js
// rollup.config.js
export default {
	//...
	onLog
(level
, { loc
, frame
, message
 }) {
		if (loc
) {
			console
.warn
(`${loc
.file
} (${loc
.line
}:${loc
.column
}) ${message
}`);
			if (frame
) console
.warn
(frame
);
		} else {
			console
.warn
(message
);
		}
	}
};
```

### onwarn 

| Type: | `(warning: RollupLog, defaultHandler: (warning: string \| RollupLog) => void) => void;` |
|---|---|

A function that will intercept warning messages. It is very similar to `onLog` but only receives warnings. If the default handler is invoked, the log will be handled as a warning. If both an `onLog` and `onwarn` handler are provided, the `onwarn` handler will only be invoked if `onLog` calls its default handler with a `level` of `warn`.

See `onLog` for more information.

### output.assetFileNames 

| Type: | `string \| ((assetInfo: PreRenderedAsset) => string)` |
|---|---|
| CLI: | `--assetFileNames <pattern>` |
| Default: | `"assets/[name]-[hash][extname]"` |

typescript

```typescript
interface PreRenderedAsset {
	names: string[];
	originalFileNames: string[];
	source: string | Uint8Array;
	type: 'asset';
}
```

The pattern to use for naming custom emitted assets to include in the build output, or a function that is called per asset to return such a pattern. Patterns support the following placeholders:

- `[extname]`: The file extension of the asset including a leading dot, e.g. `.css`.
- `[ext]`: The file extension without a leading dot, e.g. `css`.
- `[hash]`: A hash based on the content of the asset. You can also set a specific hash length via e.g. `[hash:10]`. By default, it will create a base-64 hash. If you need a reduced character sets, see `output.hashCharacters`
- `[name]`: The file name of the asset excluding any extension.

Forward slashes `/` can be used to place files in sub-directories. When using a function, `PreRenderedAsset` is a reduced version of the `OutputAsset` type in `generateBundle` without the `fileName`. See also `output.chunkFileNames`, `output.entryFileNames`.

| Type: | `string \| ((chunk: RenderedChunk) => string \| Promise<string>)` |
|---|---|
| CLI: | `--banner`/`--footer <text>` |

See the `renderChunk` hook for the `RenderedChunk` type.

A string to prepend/append to the bundle. You can also supply a function that returns a `Promise` that resolves to a `string` to generate it asynchronously (Note: `banner` and `footer` options will not break sourcemaps).

If you supply a function, `chunk` contains additional information about the chunk using a `RenderedChunk` type that is a reduced version of the `OutputChunk` type used in `generateBundle` hook with the following differences:

- `code` and `map` are not set as the chunk has not been rendered yet.
- all referenced chunk file names that would contain hashes will contain hash placeholders instead. This includes `fileName`, `imports`, `importedBindings`, `dynamicImports` and `implicitlyLoadedBefore`. When you use such a placeholder file name or part of it in the code returned from this option, Rollup will replace the placeholder with the actual hash before `generateBundle`, making sure the hash reflects the actual content of the final generated chunk including all referenced file hashes.

`chunk` is mutable and changes applied in this hook will propagate to other plugins and to the generated bundle. That means if you add or remove imports or exports in this hook, you should update `imports`, `importedBindings` and/or `exports`.

js

```js
// rollup.config.js
export default {
	// ...
	output
: {
		// ...
		banner
: '/* my-library version ' + version + ' */',
		footer
: '/* follow me on Twitter! @rich_harris */'
	}
};
```

See also `output.intro/output.outro`.

### output.chunkFileNames 

| Type: | `string \| ((chunkInfo: PreRenderedChunk) => string)` |
|---|---|
| CLI: | `--chunkFileNames <pattern>` |
| Default: | `"[name]-[hash].js"` |

typescript

```typescript
interface PreRenderedChunk {
	exports: string[];
	facadeModuleId: string | null;
	isDynamicEntry: boolean;
	isEntry: boolean;
	isImplicitEntry: boolean;
	moduleIds: string[];
	name: string;
	type: 'chunk';
}
```

The `PreRenderedChunk` type provides information about the chunk being generated:

- `exports`: The list of exported bindings from the chunk.
- `facadeModuleId`: The module id of the entry point this chunk is a facade for, or `null` if this is not a facade.
- `isDynamicEntry`: `true` if this chunk is the target of dynamic `import()` expressions.
- `isEntry`: `true` if this chunk is an entry point (either from the `input` option or emitted via `this.emitFile`).
- `isImplicitEntry`: `true` if this chunk was emitted with `implicitlyLoadedAfterOneOf` set, indicating it will only be loaded as an entry point if at least one of the specified modules have already been loaded.
- `moduleIds`: The list of module ids included in this chunk.
- `name`: The name of this chunk used for the `[name]` placeholder.
- `type`: Always `'chunk'`.

The pattern to use for naming shared chunks created when code-splitting, or a function that is called per chunk to return such a pattern. Patterns support the following placeholders:

- `[format]`: The rendering format defined in the output options, e.g. `es` or `cjs`.
- `[hash]`: A hash based only on the content of the final generated chunk, including transformations in `renderChunk` and any referenced file hashes. You can also set a specific hash length via e.g. `[hash:10]`. By default, it will create a base-64 hash. If you need a reduced character sets, see `output.hashCharacters`
- `[name]`: The name of the chunk. This can be explicitly set via the `output.manualChunks` option or when the chunk is created by a plugin via `this.emitFile`. Otherwise, it will be derived from the chunk contents.

Forward slashes `/` can be used to place files in sub-directories. When using a function, `PreRenderedChunk` is a reduced version of the `OutputChunk` type in `generateBundle` without properties that depend on file names and no information about the rendered modules as rendering only happens after file names have been generated. You can however access a list of included `moduleIds`. See also `output.assetFileNames`, `output.entryFileNames`.

### output.compact 

| Type: | `boolean` |
|---|---|
| CLI: | `--compact`/`--no-compact` |
| Default: | `false` |

This will minify the wrapper code generated by rollup. Note that this does not affect code written by the user. This option is useful when bundling pre-minified code.

### output.dynamicImportInCjs 

| Type: | `boolean` |
|---|---|
| CLI: | `--dynamicImportInCjs`/`--no-dynamicImportInCjs` |
| Default: | `true` |

While CommonJS output originally supported only `require(…)` to import dependencies, recent Node versions also started to support `import(…)`, which is the only way to import ES modules from CommonJS files. If this option is `true`, which is the default, Rollup will keep external dynamic imports as `import(…)` expressions in CommonJS output. Set this to `false` to rewrite dynamic imports using `require(…)` syntax.

js

```js
// input
import('external').then
(console
.log
);

// cjs output with dynamicImportInCjs: true or not set
import('external').then
(console
.log
);

// cjs output with dynamicImportInCjs: false
function _interopNamespaceDefault
(e
) {
	var n
 = Object
.create
(null);
	if (e
) {
		Object
.keys
(e
).forEach
(function (k
) {
			if (k
 !== 'default') {
				var d
 = Object
.getOwnPropertyDescriptor
(e
, k
);
				Object
.defineProperty
(
					n
,
					k
,
					d
.get

						? d

						: {
								enumerable
: true,
								get
: function () {
									return e
[k
];
								}
							}
				);
			}
		});
	}
	n
.default = e
;
	return Object
.freeze
(n
);
}

Promise
.resolve
()
	.then
(function () {
		return /*#__PURE__*/ _interopNamespaceDefault
(require
('external'));
	})
	.then
(console
.log
);
```

### output.entryFileNames 

| Type: | `string \| ((chunkInfo: PreRenderedChunk) => string)` |
|---|---|
| CLI: | `--entryFileNames <pattern>` |
| Default: | `"[name].js"` |

See `output.chunkFileNames` for the `PreRenderedChunk` type.

The pattern to use for chunks created from entry points, or a function that is called per entry chunk to return such a pattern. Patterns support the following placeholders:

- `[format]`: The rendering format defined in the output options, e.g. `es` or `cjs`.
- `[hash]`: A hash based only on the content of the final generated entry chunk, including transformations in `renderChunk` and any referenced file hashes. You can also set a specific hash length via e.g. `[hash:10]`. By default, it will create a base-64 hash. If you need a reduced character sets, see `output.hashCharacters`
- `[name]`: The file name (without extension) of the entry point, unless the object form of input was used to define a different name.

Forward slashes `/` can be used to place files in sub-directories. When using a function, `PreRenderedChunk` is a reduced version of the `OutputChunk` type in `generateBundle` without properties that depend on file names and no information about the rendered modules as rendering only happens after file names have been generated. You can however access a list of included `moduleIds`. See also `output.assetFileNames`, `output.chunkFileNames`.

This pattern will also be used for every file when setting the `output.preserveModules` option. Note that in this case, `[name]` will include the relative path from the output root and possibly the original file extension if it was not one of `.js`, `.jsx`, `.mjs`, `.cjs`, `.ts`, `.tsx`, `.mts`, or `.cts`.

### output.extend 

| Type: | `boolean` |
|---|---|
| CLI: | `--extend`/`--no-extend` |
| Default: | `false` |

Whether to extend the global variable defined by the `name` option in `umd` or `iife` formats. When `true`, the global variable will be defined as `(global.name = global.name || {})`. When false, the global defined by `name` will be overwritten like `(global.name = {})`.

### output.externalImportAttributes 

| Type: | `boolean` |
|---|---|
| CLI: | `--externalImportAttributes`/`--no-externalImportAttributes` |
| Default: | `true` |

Whether to add import attributes to external imports in the output if the output format is `es` or `cjs`. By default, attributes are taken from the input files, but plugins can add or remove attributes later. E.g. `import "foo" assert {type: "json"}` will cause the same import to appear in the output unless the option is set to `false`. Note that all imports of a module need to have consistent attributes, otherwise a warning is emitted.

### output.generatedCode 

| Type: | `"es5" \| "es2015" \| { arrowFunctions?: boolean, constBindings?: boolean, objectShorthand?: boolean, preset?: "es5" \| "es2015", reservedNamesAsProps?: boolean, symbols?: boolean }` |
|---|---|
| CLI: | `--generatedCode <preset>` |
| Default: | `"es5"` |

Which language features Rollup can safely use in generated code. This will not transpile any user code but only change the code Rollup uses in wrappers and helpers. You may choose one of several presets:

- `"es5"`: Do not use ES2015+ features like arrow functions, but do not quote reserved names used as props.
- `"es2015"`: Use any JavaScript features up to ES2015.

#### output.generatedCode.arrowFunctions 

| Type: | `boolean` |
|---|---|
| CLI: | `--generatedCode.arrowFunctions`/`--no-generatedCode.arrowFunctions` |
| Default: | `false` |

Whether to use arrow functions for auto-generated code snippets. Note that in certain places like module wrappers, Rollup will keep using regular functions wrapped in parentheses as in some JavaScript engines, these will provide noticeably better performance.

#### output.generatedCode.constBindings 

| Type: | `boolean` |
|---|---|
| CLI: | `--generatedCode.constBindings`/`--no-generatedCode.constBindings` |
| Default: | `false` |

This will use `const` instead of `var` in certain places and helper functions. This will allow Rollup to generate more efficient helpers due to block scoping.

js

```js
// input
export * from 'external';

// cjs output with constBindings: false
var external
 = require
('external');

Object
.keys
(external
).forEach
(function (k
) {
	if (k
 !== 'default' && !Object
.prototype
.hasOwnProperty
.call
(exports
, k
))
		Object
.defineProperty
(exports
, k
, {
			enumerable
: true,
			get
: function () {
				return external
[k
];
			}
		});
});

// cjs output with constBindings: true
const external
 = require
('external');

for (const k
 in external
) {
	if (k
 !== 'default' && !Object
.prototype
.hasOwnProperty
.call
(exports
, k
))
		Object
.defineProperty
(exports
, k
, {
			enumerable
: true,
			get
: () => external
[k
]
		});
}
```

#### output.generatedCode.objectShorthand 

| Type: | `boolean` |
|---|---|
| CLI: | `--generatedCode.objectShorthand`/`--no-generatedCode.objectShorthand` |
| Default: | `false` |

Allows the use of shorthand notation in objects when the property name matches the value.

javascript

```javascript
// input
const foo
 = 1;
export { foo
, foo
 as bar
 };

// system output with objectShorthand: false
System.register('bundle', [], function (exports
) {
	'use strict';
	return {
		execute
: function () {
			const foo
 = 1;
			exports
({ foo
: foo
, bar
: foo
 });
		}
	};
});

// system output with objectShorthand: true
System.register('bundle', [], function (exports
) {
	'use strict';
	return {
		execute
: function () {
			const foo
 = 1;
			exports
({ foo
, bar
: foo
 });
		}
	};
});
```

#### output.generatedCode.preset 

| Type: | `"es5" \| "es2015"` |
|---|---|
| CLI: | `--generatedCode <value>` |

Allows choosing one of the presets listed above while overriding some options.

js

```js
export default {
	// ...
	output
: {
		generatedCode
: {
			preset
: 'es2015',
			arrowFunctions
: false
		}
		// ...
	}
};
```

#### output.generatedCode.reservedNamesAsProps 

| Type: | `boolean` |
|---|---|
| CLI: | `--generatedCode.reservedNamesAsProps`/`--no-generatedCode.reservedNamesAsProps` |
| Default: | `true` |

Determine whether reserved words like "default" can be used as prop names without using quotes. This will make the syntax of the generated code ES3 compliant. Note however that for full ES3 compliance, you may also need to polyfill some builtin functions like `Object.keys` or `Array.prototype.forEach`.

javascript

```javascript
// input
const foo = null;
export { foo as void };

// cjs output with reservedNamesAsProps: false
const foo = null;

exports['void'] = foo;

// cjs output with reservedNamesAsProps: true
const foo = null;

exports.void = foo;
```

#### output.generatedCode.symbols 

| Type: | `boolean` |
|---|---|
| CLI: | `--generatedCode.symbols`/`--no-generatedCode.symbols` |
| Default: | `false` |

Whether to allow the use of `Symbol` in auto-generated code snippets. Currently, this only controls if namespaces will have the `Symbol.toStringTag` property set to the correct value of `Module`, which means that for a namespace, `String(namespace)` logs `[object Module]`. This again is used for feature detection in certain libraries and frameworks.

javascript

```javascript
// input
export const foo = 42;

// cjs output with symbols: false
const foo = 42;

exports.foo = foo;

// cjs output with symbols: true
Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });

const foo = 42;

exports.foo = foo;
```

### output.hashCharacters 

| Type: | `"base64" \| "base36" \| "hex"` |
|---|---|
| CLI: | `--hashCharacters <name>` |
| Default: | `"base64"` |

This determines the character set that Rollup is allowed to use in file hashes.

- the default `"base64"` will use url-safe base-64 hashes with potential characters `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_`.
- `"base36"` will only use lower-case letters and numbers `abcdefghijklmnopqrstuvwxyz0123456789`.
- `"hex"` will create hexadecimal hashes with characters `abcdef0123456789`.

### output.hoistTransitiveImports 

| Type: | `boolean` |
|---|---|
| CLI: | `--hoistTransitiveImports`/`--no-hoistTransitiveImports` |
| Default: | `true` |

By default, when creating multiple chunks, transitive imports of entry chunks will be added as empty imports to the entry chunks. See "Why do additional imports turn up in my entry chunks when code-splitting?" for details and background. Setting this option to `false` will disable this behaviour. This option is ignored when using the `output.preserveModules` option as here, imports will never be hoisted.

### output.importAttributesKey 

| Type: | `"with" \| "assert"` |
|---|---|
| CLI: | `--importAttributesKey <name>` |
| Default: | `"assert"` |

This determines the keyword set that Rollup will use for import attributes.

### output.inlineDynamicImports 

| Type: | `boolean` |
|---|---|
| CLI: | `--inlineDynamicImports`/`--no-inlineDynamicImports` |
| Default: | `false` |

This will inline dynamic imports instead of creating new chunks to create a single bundle. Only possible if a single input is provided. Note that this will change the execution order: A module that is only imported dynamically will be executed immediately if the dynamic import is inlined.

### output.interop 

| Type: | `"compat" \| "auto" \| "esModule" \| "default" \| "defaultOnly" \| ((id: string) => "compat" \| "auto" \| "esModule" \| "default" \| "defaultOnly")` |
|---|---|
| CLI: | `--interop <value>` |
| Default: | `"default"` |

Controls how Rollup handles default, namespace and dynamic imports from external dependencies in formats like CommonJS that do not natively support these concepts. Note that the default mode of "default" mimics NodeJS behavior and is different from TypeScript `esModuleInterop`. To get TypeScript's behavior, explicitly set the value to `"auto"`. In the examples, we will be using the CommonJS format, but the choice of interop similarly applies to AMD, IIFE and UMD targets as well.

To understand the different values, assume we are bundling the following code for a `cjs` target:

js

```js
import ext_default, * as external from 'external1';
console.log(ext_default, external.bar, external);
import('external2').then(console.log);
```

Keep in mind that for Rollup, `import * as ext_namespace from 'external'; console.log(ext_namespace.bar);` is completely equivalent to `import {bar} from 'external'; console.log(bar);` and will produce the same code. In the example above however, the namespace object itself is passed to a global function as well, which means we need it as a properly formed object.

- `"default"` assumes that the required value should be treated as the default export of the imported module, just like when importing CommonJS from an ES module context in NodeJS. Named imports are supported as well, which are treated as properties of the default import. To create the namespace object, Rollup injects these helpers:js`var external = require('external1'); function _interopNamespaceDefault(e) { var n = Object.create(null); if (e) { Object.keys(e).forEach(function (k) { if (k !== 'default') { var d = Object.getOwnPropertyDescriptor(e, k); Object.defineProperty( n, k, d.get ? d : { enumerable: true, get: function () { return e[k]; } } ); } }); } n.default = e; return Object.freeze(n); } var external__namespace = /*#__PURE__*/ _interopNamespaceDefault(external); console.log(external, external__namespace.bar, external__namespace); Promise.resolve() .then(function () { return /*#__PURE__*/ _interopNamespaceDefault(require('external2')); }) .then(console.log);`
- `"esModule"` assumes that required modules are transpiled ES modules where the required value corresponds to the module namespace, and the default export is the `.default` property of the exported object. This is the only interop type that will not inject any helper functions:js`var external = require('external1'); console.log(external.default, external.bar, external); Promise.resolve() .then(function () { return require('external2'); }) .then(console.log);`When `esModule` is used, Rollup adds no additional interop helpers and also supports live-bindings for default exports.
- `"auto"` combines both `"esModule"` and `"default"` by injecting helpers that contain code that detects at runtime if the required value contains the `__esModule` property. Adding this property is a hack implemented by TypeScript `esModuleInterop`, Babel and other tools to signify that the required value is the namespace of a transpiled ES module.:js`var external = require('external1'); function _interopNamespace(e) { if (e && e.__esModule) return e; var n = Object.create(null); if (e) { Object.keys(e).forEach(function (k) { if (k !== 'default') { var d = Object.getOwnPropertyDescriptor(e, k); Object.defineProperty( n, k, d.get ? d : { enumerable: true, get: function () { return e[k]; } } ); } }); } n.default = e; return Object.freeze(n); } var external__namespace = /*#__PURE__*/ _interopNamespace(external); console.log( external__namespace.default, external__namespace.bar, external__namespace ); Promise.resolve() .then(function () { return /*#__PURE__*/ _interopNamespace(require('external2')); }) .then(console.log);`Note how Rollup is reusing the created namespace object to get the `default` export. If the namespace object is not needed, Rollup will use a simpler helper:js`// input import ext_default from 'external'; console.log(ext_default); // output var ext_default = require('external'); function _interopDefault(e) { return e && e.__esModule ? e : { default: e }; } var ext_default__default = /*#__PURE__*/ _interopDefault(ext_default); console.log(ext_default__default.default);`
- `compat` is equivalent to `"auto"` except that it uses a slightly different helper for the default export that checks for the presence of a `default` property instead of the `__esModule` property. Except for the rare situation where a CommonJS module exports a property `"default"` that should not be the default export, this often helps to make interop "just work" as it does not rely on idiosyncratic hacks but instead uses duck-typing:js`var external = require('external1'); function _interopNamespaceCompat(e) { if (e && typeof e === 'object' && 'default' in e) return e; var n = Object.create(null); if (e) { Object.keys(e).forEach(function (k) { if (k !== 'default') { var d = Object.getOwnPropertyDescriptor(e, k); Object.defineProperty( n, k, d.get ? d : { enumerable: true, get: function () { return e[k]; } } ); } }); } n.default = e; return Object.freeze(n); } var external__namespace = /*#__PURE__*/ _interopNamespaceCompat(external); console.log( external__namespace.default, external__namespace.bar, external__namespace ); Promise.resolve() .then(function () { return /*#__PURE__*/ _interopNamespaceCompat(require('external2')); }) .then(console.log);`Similar to `"auto"`, Rollup will use a simpler helper if the namespace is not needed:js`// input import ext_default from 'external'; console.log(ext_default); // output var ext_default = require('external'); function _interopDefaultCompat(e) { return e && typeof e === 'object' && 'default' in e ? e : { default: e }; } var ext_default__default = /*#__PURE__*/ _interopDefaultCompat(ext_default); console.log(ext_default__default.default);`
- `"defaultOnly"` is similar to `"default"` except for the following:Here is what Rollup will create from the example code. Note that we removed `external.bar` from the code as otherwise, Rollup would have thrown an error because, as stated before, this is equivalent to a named import.js`var ext_default = require('external1'); function _interopNamespaceDefaultOnly(e) { return Object.freeze({ __proto__: null, default: e }); } var ext_default__namespace = /*#__PURE__*/ _interopNamespaceDefaultOnly(ext_default); console.log(ext_default, ext_default__namespace); Promise.resolve() .then(function () { return /*#__PURE__*/ _interopNamespaceDefaultOnly( require('external2') ); }) .then(console.log);`
  - Named imports are forbidden. If such an import is encountered, Rollup throws an error even in `es` and `system` formats. That way it is ensures that the `es` version of the code is able to import non-builtin CommonJS modules in Node correctly.
  - While namespace reexports `export * from 'external';` are not prohibited, they are ignored and will cause Rollup to display a warning because they would not have an effect if there are no named exports.
  - When a namespace object is generated, Rollup uses a much simpler helper.
- When a function is supplied, Rollup will pass each external id to this function once to control the interop type per dependency.As an example if all dependencies are CommonJs, the following config will ensure that named imports are only permitted from Node builtins:js`// rollup.config.js import builtins from 'builtins'; const nodeBuiltins = new Set(builtins()); export default { // ... output: { // ... interop(id) { if (nodeBuiltins.has(id)) { return 'default'; } return 'defaultOnly'; } } };`

There are some additional options that have an effect on the generated interop code:

- Setting `output.externalLiveBindings` to `false` will generate simplified namespace helpers as well as simplified code for extracted default imports.
- Setting `output.freeze` to `false` will prevent generated interop namespace objects from being frozen.

### output.intro/output.outro
