---
title: "Configuration Options (part 4/4)"
source: https://rollupjs.org/configuration-options/
domain: rollup
license: CC-BY-SA-4.0 / MIT (rollupjs.org)
tags: rollup bundler, rollupjs, es module bundler, rollup tree shaking
fetched: 2026-07-02
part: 4/4
---

## Experimental options 

These options reflect new features that have not yet been fully finalized. Availability, behaviour and usage may therefore be subject to change between minor versions.

### experimentalCacheExpiry 

| Type: | `number` |
|---|---|
| CLI: | `--experimentalCacheExpiry <numberOfRuns>` |
| Default: | `10` |

Determines after how many runs cached assets that are no longer used by plugins should be removed.

### experimentalLogSideEffects 

| Type: | `boolean` |
|---|---|
| CLI: | `--experimentalLogSideEffects`/`--no-experimentalLogSideEffects` |
| Default: | `false` |

When set to `true`, this will log the first side effect it finds in every file to the console. This can be very helpful to figure which files have side effects and what the actual side effects are. Removing side effects can improve tree-shaking and chunk generation and is crucial to make `output.experimentalMinChunkSize` work.

This option will only log top-level statements, though. Sometimes, e.g. in case of immediately-invoked-function-expressions, the actual side effect can be hidden inside a nested expression.

### output.experimentalMinChunkSize 

| Type: | `number` |
|---|---|
| CLI: | `--experimentalMinChunkSize <size>` |
| Default: | `1` |

Set a minimal chunk size target in Byte for code-splitting setups. When this value is set to the default of `1`, Rollup will try to merge chunks that do not contain code except imports and reexports into other chunks. A merge will only be performed if it does not change what side effects are executed when any entry is loaded. For the value of `1`, only merges are permitted that do not increase the amount of code loaded for any entry.

Larger values will try to merge any chunk below the limit into other chunks. In that case, it is accepted that entries may load some unnecessary code. The algorithm always tries to merge in a way that minimizes the amount of unnecessary code, though.

Unfortunately, due to the way chunking works, chunk size is measured before any chunk rendering plugins like minifiers ran, which means you should use a high enough limit to take this into account. It will take tree-shaking of top-level statements into account when calculating the size.

### perf 

| Type: | `boolean` |
|---|---|
| CLI: | `--perf`/`--no-perf` |
| Default: | `false` |

Whether to collect performance timings. When used from the command line or a configuration file, detailed measurements about the current bundling process will be displayed. When used from the JavaScript API, the returned bundle object will contain an additional `getTimings()` function that can be called at any time to retrieve all accumulated measurements.

`getTimings()` returns an object of the following form:

```vp
{
  "# BUILD": [ 698.020877, 33979632, 45328080 ],
  "## parse modules": [ 537.509342, 16295024, 27660296 ],
  "load modules": [ 33.253778999999994, 2277104, 38204152 ],
  ...
}
```

For each key, the first number represents the elapsed time while the second represents the change in memory consumption, and the third represents the total memory consumption after this step. The order of these steps is the order used by `Object.keys`. Top level keys start with `#` and contain the timings of nested steps, i.e. in the example above, the 698ms of the `# BUILD` step include the 538ms of the `## parse modules` step.

### fs 

| Type: | `RollupFsModule` |
|---|---|
| Default: | `node:fs.promises` in NodeJS, no default in browsers |

If you want to use a custom file system module, you can set this option to an object that implements the same API as the `RollupFsModule` interface. This is useful if you want to use a different file system implementation such as `memfs`, if you want to mock the file system for testing purposes, or if you use the browser build of Rollup.

typescript

```typescript
interface RollupFsModule {
	appendFile(
		path: string,
		data: string | Uint8Array,
		options?: {
			encoding?: BufferEncoding | null;
			mode?: string | number;
			flag?: string | number;
		}
	): Promise<void>;

	copyFile(
		source: string,
		destination: string,
		mode?: string | number
	): Promise<void>;

	mkdir(
		path: string,
		options?: { recursive?: boolean; mode?: string | number }
	): Promise<void>;

	mkdtemp(prefix: string): Promise<string>;

	readdir(
		path: string,
		options?: { withFileTypes?: boolean }
	): Promise<(string | RollupDirectoryEntry)[]>;

	readFile(
		path: string,
		options?: {
			encoding?: BufferEncoding | null;
			flag?: string | number;
			signal?: AbortSignal;
		}
	): Promise<string | Uint8Array>;

	realpath(path: string): Promise<string>;

	rename(oldPath: string, newPath: string): Promise<void>;

	rmdir(path: string, options?: { recursive?: boolean }): Promise<void>;

	stat(path: string): Promise<RollupFileStats>;

	lstat(path: string): Promise<RollupFileStats>;

	unlink(path: string): Promise<void>;

	writeFile(
		path: string,
		data: string | ArrayBuffer | ArrayBufferView,
		options?: {
			encoding?: BufferEncoding | null;
			mode?: string | number;
			flag?: string | number;
		}
	): Promise<void>;
}

type BufferEncoding =
	| 'ascii'
	| 'utf8'
	| 'utf16le'
	| 'ucs2'
	| 'base64'
	| 'base64url'
	| 'latin1'
	| 'binary'
	| 'hex';

export interface RollupDirectoryEntry {
	isFile(): boolean;
	isDirectory(): boolean;
	isSymbolicLink(): boolean;
	name: string;
}

interface RollupFileStats {
	isFile(): boolean;
	isDirectory(): boolean;
	isSymbolicLink(): boolean;
	size: number;
	mtime: Date;
	ctime: Date;
	atime: Date;
	birthtime: Date;
}
```


