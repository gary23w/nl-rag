---
title: "Expect / Should (part 1/2)"
source: https://www.chaijs.com/api/bdd/
domain: mocha-chai
license: CC-BY-SA-4.0
tags: mocha javascript, chai assertions, javascript testing, bdd assertions
fetched: 2026-07-02
part: 1/2
---

# BDD

The BDD styles are `expect` and `should`. Both use the same chainable language to construct assertions, but they differ in the way an assertion is initially constructed. Check out the Style Guide for a comparison.

## API Reference

### Language Chains

The following are provided as chainable getters to improve the readability of your assertions.

**Chains**

- to
- be
- been
- is
- that
- which
- and
- has
- have
- with
- at
- of
- same
- but
- does
- still
- also

### .not

Negates all assertions that follow in the chain.

```js
expect(function () {}).to.not.throw();
expect({a: 1}).to.not.have.property('b');
expect([1, 2]).to.be.an('array').that.does.not.include(3);
```

Just because you can negate any assertion with `.not` doesn’t mean you should. With great power comes great responsibility. It’s often best to assert that the one expected output was produced, rather than asserting that one of countless unexpected outputs wasn’t produced. See individual assertions for specific guidance.

```js
expect(2).to.equal(2); // Recommended
expect(2).to.not.equal(1); // Not recommended
```

### .deep

Causes all `.equal`, `.include`, `.members`, `.keys`, and `.property` assertions that follow in the chain to use deep equality instead of strict (`===`) equality. See the `deep-eql` project page for info on the deep equality algorithm: https://github.com/chaijs/deep-eql.

```js
// Target object deeply (but not strictly) equals `{a: 1}`
expect({a: 1}).to.deep.equal({a: 1});
expect({a: 1}).to.not.equal({a: 1});

// Target array deeply (but not strictly) includes `{a: 1}`
expect([{a: 1}]).to.deep.include({a: 1});
expect([{a: 1}]).to.not.include({a: 1});

// Target object deeply (but not strictly) includes `x: {a: 1}`
expect({x: {a: 1}}).to.deep.include({x: {a: 1}});
expect({x: {a: 1}}).to.not.include({x: {a: 1}});

// Target array deeply (but not strictly) has member `{a: 1}`
expect([{a: 1}]).to.have.deep.members([{a: 1}]);
expect([{a: 1}]).to.not.have.members([{a: 1}]);

// Target set deeply (but not strictly) has key `{a: 1}`
expect(new Set([{a: 1}])).to.have.deep.keys([{a: 1}]);
expect(new Set([{a: 1}])).to.not.have.keys([{a: 1}]);

// Target object deeply (but not strictly) has property `x: {a: 1}`
expect({x: {a: 1}}).to.have.deep.property('x', {a: 1});
expect({x: {a: 1}}).to.not.have.property('x', {a: 1});
```

### .nested

Enables dot- and bracket-notation in all `.property` and `.include` assertions that follow in the chain.

```js
expect({a: {b: ['x', 'y']}}).to.have.nested.property('a.b[1]');
expect({a: {b: ['x', 'y']}}).to.nested.include({'a.b[1]': 'y'});
```

If `.` or `[]` are part of an actual property name, they can be escaped by adding two backslashes before them.

```js
expect({'.a': {'[b]': 'x'}}).to.have.nested.property('\\.a.\\[b\\]');
expect({'.a': {'[b]': 'x'}}).to.nested.include({'\\.a.\\[b\\]': 'x'});
```

`.nested` cannot be combined with `.own`.

### .own

Causes all `.property` and `.include` assertions that follow in the chain to ignore inherited properties.

```js
Object.prototype.b = 2;

expect({a: 1}).to.have.own.property('a');
expect({a: 1}).to.have.property('b');
expect({a: 1}).to.not.have.own.property('b');

expect({a: 1}).to.own.include({a: 1});
expect({a: 1}).to.include({b: 2}).but.not.own.include({b: 2});
```

`.own` cannot be combined with `.nested`.

### .ordered

Causes all `.members` assertions that follow in the chain to require that members be in the same order.

```js
expect([1, 2]).to.have.ordered.members([1, 2])
  .but.not.have.ordered.members([2, 1]);
```

