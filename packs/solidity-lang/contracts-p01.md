---
title: "Contracts (part 1/3)"
source: https://docs.soliditylang.org/en/latest/contracts.html
domain: solidity-lang
license: GPL-3.0 (soliditylang.org)
tags: solidity, solidity contract, solidity types, contract inheritance
fetched: 2026-07-02
part: 1/3
---

# Contracts

Contracts in Solidity are similar to classes in object-oriented languages. They contain persistent data in state variables, and functions that can modify these variables. Calling a function on a different contract (instance) will perform an EVM function call and thus switch the context such that state variables in the calling contract are inaccessible. A contract and its functions need to be called for anything to happen. There is no “cron” concept in Ethereum to call a function at a particular event automatically.


## Creating Contracts

Contracts can be created “from outside” via Ethereum transactions or from within Solidity contracts.

IDEs, such as Remix, make the creation process seamless using UI elements.

One way to create contracts programmatically on Ethereum is via the JavaScript API web3.js. It has a function called web3.eth.Contract to facilitate contract creation.

When a contract is created, its constructor (a function declared with the `constructor` keyword) is executed once.

A constructor is optional. Only one constructor is allowed, which means overloading is not supported.

After the constructor has executed, the final code of the contract is stored on the blockchain. This code includes all public and external functions and all functions that are reachable from there through function calls. The deployed code does not include the constructor code or internal functions only called from the constructor.

Internally, constructor arguments are passed ABI encoded after the code of the contract itself, but you do not have to care about this if you use `web3.js`.

If a contract wants to create another contract, the source code (and the binary) of the created contract has to be known to the creator. This means that cyclic creation dependencies are impossible.

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.9.0;

contract OwnedToken {
    // `TokenCreator` is a contract type that is defined below.
    // It is fine to reference it as long as it is not used
    // to create a new contract.
    TokenCreator creator;
    address owner;
    bytes32 name;

    // This is the constructor which registers the
    // creator and the assigned name.
    constructor(bytes32 name_) {
        // State variables are accessed via their name
        // and not via e.g. `this.owner`. Functions can
        // be accessed directly or through `this.f`,
        // but the latter provides an external view
        // to the function. Especially in the constructor,
        // you should not access functions externally,
        // because the function does not exist yet.
        // See the next section for details.
        owner = msg.sender;

        // We perform an explicit type conversion from `address`
        // to `TokenCreator` and assume that the type of
        // the calling contract is `TokenCreator`, there is
        // no real way to verify that.
        // This does not create a new contract.
        creator = TokenCreator(msg.sender);
        name = name_;
    }

    function changeName(bytes32 newName) public {
        // Only the creator can alter the name.
        // We compare the contract based on its
        // address which can be retrieved by
        // explicit conversion to address.
        if (msg.sender == address(creator))
            name = newName;
    }

    function transfer(address newOwner) public {
        // Only the current owner can transfer the token.
        if (msg.sender != owner) return;

        // We ask the creator contract if the transfer
        // should proceed by using a function of the
        // `TokenCreator` contract defined below. If
        // the call fails (e.g. due to out-of-gas),
        // the execution also fails here.
        if (creator.isTokenTransferOK(owner, newOwner))
            owner = newOwner;
    }
}

