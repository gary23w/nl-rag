---
title: "Vaadin"
source: https://en.wikipedia.org/wiki/Vaadin
domain: vaadin-flow
license: CC-BY-SA-4.0
tags: vaadin flow framework, java server side ui, jvm web components, vaadin component model
fetched: 2026-07-02
---

# Vaadin

**Vaadin** (Finnish pronunciation: [ˈʋɑːdin]) is an open-source web application development platform for Java. Vaadin includes a set of Web Components, a Java web framework, and a set of tools that enable developers to implement modern web graphical user interfaces (GUI) using the Java programming language only (instead of HTML and JavaScript), TypeScript only, or a combination of both.

## History

Development began as the Millstone web framework in 2000. It was first released as open-source in 2002. Millstone introduced a component-oriented programming model for the web and an Ajax-based client communication and rendering engine. As a result, a large part of Vaadin's server-side API remains compatible with Millstone's Swing-like APIs.

In early 2007 the product name was changed to IT Mill Toolkit and version 4 was released. It used a proprietary JavaScript Ajax-implementation for the client-side rendering, which made it rather complicated to implement new widgets. By the end of the year 2007 the proprietary client-side implementation was abandoned and GWT was integrated on top of the server-side components. At the same time, the product license was changed to the open source Apache License 2.0. The first production-ready release of IT Mill Toolkit 5 was made on March 4, 2009, after an over one year beta period.

On September 11, 2008, it was publicly announced that Michael Widenius–the main author of the original version of MySQL–invested in IT Mill, the Finnish developer of Vaadin. The size of the investment is undisclosed.

On May 20, 2009, IT Mill Toolkit changed its name to Vaadin Framework. The name originates from the Finnish word for doe, more precisely put, a female reindeer. It can also be translated from Finnish as "I insist". In addition to the name change, a pre-release of version 6 along with a community website was launched. Later, IT Mill Ltd, the company behind the open source Vaadin Framework, changed its name to Vaadin Ltd.

On March 30, 2010, Vaadin Directory was opened. It added a channel for distributing add-on components to the core Vaadin Framework, both for free or commercially. On launch date, there were 95 add-ons already available for download.

| LTS Version | Release date | Notes and new features since the previous LTS version launch |
|---|---|---|
| 6 | 20 May 2009 | Initial release |
| 7 | 3 February 2013 |   |
| 8 | 21 February 2017 | Improvements include a re-written data binding API that uses modern Java features such as type parameters and lambda expressions, and more efficient memory and CPU usage. |
| 10 | 25 June 2018 | It's possible to use Vaadin's UI components from any technology compatible with Web Components. Vaadin Directory adds Web Components distribution. Vaadin Flow—the next generation of Vaadin Framework—was presented as a server-side Java web framework on top of Vaadin's UI components. |
| 14 | 14 August 2019 | New UI components, CDI and OSGi support, Gradle integration, dynamic registration of routes, keyboard shortcuts API, support for npm and Bower. |
| 23 | 1 March 2022 | New release model. New UI components, reworked design system, feature flags, npm is now the default package manager. |
| 24 | 8 March 2023 | Java 17 baseline along with Spring Boot 3 and Jakarta EE 10. The free version no longer supports Polymer templates, and Lit-templateshave been introduced as a replacement. |
| 25 | 17 December 2025 | Java 21 baseline along with Spring Boot 4 and Jakarta EE 11. New Aura theme , Tailwind CSS support, improved React integration, and development time tooling in Vaadin Copilot. |

## Vaadin Flow (Java API)

**Vaadin Flow** (formerly **Vaadin Framework**) is a Java web framework for building web applications and websites. Vaadin Flow's programming model allows developers to use Java as the programming language for implementing User Interfaces (UIs) without having to directly use HTML or JavaScript. Vaadin Flow features a server-side architecture which means that most of the UI logic runs securely on the server reducing the exposure to attackers. On the client-side, Vaadin Flow is built on top of Web Component standards. The client/server communication is automatically handled through WebSocket or HTTP with light JSON messages that update both, the UI in the browser and the UI state in the server.

