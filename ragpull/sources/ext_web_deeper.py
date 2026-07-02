"""Advanced web platform: performance, security, rendering strategies, i18n, SEO."""
from .common import CC_BY_SA, CC_BY_SA_25, WIKI, mdn, wiki

DOMAINS = {
    "content-security-policy": {
        "tags": ["content security policy", "csp header", "xss mitigation", "script-src directive", "default-src fallback"],
        "license": CC_BY_SA,
        "pages": wiki("Content_Security_Policy", "Cross-site_scripting")
        + [mdn("Web/HTTP/Guides/CSP"),
           mdn("Web/HTTP/Reference/Headers/Content-Security-Policy"),
           mdn("Web/HTTP/Reference/Headers/Content-Security-Policy/script-src"),
           mdn("Web/HTTP/Reference/Headers/Content-Security-Policy/default-src")],
    },
    "subresource-integrity": {
        "tags": ["subresource integrity", "integrity attribute", "cdn tamper protection", "cryptographic hash digest"],
        "license": CC_BY_SA,
        "pages": wiki("Subresource_Integrity", "Cryptographic_hash_function", "SHA-2")
        + [mdn("Web/HTML/Reference/Elements/script"),
           mdn("Web/HTML/Attributes/crossorigin"),
           mdn("Web/API/SubtleCrypto/digest")],
    },
    "cross-origin-resource-sharing": {
        "tags": ["cross-origin resource sharing", "cors preflight request", "access-control-allow-origin header", "credentialed cross-origin request"],
        "license": CC_BY_SA,
        "pages": wiki("Cross-origin_resource_sharing")
        + [mdn("Web/HTTP/Guides/CORS"),
           mdn("Web/HTTP/Reference/Headers/Access-Control-Allow-Origin"),
           mdn("Web/HTTP/Reference/Headers/Access-Control-Allow-Credentials"),
           mdn("Web/HTTP/Guides/CORS/Errors"),
           mdn("Web/API/Request/mode")],
    },
    "same-origin-policy": {
        "tags": ["same-origin policy", "web origin model", "cross-origin isolation", "document domain property"],
        "license": CC_BY_SA,
        "pages": wiki("Same-origin_policy")
        + [mdn("Glossary/Origin"),
           mdn("Web/API/Location"),
           mdn("Web/API/Window/origin"),
           mdn("Web/API/URL"),
           mdn("Web/API/Document/domain")],
    },
    "cross-site-scripting-defense": {
        "tags": ["cross-site scripting", "xss attack vector", "html output encoding", "cross-site request forgery"],
        "license": CC_BY_SA,
        "pages": wiki("Cross-site_scripting", "Cross-site_request_forgery", "Session_hijacking")
        + [mdn("Web/Security/Types_of_attacks"),
           mdn("Web/HTTP/Reference/Headers/X-Content-Type-Options"),
           mdn("Web/Security/Practical_implementation_guides")],
    },
    "clickjacking-defense": {
        "tags": ["clickjacking defense", "x-frame-options header", "ui redress attack", "frame busting script"],
        "license": CC_BY_SA,
        "pages": wiki("Clickjacking", "Framekiller")
        + [mdn("Web/HTTP/Reference/Headers/X-Frame-Options"),
           mdn("Web/CSS/pointer-events"),
           mdn("Web/HTML/Reference/Elements/iframe"),
           mdn("Web/HTTP/Reference/Headers/Referrer-Policy")],
    },
    "http-strict-transport-security": {
        "tags": ["http strict transport security", "hsts header", "https enforcement", "transport layer security"],
        "license": CC_BY_SA,
        "pages": wiki("HTTP_Strict_Transport_Security", "HTTPS", "Transport_Layer_Security")
        + [mdn("Web/HTTP/Reference/Headers/Strict-Transport-Security"),
           mdn("Glossary/HSTS"),
           mdn("Web/HTTP/Reference/Headers/X-Content-Type-Options")],
    },
    "secure-cookies": {
        "tags": ["secure cookie flag", "httponly cookie", "samesite attribute", "set-cookie header"],
        "license": CC_BY_SA,
        "pages": wiki("Secure_cookie", "HTTP_cookie")
        + [mdn("Web/HTTP/Guides/Cookies"),
           mdn("Web/HTTP/Reference/Headers/Set-Cookie"),
           mdn("Web/API/Document/cookie"),
           mdn("Web/HTTP/Guides/Session")],
    },
    "web-authentication-api": {
        "tags": ["web authentication api", "webauthn passkey", "public key credential", "multi-factor authentication"],
        "license": CC_BY_SA,
        "pages": wiki("WebAuthn", "FIDO2_Project", "Multi-factor_authentication")
        + [mdn("Web/API/Web_Authentication_API"),
           mdn("Web/API/CredentialsContainer"),
           mdn("Web/API/PublicKeyCredential")],
    },
    "core-web-vitals": {
        "tags": ["core web vitals", "largest contentful paint", "cumulative layout shift", "performance observer entry"],
        "license": CC_BY_SA,
        "pages": wiki("Web_performance")
        + [mdn("Web/Performance"),
           mdn("Web/API/Largest_Contentful_Paint_API"),
           mdn("Web/API/Layout_Instability_API"),
           mdn("Web/API/LargestContentfulPaint"),
           mdn("Web/API/LayoutShift")],
    },
    "lighthouse-audit": {
        "tags": ["lighthouse audit", "navigation timing api", "resource timing api", "user timing marks"],
        "license": CC_BY_SA,
        "pages": wiki("Google_Lighthouse")
        + [mdn("Web/API/Navigation_timing_API"),
           mdn("Web/API/Resource_Timing_API"),
           mdn("Web/API/User_Timing_API"),
           mdn("Web/API/PerformanceObserver"),
           "https://developer.chrome.com/docs/lighthouse/overview"],
    },
    "critical-rendering-path": {
        "tags": ["critical rendering path", "browser rendering engine", "document object model", "css object model"],
        "license": CC_BY_SA,
        "pages": wiki("Web_browser_engine")
        + [mdn("Web/Performance/Critical_rendering_path"),
           mdn("Web/Performance/How_browsers_work"),
           mdn("Web/API/Document_Object_Model"),
           mdn("Web/API/CSS_Object_Model"),
           mdn("Web/CSS/content-visibility")],
    },
    "lazy-loading": {
        "tags": ["lazy loading images", "intersection observer", "loading attribute", "deferred asset loading"],
        "license": CC_BY_SA,
        "pages": wiki("Lazy_loading")
        + [mdn("Web/CSS/content-visibility"),
           mdn("Web/HTML/Element/img"),
           mdn("Web/API/IntersectionObserver"),
           mdn("Web/API/HTMLImageElement/loading"),
           mdn("Web/API/HTMLImageElement/decoding")],
    },
    "code-splitting": {
        "tags": ["code splitting", "dynamic import expression", "javascript module bundle", "on-demand chunk loading"],
        "license": CC_BY_SA,
        "pages": wiki("Bundle_(software_distribution)", "Dynamic_loading")
        + [mdn("Web/JavaScript/Guide/Modules"),
           mdn("Web/JavaScript/Reference/Operators/import"),
           mdn("Web/JavaScript/Reference/Operators/import.meta"),
           mdn("Web/HTML/Reference/Elements/script/type/importmap")],
    },
    "tree-shaking": {
        "tags": ["tree shaking", "dead code elimination", "es module exports", "code minification"],
        "license": CC_BY_SA,
        "pages": wiki("Tree_shaking", "Dead_code_elimination", "Minification_(programming)")
        + [mdn("Web/JavaScript/Guide/Modules"),
           mdn("Web/JavaScript/Reference/Statements/export"),
           mdn("Web/JavaScript/Reference/Statements/import")],
    },
    "resource-hints": {
        "tags": ["resource hints", "rel preload", "rel preconnect", "dns prefetch link"],
        "license": CC_BY_SA,
        "pages": [mdn("Web/HTML/Attributes/rel"),
                  mdn("Web/HTML/Attributes/rel/preload"),
                  mdn("Web/HTML/Attributes/rel/preconnect"),
                  mdn("Web/HTML/Attributes/rel/prefetch"),
                  mdn("Web/HTML/Attributes/rel/dns-prefetch"),
                  mdn("Web/HTML/Reference/Elements/link")],
    },
    "http-caching-strategies": {
        "tags": ["http caching strategies", "cache-control header", "etag validation", "web cache freshness"],
        "license": CC_BY_SA,
        "pages": wiki("Web_cache")
        + [mdn("Web/HTTP/Guides/Caching"),
           mdn("Web/HTTP/Reference/Headers/Cache-Control"),
           mdn("Web/HTTP/Headers/ETag"),
           mdn("Web/HTTP/Reference/Headers/Vary"),
           mdn("Web/HTTP/Reference/Headers/Age")],
    },
    "service-worker-caching": {
        "tags": ["service worker caching", "cache storage api", "offline first strategy", "fetch interception"],
        "license": CC_BY_SA,
        "pages": wiki("Service_worker")
        + [mdn("Web/API/Service_Worker_API"),
           mdn("Web/API/Cache"),
           mdn("Web/API/CacheStorage"),
           mdn("Web/Progressive_web_apps/Guides/Caching"),
           mdn("Web/API/Fetch_API")],
    },
    "image-optimization-web": {
        "tags": ["image optimization", "responsive picture element", "webp image format", "avif image format"],
        "license": CC_BY_SA,
        "pages": wiki("Image_compression", "WebP", "AVIF")
        + [mdn("Web/Media/Formats/Image_types"),
           mdn("Web/HTML/Element/picture"),
           mdn("Web/HTML/Element/img")],
    },
    "font-loading-strategy": {
        "tags": ["web font loading", "font-display swap", "font face rule", "css font loading api"],
        "license": CC_BY_SA,
        "pages": wiki("Web_typography", "Web_Open_Font_Format")
        + [mdn("Web/CSS/@font-face"),
           mdn("Web/CSS/@font-face/font-display"),
           mdn("Web/API/CSS_Font_Loading_API"),
           mdn("Web/API/FontFace")],
    },
    "server-side-rendering-web": {
        "tags": ["server side rendering", "client side hydration", "dynamic web page", "server-side scripting"],
        "license": CC_BY_SA,
        "pages": wiki("Server-side_scripting", "Dynamic_web_page", "Hydration_(web_development)")
        + [mdn("Glossary/SSR"),
           mdn("Web/Guide/AJAX"),
           mdn("Web/API/Streams_API")],
    },
    "static-site-generation": {
        "tags": ["static site generation", "static web page", "web template system", "prerendered html output"],
        "license": CC_BY_SA,
        "pages": wiki("Static_site_generator", "Static_web_page", "Web_template_system", "Single-source_publishing")
        + [mdn("Glossary/SSG"),
           mdn("Web/HTML/Reference/Elements/template")],
    },
    "edge-rendering": {
        "tags": ["edge rendering", "content delivery network", "edge computing", "serverless function compute"],
        "license": CC_BY_SA,
        "pages": wiki("Content_delivery_network", "Edge_computing", "Serverless_computing", "Function_as_a_service")
        + [mdn("Glossary/CDN"),
           mdn("Web/API/Streams_API/Using_readable_streams")],
    },
    "micro-frontends": {
        "tags": ["micro frontends", "frontend composition", "separation of concerns", "iframe isolation boundary"],
        "license": CC_BY_SA,
        "pages": wiki("Micro_frontend", "Separation_of_concerns", "Front_and_back_ends")
        + [mdn("Web/API/Web_components"),
           mdn("Web/API/HTMLIFrameElement"),
           mdn("Web/HTML/Element/iframe")],
    },
    "module-federation": {
        "tags": ["module federation", "modular programming", "loose coupling", "javascript module system"],
        "license": CC_BY_SA,
        "pages": wiki("Modular_programming", "Loose_coupling", "Decoupling")
        + [mdn("Web/JavaScript/Guide/Modules"),
           mdn("Web/JavaScript/Reference/Statements/export"),
           mdn("Web/JavaScript/Reference/Operators/import")],
    },
    "jamstack": {
        "tags": ["jamstack architecture", "prebuilt markup delivery", "client side rendering", "web development workflow"],
        "license": CC_BY_SA,
        "pages": wiki("Static_site_generator", "Web_development", "Web_framework")
        + [mdn("Web/API/Fetch_API/Using_Fetch"),
           mdn("Glossary/SSG"),
           mdn("Web/API/Fetch_API")],
    },
    "headless-architecture": {
        "tags": ["headless content management", "decoupled cms backend", "rest api backend", "graphql data layer"],
        "license": CC_BY_SA,
        "pages": wiki("Headless_content_management_system", "Content_management_system",
                      "Representational_state_transfer", "GraphQL", "Web_API")
        + [mdn("Web/API/Fetch_API/Using_Fetch")],
    },
    "web-internationalization": {
        "tags": ["web internationalization", "ecmascript intl api", "language attribute tag", "locale-aware formatting"],
        "license": CC_BY_SA,
        "pages": wiki("Internationalization_and_localization", "IETF_language_tag")
        + [mdn("Web/JavaScript/Reference/Global_Objects/Intl"),
           mdn("Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat"),
           mdn("Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat"),
           mdn("Web/HTML/Global_attributes/lang")],
    },
    "localization-i18n": {
        "tags": ["software localization", "language localisation", "plural rules formatting", "relative time formatting"],
        "license": CC_BY_SA,
        "pages": wiki("Language_localisation", "Pseudolocalization", "Language_code")
        + [mdn("Web/JavaScript/Reference/Global_Objects/Intl/PluralRules"),
           mdn("Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat"),
           mdn("Web/JavaScript/Reference/Global_Objects/Intl/Locale")],
    },
    "unicode-bidi-web": {
        "tags": ["bidirectional text", "unicode bidi property", "right-to-left script", "writing mode direction"],
        "license": CC_BY_SA,
        "pages": wiki("Bidirectional_text", "Right-to-left_script", "Unicode")
        + [mdn("Web/CSS/direction"),
           mdn("Web/CSS/unicode-bidi"),
           mdn("Web/CSS/writing-mode"),
           mdn("Web/HTML/Element/bdi"),
           mdn("Web/HTML/Element/bdo")],
    },
    "search-engine-optimization": {
        "tags": ["search engine optimization", "meta description tag", "canonical link relation", "web crawler indexing"],
        "license": CC_BY_SA,
        "pages": wiki("Search_engine_optimization", "Meta_element", "Web_crawler", "URL_canonicalization")
        + [mdn("Glossary/SEO"),
           mdn("Web/API/HTMLLinkElement/rel")],
    },
    "structured-data-schema": {
        "tags": ["structured data markup", "schema microdata", "json-ld linked data", "rdfa annotation"],
        "license": CC_BY_SA,
        "pages": wiki("Structured_data", "Microdata_(HTML)", "JSON-LD", "RDFa", "Schema.org")
        + [mdn("Web/HTML/Global_attributes/itemtype"),
           mdn("Web/HTML/Microdata")],
    },
    "open-graph-protocol": {
        "tags": ["open graph protocol", "social sharing metadata", "meta property tags", "link preview cards"],
        "license": CC_BY_SA,
        "pages": wiki("Open_Graph_protocol", "Facebook_Platform", "Metadata", "Meta_element")
        + [mdn("Web/HTML/Element/meta"),
           mdn("Web/HTML/Reference/Elements/head")],
    },
    "sitemap-xml": {
        "tags": ["xml sitemap", "site map index", "crawler discovery", "structured url listing"],
        "license": CC_BY_SA,
        "pages": wiki("Sitemaps", "Site_map", "XML", "Web_crawler", "Google_Search_Console")
        + [mdn("Glossary/SEO")],
    },
    "robots-txt": {
        "tags": ["robots exclusion standard", "robots txt file", "crawler directives", "noindex directive", "nofollow link"],
        "license": CC_BY_SA,
        "pages": wiki("Robots.txt", "Robots_exclusion_standard", "Noindex", "Nofollow", "Meta_refresh")
        + [mdn("Web/HTTP/Headers/X-Robots-Tag")],
    },
    "web-vitals-monitoring": {
        "tags": ["web vitals monitoring", "performance entry timeline", "performance mark measure", "user timing metrics"],
        "license": CC_BY_SA,
        "pages": wiki("Web_performance")
        + [mdn("Web/API/Performance_API"),
           mdn("Web/API/PerformanceEntry"),
           mdn("Web/API/Performance/mark"),
           mdn("Web/API/Performance/measure"),
           mdn("Web/API/PerformancePaintTiming")],
    },
    "real-user-monitoring": {
        "tags": ["real user monitoring", "beacon api reporting", "website monitoring", "field performance data", "web analytics collection"],
        "license": CC_BY_SA,
        "pages": wiki("Real_user_monitoring", "Website_monitoring", "Web_analytics")
        + [mdn("Web/API/Beacon_API"),
           mdn("Web/API/Navigator/sendBeacon"),
           mdn("Web/API/PerformanceObserver")],
    },
    "synthetic-monitoring": {
        "tags": ["synthetic monitoring", "scripted uptime probe", "website availability check", "lab performance measurement"],
        "license": CC_BY_SA,
        "pages": wiki("Synthetic_monitoring", "Website_monitoring", "Web_performance")
        + [mdn("Web/API/Navigation_timing_API"),
           mdn("Web/API/PerformanceNavigationTiming"),
           mdn("Web/API/PerformanceResourceTiming")],
    },
    "single-page-application": {
        "tags": ["single-page application", "history api routing", "client side navigation", "popstate event handling"],
        "license": CC_BY_SA,
        "pages": wiki("Single-page_application", "Ajax_(programming)")
        + [mdn("Web/API/History_API"),
           mdn("Web/API/History"),
           mdn("Web/API/Window/popstate_event"),
           mdn("Web/API/Navigation_API")],
    },
    "progressive-enhancement": {
        "tags": ["progressive enhancement", "graceful degradation", "feature detection strategy", "layered web experience"],
        "license": CC_BY_SA,
        "pages": wiki("Progressive_enhancement", "Graceful_degradation", "Responsive_web_design")
        + [mdn("Glossary/Progressive_Enhancement"),
           mdn("Web/API/Fetch_API"),
           mdn("Web/JavaScript/Guide/Modules")],
    },
    "responsive-images": {
        "tags": ["responsive images", "srcset image candidates", "image-set css function", "adaptive image sizes"],
        "license": CC_BY_SA,
        "pages": wiki("Responsive_web_design")
        + [mdn("Web/HTML/Guides/Responsive_images"),
           mdn("Web/CSS/image-set"),
           mdn("Web/API/HTMLImageElement/sizes"),
           mdn("Web/API/HTMLImageElement/srcset"),
           mdn("Web/API/HTMLImageElement/currentSrc")],
    },
    "viewport-meta": {
        "tags": ["viewport meta tag", "mobile viewport scaling", "css viewport concepts", "device width layout", "media query breakpoints"],
        "license": CC_BY_SA,
        "pages": wiki("Viewport")
        + [mdn("Web/HTML/Guides/Viewport_meta_element"),
           mdn("Web/CSS/Viewport_concepts"),
           mdn("Web/CSS/@media"),
           mdn("Web/CSS/CSS_media_queries/Using_media_queries"),
           mdn("Learn_web_development/Core/CSS_layout/Responsive_Design")],
    },
    "web-components-advanced": {
        "tags": ["web components", "custom element registry", "shadow dom encapsulation", "reusable web widgets"],
        "license": CC_BY_SA,
        "pages": wiki("Web_Components")
        + [mdn("Web/API/Web_components"),
           mdn("Web/API/Web_components/Using_custom_elements"),
           mdn("Web/API/Web_components/Using_shadow_DOM"),
           mdn("Web/API/Web_components/Using_templates_and_slots"),
           mdn("Web/API/ShadowRoot")],
    },
    "custom-elements": {
        "tags": ["custom elements", "custom element registry", "autonomous html element", "define web component"],
        "license": CC_BY_SA,
        "pages": [mdn("Web/API/CustomElementRegistry"),
                  mdn("Web/API/CustomElementRegistry/define"),
                  mdn("Web/API/Window/customElements"),
                  mdn("Web/API/HTMLElement"),
                  mdn("Web/API/Web_components/Using_custom_elements"),
                  mdn("Web/API/Window")],
    },
    "html-templates": {
        "tags": ["html template element", "content slot projection", "document fragment reuse", "declarative markup template"],
        "license": CC_BY_SA,
        "pages": [mdn("Web/HTML/Element/template"),
                  mdn("Web/API/HTMLTemplateElement"),
                  mdn("Web/HTML/Element/slot"),
                  mdn("Web/API/HTMLSlotElement"),
                  mdn("Web/API/DocumentFragment"),
                  mdn("Web/API/ShadowRoot")],
    },
    "css-container-queries": {
        "tags": ["css container queries", "container type property", "container-name selector", "at-container query rule"],
        "license": CC_BY_SA,
        "pages": [mdn("Web/CSS/CSS_containment/Container_queries"),
                  mdn("Web/CSS/@container"),
                  mdn("Web/CSS/container-type"),
                  mdn("Web/CSS/container-name"),
                  mdn("Web/CSS/container"),
                  mdn("Web/CSS/contain")],
    },
    "css-cascade-layers": {
        "tags": ["css cascade layers", "at-layer rule", "cascade specificity ordering", "layered style precedence"],
        "license": CC_BY_SA,
        "pages": [mdn("Web/CSS/@layer"),
                  mdn("Web/CSS/CSS_cascade"),
                  mdn("Web/CSS/Cascade"),
                  mdn("Web/CSS/Specificity"),
                  mdn("Web/CSS/revert-layer"),
                  mdn("Web/API/CSSLayerBlockRule")],
    },
    "css-houdini": {
        "tags": ["css houdini apis", "css painting worklet", "css properties and values api", "registered custom property"],
        "license": CC_BY_SA,
        "pages": [mdn("Web/API/Houdini_APIs"),
                  mdn("Web/API/CSS_Painting_API"),
                  mdn("Web/API/CSS_Properties_and_Values_API"),
                  mdn("Web/API/CSS/registerProperty_static"),
                  mdn("Web/API/Worklet"),
                  mdn("Web/CSS/@property")],
    },
    "view-transitions-api": {
        "tags": ["view transitions api", "start view transition", "view-transition-name property", "animated dom state change"],
        "license": CC_BY_SA,
        "pages": [mdn("Web/API/View_Transitions_API"),
                  mdn("Web/API/Document/startViewTransition"),
                  mdn("Web/API/ViewTransition"),
                  mdn("Web/CSS/::view-transition"),
                  mdn("Web/CSS/view-transition-name"),
                  mdn("Web/CSS/@view-transition")],
    },
}