contract TokenCreator {
    function createToken(bytes32 name)
        public
        returns (OwnedToken tokenAddress)
    {
        // Create a new `Token` contract and return its address.
        // From the JavaScript side, the return type
        // of this function is `address`, as this is
        // the closest type available in the ABI.
        return new OwnedToken(name);
    }

    function changeName(OwnedToken tokenAddress, bytes32 name) public {
        // Again, the external type of `tokenAddress` is
        // simply `address`.
        tokenAddress.changeName(name);
    }

    // Perform checks to determine if transferring a token to the
    // `OwnedToken` contract should proceed
    function isTokenTransferOK(address currentOwner, address newOwner)
        public
        pure
        returns (bool ok)
    {
        // Check an arbitrary condition to see if transfer should proceed
        return keccak256(abi.encodePacked(currentOwner, newOwner))[0] == 0x7f;
    }
}
```


## Visibility and Getters

### State Variable Visibility

**`public`**

Public state variables differ from internal ones only in that the compiler automatically generates getter functions for them, which allows other contracts to read their values. When used within the same contract, the external access (e.g. `this.x`) invokes the getter while internal access (e.g. `x`) gets the variable value directly from storage. Setter functions are not generated so other contracts cannot directly modify their values.

**`internal`**

Internal state variables can only be accessed from within the contract they are defined in and in derived contracts. They cannot be accessed externally. This is the default visibility level for state variables.

**`private`**

Private state variables are like internal ones but they are not visible in derived contracts.

Warning

Making something `private` or `internal` only prevents other contracts from reading or modifying the information, but it will still be visible to the whole world outside of the blockchain.

### Function Visibility

Solidity knows two kinds of function calls: external ones that do create an actual EVM message call and internal ones that do not. Furthermore, internal functions can be made inaccessible to derived contracts. This gives rise to four types of visibility for functions.

**`external`**

External functions are part of the contract interface, which means they can be called from other contracts and via transactions. An external function `f` cannot be called internally (i.e. `f()` does not work, but `this.f()` works).

**`public`**

Public functions are part of the contract interface and can be either called internally or via message calls.

**`internal`**

Internal functions can only be accessed from within the current contract or contracts deriving from it. They cannot be accessed externally. Since they are not exposed to the outside through the contract’s ABI, they can take parameters of internal types like mappings or storage references.

**`private`**

Private functions are like internal ones but they are not visible in derived contracts.

Warning

Making something `private` or `internal` only prevents other contracts from reading or modifying the information, but it will still be visible to the whole world outside of the blockchain.

The visibility specifier is given after the type for state variables and between parameter list and return parameter list for functions.

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract C {
    function f(uint a) private pure returns (uint b) { return a + 1; }
    function setData(uint a) internal { data = a; }
    uint public data;
}
```

In the following example, `D`, can call `c.getData()` to retrieve the value of `data` in state storage, but is not able to call `f`. Contract `E` is derived from `C` and, thus, can call `compute`.

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract C {
    uint private data;

    function f(uint a) private pure returns(uint b) { return a + 1; }
    function setData(uint a) public { data = a; }
    function getData() public view returns(uint) { return data; }
    function compute(uint a, uint b) internal pure returns (uint) { return a + b; }
}

// This will not compile
contract D {
    function readData() public {
        C c = new C();
        uint local = c.f(7); // error: member `f` is not visible
        c.setData(3);
        local = c.getData();
        local = c.compute(3, 5); // error: member `compute` is not visible
    }
}

contract E is C {
    function g() public {
        C c = new C();
        uint val = compute(3, 5); // access to internal member (from derived to parent contract)
    }
}
```

### Getter Functions

The compiler automatically creates getter functions for all **public** state variables. For the contract given below, the compiler will generate a function called `data` that does not take any arguments and returns a `uint`, the value of the state variable `data`. State variables can be initialized when they are declared.

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract C {
    uint public data = 42;
}

contract Caller {
    C c = new C();
    function f() public view returns (uint) {
        return c.data();
    }
}
```

The getter functions have external visibility. If the symbol is accessed internally (i.e. without `this.`), it evaluates to a state variable. If it is accessed externally (i.e. with `this.`), it evaluates to a function.

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0 <0.9.0;

contract C {
    uint public data;
    function x() public returns (uint) {
        data = 3; // internal access
        return this.data(); // external access
    }
}
```

If you have a `public` state variable of array type, then you can only retrieve single elements of the array via the generated getter function. This mechanism exists to avoid high gas costs when returning an entire array. You can use arguments to specify which individual element to return, for example `myArray(0)`. If you want to return an entire array in one call, then you need to write a function, for example:

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract arrayExample {
    // public state variable
    uint[] public myArray;

    // Getter function generated by the compiler
    /*
    function myArray(uint i) public view returns (uint) {
        return myArray[i];
    }
    */

    // function that returns entire array
    function getArray() public view returns (uint[] memory) {
        return myArray;
    }
}
```