When `.include` and `.ordered` are combined, the ordering begins at the start of both arrays.

```js
expect([1, 2, 3]).to.include.ordered.members([1, 2])
  .but.not.include.ordered.members([2, 3]);
```

### .any

Causes all `.keys` assertions that follow in the chain to only require that the target have at least one of the given keys. This is the opposite of `.all`, which requires that the target have all of the given keys.

```js
expect({a: 1, b: 2}).to.not.have.any.keys('c', 'd');
```

See the `.keys` doc for guidance on when to use `.any` or `.all`.

### .all

Causes all `.keys` assertions that follow in the chain to require that the target have all of the given keys. This is the opposite of `.any`, which only requires that the target have at least one of the given keys.

```js
expect({a: 1, b: 2}).to.have.all.keys('a', 'b');
```

Note that `.all` is used by default when neither `.all` nor `.any` are added earlier in the chain. However, it’s often best to add `.all` anyway because it improves readability.

See the `.keys` doc for guidance on when to use `.any` or `.all`.

### .a(type[, msg])

- @param { String } type
- @param { String } msg _optional_

Asserts that the target’s type is equal to the given string `type`. Types are case insensitive. See the `type-detect` project page for info on the type detection algorithm: https://github.com/chaijs/type-detect.

```js
expect('foo').to.be.a('string');
expect({a: 1}).to.be.an('object');
expect(null).to.be.a('null');
expect(undefined).to.be.an('undefined');
expect(new Error).to.be.an('error');
expect(Promise.resolve()).to.be.a('promise');
expect(new Float32Array).to.be.a('float32array');
expect(Symbol()).to.be.a('symbol');
```

`.a` supports objects that have a custom type set via `Symbol.toStringTag`.

```js
var myObj = {
  [Symbol.toStringTag]: 'myCustomType'
};

expect(myObj).to.be.a('myCustomType').but.not.an('object');
```

It’s often best to use `.a` to check a target’s type before making more assertions on the same target. That way, you avoid unexpected behavior from any assertion that does different things based on the target’s type.

```js
expect([1, 2, 3]).to.be.an('array').that.includes(2);
expect([]).to.be.an('array').that.is.empty;
```

Add `.not` earlier in the chain to negate `.a`. However, it’s often best to assert that the target is the expected type, rather than asserting that it isn’t one of many unexpected types.

```js
expect('foo').to.be.a('string'); // Recommended
expect('foo').to.not.be.an('array'); // Not recommended
```

`.a` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect(1).to.be.a('string', 'nooo why fail??');
expect(1, 'nooo why fail??').to.be.a('string');
```

`.a` can also be used as a language chain to improve the readability of your assertions.

```js
expect({b: 2}).to.have.a.property('b');
```

The alias `.an` can be used interchangeably with `.a`.

### .include(val[, msg])

- @param { Mixed } val
- @param { String } msg _optional_

When the target is a string, `.include` asserts that the given string `val` is a substring of the target.

```js
expect('foobar').to.include('foo');
```

When the target is an array, `.include` asserts that the given `val` is a member of the target.

```js
expect([1, 2, 3]).to.include(2);
```

When the target is an object, `.include` asserts that the given object `val`’s properties are a subset of the target’s properties.

```js
expect({a: 1, b: 2, c: 3}).to.include({a: 1, b: 2});
```

When the target is a Set or WeakSet, `.include` asserts that the given `val` is a member of the target. SameValueZero equality algorithm is used.

```js
expect(new Set([1, 2])).to.include(2);
```

When the target is a Map, `.include` asserts that the given `val` is one of the values of the target. SameValueZero equality algorithm is used.

```js
expect(new Map([['a', 1], ['b', 2]])).to.include(2);
```

Because `.include` does different things based on the target’s type, it’s important to check the target’s type before using `.include`. See the `.a` doc for info on testing a target’s type.

```js
expect([1, 2, 3]).to.be.an('array').that.includes(2);
```

By default, strict (`===`) equality is used to compare array members and object properties. Add `.deep` earlier in the chain to use deep equality instead (WeakSet targets are not supported). See the `deep-eql` project page for info on the deep equality algorithm: https://github.com/chaijs/deep-eql.

```js
// Target array deeply (but not strictly) includes `{a: 1}`
expect([{a: 1}]).to.deep.include({a: 1});
expect([{a: 1}]).to.not.include({a: 1});

