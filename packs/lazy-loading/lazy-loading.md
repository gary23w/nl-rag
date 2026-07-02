---
title: "Lazy loading"
source: https://en.wikipedia.org/wiki/Lazy_loading
domain: lazy-loading
license: CC-BY-SA-4.0
tags: lazy loading images, intersection observer, loading attribute, deferred asset loading
fetched: 2026-07-02
---

# Lazy loading

**Lazy loading** (also known as **asynchronous loading**) is a technique used in computer programming, especially web design and web development, to defer initialization of an object until it is needed. It can contribute to efficiency in the program's operation if properly and appropriately used. This makes it ideal in use cases where network content is accessed and initialization times are to be kept at a minimum, such as in the case of web pages. For example, deferring loading of images on a web page until they are needed for viewing can make the initial display of the web page faster. The opposite of lazy loading is **eager loading**.

## Examples

### With web frameworks

Prior to being established as a web standard, web frameworks were generally used to implement lazy loading.

One of these is Angular. Since lazy loading decreases bandwidth and subsequently server resources, it is a strong contender to implement in a website, especially in order to improve user retention by having less delay when loading the page, which may also improve search engine optimization (SEO).

Below is an example of lazy loading being used in Angular, programmed in TypeScript, from Farata Systems

```mw
@NgModule({
  imports: [ BrowserModule,
    RouterModule.forRoot([
      {path: '',        component: HomeComponent},
      {path: 'product', component: ProductDetailComponent},

      {path: 'luxury', loadChildren: () => import('./luxury.module').then(m => m.LuxuryModule), data: {preloadme: true} } ]
//      , {preloadingStrategy: CustomPreloadingStrategy}
      )
  ],
  declarations: [ AppComponent, HomeComponent, ProductDetailComponent],
  providers:[{provide: LocationStrategy, useClass: HashLocationStrategy}, CustomPreloadingStrategy],
  bootstrap:    [ AppComponent ]
})
```

### As a web standard

Since 2020, major web browsers have enabled native handling of lazy loading by default.

This allows lazy loading to be incorporated into a webpage by adding HTML attributes.

The `loading` attribute support two values, `lazy` and `eager`. Setting the value to `lazy` will fetch the resource only when it is required (such as when an image scrolls into view when a user scrolls down), while setting it to `eager`, the default state, the resource will be immediately loaded.

```mw
<!-- These resources will be loaded immediately -->
<img src="header_image.jpg">
<img src="header_image2.jpg" loading="eager">

<!-- While these resources will be lazy loaded -->
<img src="article_image.jpg" alt="..." loading="lazy"> 
<iframe src="video-player.html" title="..." loading="lazy"></iframe>
```

## Methods

There are four common ways of implementing the lazy load design pattern: *lazy initialization*; a *virtual proxy*; a *ghost*, and a *value holder*. Each has its own advantages and disadvantages.

### Lazy initialization

With lazy initialization, the object is first set to `null`.

Whenever the object is requested, the object is checked, and if it is `null`, the object is then immediately created and returned.

For example, lazy loading for a widget can be implemented in the C# programming language as such:

```mw
private int _myWidgetID;
private Widget _myWidget = null;

public Widget MyWidget
{
    get
    {
        if (_myWidget == null)
        {
            _myWidget = Widget.Load(_myWidgetID);
        }

        return _myWidget;
    }
}
```

Or alternatively, with the null-coalescing assignment operator `??=`

```mw
private int _myWidgetID;
private Widget _myWidget = null;

public Widget MyWidget
{
    get => _myWidget ??= Widget.Load(_myWidgetID);
}
```

This method is the simplest to implement, although if `null` is a legitimate return value, it may be necessary to use a placeholder object to signal that it has not been initialized. If this method is used in a multithreaded application, synchronization must be used to avoid race conditions.

### Virtual proxy

A virtual proxy is an object with the same interface as the real object. The first time one of its methods is called it loads the real object and then delegates.

### Ghost

A *ghost* is the object that is to be loaded in a partial state. It may initially only contain the object's identifier, but it loads its own data the first time one of its properties is accessed. For example, consider that a user is about to request content via an online form. At the time of creation, the only information available is that content will be accessed, but the specific action and content is unknown.

An example in PHP:

```mw
$userData = array (
    "UID" = > uniqid(),
    "requestTime" => microtime(true),
    "dataType" => "",
    "request" => ""
);

if (isset($_POST['data']) && $userData) {
    // ...
}
```

### Value holder

A *value holder* is a generic object that handles the lazy loading behavior, and appears in place of the object's data fields:

```mw
private ValueHolder<Widget> valueHolder;

public Widget MyWidget => valueHolder.GetValue();
```