Now you can use `getArray()` to retrieve the entire array, instead of `myArray(i)`, which returns a single element per call.

The next example is more complex:

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0 <0.9.0;

contract Complex {
    struct Data {
        uint a;
        bytes3 b;
        mapping(uint => uint) map;
        uint[3] c;
        uint[] d;
        bytes e;
    }
    mapping(uint => mapping(bool => Data[])) public data;
}
```

It generates a function of the following form. The mapping and arrays (with the exception of byte arrays) in the struct are omitted because there is no good way to select individual struct members or provide a key for the mapping:

open in Remix

```solidity
function data(uint arg1, bool arg2, uint arg3)
    public
    returns (uint a, bytes3 b, bytes memory e)
{
    a = data[arg1][arg2][arg3].a;
    b = data[arg1][arg2][arg3].b;
    e = data[arg1][arg2][arg3].e;
}
```


## Function Modifiers

Modifiers can be used to change the behavior of functions in a declarative way. For example, you can use a modifier to automatically check a condition prior to executing the function.

Modifiers are inheritable properties of contracts and may be overridden by derived contracts, but only if they are marked `virtual`. For details, please see Modifier Overriding.

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.1 <0.9.0;

contract owned {
    constructor() { owner = payable(msg.sender); }
    address payable owner;

    // This contract only defines a modifier but does not use
    // it: it will be used in derived contracts.
    // The function body is inserted where the special symbol
    // `_;` in the definition of a modifier appears.
    // This means that if the owner calls this function, the
    // function is executed and otherwise, an exception is
    // thrown.
    modifier onlyOwner {
        require(
            msg.sender == owner,
            "Only owner can call this function."
        );
        _;
    }
}

contract priced {
    // Modifiers can receive arguments:
    modifier costs(uint price) {
        if (msg.value >= price) {
            _;
        }
    }
}

contract Register is priced, owned {
    mapping(address => bool) registeredAddresses;
    uint price;

    constructor(uint initialPrice) { price = initialPrice; }

    // It is important to also provide the
    // `payable` keyword here, otherwise the function will
    // automatically reject all Ether sent to it.
    function register() public payable costs(price) {
        registeredAddresses[msg.sender] = true;
    }

    // This contract inherits the `onlyOwner` modifier from
    // the `owned` contract. As a result, calls to `changePrice` will
    // only take effect if they are made by the stored owner.
    function changePrice(uint price_) public onlyOwner {
        price = price_;
    }
}

contract Mutex {
    bool locked;
    modifier noReentrancy() {
        require(
            !locked,
            "Reentrant call."
        );
        locked = true;
        _;
        locked = false;
    }

    /// This function is protected by a mutex, which means that
    /// reentrant calls from within `msg.sender.call` cannot call `f` again.
    /// The `return 7` statement assigns 7 to the return value but still
    /// executes the statement `locked = false` in the modifier.
    function f() public noReentrancy returns (uint) {
        (bool success,) = msg.sender.call("");
        require(success);
        return 7;
    }
}
```

If you want to access a modifier `m` defined in a contract `C`, you can use `C.m` to reference it without virtual lookup. It is only possible to use modifiers defined in the current contract or its base contracts. Modifiers can also be defined in libraries but their use is limited to functions of the same library.

Multiple modifiers are applied to a function by specifying them in a whitespace-separated list and are evaluated in the order presented.

Modifiers cannot implicitly access or change the arguments and return values of functions they modify. Their values can only be passed to them explicitly at the point of invocation.

In function modifiers, it is necessary to specify when you want the function to which the modifier is applied to be run. The placeholder statement (denoted by a single underscore character `_`) is used to denote where the body of the function being modified should be inserted. Note that the placeholder operator is different from using underscores as leading or trailing characters in variable names, which is a stylistic choice.

Explicit returns from a modifier or function body only leave the current modifier or function body. Return variables are assigned and control flow continues after the `_` in the preceding modifier.