Vaadin Flow's Java API includes classes such as `TextField`, `Button`, `ComboBox`, `Grid`, and many others that can be configured, styled, and added into layout objects instances of classes such as `VerticalLayout`, `HorizontalLayout`, `SplitLayout`, and others. Behaviour is implemented by adding listeners to events such as clicks, input value changes, and others. Views are created by custom Java classes that implement another UI component (custom or provided by the framework). This view classes are annotated with `@Route` to expose them to the browser with a specific URL. The following example illustrates these concepts:

```mw
@Route("hello-world") // exposes the view through http://localhost:8080/hello-world
public class MainView extends VerticalLayout { // extends an existing UI component

    public MainView() {
        // creates a text field
        TextField textField = new TextField("Enter your name");

        // creates a button
        Button button = new Button("Send");
        
        // adds behaviour to the button using the click event
        button.addClickListener(event ->
                add(new Paragraph("Hello, " + textField.getValue()))
        );

        // adds the UI components to the view (VerticalLayout)
        add(textField, button);
    }
}
```

The following is a screenshot of the previous example:

## Hilla (TypeScript API)

**Hilla** (formerly **Vaadin Fusion**) is a web framework that integrates Spring Boot Java backends with reactive front ends implemented in TypeScript. This combination offers a fully type-safe development platform by combining server-side business logic in Java and type-safety in the client side with the TypeScript programming language. Views are implemented using Lit—a lightweight library for creating Web Components. The following is an example of a basic view implemented with Hilla:

```mw
@customElement('hello-world-view')
export class HelloWorldView extends LitElement {
  render() {
    return html`
      <div>
        <vaadin-text-field label="Your name"></vaadin-text-field>
        <vaadin-button @click="${this.sayHello}">Say hello</vaadin-button>
      </div>
    `;
  }

  sayHello() {
    showNotification('Hello!');
  }
}
```

Starting in October 2025, Hilla is being discontinued as a stand-alone product and merged into Flow.

## Vaadin's UI components

Vaadin includes a set of User Interface (UI) components implemented as Web Components. These components include a server-side Java API (Vaadin Flow) but can also be used directly in HTML documents as well. Vaadin's UI components work with mouse and touch events, can be customized with CSS, are compatible with WAI-ARIA, include keyboard and screen readers support, and support right-to-left languages.

The following table shows a list of the UI components included in Vaadin:

