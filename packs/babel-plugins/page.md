---
title: "What is Babel? · Babel"
source: https://babeljs.io/docs/
domain: babel-plugins
license: CC-BY-SA-4.0
tags: babel plugins, javascript transpiler, babel transcompiler, ecmascript downleveling
fetched: 2026-07-02
---

# What is Babel?

## Babel is a JavaScript compiler

Babel is a toolchain that is mainly used to convert ECMAScript 2015+ code into a backwards compatible version of JavaScript in current and older browsers or environments. Here are the main things Babel can do for you:

- Transform syntax
- Polyfill features that are missing in your target environment (through a third-party polyfill such as core-js)
- Source code transformations (codemods)
- And more! (check out these videos for inspiration)

JavaScript

```js
[1, 2, 3].map(n => n + 1);

[1, 2, 3].map(function(n) {
  return n + 1;
});
```

tip

For an awesome tutorial on compilers, check out the-super-tiny-compiler, which also explains how Babel itself works on a high level.

## ES2015 and beyond

Babel has support for the latest version of JavaScript through syntax transformers.

These plugins allow you to use new syntax, **right now** without waiting for browser support. Check out our usage guide to get started.

## JSX and React

Babel can convert JSX syntax! Check out our React preset to get started. Use it together with the babel-sublime package to bring syntax highlighting to a whole new level.

You can install this preset with

- npm
- Yarn
- pnpm
- Bun

```shell
npm install --save-dev @babel/preset-react
```

```shell
yarn add --dev @babel/preset-react
```

```shell
pnpm add --save-dev @babel/preset-react
```

```shell
bun add --dev @babel/preset-react
```

and add `@babel/preset-react` to your Babel configuration.

JSX

```jsx
export default function DiceRoll(){
  const getRandomNumber = () => {
    return Math.ceil(Math.random() * 6);
  };

  const [num, setNum] = useState(getRandomNumber());

  const handleClick = () => {
    const newNum = getRandomNumber();
    setNum(newNum);
  };

  return (
    <div>
      Your dice roll: {num}.
      <button onClick={handleClick}>Click to get a new number</button>
    </div>
  );
};
```

tip

Learn more about JSX

## Type Annotations (Flow and TypeScript)

Babel can strip out type annotations! Check out either our Flow preset or TypeScript preset to get started. Keep in mind that **Babel doesn't do type checking**; you'll still have to install and use Flow or TypeScript to check types.

You can install the flow preset with

- npm
- Yarn
- pnpm
- Bun

```shell
npm install --save-dev @babel/preset-flow
```

```shell
yarn add --dev @babel/preset-flow
```

```shell
pnpm add --save-dev @babel/preset-flow
```

```shell
bun add --dev @babel/preset-flow
```

JavaScript

```js
function square(n: number): number {
  return n * n;
}
```

or the typescript preset with

- npm
- Yarn
- pnpm
- Bun

```shell
npm install --save-dev @babel/preset-typescript
```

```shell
yarn add --dev @babel/preset-typescript
```

```shell
pnpm add --save-dev @babel/preset-typescript
```

```shell
bun add --dev @babel/preset-typescript
```

JavaScript

```js
function Greeter(greeting: string) {
  this.greeting = greeting;
}
```

tip

Learn more about Flow and TypeScript!

## Pluggable

Babel is built out of plugins. Compose your own transformation pipeline using existing plugins or write your own. Easily use a set of plugins by using or creating a preset.

Create a plugin on the fly with astexplorer.net or use generator-babel-plugin to generate a plugin template.

example-babel-plugin.js

```javascript
export default function({ types: t }) {
  return {
    visitor: {
      Identifier(path) {
        let name = path.node.name; 
        path.node.name = [...name]
          .reverse()
          .join("");
      },
    },
  };
}
```

## Debuggable

**Source map** support so you can debug your compiled code with ease.

## Spec Compliant

Babel tries to stay true to the ECMAScript standard, as much as reasonably possible. It may also have specific options to be more spec compliant as a tradeoff to performance.

## Compact

Babel tries using the least amount of code possible with no dependence on a bulky runtime.

This may be difficult to do in cases, and there are "assumptions" options that tradeoff spec compliancy for readability, file size, and speed.