// Target object deeply (but not strictly) includes `x: {a: 1}`
expect({x: {a: 1}}).to.deep.include({x: {a: 1}});
expect({x: {a: 1}}).to.not.include({x: {a: 1}});
```

By default, all of the target’s properties are searched when working with objects. This includes properties that are inherited and/or non-enumerable. Add `.own` earlier in the chain to exclude the target’s inherited properties from the search.

```js
Object.prototype.b = 2;

expect({a: 1}).to.own.include({a: 1});
expect({a: 1}).to.include({b: 2}).but.not.own.include({b: 2});
```

Note that a target object is always only searched for `val`’s own enumerable properties.

`.deep` and `.own` can be combined.

```js
expect({a: {b: 2}}).to.deep.own.include({a: {b: 2}});
```

Add `.nested` earlier in the chain to enable dot- and bracket-notation when referencing nested properties.

```js
expect({a: {b: ['x', 'y']}}).to.nested.include({'a.b[1]': 'y'});
```

If `.` or `[]` are part of an actual property name, they can be escaped by adding two backslashes before them.

```js
expect({'.a': {'[b]': 2}}).to.nested.include({'\\.a.\\[b\\]': 2});
```

`.deep` and `.nested` can be combined.

```js
expect({a: {b: [{c: 3}]}}).to.deep.nested.include({'a.b[0]': {c: 3}});
```

`.own` and `.nested` cannot be combined.

Add `.not` earlier in the chain to negate `.include`.

```js
expect('foobar').to.not.include('taco');
expect([1, 2, 3]).to.not.include(4);
```

However, it’s dangerous to negate `.include` when the target is an object. The problem is that it creates uncertain expectations by asserting that the target object doesn’t have all of `val`’s key/value pairs but may or may not have some of them. It’s often best to identify the exact output that’s expected, and then write an assertion that only accepts that exact output.

When the target object isn’t even expected to have `val`’s keys, it’s often best to assert exactly that.

```js
expect({c: 3}).to.not.have.any.keys('a', 'b'); // Recommended
expect({c: 3}).to.not.include({a: 1, b: 2}); // Not recommended
```

When the target object is expected to have `val`’s keys, it’s often best to assert that each of the properties has its expected value, rather than asserting that each property doesn’t have one of many unexpected values.

```js
expect({a: 3, b: 4}).to.include({a: 3, b: 4}); // Recommended
expect({a: 3, b: 4}).to.not.include({a: 1, b: 2}); // Not recommended
```

`.include` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect([1, 2, 3]).to.include(4, 'nooo why fail??');
expect([1, 2, 3], 'nooo why fail??').to.include(4);
```

`.include` can also be used as a language chain, causing all `.members` and `.keys` assertions that follow in the chain to require the target to be a superset of the expected set, rather than an identical set. Note that `.members` ignores duplicates in the subset when `.include` is added.

```js
// Target object's keys are a superset of ['a', 'b'] but not identical
expect({a: 1, b: 2, c: 3}).to.include.all.keys('a', 'b');
expect({a: 1, b: 2, c: 3}).to.not.have.all.keys('a', 'b');

// Target array is a superset of [1, 2] but not identical
expect([1, 2, 3]).to.include.members([1, 2]);
expect([1, 2, 3]).to.not.have.members([1, 2]);

// Duplicates in the subset are ignored
expect([1, 2, 3]).to.include.members([1, 2, 2, 2]);
```

Note that adding `.any` earlier in the chain causes the `.keys` assertion to ignore `.include`.

```js
// Both assertions are identical
expect({a: 1}).to.include.any.keys('a', 'b');
expect({a: 1}).to.have.any.keys('a', 'b');
```

The aliases `.includes`, `.contain`, and `.contains` can be used interchangeably with `.include`.

### .ok

Asserts that the target is a truthy value (considered `true` in boolean context). However, it’s often best to assert that the target is strictly (`===`) or deeply equal to its expected value.

```js
expect(1).to.equal(1); // Recommended
expect(1).to.be.ok; // Not recommended

expect(true).to.be.true; // Recommended
expect(true).to.be.ok; // Not recommended
```

