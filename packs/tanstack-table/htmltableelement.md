---
title: "HTMLTableElement - Web APIs"
source: https://developer.mozilla.org/en-US/docs/Web/API/HTMLTableElement
domain: tanstack-table
license: CC-BY-SA-4.0
tags: tanstack table, headless table library, data grid state, sorting pagination model
fetched: 2026-07-02
---

# HTMLTableElement

Baseline

Widely available

*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

* Some parts of this feature may have varying levels of support.

- Learn more
- See full compatibility

The **`HTMLTableElement`** interface provides special properties and methods (beyond the regular `HTMLElement` object interface it also has available to it by inheritance) for manipulating the layout and presentation of tables in an HTML document.

## Instance properties

*Inherits properties from its parent, `HTMLElement`.*

**`HTMLTableElement.caption`**

A `HTMLTableCaptionElement` representing the first `<caption>` that is a child of the element, or `null` if none is found. When set, if the object doesn't represent a `<caption>`, a `DOMException` with the `HierarchyRequestError` name is thrown. If a correct object is given, it is inserted in the tree as the first child of this element and the first `<caption>` that is a child of this element is removed from the tree, if any.

**`HTMLTableElement.tHead`**

A `HTMLTableSectionElement` representing the first `<thead>` that is a child of the element, or `null` if none is found. When set, if the object doesn't represent a `<thead>`, a `DOMException` with the `HierarchyRequestError` name is thrown. If a correct object is given, it is inserted in the tree immediately before the first element that is neither a `<caption>`, nor a `<colgroup>`, or as the last child if there is no such element, and the first `<thead>` that is a child of this element is removed from the tree, if any.

**`HTMLTableElement.tFoot`**

A `HTMLTableSectionElement` representing the first `<tfoot>` that is a child of the element, or `null` if none is found. When set, if the object doesn't represent a `<tfoot>`, a `DOMException` with the `HierarchyRequestError` name is thrown. If a correct object is given, it is inserted in the tree immediately before the first element that is neither a `<caption>`, a `<colgroup>`, nor a `<thead>`, or as the last child if there is no such element, and the first `<tfoot>` that is a child of this element is removed from the tree, if any.

**`HTMLTableElement.rows` Read only**

Returns a live `HTMLCollection` containing all the rows of the element, that is all `<tr>` that are a child of the element, or a child of one of its `<thead>`, `<tbody>` and `<tfoot>` children. The rows members of a `<thead>` appear first, in tree order, and those members of a `<tbody>` last, also in tree order. The `HTMLCollection` is live and is automatically updated when the `HTMLTableElement` changes.

**`HTMLTableElement.tBodies` Read only**

Returns a live `HTMLCollection` containing all the `<tbody>` of the element. The `HTMLCollection` is live and is automatically updated when the `HTMLTableElement` changes.

### Obsolete Properties

**Warning:** The following properties are obsolete. You should avoid using them.

**`HTMLTableElement.align`**

A string containing an enumerated value reflecting the `align` attribute. It indicates the alignment of the element's contents with respect to the surrounding context. The possible values are `"left"`, `"right"`, and `"center"`.

**`HTMLTableElement.bgColor`**

A string containing the background color of the cells. It reflects the obsolete `bgColor` attribute.

**`HTMLTableElement.border`**

A string containing the width in pixels of the border of the table. It reflects the obsolete `border` attribute.

**`HTMLTableElement.cellPadding`**

A string containing the width in pixels of the horizontal and vertical space between cell content and cell borders. It reflects the obsolete `cellpadding` attribute.

**`HTMLTableElement.cellSpacing`**

A string containing the width in pixels of the horizontal and vertical separation between cells. It reflects the obsolete `cellspacing` attribute.

**`HTMLTableElement.frame`**

A string containing the type of the external borders of the table. It reflects the obsolete `frame` attribute and can take one of the following values: `"void"`, `"above"`, `"below"`, `"hsides"`, `"vsides"`, `"lhs"`, `"rhs"`, `"box"`, or `"border"`.

**`HTMLTableElement.rules`**

A string containing the type of the internal borders of the table. It reflects the obsolete `rules` attribute and can take one of the following values: `"none"`, `"groups"`, `"rows"`, `"cols"`, or `"all"`.

**`HTMLTableElement.summary`**

A string containing a description of the purpose or the structure of the table. It reflects the obsolete `summary` attribute.

**`HTMLTableElement.width`**

A string containing the length in pixels or in percentage of the desired width of the entire table. It reflects the obsolete `width` attribute.

## Instance methods

*Inherits methods from its parent, `HTMLElement`*.

**`HTMLTableElement.createTHead()`**

Returns an `HTMLTableSectionElement` representing the first `<thead>` that is a child of the element. If none is found, a new one is created and inserted in the tree immediately before the first element that is neither a `<caption>`, nor a `<colgroup>`, or as the last child if there is no such element.

**`HTMLTableElement.deleteTHead()`**

Removes the first `<thead>` that is a child of the element.

**`HTMLTableElement.createTFoot()`**

Returns an `HTMLTableSectionElement` representing the first `<tfoot>` that is a child of the element. If none is found, a new one is created and inserted in the tree as the last child.

**`HTMLTableElement.deleteTFoot()`**

Removes the first `<tfoot>` that is a child of the element.

**`HTMLTableElement.createTBody()`**

Returns a `HTMLTableSectionElement` representing a new `<tbody>` that is a child of the element. It is inserted in the tree after the last element that is a `<tbody>`, or as the last child if there is no such element.

**`HTMLTableElement.createCaption()`**

Returns an `HTMLElement` representing the first `<caption>` that is a child of the element. If none is found, a new one is created and inserted in the tree as the first child of the `<table>` element.

**`HTMLTableElement.deleteCaption()`**

Removes the first `<caption>` that is a child of the element.

**`HTMLTableElement.insertRow()`**

Returns an `HTMLTableRowElement` representing a new row of the table. It inserts it in the rows collection immediately before the `<tr>` element at the given `index` position. If necessary a `<tbody>` is created. If the `index` is `-1`, the new row is appended to the collection. If the `index` is smaller than `-1` or greater than the number of rows in the collection, a `DOMException` with the value `IndexSizeError` is raised.

**`HTMLTableElement.deleteRow()`**

Removes the row corresponding to the `index` given in parameter. If the `index` value is `-1` the last row is removed; if it is smaller than `-1` or greater than the amount of rows in the collection, a `DOMException` with the value `IndexSizeError` is raised.

## Examples

### Using the DOM Table Interface

The `HTMLTableElement` interface provides some convenience methods for creating and manipulating tables. Two frequently used methods are `HTMLTableElement.insertRow` and `HTMLTableRowElement.insertCell`.

To add a row and some cells to an existing table:

```html
<table id="table0">
  <tbody>
    <tr>
      <td>Row 0 Cell 0</td>
      <td>Row 0 Cell 1</td>
    </tr>
  </tbody>
</table>
```

```js
const table = document.getElementById("table0");
const row = table.insertRow(-1);

for (let i = 0; i < 2; i++) {
  const cell = row.insertCell(-1);
  const text = `Row ${row.rowIndex} Cell ${i}`;
  cell.appendChild(document.createTextNode(text));
}
```

## Specifications

| Specification |
|---|
| HTML # htmltableelement |

## Browser compatibility
