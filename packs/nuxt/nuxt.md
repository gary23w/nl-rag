---
title: "Nuxt"
source: https://en.wikipedia.org/wiki/Nuxt
domain: nuxt
license: CC-BY-SA-4.0
tags: nuxt, nuxtjs, vue ssr, vue meta-framework
fetched: 2026-07-02
---

# Nuxt

**Nuxt** is a free and open source full-stack web framework based on Vue.js, Nitro, and Vite. Nuxt is inspired by Next.js, which is a similar framework based on React rather than the Vue JavaScript library.

The main advantage of Nuxt over using Vue alone is its universal rendering system. The framework works as both an in-browser single-page application (SPA) as well as a server-rendered static website, by "hydrating" a server-rendered page to a full SPA after it is loaded. This allows websites to have the search engine optimization and performance benefits of a server-rendered site in addition to the interactivity of a client-rendered application. Nuxt largely abstracts the server-rendering features from the developer, and it's therefore able to have a similar development experience to a traditional SPA using Vue's single-file component (SFC) system.

In addition to its universal rendering mechanism, Nuxt also provides many other benefits and quality-of-life features, such as path-based routing, hot module replacement (HMR), TypeScript support out of the box, and middleware and server logic.

## Features

### Path-based routing

Rather than a regular Vue.js application, which ordinarily requires every route to be manually registered, Nuxt uses path-based routing to automatically register every route in an application.

Pages are declared in the `pages/` folder, where the name of the page file becomes the name of the route. Dynamic parameters can be added using square brackets, and catch-all routes can be added using three dots and square brackets, much like JavaScript's array spread syntax.

- `/pages/about.vue` - Matches /about.
- `/pages/user/[id].vue` - Matches all routes directly under /user.
- `/pages/posts/[...slug].vue` - Matches all routes under /posts.
- `/pages/admin/[[page]].vue` - Matches /admin in addition to all routes directly under it.

### Automatic imports

Nuxt automatically imports most Vue composition API functions, and any helper functions from the `composables/` and `utils/` folders.

```mw
<script setup>
    // ref is automatically imported
    const count = ref(0);
    // useRoute is also automatically imported
    const route = useRoute();
</script>

<template>
    <span>{{ count }}</span>
</template>
```

### Layouts

Nuxt supports SSR-friendly layouts out of the box, which allows similar pages to use the same basic templates, such as a header and footer. Layouts are declared in the `layouts/` folder, and work using native Vue slots.

To enable layouts in a Nuxt project, the entry point of the application, `app.vue`, must include a `NuxtLayout` component to toggle between layouts for each page.

```mw
<!-- sample app.vue file content -->
<template>
    <NuxtLayout>
        <NuxtPage />
    </NuxtLayout>
</template>
```

The default layout is located at `layouts/default.vue`, and must include a slot for the page content.

```mw
<!-- sample layout file content -->
<template>
    <CustomNavbar />
    <slot />
    <CustomFooter />
</template>
```

A page can use a custom layout by using the `definePageMeta` helper in a setup function or block.

```mw
<script setup>
definePageMeta({
    layout: "custom",
});
</script>

<template>
    <!-- this will now fill the slot of the custom layout -->
</template>
```

### Middleware

Nuxt adds middleware support to applications, which enables server logic to run between navigation changes. Both global and page-specific middleware files are supported.

Middleware is declared in the `middleware/` folder, which exports a function that takes in the current and previous routes as parameters. From there, globally-available helpers like abortNavigation and navigateTo can be used to control navigation.

```mw
export default defineNuxtMiddleware((to, from) => {
    // navigation logic
    if (to.params.id === "0")
        return abortNavigation();
    return navigateTo(`/users/${to.params.id}`);
});
```

### Server API

Nuxt can also generate server API routes and handlers, using the `server/` folder. Any file placed in `server/api` will become an API route, and any file placed in `server/routes` will become a route file, the difference being the final file location (`server/api` adds an api prefix to the path).

```mw
// server/api/hello.ts
export default defineEventHandler((event) => {
    return {
        some: "data here",
    };
});
```

This can now be called from components using the `useFetch` composable.

```mw
<script setup>
const { data } = await useFetch('/api/hello')
</script>

<template>
  <pre>{{ data }}</pre>
</template>
```
