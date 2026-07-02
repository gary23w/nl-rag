---
title: "CSS-in-JS"
source: https://en.wikipedia.org/wiki/CSS-in-JS
domain: styled-components
license: CC-BY-SA-4.0
tags: styled components, css-in-js, component-scoped styling, tagged template css
fetched: 2026-07-02
---

# CSS-in-JS

**CSS-in-JS** is a styling technique by which JavaScript is used to style components. When this JavaScript is parsed, CSS is generated (usually as a `<style>` element) and attached into the DOM. It enables the abstraction of CSS to the component level itself, using JavaScript to describe styles in a declarative and maintainable way. There are multiple implementations of this concept in the form of libraries such as

- Emotion
- Styled Components
- JSS

These libraries allow the creation of styled components using tagged template literals. For example, using styled components in a React project would look like the following:

```mw
import styled from 'styled-components';
// Create a component that renders a <p> element with blue text
const BlueText = styled.p`
  color: blue;
`;

<BlueText>My blue text</BlueText>
```

Some outcomes that may be achieved through CSS-in-JS can not be obtained using traditional CSS techniques. It is possible to make the styles dynamic in line with just a few conditional statements. Programmers may also write more modular code, with CSS being encapsulated in the same block as the programmer's JavaScript, scoping it to that module only.

## Industry use

CSS-in-JS is used by Reddit, Patreon, Target, Atlassian, Vogue, GitHub and Coinbase.