Add `.not` earlier in the chain to negate `.ok`.

```js
expect(0).to.equal(0); // Recommended
expect(0).to.not.be.ok; // Not recommended

expect(false).to.be.false; // Recommended
expect(false).to.not.be.ok; // Not recommended

expect(null).to.be.null; // Recommended
expect(null).to.not.be.ok; // Not recommended

expect(undefined).to.be.undefined; // Recommended
expect(undefined).to.not.be.ok; // Not recommended
```

A custom error message can be given as the second argument to `expect`.

```js
expect(false, 'nooo why fail??').to.be.ok;
```

### .true

Asserts that the target is strictly (`===`) equal to `true`.

```js
expect(true).to.be.true;
```

Add `.not` earlier in the chain to negate `.true`. However, it’s often best to assert that the target is equal to its expected value, rather than not equal to `true`.

```js
expect(false).to.be.false; // Recommended
expect(false).to.not.be.true; // Not recommended

expect(1).to.equal(1); // Recommended
expect(1).to.not.be.true; // Not recommended
```

A custom error message can be given as the second argument to `expect`.

```js
expect(false, 'nooo why fail??').to.be.true;
```

### .false

Asserts that the target is strictly (`===`) equal to `false`.

```js
expect(false).to.be.false;
```

Add `.not` earlier in the chain to negate `.false`. However, it’s often best to assert that the target is equal to its expected value, rather than not equal to `false`.

```js
expect(true).to.be.true; // Recommended
expect(true).to.not.be.false; // Not recommended

expect(1).to.equal(1); // Recommended
expect(1).to.not.be.false; // Not recommended
```

A custom error message can be given as the second argument to `expect`.

```js
expect(true, 'nooo why fail??').to.be.false;
```

### .null

Asserts that the target is strictly (`===`) equal to `null`.

```js
expect(null).to.be.null;
```

Add `.not` earlier in the chain to negate `.null`. However, it’s often best to assert that the target is equal to its expected value, rather than not equal to `null`.

```js
expect(1).to.equal(1); // Recommended
expect(1).to.not.be.null; // Not recommended
```

A custom error message can be given as the second argument to `expect`.

```js
expect(42, 'nooo why fail??').to.be.null;
```

### .undefined

Asserts that the target is strictly (`===`) equal to `undefined`.

```js
expect(undefined).to.be.undefined;
```

Add `.not` earlier in the chain to negate `.undefined`. However, it’s often best to assert that the target is equal to its expected value, rather than not equal to `undefined`.

```js
expect(1).to.equal(1); // Recommended
expect(1).to.not.be.undefined; // Not recommended
```

A custom error message can be given as the second argument to `expect`.

```js
expect(42, 'nooo why fail??').to.be.undefined;
```

### .NaN

Asserts that the target is exactly `NaN`.

```js
expect(NaN).to.be.NaN;
```

Add `.not` earlier in the chain to negate `.NaN`. However, it’s often best to assert that the target is equal to its expected value, rather than not equal to `NaN`.

```js
expect('foo').to.equal('foo'); // Recommended
expect('foo').to.not.be.NaN; // Not recommended
```

A custom error message can be given as the second argument to `expect`.

```js
expect(42, 'nooo why fail??').to.be.NaN;
```

### .exist

Asserts that the target is not strictly (`===`) equal to either `null` or `undefined`. However, it’s often best to assert that the target is equal to its expected value.

```js
expect(1).to.equal(1); // Recommended
expect(1).to.exist; // Not recommended

expect(0).to.equal(0); // Recommended
expect(0).to.exist; // Not recommended
```

Add `.not` earlier in the chain to negate `.exist`.

```js
expect(null).to.be.null; // Recommended
expect(null).to.not.exist; // Not recommended

expect(undefined).to.be.undefined; // Recommended
expect(undefined).to.not.exist; // Not recommended
```

A custom error message can be given as the second argument to `expect`.

```js
expect(null, 'nooo why fail??').to.exist;
```

The alias `.exists` can be used interchangeably with `.exist`.

### .empty

When the target is a string or array, `.empty` asserts that the target’s `length` property is strictly (`===`) equal to `0`.

```js
expect([]).to.be.empty;
expect('').to.be.empty;
```