Warning

In an earlier version of Solidity, `return` statements in functions having modifiers behaved differently.

An explicit return from a modifier with `return;` does not affect the values returned by the function. The modifier can, however, choose not to execute the function body at all and in that case the return variables are set to their default values just as if the function had an empty body.

The `_` symbol can appear in the modifier multiple times. Each occurrence is replaced with the function body, and the function returns the return value of the final occurrence.

Arbitrary expressions are allowed for modifier arguments and in this context, all symbols visible from the function are visible in the modifier. Symbols introduced in the modifier are not visible in the function (as they might change by overriding).


## Transient Storage

Transient storage is another data location besides memory, storage, calldata (and return-data and code) which was introduced alongside its respective opcodes `TSTORE` and `TLOAD` by EIP-1153. This new data location behaves as a key-value store similar to storage with the main difference being that data in transient storage is not permanent, but is scoped to the current transaction only, after which it will be reset to zero. Since the content of transient storage has very limited lifetime and size, it does not need to be stored permanently as a part of state and the associated gas costs are much lower than in case of storage. EVM version `cancun` or newer is required for transient storage to be available.

Transient storage variables cannot be initialized in place, i.e., they cannot be assigned to upon declaration, since the value would be cleared at the end of the creation transaction, rendering the initialization ineffective. Transient variables will be default value initialized depending on their underlying type. `constant` and `immutable` variables conflict with transient storage, since their values are either inlined or directly stored in code.

Transient storage variables have completely independent address space from storage, so that the order of transient state variables does not affect the layout of storage state variables and vice-versa. They do need distinct names though because all state variables share the same namespace. It is also important to note that the values in transient storage are packed in the same fashion as those in persistent storage. See Storage Layout for more information.

Besides that, transient variables can have visibility as well and `public` ones will have a getter function generated automatically as usual.

Note that, currently, such use of `transient` as a data location is only allowed for value type state variable declarations. Reference types, such as arrays, mappings and structs, as well as local or parameter variables are not yet supported.

An expected canonical use case for transient storage is cheaper reentrancy locks, which can be readily implemented with the opcodes as showcased next.

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.28;

contract Generosity {
    mapping(address => bool) sentGifts;
    bool transient locked;

    modifier nonReentrant {
        require(!locked, "Reentrancy attempt");
        locked = true;
        _;
        // Unlocks the guard, making the pattern composable.
        // After the function exits, it can be called again, even in the same transaction.
        locked = false;
    }

    function claimGift() nonReentrant public {
        require(address(this).balance >= 1 ether);
        require(!sentGifts[msg.sender]);
        (bool success, ) = msg.sender.call{value: 1 ether}("");
        require(success);

        // In a reentrant function, doing this last would open up the vulnerability
        sentGifts[msg.sender] = true;
    }
}
```

Transient storage is private to the contract that owns it, in the same way as persistent storage. Only owning contract frames may access their transient storage, and when they do, all the frames access the same transient store.

Transient storage is part of the EVM state and is subject to the same mutability enforcements as persistent storage. As such, any read access to it is not `pure` and writing access is not `view`.

If the `TSTORE` opcode is called within the context of a `STATICCALL`, it will result in an exception instead of performing the modification. `TLOAD` is allowed within the context of a `STATICCALL`.

When transient storage is used in the context of `DELEGATECALL` or `CALLCODE`, then the owning contract of the transient storage is the contract that issued `DELEGATECALL` or `CALLCODE` instruction (the caller) as with persistent storage. When transient storage is used in the context of `CALL` or `STATICCALL`, then the owning contract of the transient storage is the contract that is the target of the `CALL` or `STATICCALL` instruction (the callee).

Note

In the case of `DELEGATECALL`, since references to transient storage variables are currently not supported, it is not possible to pass those into library calls. In libraries, access to transient storage is only possible using inline assembly.

If a frame reverts, all writes to transient storage that took place between entry to the frame and the return are reverted, including those that took place in inner calls. The caller of an external call may employ a `try ... catch` block to prevent reverts bubbling up from the inner calls.


## Composability of Smart Contracts and the Caveats of Transient Storage

Given the caveats mentioned in the specification of EIP-1153, in order to preserve the composability of your smart contract, utmost care is recommended for more advanced use cases of transient storage.

For smart contracts, composability is a very important design principle to achieve self-contained behaviour, such that multiple calls into individual smart contracts can be composed to more complex applications. So far the EVM largely guaranteed composable behaviour, since multiple calls into a smart contract within a complex transaction are virtually indistinguishable from multiple calls to the contract stretched over several transactions. However, transient storage allows a violation of this principle, and incorrect use may lead to complex bugs that only surface when used across several calls.

Let’s illustrate the problem with a simple example:

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.28;

contract MulService {
    uint transient multiplier;
    function setMultiplier(uint mul) external {
        multiplier = mul;
    }

    function multiply(uint value) external view returns (uint) {
        return value * multiplier;
    }
}
```

