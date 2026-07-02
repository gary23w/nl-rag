"""Web frontend frameworks, libraries, styling, and browser APIs."""

from .common import CC_BY_SA, CC_BY_SA_25, WIKI, mdn, wiki

DOMAINS = {
    "angular": {
        "tags": ["angular framework", "angularjs", "angular component", "typescript spa"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Angular_(web_framework)",
            "AngularJS",
            "Single-page_application",
            "Web_framework",
        ) + [
            mdn("Glossary/SPA"),
            mdn("Learn_web_development/Core/Frameworks_libraries"),
        ],
    },
    "nextjs": {
        "tags": ["next.js", "nextjs", "server-side rendering", "static site generator", "react ssr"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Next.js",
            "React_(software)",
            "Server-side_rendering",
            "Static_site_generator",
        ) + [
            mdn("Glossary/SSR"),
            mdn("Web/Performance"),
        ],
    },
    "nuxt": {
        "tags": ["nuxt", "nuxtjs", "vue ssr", "vue meta-framework"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Nuxt",
            "Vue.js",
            "Server-side_rendering",
            "JavaScript_framework",
        ) + [
            mdn("Web/Performance"),
            mdn("Learn_web_development/Core/Frameworks_libraries"),
        ],
    },
    "remix": {
        "tags": ["remix framework", "remix run", "nested routing", "react router framework"],
        "license": CC_BY_SA + " / MIT (remix.run)",
        "pages": wiki(
            "React_(software)",
            "Server-side_rendering",
            "Web_framework",
        ) + [
            "https://remix.run/docs/en/main/discussion/introduction",
            "https://remix.run/docs/en/main/start/quickstart",
            mdn("Glossary/Progressive_web_apps"),
        ],
    },
    "astro": {
        "tags": ["astro framework", "astro islands", "islands architecture", "content-driven site"],
        "license": CC_BY_SA + " / MIT (astro.build)",
        "pages": wiki(
            "Static_site_generator",
            "Web_framework",
            "Server-side_rendering",
        ) + [
            "https://docs.astro.build/en/concepts/why-astro/",
            "https://docs.astro.build/en/concepts/islands/",
            "https://docs.astro.build/en/basics/astro-components/",
        ],
    },
    "solidjs": {
        "tags": ["solidjs", "solid js", "fine-grained reactivity", "reactive signals"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Reactive_programming",
            "Virtual_DOM",
            "JavaScript_library",
            "Comparison_of_JavaScript-based_web_frameworks",
        ) + [
            mdn("Web/API/Document_Object_Model"),
            mdn("Learn_web_development/Core/Frameworks_libraries"),
        ],
    },
    "preact": {
        "tags": ["preact", "lightweight react alternative", "virtual dom library", "small react runtime"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Virtual_DOM",
            "React_(software)",
            "JavaScript_library",
            "Document_Object_Model",
        ) + [
            mdn("Web/API/Document_Object_Model/Introduction"),
            mdn("Learn_web_development/Core/Frameworks_libraries"),
        ],
    },
    "alpinejs": {
        "tags": ["alpine.js", "alpinejs", "x-data directive", "lightweight reactivity"],
        "license": CC_BY_SA + " / MIT (alpinejs.dev)",
        "pages": wiki(
            "JavaScript_library",
            "Reactive_programming",
            "Document_Object_Model",
        ) + [
            "https://alpinejs.dev/start-here",
            "https://alpinejs.dev/essentials/state",
            "https://alpinejs.dev/directives/data",
        ],
    },
    "htmx": {
        "tags": ["htmx", "hypermedia driven", "hx-get", "ajax attributes"],
        "license": CC_BY_SA + " / BSD (htmx.org)",
        "pages": wiki(
            "HTMX",
            "Ajax_(programming)",
            "Hypertext_Transfer_Protocol",
        ) + [
            "https://htmx.org/docs/",
            "https://htmx.org/reference/",
            "https://htmx.org/examples/",
        ],
    },
    "jquery": {
        "tags": ["jquery", "jquery selector", "dom manipulation library", "jquery ajax"],
        "license": CC_BY_SA,
        "pages": wiki(
            "JQuery",
            "Ajax_(programming)",
            "JavaScript_library",
        ) + [
            mdn("Web/API/Document_Object_Model"),
            mdn("Web/API/Document_Object_Model/Introduction"),
            mdn("Web/API/EventTarget"),
        ],
    },
    "emberjs": {
        "tags": ["ember.js", "emberjs", "handlebars templates", "convention over configuration ui"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Ember.js",
            "Handlebars_(template_system)",
            "Web_framework",
            "Single-page_application",
        ) + [
            mdn("Learn_web_development/Core/Frameworks_libraries"),
            mdn("Web/API/Document_Object_Model"),
        ],
    },
    "lit-element": {
        "tags": ["lit element", "lit html", "reactive web component", "lit template"],
        "license": CC_BY_SA + " / BSD (lit.dev)",
        "pages": wiki(
            "Web_Components",
            "Document_Object_Model",
        ) + [
            mdn("Web/API/Web_components/Using_custom_elements"),
            "https://lit.dev/docs/",
            "https://lit.dev/docs/components/overview/",
            "https://lit.dev/docs/templates/overview/",
        ],
    },
    "qwik": {
        "tags": ["qwik framework", "resumability", "qwik resumable", "lazy hydration"],
        "license": CC_BY_SA + " / MIT (qwik.dev)",
        "pages": wiki(
            "Server-side_rendering",
            "Web_framework",
            "JavaScript_framework",
        ) + [
            "https://qwik.dev/docs/concepts/resumable/",
            "https://qwik.dev/docs/concepts/think-qwik/",
            mdn("Web/Performance"),
        ],
    },
    "tailwind-css": {
        "tags": ["tailwind css", "utility-first css", "tailwind utility classes", "atomic css"],
        "license": CC_BY_SA,
        "pages": wiki("Tailwind_CSS", "CSS_framework", "Cascading_Style_Sheets") + [
            mdn("Learn_web_development/Core/Styling_basics"),
            mdn("Web/CSS/Reference"),
            mdn("Web/CSS/CSS_grid_layout"),
        ],
    },
    "bootstrap-css": {
        "tags": ["bootstrap css", "bootstrap grid", "responsive framework", "twitter bootstrap"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Bootstrap_(front-end_framework)",
            "CSS_framework",
            "Responsive_web_design",
        ) + [
            mdn("Web/CSS/CSS_grid_layout"),
            mdn("Learn_web_development/Core/CSS_layout/Responsive_Design"),
            mdn("Web/CSS/CSS_flexible_box_layout"),
        ],
    },
    "sass-scss": {
        "tags": ["sass", "scss", "css preprocessor", "sass mixin", "sass nesting"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Sass_(style_sheet_language)",
            "Cascading_Style_Sheets",
        ) + [
            mdn("Web/CSS/CSS_nesting"),
            mdn("Web/CSS/Syntax"),
            mdn("Web/CSS/@import"),
            mdn("Web/CSS/CSS_cascade/Specificity"),
        ],
    },
    "less-css": {
        "tags": ["less css", "less style sheet", "css preprocessor language", "less mixin"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Less_(style_sheet_language)",
            "Cascading_Style_Sheets",
        ) + [
            mdn("Web/CSS/CSS_nesting"),
            mdn("Web/CSS/CSS_cascade/Cascade"),
            mdn("Web/CSS/CSS_cascade/Specificity"),
            mdn("Web/CSS/@import"),
        ],
    },
    "css-modules": {
        "tags": ["css modules", "scoped class names", "locally scoped css", "css module composition"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "Cascading_Style_Sheets",
        ) + [
            mdn("Web/CSS/CSS_scoping"),
            mdn("Web/CSS/CSS_cascade/Specificity"),
            mdn("Web/CSS/CSS_cascade/Cascade"),
            mdn("Web/CSS/Syntax"),
            mdn("Web/CSS/Reference"),
        ],
    },
    "styled-components": {
        "tags": ["styled components", "css-in-js", "component-scoped styling", "tagged template css"],
        "license": CC_BY_SA,
        "pages": wiki(
            "CSS-in-JS",
            "Cascading_Style_Sheets",
        ) + [
            mdn("Web/API/CSSStyleSheet"),
            mdn("Web/CSS/CSS_scoping"),
            mdn("Web/CSS/Reference"),
            mdn("Web/JavaScript/Reference/Global_Objects/Proxy"),
        ],
    },
    "web-components": {
        "tags": ["web components", "custom elements", "html template element", "customelementregistry"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "Web_Components",
        ) + [
            mdn("Web/API/Web_components/Using_custom_elements"),
            mdn("Web/API/CustomElementRegistry"),
            mdn("Web/API/HTMLTemplateElement"),
            mdn("Web/HTML/Reference/Elements/slot"),
            mdn("Web/API/CustomEvent"),
        ],
    },
    "progressive-web-apps": {
        "tags": ["progressive web app", "pwa", "web app manifest", "installable web app"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "Progressive_web_app",
        ) + [
            mdn("Web/Progressive_web_apps"),
            mdn("Web/Manifest"),
            mdn("Web/Manifest/Reference"),
            mdn("Web/API/BeforeInstallPromptEvent"),
            mdn("Web/API/Notification"),
        ],
    },
    "service-workers": {
        "tags": ["service worker", "offline caching", "cache storage api", "background sync"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "Service_worker",
        ) + [
            mdn("Web/API/Service_Worker_API"),
            mdn("Web/API/Service_Worker_API/Using_Service_Workers"),
            mdn("Web/API/CacheStorage"),
            mdn("Web/API/Navigator/serviceWorker"),
            mdn("Web/API/Clients"),
        ],
    },
    "webrtc": {
        "tags": ["webrtc", "rtcpeerconnection", "peer-to-peer media", "getusermedia", "rtc data channel"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "WebRTC",
        ) + [
            mdn("Web/API/WebRTC_API"),
            mdn("Web/API/RTCPeerConnection"),
            mdn("Web/API/MediaDevices/getUserMedia"),
            mdn("Web/API/RTCDataChannel"),
            mdn("Web/API/MediaStream"),
        ],
    },
    "canvas-api": {
        "tags": ["canvas api", "canvas element", "2d rendering context", "canvasrenderingcontext2d"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "Canvas_element",
        ) + [
            mdn("Web/API/Canvas_API"),
            mdn("Web/API/CanvasRenderingContext2D"),
            mdn("Web/API/Canvas_API/Tutorial/Drawing_shapes"),
            mdn("Web/API/Canvas_API/Tutorial/Basic_animations"),
            mdn("Web/API/OffscreenCanvas"),
        ],
    },
    "webgpu": {
        "tags": ["webgpu", "gpu compute web", "gpudevice", "webgpu render pipeline"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "WebGPU",
        ) + [
            mdn("Web/API/WebGPU_API"),
            mdn("Web/API/GPUDevice"),
            mdn("Web/API/GPUBuffer"),
            mdn("Web/API/GPURenderPipeline"),
            mdn("Web/API/GPUQueue"),
        ],
    },
    "threejs": {
        "tags": ["three.js", "threejs", "webgl 3d library", "3d scene rendering"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Three.js",
            "WebGL",
        ) + [
            mdn("Web/API/WebGL_API"),
            mdn("Web/API/WebGL_API/Tutorial"),
            mdn("Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL"),
            mdn("Web/API/WebGLRenderingContext"),
        ],
    },
    "d3js": {
        "tags": ["d3.js", "d3js", "data-driven documents", "svg data binding"],
        "license": CC_BY_SA,
        "pages": wiki(
            "D3.js",
            "Data_visualization",
            "Scalable_Vector_Graphics",
        ) + [
            mdn("Web/SVG"),
            mdn("Web/API/SVGElement"),
            mdn("Web/SVG/Tutorials/SVG_from_scratch"),
        ],
    },
    "chartjs": {
        "tags": ["chart.js", "chartjs", "canvas charting", "javascript charts"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Chart.js",
            "Data_visualization",
            "Infographic",
        ) + [
            mdn("Web/API/Canvas_API"),
            mdn("Web/API/CanvasRenderingContext2D"),
            mdn("Web/API/Canvas_API/Tutorial"),
        ],
    },
    "redux": {
        "tags": ["redux library", "redux store", "flux architecture", "predictable state container"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Redux_(JavaScript_library)",
            "State_management",
            "Flux_(software)",
            "Reactive_programming",
        ) + [
            mdn("Web/JavaScript/Guide/Using_classes"),
            mdn("Web/API/EventTarget"),
        ],
    },
    "mobx": {
        "tags": ["mobx", "observable state", "transparent reactivity", "mobx reaction"],
        "license": CC_BY_SA + " / MIT (mobx.js.org)",
        "pages": wiki(
            "Reactive_programming",
            "Observer_pattern",
            "State_management",
        ) + [
            "https://mobx.js.org/the-gist-of-mobx.html",
            "https://mobx.js.org/observable-state.html",
            "https://mobx.js.org/reactions.html",
        ],
    },
    "zustand": {
        "tags": ["zustand store", "hook-based state", "minimal state management", "zustand selector"],
        "license": CC_BY_SA,
        "pages": wiki(
            "State_management",
            "Reactive_programming",
            "JavaScript_library",
            "Observer_pattern",
        ) + [
            mdn("Web/API/EventTarget"),
            mdn("Web/JavaScript/Guide/Using_classes"),
        ],
    },
    "react-query": {
        "tags": ["react query", "tanstack query", "server state caching", "data fetching library"],
        "license": CC_BY_SA,
        "pages": wiki(
            "State_management",
            "Ajax_(programming)",
            "Reactive_programming",
        ) + [
            mdn("Web/API/Fetch_API"),
            mdn("Web/API/Fetch_API/Using_Fetch"),
            mdn("Web/API/AbortController"),
        ],
    },
    "vite-build": {
        "tags": ["vite build", "vite dev server", "esm bundler", "vite hmr"],
        "license": CC_BY_SA + " / MIT (vitejs.dev)",
        "pages": wiki(
            "Vite",
            "Module_bundler",
        ) + [
            "https://vitejs.dev/guide/why",
            "https://vitejs.dev/guide/features",
            "https://vitejs.dev/guide/dep-pre-bundling",
            mdn("Glossary/Tree_shaking"),
        ],
    },
    "webpack": {
        "tags": ["webpack bundler", "webpack loader", "webpack bundle", "module bundler config"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Webpack",
            "Module_bundler",
            "Minification_(programming)",
            "Build_automation",
        ) + [
            mdn("Glossary/Tree_shaking"),
            mdn("Learn_web_development/Extensions/Client-side_tools/Overview"),
        ],
    },
    "rollup": {
        "tags": ["rollup bundler", "rollupjs", "es module bundler", "rollup tree shaking"],
        "license": CC_BY_SA + " / MIT (rollupjs.org)",
        "pages": wiki(
            "Module_bundler",
            "Tree_shaking",
            "Minification_(programming)",
        ) + [
            "https://rollupjs.org/introduction/",
            "https://rollupjs.org/tutorial/",
            "https://rollupjs.org/configuration-options/",
        ],
    },
    "esbuild": {
        "tags": ["esbuild bundler", "go javascript bundler", "fast transpiler", "esbuild bundling"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Esbuild",
            "Module_bundler",
            "Source-to-source_compiler",
            "Minification_(programming)",
        ) + [
            mdn("Glossary/Tree_shaking"),
            mdn("Web/JavaScript/Guide/Modules"),
        ],
    },
    "babel": {
        "tags": ["babel transpiler", "babel transcompiler", "ecmascript polyfill", "jsx transform"],
        "license": CC_BY_SA,
        "pages": wiki(
            "Babel_(transcompiler)",
            "Source-to-source_compiler",
            "Polyfill_(programming)",
            "ECMAScript",
        ) + [
            mdn("Web/JavaScript/Guide/Modules"),
            mdn("Web/JavaScript/Reference/Statements/import"),
        ],
    },
    "eslint": {
        "tags": ["eslint linter", "javascript linter", "lint rules", "static analysis js"],
        "license": CC_BY_SA,
        "pages": wiki(
            "ESLint",
            "Lint_(software)",
            "Static_program_analysis",
            "Programming_style",
        ) + [
            mdn("Web/JavaScript/Guide/Using_classes"),
            mdn("Learn_web_development/Extensions/Client-side_tools/Overview"),
        ],
    },
    "prettier": {
        "tags": ["prettier formatter", "code formatter", "opinionated formatting", "prettier options"],
        "license": CC_BY_SA + " / MIT (prettier.io)",
        "pages": wiki(
            "Programming_style",
            "Indentation_style",
            "Lint_(software)",
        ) + [
            "https://prettier.io/docs/why-prettier",
            "https://prettier.io/docs/options",
            "https://prettier.io/docs/rationale",
        ],
    },
    "storybook": {
        "tags": ["storybook ui", "component explorer", "ui component stories", "isolated component development"],
        "license": CC_BY_SA + " / MIT (storybook.js.org)",
        "pages": wiki(
            "Component-based_software_engineering",
            "JavaScript_library",
        ) + [
            "https://storybook.js.org/docs",
            "https://storybook.js.org/docs/writing-stories",
            "https://storybook.js.org/docs/essentials",
            mdn("Learn_web_development/Core/Frameworks_libraries"),
        ],
    },
    "css-grid": {
        "tags": ["css grid", "grid layout", "grid template", "grid auto-placement"],
        "license": CC_BY_SA_25,
        "pages": [
            mdn("Web/CSS/CSS_grid_layout"),
            mdn("Web/CSS/CSS_grid_layout/Basic_concepts_of_grid_layout"),
            mdn("Web/CSS/CSS_grid_layout/Auto-placement_in_grid_layout"),
            mdn("Web/CSS/grid"),
            mdn("Web/CSS/grid-template-columns"),
            mdn("Web/CSS/gap"),
        ] + wiki("Grid_(graphic_design)"),
    },
    "flexbox": {
        "tags": ["flexbox", "flexible box layout", "flex container", "justify-content", "align-items"],
        "license": CC_BY_SA_25,
        "pages": [
            mdn("Web/CSS/CSS_flexible_box_layout"),
            mdn("Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox"),
            mdn("Web/CSS/CSS_flexible_box_layout/Aligning_items_in_a_flex_container"),
            mdn("Web/CSS/flex"),
            mdn("Web/CSS/justify-content"),
            mdn("Web/CSS/align-items"),
        ],
    },
    "web-animations": {
        "tags": ["web animations api", "keyframe animation", "css transition", "animation timeline"],
        "license": CC_BY_SA_25,
        "pages": [
            mdn("Web/API/Web_Animations_API"),
            mdn("Web/CSS/CSS_animations"),
            mdn("Web/CSS/CSS_transitions"),
            mdn("Web/CSS/@keyframes"),
            mdn("Web/API/KeyframeEffect"),
            mdn("Web/API/Animation"),
        ],
    },
    "dom-events": {
        "tags": ["dom events", "event listener", "event bubbling", "event delegation", "addeventlistener"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "DOM_events",
            "Event_(computing)",
        ) + [
            mdn("Web/API/Event"),
            mdn("Web/API/EventTarget"),
            mdn("Learn_web_development/Core/Scripting/Events"),
            mdn("Web/API/Event/bubbles"),
        ],
    },
    "fetch-api": {
        "tags": ["fetch api", "fetch request", "http request browser", "abortcontroller", "fetch response"],
        "license": CC_BY_SA_25,
        "pages": [
            mdn("Web/API/Fetch_API"),
            mdn("Web/API/Fetch_API/Using_Fetch"),
            mdn("Web/API/Request"),
            mdn("Web/API/Response"),
            mdn("Web/API/AbortController"),
        ] + wiki("Ajax_(programming)"),
    },
    "web-storage": {
        "tags": ["web storage", "localstorage", "sessionstorage", "browser key-value storage"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "Web_storage",
        ) + [
            mdn("Web/API/Web_Storage_API"),
            mdn("Web/API/Window/localStorage"),
            mdn("Web/API/Window/sessionStorage"),
            mdn("Web/API/Storage"),
            mdn("Web/API/StorageEvent"),
        ],
    },
    "indexeddb": {
        "tags": ["indexeddb", "indexed database api", "client-side database", "object store"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "Indexed_Database_API",
        ) + [
            mdn("Web/API/IndexedDB_API"),
            mdn("Web/API/IndexedDB_API/Using_IndexedDB"),
            mdn("Web/API/IDBObjectStore"),
            mdn("Web/API/IDBDatabase"),
            mdn("Web/API/IDBTransaction"),
        ],
    },
    "websockets-browser": {
        "tags": ["websocket", "websocket client", "full-duplex browser", "realtime messaging", "server-sent events"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "WebSocket",
            "Server-sent_events",
        ) + [
            mdn("Web/API/WebSockets_API"),
            mdn("Web/API/WebSocket"),
            mdn("Web/API/WebSockets_API/Writing_WebSocket_client_applications"),
            mdn("Web/API/EventSource"),
        ],
    },
    "intersection-observer": {
        "tags": ["intersection observer", "lazy loading", "viewport visibility", "resize observer", "mutation observer"],
        "license": CC_BY_SA_25,
        "pages": [
            mdn("Web/API/Intersection_Observer_API"),
            mdn("Web/API/IntersectionObserver"),
            mdn("Web/API/ResizeObserver"),
            mdn("Web/API/MutationObserver"),
            mdn("Web/Performance/Lazy_loading"),
            mdn("Web/API/PerformanceObserver"),
        ],
    },
    "shadow-dom": {
        "tags": ["shadow dom", "shadow root", "attachshadow", "encapsulated dom", "template and slots"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "Web_Components",
        ) + [
            mdn("Web/API/Web_components/Using_shadow_DOM"),
            mdn("Web/API/ShadowRoot"),
            mdn("Web/API/Element/attachShadow"),
            mdn("Web/API/Web_components/Using_templates_and_slots"),
            mdn("Web/API/Element/slot"),
        ],
    },
    "css-variables": {
        "tags": ["css variables", "css custom properties", "css var function", "theming with css"],
        "license": CC_BY_SA_25,
        "pages": [
            mdn("Web/CSS/Using_CSS_custom_properties"),
            mdn("Web/CSS/var"),
            mdn("Web/CSS/env"),
            mdn("Web/CSS/CSS_cascade/Cascade"),
            mdn("Web/CSS/inherit"),
        ] + wiki("Cascading_Style_Sheets"),
    },
    "viewport-responsive": {
        "tags": ["viewport meta", "media queries", "responsive design", "viewport units", "breakpoints"],
        "license": CC_BY_SA_25,
        "pages": wiki(
            "Responsive_web_design",
        ) + [
            mdn("Web/CSS/Viewport_concepts"),
            mdn("Web/HTML/Guides/Viewport_meta_element"),
            mdn("Web/CSS/Media_Queries/Using_media_queries"),
            mdn("Web/CSS/@media"),
            mdn("Web/API/Window/matchMedia"),
        ],
    },
}