When the target is a map or set, `.empty` asserts that the target’s `size` property is strictly equal to `0`.

```js
expect(new Set()).to.be.empty;
expect(new Map()).to.be.empty;
```

When the target is a non-function object, `.empty` asserts that the target doesn’t have any own enumerable properties. Properties with Symbol-based keys are excluded from the count.

```js
expect({}).to.be.empty;
```

Because `.empty` does different things based on the target’s type, it’s important to check the target’s type before using `.empty`. See the `.a` doc for info on testing a target’s type.

```js
expect([]).to.be.an('array').that.is.empty;
```

Add `.not` earlier in the chain to negate `.empty`. However, it’s often best to assert that the target contains its expected number of values, rather than asserting that it’s not empty.

```js
expect([1, 2, 3]).to.have.lengthOf(3); // Recommended
expect([1, 2, 3]).to.not.be.empty; // Not recommended

expect(new Set([1, 2, 3])).to.have.property('size', 3); // Recommended
expect(new Set([1, 2, 3])).to.not.be.empty; // Not recommended

expect(Object.keys({a: 1})).to.have.lengthOf(1); // Recommended
expect({a: 1}).to.not.be.empty; // Not recommended
```

A custom error message can be given as the second argument to `expect`.

```js
expect([1, 2, 3], 'nooo why fail??').to.be.empty;
```

### .arguments

Asserts that the target is an `arguments` object.

```js
function test () {
  expect(arguments).to.be.arguments;
}

test();
```

Add `.not` earlier in the chain to negate `.arguments`. However, it’s often best to assert which type the target is expected to be, rather than asserting that it’s not an `arguments` object.

```js
expect('foo').to.be.a('string'); // Recommended
expect('foo').to.not.be.arguments; // Not recommended
```

A custom error message can be given as the second argument to `expect`.

```js
expect({}, 'nooo why fail??').to.be.arguments;
```

The alias `.Arguments` can be used interchangeably with `.arguments`.

### .equal(val[, msg])

- @param { Mixed } val
- @param { String } msg _optional_

Asserts that the target is strictly (`===`) equal to the given `val`.

```js
expect(1).to.equal(1);
expect('foo').to.equal('foo');
```

Add `.deep` earlier in the chain to use deep equality instead. See the `deep-eql` project page for info on the deep equality algorithm: https://github.com/chaijs/deep-eql.

```js
// Target object deeply (but not strictly) equals `{a: 1}`
expect({a: 1}).to.deep.equal({a: 1});
expect({a: 1}).to.not.equal({a: 1});

// Target array deeply (but not strictly) equals `[1, 2]`
expect([1, 2]).to.deep.equal([1, 2]);
expect([1, 2]).to.not.equal([1, 2]);
```

Add `.not` earlier in the chain to negate `.equal`. However, it’s often best to assert that the target is equal to its expected value, rather than not equal to one of countless unexpected values.

```js
expect(1).to.equal(1); // Recommended
expect(1).to.not.equal(2); // Not recommended
```

`.equal` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect(1).to.equal(2, 'nooo why fail??');
expect(1, 'nooo why fail??').to.equal(2);
```

The aliases `.equals` and `eq` can be used interchangeably with `.equal`.

### .eql(obj[, msg])

- @param { Mixed } obj
- @param { String } msg _optional_

Asserts that the target is deeply equal to the given `obj`. See the `deep-eql` project page for info on the deep equality algorithm: https://github.com/chaijs/deep-eql.

```js
// Target object is deeply (but not strictly) equal to {a: 1}
expect({a: 1}).to.eql({a: 1}).but.not.equal({a: 1});

// Target array is deeply (but not strictly) equal to [1, 2]
expect([1, 2]).to.eql([1, 2]).but.not.equal([1, 2]);
```

Add `.not` earlier in the chain to negate `.eql`. However, it’s often best to assert that the target is deeply equal to its expected value, rather than not deeply equal to one of countless unexpected values.

```js
expect({a: 1}).to.eql({a: 1}); // Recommended
expect({a: 1}).to.not.eql({b: 2}); // Not recommended
```

`.eql` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect({a: 1}).to.eql({b: 2}, 'nooo why fail??');
expect({a: 1}, 'nooo why fail??').to.eql({b: 2});
```