and a sequence of external calls:

open in Remix

```solidity
setMultiplier(42);
multiply(1);
multiply(2);
```

If the example used memory or storage to store the multiplier, it would be fully composable. It would not matter whether you split the sequence into separate transactions or grouped them in some way. You would always get the same result: after `multiplier` is set to `42`, the subsequent calls would return `42` and `84` respectively. This enables use cases such as batching calls from multiple transactions together to reduce gas costs. Transient storage potentially breaks such use cases since composability can no longer be taken for granted. In the example, if the calls are not executed in the same transaction, then `multiplier` is reset and the next calls to function `multiply` would always return `0`.

As another example, since transient storage is constructed as a relatively cheap key-value store, a smart contract author may be tempted to use transient storage as a replacement for in-memory mappings without keeping track of the modified keys in the mapping and thereby without clearing the mapping at the end of the call. This, however, can easily lead to unexpected behaviour in complex transactions, in which values set by a previous call into the contract within the same transaction remain.

The use of transient storage for reentrancy locks that are cleared at the end of the call frame into the contract, is safe. However, be sure to resist the temptation to save the 100 gas used for resetting the reentrancy lock, since failing to do so, will restrict your contract to only one call within a transaction, preventing its use in complex composed transactions, which have been a cornerstone for complex applications on chain.

It is recommend to generally always clear transient storage completely at the end of a call into your smart contract to avoid these kinds of issues and to simplify the analysis of the behaviour of your contract within complex transactions. Check the Security Considerations section of EIP-1153 for further details.


## Constant and Immutable State Variables

State variables can be declared as `constant` or `immutable`. In both cases, the variables cannot be modified after the contract has been constructed. For `constant` variables, the value has to be fixed at compile-time, while for `immutable`, it can still be assigned at construction time.

It is also possible to define `constant` variables at the file level.

Every occurrence of such a variable in the source is replaced by its underlying value and the compiler does not reserve a storage slot for it. It cannot be assigned a slot in transient storage using the `transient` keyword either.

Compared to regular state variables, the gas costs of constant and immutable variables are much lower. For a constant variable, the expression assigned to it is copied to all the places where it is accessed and also re-evaluated each time. This allows for local optimizations. Immutable variables are evaluated once at construction time and their value is copied to all the places in the code where they are accessed. For these values, 32 bytes are reserved, even if they would fit in fewer bytes. Due to this, constant values can sometimes be cheaper than immutable values.

Not all types for constants and immutables are implemented at this time. The only supported types are strings (only for constants) and value types.

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.21;

uint constant X = 32**22 + 8;

