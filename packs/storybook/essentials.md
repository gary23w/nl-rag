---
title: "Essentials"
source: https://storybook.js.org/docs/essentials
domain: storybook
license: CC-BY-SA-4.0 / MIT (storybook.js.org)
tags: storybook ui, component explorer, ui component stories, isolated component development
fetched: 2026-07-02
---

# Essentials

Storybook essentials is a set of tools that help you build, test, and document your components within Storybook. It includes the following:

- Actions
- Backgrounds
- Controls
- Highlight
- Measure & outline
- Toolbars & globals
- Viewport

## Configuration

Essentials is “zero-config”. It comes with a recommended configuration out of the box.

Many of the features above can be configured via parameters. See each feature's documentation (linked above) for more details.

## Disabling features

If you need to disable any of the essential features, you can do it by changing your `.storybook/main.js|ts` file.

For example, if you wanted to disable the backgrounds feature, you would apply the following change to your Storybook configuration:

.storybook/main.ts

```
// Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
import type { StorybookConfig } from '@storybook/your-framework';
 
const config: StorybookConfig = {
  framework: '@storybook/your-framework',
  stories: ['../src/**/*.mdx', '../src/**/*.stories.@(js|jsx|mjs|ts|tsx)'],
  features: {
    backgrounds: false, // 👈 disable the backgrounds feature
  },
};
 
export default config;
```

💡

You can use the following keys for each individual feature: `actions`, `backgrounds`, `controls`, `highlight`, `measure`, `outline`, `toolbars`, and `viewport`.