The alias `.eqls` can be used interchangeably with `.eql`.

The `.deep.equal` assertion is almost identical to `.eql` but with one difference: `.deep.equal` causes deep equality comparisons to also be used for any other assertions that follow in the chain.

### .above(n[, msg])

- @param { Number } n
- @param { String } msg _optional_

Asserts that the target is a number or a date greater than the given number or date `n` respectively. However, it’s often best to assert that the target is equal to its expected value.

```js
expect(2).to.equal(2); // Recommended
expect(2).to.be.above(1); // Not recommended
```

Add `.lengthOf` earlier in the chain to assert that the target’s `length` or `size` is greater than the given number `n`.

```js
expect('foo').to.have.lengthOf(3); // Recommended
expect('foo').to.have.lengthOf.above(2); // Not recommended

expect([1, 2, 3]).to.have.lengthOf(3); // Recommended
expect([1, 2, 3]).to.have.lengthOf.above(2); // Not recommended
```

Add `.not` earlier in the chain to negate `.above`.

```js
expect(2).to.equal(2); // Recommended
expect(1).to.not.be.above(2); // Not recommended
```

`.above` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect(1).to.be.above(2, 'nooo why fail??');
expect(1, 'nooo why fail??').to.be.above(2);
```

The aliases `.gt` and `.greaterThan` can be used interchangeably with `.above`.

### .least(n[, msg])

- @param { Number } n
- @param { String } msg _optional_

Asserts that the target is a number or a date greater than or equal to the given number or date `n` respectively. However, it’s often best to assert that the target is equal to its expected value.

```js
expect(2).to.equal(2); // Recommended
expect(2).to.be.at.least(1); // Not recommended
expect(2).to.be.at.least(2); // Not recommended
```

Add `.lengthOf` earlier in the chain to assert that the target’s `length` or `size` is greater than or equal to the given number `n`.

```js
expect('foo').to.have.lengthOf(3); // Recommended
expect('foo').to.have.lengthOf.at.least(2); // Not recommended

expect([1, 2, 3]).to.have.lengthOf(3); // Recommended
expect([1, 2, 3]).to.have.lengthOf.at.least(2); // Not recommended
```

Add `.not` earlier in the chain to negate `.least`.

```js
expect(1).to.equal(1); // Recommended
expect(1).to.not.be.at.least(2); // Not recommended
```

`.least` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect(1).to.be.at.least(2, 'nooo why fail??');
expect(1, 'nooo why fail??').to.be.at.least(2);
```

The aliases `.gte` and `.greaterThanOrEqual` can be used interchangeably with `.least`.

### .below(n[, msg])

- @param { Number } n
- @param { String } msg _optional_

Asserts that the target is a number or a date less than the given number or date `n` respectively. However, it’s often best to assert that the target is equal to its expected value.

```js
expect(1).to.equal(1); // Recommended
expect(1).to.be.below(2); // Not recommended
```

Add `.lengthOf` earlier in the chain to assert that the target’s `length` or `size` is less than the given number `n`.

```js
expect('foo').to.have.lengthOf(3); // Recommended
expect('foo').to.have.lengthOf.below(4); // Not recommended

expect([1, 2, 3]).to.have.length(3); // Recommended
expect([1, 2, 3]).to.have.lengthOf.below(4); // Not recommended
```

Add `.not` earlier in the chain to negate `.below`.

```js
expect(2).to.equal(2); // Recommended
expect(2).to.not.be.below(1); // Not recommended
```

`.below` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect(2).to.be.below(1, 'nooo why fail??');
expect(2, 'nooo why fail??').to.be.below(1);
```

The aliases `.lt` and `.lessThan` can be used interchangeably with `.below`.

### .most(n[, msg])

- @param { Number } n
- @param { String } msg _optional_

Asserts that the target is a number or a date less than or equal to the given number or date `n` respectively. However, it’s often best to assert that the target is equal to its expected value.

```js
expect(1).to.equal(1); // Recommended
expect(1).to.be.at.most(2); // Not recommended
expect(1).to.be.at.most(1); // Not recommended
```

Add `.lengthOf` earlier in the chain to assert that the target’s `length` or `size` is less than or equal to the given number `n`.

```js
expect('foo').to.have.lengthOf(3); // Recommended
expect('foo').to.have.lengthOf.at.most(4); // Not recommended