contract C {
    string constant TEXT = "abc";
    bytes32 constant MY_HASH = keccak256("abc");
    uint immutable decimals = 18;
    uint immutable maxBalance;
    address immutable owner = msg.sender;

    constructor(uint decimals_, address ref) {
        if (decimals_ != 0)
            // Immutables are only immutable when deployed.
            // At construction time they can be assigned to any number of times.
            decimals = decimals_;

        // Assignments to immutables can even access the environment.
        maxBalance = ref.balance;
    }

    function isBalanceTooHigh(address other) public view returns (bool) {
        return other.balance > maxBalance;
    }
}
```

### Constant

For `constant` variables, the value has to be a constant at compile time and it has to be assigned where the variable is declared. Any expression that accesses storage, blockchain data (e.g. `block.timestamp`, `address(this).balance` or `block.number`) or execution data (`msg.value` or `gasleft()`) or makes calls to external contracts is disallowed. Expressions that might have a side-effect on memory allocation are allowed, but those that might have a side-effect on other memory objects are not. The built-in functions `keccak256`, `sha256`, `ripemd160`, `ecrecover`, `addmod` and `mulmod` are allowed (even though, with the exception of `keccak256`, they do call external contracts).

The reason behind allowing side-effects on the memory allocator is that it should be possible to construct complex objects like e.g. lookup-tables. This feature is not yet fully usable.

### Immutable

Variables declared as `immutable` are a bit less restricted than those declared as `constant`: Immutable variables can be assigned a value at construction time. The value can be changed at any time before deployment and then it becomes permanent.

One additional restriction is that immutables can only be assigned to inside expressions for which there is no possibility of being executed after creation. This excludes all modifier definitions and functions other than constructors.

There are no restrictions on reading immutable variables. The read is even allowed to happen before the variable is written to for the first time because variables in Solidity always have a well-defined initial value. For this reason it is also allowed to never explicitly assign a value to an immutable.

Warning

When accessing immutables at construction time, please keep the initialization order in mind. Even if you provide an explicit initializer, some expressions may end up being evaluated before that initializer, especially when they are at a different level in inheritance hierarchy.

Note

Before Solidity 0.8.21 initialization of immutable variables was more restrictive. Such variables had to be initialized exactly once at construction time and could not be read before then.

The contract creation code generated by the compiler will modify the contract’s runtime code before it is returned by replacing all references to immutables with the values assigned to them. This is important if you are comparing the runtime code generated by the compiler with the one actually stored in the blockchain. The compiler outputs where these immutables are located in the deployed bytecode in the `immutableReferences` field of the compiler JSON standard output.


## Custom Storage Layout

A contract can define an arbitrary location for its storage using the `layout` specifier. The contract’s state variables, including those inherited from base contracts, start from the specified base slot instead of the default slot zero.

open in Remix

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.29;

contract C layout at 0xAAAA + 0x11 {
    uint[3] x; // Occupies slots 0xAABB..0xAABD
}
```

As the above example shows, the specifier uses the `layout at <base-slot-expression>` syntax and is located in the header of a contract definition.

The layout specifier can be placed either before or after the inheritance specifier, and can appear at most once. The `base-slot-expression` must be an integer literal expression that can be evaluated at compilation time and yields a value in the range of `uint256`. The use of constants initialized using such expressions and the built-in function erc7201 is also allowed.

A custom layout cannot make contract’s storage “wrap around”. If the selected base slot would push the static variables past the end of storage, the compiler will issue an error. Note that the data areas of dynamic arrays and mappings are not affected by this check because their layout is not linear. Regardless of the base slot used, their locations are calculated in a way that always puts them within the range of `uint256` and their sizes are not known at compilation time.

While there are no other limits placed on the base slot, it is recommended to avoid locations that are too close to the end of the address space. Leaving too little space may complicate contract upgrades or cause problems for contracts that store additional values past their allocated space using inline assembly.

The storage layout can only be specified for the topmost contract of an inheritance tree, and affects locations of all the storage variables in all the contracts in that tree. Variables are laid out according to the order of their definitions and the positions of their contracts in the linearized inheritance hierarchy and a custom base slot preserves their relative positions, shifting them all by the same amount.

The storage layout cannot be specified for abstract contracts, interfaces and libraries. Also, it is important to note that it does *not* affect transient state variables.

For details about storage layout and the effect of the layout specifier on it see layout of storage variables.

Warning

The identifiers `layout` and `at` are not yet reserved as keywords in the language. It is strongly recommended to avoid using them since they will become reserved in a future breaking release.