| Java class | HTML element name | Description | License |
|---|---|---|---|
| `Accordion` | `vaadin-accordion` | A vertically stacked set of expandable panels | Apache 2.0 |
| `Anchor` | `a` | Allows navigation to a given URL | Apache 2.0 |
| `AppLayout` | `vaadin-app-layout` | A common application layout structure | Apache 2.0 |
| `Avatar` | `vaadin-avatar` | A graphical representation of a person | Apache 2.0 |
| (not available) | `vaadin-badge` | A coloured text element for labelling content | Apache 2.0 |
| `Board` | `vaadin-board-row` | Layout component for building responsive views | Commercial |
| `Button` | `vaadin-button` | Allows users to perform actions | Apache 2.0 |
| `Crud` | `vaadin-crud` | A component to manage Create, Read, Update, and Delete operations | Commercial |
| `Chart` | `vaadin-chart` | Interactive charts with different types such as bar, pie, line, and others | Commercial |
| `Checkbox` | `vaadin-checkbox` | An input field representing a binary choice | Apache 2.0 |
| `Combo box` | `vaadin-combo-box` | Shows a list of items that can be filtered | Apache 2.0 |
| `ConfirmDialog` | `vaadin-confirm-dialog` | A modal Dialog used to confirm user actions | Apache 2.0 |
| `ContextMenu` | `vaadin-context-menu` | A menu that appears on right-click or long touch press | Apache 2.0 |
| `CookieConsent` | `vaadin-cookie-consent` | A banner that to comply with privacy laws such as GDPR and CCPA | Commercial |
| `CustomField` | `vaadin-custom-field` | A component for wrapping multiple components as a single field | Apache 2.0 |
| `DatePicker` | `vaadin-date-picker` | Allows to enter a date by typing or by selecting from a calendar overlay | Apache 2.0 |
| `DateTimePicker` | `vaadin-date-time-picker` | An input field for selecting both a date and a time | Apache 2.0 |
| `Details` | `vaadin-details` | An expandable panel for showing and hiding content | Apache 2.0 |
| `Dialog` | `vaadin-dialog` | A popup window to show other components in an overlay | Apache 2.0 |
| `EmailField` | `vaadin-email-field` | A text field that only accepts email addresses as input | Apache 2.0 |
| `Form layout` | `vaadin-form-layout` | A layout for building responsive forms with multiple columns | Apache 2.0 |
| `Grid` | `vaadin-grid` | Data grid or data table component for tabular data | Apache 2.0 |
| `GridPro` | `vaadin-grid-pro` | Provides inline editing with full keyboard navigation | Commercial |
| `HorizontalLayout` | `vaadin-horizontal-layout` | Places components side-by-side in a row | Apache 2.0 |
| `Icon` | `iron-icon` | Shows a custom icon or from a collection of 600+ icons (`VaadinIcons` enum) | Apache 2.0 |
| `Image` | `img` | Shows an image from a resource file or from binary data generated at runtime | Apache 2.0 |
| `ListBox` | `vaadin-list-box` | Allows to select one or more values from a scrollable list of items | Apache 2.0 |
| `LoginForm` | `vaadin-login-form` | A component that contains a login form | Apache 2.0 |
| `LoginOverlay` | `vaadin-login-overlay` | A modal or full-screen login form | Apache 2.0 |
| `MenuBar` | `vaadin-menu-bar` | A horizontal button bar with hierarchical drop-down menus | Apache 2.0 |
| `MessageList` | `vaadin-message-list` | A component for displaying messages and building chats and comment sections | Apache 2.0 |
| `Notification` | `vaadin-notification` | Overlay component used to provide feedback to the user | Apache 2.0 |
| `NumberField` | `vaadin-number-field` | A text field that only accepts numeric input (decimal, integral, or big decimal) | Apache 2.0 |
| `PasswordField` | `vaadin-password-field` | An input field for entering passwords masked by default | Apache 2.0 |
| `ProgressBar` | `vaadin-progress-bar` | Shows the completion status of a task or process | Apache 2.0 |
| `Radio button` | `vaadin-radio-button` | Allows to select exactly one value from a list of related but mutually exclusive options | Apache 2.0 |
| `RichTextEditor` | `vaadin-rich-text-editor` | An input field for entering rich text | Commercial |
| `Scroller` | `vaadin-scroller` | A component container for creating scrollable areas in the UI | Apache 2.0 |
| `Select` | `vaadin-select` | An input field component for choosing a single value from a set of options | Apache 2.0 |
| `SplitLayout` | `vaadin-split-layout` | A component with two content areas and a draggable split handle between them | Apache 2.0 |
| `Tabs` | `vaadin-tabs` | Organize and group content into sections | Apache 2.0 |
| `TextArea` | `vaadin-text-area` | An input field component for multi-line text input | Apache 2.0 |
| `TextField` | `vaadin-text-field` | A component for introducing and editing text | Apache 2.0 |
| `TimePicker` | `vaadin-time-picker` | An input field for entering or selecting a specific time | Apache 2.0 |
| `TreeGrid` | `vaadin-grid` | A component for displaying hierarchical tabular data grouped into expandable and collapsible nodes | Apache 2.0 |
| `Upload` | `vaadin-upload` | A component for uploading one or more files with upload progress and status | Apache 2.0 |
| `VerticalLayout` | `vaadin-vertical-layout` | Places components top-to-bottom in a column | Apache 2.0 |

## Certifications

Vaadin offers two certification tracks to prove that a developer is proficient with Vaadin Flow:

- Certified Vaadin 14 Developer
- Certified Vaadin 14 Professional

To pass the certification, a developer should go through the documentation, follow the training videos, and take an online test.

Previous (now unavailable) certifications included:

- Vaadin Online Exam for Vaadin 7 Certified Developer
- Vaadin Online Exam for Vaadin 8 Certified Developer
