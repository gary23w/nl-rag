---
title: "Adapter pattern"
source: https://en.wikipedia.org/wiki/Adapter_pattern
domain: software-design
license: CC-BY-SA-4.0
tags: design pattern, software architecture, software design, refactoring
fetched: 2026-07-02
---

# Adapter pattern

In software engineering, the **adapter pattern** is a software design pattern (also known as wrapper, an alternative naming shared with the decorator pattern) that allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.

An example is an adapter that converts the interface of a Document Object Model of an XML document into a tree structure that can be displayed.

## Overview

The adapter design pattern is one of the twenty-three well-known Gang of Four design patterns that describe how to solve recurring design problems to design flexible and reusable object-oriented software, that is, objects that are easier to implement, change, test, and reuse.

The adapter design pattern solves problems like:

- How can a class be reused that does not have an interface that a client requires?
- How can classes that have incompatible interfaces work together?
- How can an alternative interface be provided for a class?

Often an (already existing) class can not be reused only because its interface does not conform to the interface clients require.

The adapter design pattern describes how to solve such problems:

- Define a separate `adapter` class that converts the (incompatible) interface of a class (`adaptee`) into another interface (`target`) clients require.
- Work through an `adapter` to work with (reuse) classes that do not have the required interface.

The key idea in this pattern is to work through a separate `adapter` that adapts the interface of an (already existing) class without changing it.

Clients don't know whether they work with a `target` class directly or through an `adapter` with a class that does not have the `target` interface.

See also the UML class diagram below.

## Definition

An adapter allows two incompatible interfaces to work together. This is the real-world definition for an adapter. Interfaces may be incompatible, but the inner functionality should suit the need. The adapter design pattern allows otherwise incompatible classes to work together by converting the interface of one class into an interface expected by the clients.

## Usage

An adapter can be used when the wrapper must respect a particular interface and must support polymorphic behavior. Alternatively, a decorator pattern makes it possible to add or alter behavior of an interface at run-time, and a facade pattern is used when an easier or simpler interface to an underlying object is desired.

| Pattern | Intent |
|---|---|
| Adapter or wrapper | Converts one interface to another so that it matches what the client is expecting |
| Decorator | Dynamically adds responsibility to the interface by wrapping the original code |
| Delegation | Support "composition over inheritance" |
| Facade | Provides a simplified interface |

## Structure

### UML class diagram

In the above UML class diagram, the `client` class that requires a `target` interface cannot reuse the `adaptee` class directly because its interface doesn't conform to the `target` interface. Instead, the `client` works through an `adapter` class that implements the `target` interface in terms of `adaptee`:

- The `object adapter` way implements the `target` interface by delegating to an `adaptee` object at run-time (`adaptee.specificOperation()`).
- The `class adapter` way implements the `target` interface by inheriting from an `adaptee` class at compile-time (`specificOperation()`).

### Object adapter pattern

In this adapter pattern, the adapter contains an instance of the class it wraps. In this situation, the adapter makes calls to the instance of the wrapped object.

### Class adapter pattern

This adapter pattern uses multiple polymorphic interfaces implementing or inheriting both the interface that is expected and the interface that is pre-existing. It is typical for the expected interface to be created as a pure interface class, especially in languages such as Java (before JDK 1.8) that do not support multiple inheritance of classes.

### A further form of runtime adapter pattern

#### Motivation from compile time solution

It is desired for `classA` to supply `classB` with some data, let us suppose some `String` data. A compile time solution is:

```mw
classB.setStringData(classA.getStringData());
```

However, suppose that the format of the string data must be varied. A compile time solution is to use inheritance:

```mw
public class Format1ClassA extends ClassA {
    @Override
    public String getStringData() {
        return format(toString());
    }
}
```

and perhaps create the correctly "formatting" object at runtime by means of the factory pattern.

#### Run-time adapter solution

A solution using "adapters" proceeds as follows:

