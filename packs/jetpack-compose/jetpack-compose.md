---
title: "Jetpack Compose"
source: https://en.wikipedia.org/wiki/Jetpack_Compose
domain: jetpack-compose
license: CC-BY-SA-4.0
tags: jetpack compose, declarative ui, kotlin language, android development
fetched: 2026-07-02
---

# Jetpack Compose

**Jetpack Compose** is an open-source reactive user interface (UI) framework developed by Google for cross-platform software development in Kotlin. The first preview was announced in May 2019, and the framework was made ready for production in July 2021.

In Compose, a user interface is defined using functions that have been annotated with the `@Composable` annotation, which are known as composable functions and define the screen's state. Jetpack Compose uses a Kotlin compiler plugin to transform composable functions into UI elements. For example, the following code defines a simple UI element:

```mw
@Composable
fun Greeting(name: String) {
    Text(text = "Hello $name")
}
```

## History

The first preview of Jetpack Compose was announced at the Google I/O conference in May 2019. The developer preview was released in October 2019, and the alpha release occurred in August 2020.

Compose entered its beta phase in February 2021, with its first production release taking place that July.

## Features

Jetpack Compose supports Android 5.0 and later. It uses the Kotlin programming language, and provides a reactive programming model similar to other UI frameworks such as Flutter, Vue.js, and React Native. Compose is designed to integrate seamlessly with existing Android apps and libraries, allowing developers to gradually migrate their apps to Compose.

In Compose, a user interface is defined using functions that have been annotated with the `@Composable` annotation, which are known as composable functions and define the screen's state. The annotation is used by the Compose compiler to generate the UI boilerplate code. When the state is updated, composable functions are called again with new data, which causes the widgets they emit to be redrawn in a process known as recomposition. Recomposition is only performed for composable functions that need to be updated, which improves UI efficiency.

The 1.0 release introduced Compose Preview, which is built into Android Studio starting with Arctic Fox. It allows composables to be previewed using different configurations without deploying the app to a device.

Jetpack Glance is a Jetpack Compose-based framework for developing widgets for Android. Glance's first stable release occurred in September 2023.

In September 2024, the 1.0 stable version of the Jetpack Compose application programming interfaces (APIs) for building adaptive UIs with Material 3 was released.

## Use

When Jetpack Compose 1.0 was released, Google said, "There are already over 2,000 apps in the Play Store using Compose – in fact, the Play Store app itself uses Compose." As of October 2022, 16% of the top 1000 apps on the Play Store included Compose. The apps included those from companies such as Airbnb, Lyft, and Square. In May 2024, this number had grown to 40%.

In 2022, Google detailed how it utilized Jetpack Compose as part of its rewrite of the Play Store app, stating that "writing UI requires much less code, sometimes up to 50%" and that the developers were able to improve the app's performance. Google rewrote parts of Android's Settings app using Jetpack Compose in Android 14. Meta Platforms developed its Threads social media app in five months using Jetpack Compose. The Instagram for Android app has also been written using Jetpack Compose.

## Compose Multiplatform

*Compose Multiplatform* is a multi-platform UI framework developed by JetBrains and based on Jetpack Compose. It is a port of Jetpack Compose for Windows, macOS, Linux, and the web. Version 1.0 alpha was released in August 2021. iOS support was added in May 2023.