expect([1, 2, 3]).to.have.lengthOf(3); // Recommended
expect([1, 2, 3]).to.have.lengthOf.at.most(4); // Not recommended
```

Add `.not` earlier in the chain to negate `.most`.

```js
expect(2).to.equal(2); // Recommended
expect(2).to.not.be.at.most(1); // Not recommended
```

`.most` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect(2).to.be.at.most(1, 'nooo why fail??');
expect(2, 'nooo why fail??').to.be.at.most(1);
```

The aliases `.lte` and `.lessThanOrEqual` can be used interchangeably with `.most`.

### .within(start, finish[, msg])

- @param { Number } start lower bound inclusive
- @param { Number } finish upper bound inclusive
- @param { String } msg _optional_

Asserts that the target is a number or a date greater than or equal to the given number or date `start`, and less than or equal to the given number or date `finish` respectively. However, it’s often best to assert that the target is equal to its expected value.

```js
expect(2).to.equal(2); // Recommended
expect(2).to.be.within(1, 3); // Not recommended
expect(2).to.be.within(2, 3); // Not recommended
expect(2).to.be.within(1, 2); // Not recommended
```

Add `.lengthOf` earlier in the chain to assert that the target’s `length` or `size` is greater than or equal to the given number `start`, and less than or equal to the given number `finish`.

```js
expect('foo').to.have.lengthOf(3); // Recommended
expect('foo').to.have.lengthOf.within(2, 4); // Not recommended

expect([1, 2, 3]).to.have.lengthOf(3); // Recommended
expect([1, 2, 3]).to.have.lengthOf.within(2, 4); // Not recommended
```

Add `.not` earlier in the chain to negate `.within`.

```js
expect(1).to.equal(1); // Recommended
expect(1).to.not.be.within(2, 4); // Not recommended
```

`.within` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect(4).to.be.within(1, 3, 'nooo why fail??');
expect(4, 'nooo why fail??').to.be.within(1, 3);
```

### .instanceof(constructor[, msg])

- @param { Constructor } constructor
- @param { String } msg _optional_

Asserts that the target is an instance of the given `constructor`.

```js
function Cat () { }

expect(new Cat()).to.be.an.instanceof(Cat);
expect([1, 2]).to.be.an.instanceof(Array);
```

Add `.not` earlier in the chain to negate `.instanceof`.

```js
expect({a: 1}).to.not.be.an.instanceof(Array);
```

`.instanceof` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`.

```js
expect(1).to.be.an.instanceof(Array, 'nooo why fail??');
expect(1, 'nooo why fail??').to.be.an.instanceof(Array);
```

Due to limitations in ES5, `.instanceof` may not always work as expected when using a transpiler such as Babel or TypeScript. In particular, it may produce unexpected results when subclassing built-in object such as `Array`, `Error`, and `Map`. See your transpiler’s docs for details:

- (Babel)
- (TypeScript)

The alias `.instanceOf` can be used interchangeably with `.instanceof`.

### .property(name[, val[, msg]])

- @param { String } name
- @param { Mixed } val (optional)
- @param { String } msg _optional_

Asserts that the target has a property with the given key `name`.

```js
expect({a: 1}).to.have.property('a');
```

When `val` is provided, `.property` also asserts that the property’s value is equal to the given `val`.

```js
expect({a: 1}).to.have.property('a', 1);
```

By default, strict (`===`) equality is used. Add `.deep` earlier in the chain to use deep equality instead. See the `deep-eql` project page for info on the deep equality algorithm: https://github.com/chaijs/deep-eql.

```js
// Target object deeply (but not strictly) has property `x: {a: 1}`
expect({x: {a: 1}}).to.have.deep.property('x', {a: 1});
expect({x: {a: 1}}).to.not.have.property('x', {a: 1});
```

The target’s enumerable and non-enumerable properties are always included in the search. By default, both own and inherited properties are included. Add `.own` earlier in the chain to exclude inherited properties from the search.

```js
Object.prototype.b = 2;

expect({a: 1}).to.have.own.property('a');
expect({a: 1}).to.have.own.property('a', 1);
expect({a: 1}).to.have.property('b');
expect({a: 1}).to.not.have.own.property('b');
```