1. Define an intermediary "provider" interface, and write an implementation of that provider interface that wraps the source of the data, `ClassA` in this example, and outputs the data formatted as appropriate: interface StringProvider { public String getStringData(); } public class ClassAFormat1 implements StringProvider { private ClassA classA = null; public ClassAFormat1(final ClassA a) { classA = a; } public String getStringData() { return format(classA.getStringData()); } private String format(final String sourceValue) { // Manipulate the source string into a format required // by the object needing the source object's data return sourceValue.trim(); } }
2. Write an adapter class that returns the specific implementation of the provider: public class ClassAFormat1Adapter extends Adapter { public Object adapt(final Object anObject) { return new ClassAFormat1((ClassA) anObject); } }
3. Register the `adapter` with a global registry, so that the `adapter` can be looked up at runtime: AdapterFactory.getInstance().registerAdapter(ClassA.class, ClassAFormat1Adapter.class, "format1");
4. In code, when wishing to transfer data from `ClassA` to `ClassB`, write: Adapter adapter = AdapterFactory.getInstance() .getAdapterFromTo(ClassA.class, StringProvider.class, "format1"); StringProvider provider = (StringProvider) adapter.adapt(classA); String string = provider.getStringData(); classB.setStringData(string); or more concisely: classB.setStringData(((StringProvider)AdapterFactory.getInstance() .getAdapterFromTo(ClassA.class, StringProvider.class, "format1") .adapt(classA)) .getStringData() );
5. The advantage can be seen in that, if it is desired to transfer the data in a second format, then look up the different adapter/provider: Adapter adapter = AdapterFactory.getInstance() .getAdapterFromTo(ClassA.class, StringProvider.class, "format2");
6. And if it is desired to output the data from `ClassA` as, say, image data in `Class C`: Adapter adapter = AdapterFactory.getInstance() .getAdapterFromTo(ClassA.class, ImageProvider.class, "format2"); ImageProvider provider = (ImageProvider) adapter.adapt(classA); classC.setImage(provider.getImage());
7. In this way, the use of adapters and providers allows multiple "views" by `ClassB` and `ClassC` into `ClassA` without having to alter the class hierarchy. In general, it permits a mechanism for arbitrary data flows between objects that can be retrofitted to an existing object hierarchy.

### Implementation of the adapter pattern

When implementing the adapter pattern, for clarity, one can apply the class name `[ClassName]To[Interface]Adapter` to the provider implementation; for example, `DAOToProviderAdapter`. It should have a constructor method with an adaptee class variable as a parameter. This parameter will be passed to an instance member of `[ClassName]To[Interface]Adapter`. When the clientMethod is called, it will have access to the adaptee instance that allows for accessing the required data of the adaptee and performing operations on that data that generates the desired output.

#### Java

```mw
package org.wikipedia.examples;

interface ILightningPhone {
    void recharge();
    void useLightning();
}

interface IMicroUsbPhone {
    void recharge();
    void useMicroUsb();
}

class Iphone implements ILightningPhone {
    private boolean connector;

    @Override
    public void useLightning() {
        connector = true;
        System.out.println("Lightning connected");
    }

    @Override
    public void recharge() {
        if (connector) {
            System.out.println("Recharge started");
            System.out.println("Recharge finished");
        } else {
            System.out.println("Connect Lightning first");
        }
    }
}

class Android implements IMicroUsbPhone {
    private boolean connector;

    @Override
    public void useMicroUsb() {
        connector = true;
        System.out.println("MicroUsb connected");
    }

    @Override
    public void recharge() {
        if (connector) {
            System.out.println("Recharge started");
            System.out.println("Recharge finished");
        } else {
            System.out.println("Connect MicroUsb first");
        }
    }
}
/* exposing the target interface while wrapping source object */
class LightningToMicroUsbAdapter implements IMicroUsbPhone {
    private final ILightningPhone lightningPhone;

    public LightningToMicroUsbAdapter(ILightningPhone lightningPhone) {
        this.lightningPhone = lightningPhone;
    }

    @Override
    public void useMicroUsb() {
        System.out.println("MicroUsb connected");
        lightningPhone.useLightning();
    }

    @Override
    public void recharge() {
        lightningPhone.recharge();
    }
}

public class AdapterDemo {
    static void rechargeMicroUsbPhone(IMicroUsbPhone phone) {
        phone.useMicroUsb();
        phone.recharge();
    }

    static void rechargeLightningPhone(ILightningPhone phone) {
        phone.useLightning();
        phone.recharge();
    }

    public static void main(String[] args) {
        Android android = new Android();
        Iphone iPhone = new Iphone();

        System.out.println("Recharging android with MicroUsb");
        rechargeMicroUsbPhone(android);

        System.out.println("Recharging iPhone with Lightning");
        rechargeLightningPhone(iPhone);

        System.out.println("Recharging iPhone with MicroUsb");
        rechargeMicroUsbPhone(new LightningToMicroUsbAdapter(iPhone));
    }
}
```

Output

```
Recharging android with MicroUsb
MicroUsb connected
Recharge started
Recharge finished
Recharging iPhone with Lightning
Lightning connected
Recharge started
Recharge finished
Recharging iPhone with MicroUsb
MicroUsb connected
Lightning connected
Recharge started
Recharge finished
```

#### Python

```mw
"""
Adapter pattern example.
"""
from abc import ABCMeta, abstractmethod
from typing import NoReturn

RECHARGE: list[str] = ["Recharge started.", "Recharge finished."]
POWER_ADAPTERS: dict[str, str] = {"Android": "MicroUSB", "iPhone": "Lightning"}
CONNECTED_MSG: str = "{} connected."
CONNECT_FIRST_MSG: str = "Connect {} first."

class RechargeTemplate(metaclass = ABCMeta):
    @abstractmethod
    def recharge(self) -> NoReturn:
        raise NotImplementedError("You should implement this.")

class FormatIPhone(RechargeTemplate):
    @abstractmethod
    def use_lightning(self) -> NoReturn:
        raise NotImplementedError("You should implement this.")

class FormatAndroid(RechargeTemplate):
    @abstractmethod
    def use_micro_usb(self) -> NoReturn:
        raise NotImplementedError("You should implement this.")

class IPhone(FormatIPhone):
    __name__: str = "iPhone"

    def __init__(self):
        self.connector: bool = False

    def use_lightning(self) -> None:
        self.connector = True
        print(CONNECTED_MSG.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self) -> None:
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST_MSG.format(POWER_ADAPTERS[self.__name__]))

class Android(FormatAndroid):
    __name__: str = "Android"

    def __init__(self) -> None:
        self.connector: bool = False

    def use_micro_usb(self) -> None:
        self.connector = True
        print(CONNECTED_MSG.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self) -> None:
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST_MSG.format(POWER_ADAPTERS[self.__name__]))

class IPhoneAdapter(FormatAndroid):
    def __init__(self, mobile: FormatAndroid) -> None:
        self.mobile: FormatAndroid = mobile

    def recharge(self) -> None:
        self.mobile.recharge()

    def use_micro_usb(self) -> None:
        print(CONNECTED_MSG.format(POWER_ADAPTERS["Android"]))
        self.mobile.use_lightning()

class AndroidRecharger:
    def __init__(self) -> None:
        self.phone: Android = Android()
        self.phone.use_micro_usb()
        self.phone.recharge()

class IPhoneMicroUSBRecharger:
    def __init__(self) -> None:
        self.phone: IPhone = IPhone()
        self.phone_adapter: IPhoneAdapter = IPhoneAdapter(self.phone)
        self.phone_adapter.use_micro_usb()
        self.phone_adapter.recharge()

class IPhoneRecharger:
    def __init__(self) -> None:
        self.phone: IPhone = IPhone()
        self.phone.use_lightning()
        self.phone.recharge()

print("Recharging Android with MicroUSB recharger.")
AndroidRecharger()
print()

print("Recharging iPhone with MicroUSB using adapter pattern.")
IPhoneMicroUSBRecharger()
print()

print("Recharging iPhone with iPhone recharger.")
IPhoneRecharger()
```

#### C

```mw
namespace Wikipedia.Examples;

using System;

interface ILightningPhone
{
	void ConnectLightning();
	void Recharge();
}

interface IUsbPhone
{
	void ConnectUsb();
	void Recharge();
}

sealed class AndroidPhone : IUsbPhone
{
	private bool isConnected;

	public void ConnectUsb()
	{
		this.isConnected = true;
		Console.WriteLine("Android phone connected.");
	}

	public void Recharge()
	{
		if (this.isConnected)
		{
			Console.WriteLine("Android phone recharging.");
		}
		else
		{
			Console.WriteLine("Connect the USB cable first.");
		}
	}
}

sealed class ApplePhone : ILightningPhone
{
	private bool isConnected;

	public void ConnectLightning()
	{
		this.isConnected = true;
		Console.WriteLine("Apple phone connected.");
	}

	public void Recharge()
	{
		if (this.isConnected)
		{
			Console.WriteLine("Apple phone recharging.");
		}
		else
		{
			Console.WriteLine("Connect the Lightning cable first.");
		}
	}
}

sealed class LightningToUsbAdapter : IUsbPhone
{
	private readonly ILightningPhone lightningPhone;

	private bool isConnected;

	public LightningToUsbAdapter(ILightningPhone lightningPhone)
	{
		this.lightningPhone = lightningPhone;
	}

	public void ConnectUsb()
	{
		this.lightningPhone.ConnectLightning();
	}

	public void Recharge()
	{
		this.lightningPhone.Recharge();
	}
}

public class AdapterDemo
{
    static void Main(string[] args)
    {
	    ILightningPhone applePhone = new ApplePhone();
	    IUsbPhone adapterCable = new LightningToUsbAdapter(applePhone);
	    adapterCable.ConnectUsb();
	    adapterCable.Recharge();
    }
}
```

Output:

```mw
Apple phone connected.
Apple phone recharging.
```