## watch 

| Type: | `WatcherOptions \| false` |
|---|---|
| Default: | `{}` |

typescript

```typescript
interface WatcherOptions {
	allowInputInsideOutputPath?: boolean;
	buildDelay?: number;
	chokidar?: ChokidarOptions;
	clearScreen?: boolean;
	exclude?: string | RegExp | (string | RegExp)[];
	include?: string | RegExp | (string | RegExp)[];
	skipWrite?: boolean;
	onInvalidate?: (id: string) => void;
}
```

Specify options for watch mode or prevent this configuration from being watched. Specifying `false` is only really useful when an array of configurations is used. In that case, this configuration will not be built or rebuilt on change in watch mode, but it will be built when running Rollup regularly:

js

```js
// rollup.config.js
export default [
	{
		input
: 'main.js',
		output
: { file
: 'bundle.cjs.js', format
: 'cjs' }
	},
	{
		input
: 'main.js',
		watch
: false,
		output
: { file
: 'bundle.es.js', format
: 'es' }
	}
];
```

These options only take effect when running Rollup with the `--watch` flag, or using `rollup.watch`.

### watch.allowInputInsideOutputPath 

| Type: | `boolean` |
|---|---|
| CLI: | `--watch.allowInputInsideOutputPath`/`--no-watch.allowInputInsideOutputPath` |
| Default: | `false` |

Whether the input path is allowed to be a subpath of the output path.

### watch.buildDelay 

| Type: | `number` |
|---|---|
| CLI: | `--watch.buildDelay <number>` |
| Default: | `0` |

Configures how long Rollup will wait for further changes until it triggers a rebuild in milliseconds. By default, Rollup does not wait but there is a small debounce timeout configured in the chokidar instance. Setting this to a value greater than `0` will mean that Rollup will only trigger a rebuild if there was no change for the configured number of milliseconds. If several configurations are watched, Rollup will use the largest configured build delay.

### watch.chokidar 

| Type: | `ChokidarOptions` |
|---|---|

An optional object of watch options that will be passed to the bundled chokidar instance. See the chokidar documentation to find out what options are available.

### watch.clearScreen 

| Type: | `boolean` |
|---|---|
| CLI: | `--watch.clearScreen`/`--no-watch.clearScreen` |
| Default: | `true` |

Whether to clear the screen when a rebuild is triggered.

### watch.exclude 

| Type: | `string \| RegExp \| (string \| RegExp)[]` |
|---|---|
| CLI: | `--watch.exclude <files>` |

Prevent files from being watched:

js

```js
// rollup.config.js
export default {
	// ...
	watch
: {
		exclude
: 'node_modules/**'
	}
};
```

### watch.include 

| Type: | `string \| RegExp \| (string \| RegExp)[]` |
|---|---|
| CLI: | `--watch.include <files>` |

Limit the file-watching to certain files. Note that this only filters the module graph but does not allow adding additional watch files:

js

```js
// rollup.config.js
export default {
	// ...
	watch
: {
		include
: 'src/**'
	}
};
```

### watch.skipWrite 

| Type: | `boolean` |
|---|---|
| CLI: | `--watch.skipWrite`/`--no-watch.skipWrite` |
| Default: | `false` |

Whether to skip the `bundle.write()` step when a rebuild is triggered.

### watch.onInvalidate 

| Type: | `(id: string) => void` |
|---|---|

An optional function that will be called immediately every time a module changes that is part of the build. It receives the id of the changed module as argument. This is different from the `watchChange` plugin hook, which is only called once the running build has finished. This may for instance be used to prevent additional steps from being performed if we know another build will be started anyway once the current build finished. This callback may be called multiple times per build as it tracks every change.


## Deprecated options 

☢️ These options have been deprecated and may be removed in a future Rollup version.

### output.externalImportAssertions 

*Use the `output.externalImportAttributes` option instead.*

| Type: | `boolean` |
|---|---|
| CLI: | `--externalImportAssertions`/`--no-externalImportAssertions` |
| Default: | `true` |

Whether to add import assertions to external imports in the output if the output format is `es`. By default, assertions are taken from the input files, but plugins can add or remove assertions later. E.g. `import "foo" assert {type: "json"}` will cause the same import to appear in the output unless the option is set to `false`. Note that all imports of a module need to have consistent assertions, otherwise a warning is emitted.

### output.onlyExplicitManualChunks 

| Type: | `boolean` |
|---|---|

If set to true, using the output.manualChunks function form won't merge dependencies into the output chunk.

For instance, with

js

```js
// src/main.js (entry point)
import './manual1';
import './manual2';

console.log('main');

// src/manual1.js
import './dep.js';

console.log('manual1');

// src/manual2.js
import './dep.js';

console.log('manual2');

// src/dep.js
console.log('dep');
```

and

js

```js
function manualChunks
(id
) {
	if (id
.endsWith
('manual1.js') && id
.endsWith
('manual2.js')) {
		return 'manual';
	}
}
```

the dep.js `export const dep = 'dep';` code, won't be merged into the `manual` output chunk. This gives you full control over what code goes into which manual chunks, and if your manual chunking is very granular, this can prevent import graph inaccuracies and help reduce cache invalidation.

Note: although this option is new in Rollup 4, it is marked as deprecated because it will become the new default for the function form in Rollup 5.