`.deep` and `.own` can be combined.

```js
expect({x: {a: 1}}).to.have.deep.own.property('x', {a: 1});
```

Add `.nested` earlier in the chain to enable dot- and bracket-notation when referencing nested properties.

```js
expect({a: {b: ['x', 'y']}}).to.have.nested.property('a.b[1]');
expect({a: {b: ['x', 'y']}}).to.have.nested.property('a.b[1]', 'y');
```

If `.` or `[]` are part of an actual property name, they can be escaped by adding two backslashes before them.

```js
expect({'.a': {'[b]': 'x'}}).to.have.nested.property('\\.a.\\[b\\]');
```

`.deep` and `.nested` can be combined.

```js
expect({a: {b: [{c: 3}]}})
  .to.have.deep.nested.property('a.b[0]', {c: 3});
```

`.own` and `.nested` cannot be combined.

Add `.not` earlier in the chain to negate `.property`.

```js
expect({a: 1}).to.not.have.property('b');
```

However, it’s dangerous to negate `.property` when providing `val`. The problem is that it creates uncertain expectations by asserting that the target either doesn’t have a property with the given key `name`, or that it does have a property with the given key `name` but its value isn’t equal to the given `val`. It’s often best to identify the exact output that’s expected, and then write an assertion that only accepts that exact output.

When the target isn’t expected to have a property with the given key `name`, it’s often best to assert exactly that.

```js
expect({b: 2}).to.not.have.property('a'); // Recommended
expect({b: 2}).to.not.have.property('a', 1); // Not recommended
```

When the target is expected to have a property with the given key `name`, it’s often best to assert that the property has its expected value, rather than asserting that it doesn’t have one of many unexpected values.

```js
expect({a: 3}).to.have.property('a', 3); // Recommended
expect({a: 3}).to.not.have.property('a', 1); // Not recommended
```

`.property` changes the target of any assertions that follow in the chain to be the value of the property from the original target object.

```js
expect({a: 1}).to.have.property('a').that.is.a('number');
```

`.property` accepts an optional `msg` argument which is a custom error message to show when the assertion fails. The message can also be given as the second argument to `expect`. When not providing `val`, only use the second form.

```js
// Recommended
expect({a: 1}).to.have.property('a', 2, 'nooo why fail??');
expect({a: 1}, 'nooo why fail??').to.have.property('a', 2);
expect({a: 1}, 'nooo why fail??').to.have.property('b');

// Not recommended
expect({a: 1}).to.have.property('b', undefined, 'nooo why fail??');
```

The above assertion isn’t the same thing as not providing `val`. Instead, it’s asserting that the target object has a `b` property that’s equal to `undefined`.

The assertions `.ownProperty` and `.haveOwnProperty` can be used interchangeably with `.own.property`.

### .ownPropertyDescriptor(name[, descriptor[, msg]])

- @param { String } name
- @param { Object } descriptor _optional_
- @param { String } msg _optional_

Asserts that the target has its own property descriptor with the given key `name`. Enumerable and non-enumerable properties are included in the search.

```js
expect({a: 1}).to.have.ownPropertyDescriptor('a');
```

When `descriptor` is provided, `.ownPropertyDescriptor` also asserts that the property’s descriptor is deeply equal to the given `descriptor`. See the `deep-eql` project page for info on the deep equality algorithm: https://github.com/chaijs/deep-eql.

```js
expect({a: 1}).to.have.ownPropertyDescriptor('a', {
  configurable: true,
  enumerable: true,
  writable: true,
  value: 1,
});
```

Add `.not` earlier in the chain to negate `.ownPropertyDescriptor`.

```js
expect({a: 1}).to.not.have.ownPropertyDescriptor('b');
```

However, it’s dangerous to negate `.ownPropertyDescriptor` when providing a `descriptor`. The problem is that it creates uncertain expectations by asserting that the target either doesn’t have a property descriptor with the given key `name`, or that it does have a property descriptor with the given key `name` but it’s not deeply equal to the given `descriptor`. It’s often best to identify the exact output that’s expected, and then write an assertion that only accepts that exact output.

When the target isn’t expected to have a property descriptor with the given key `name`, it’s often best to assert exactly that.
