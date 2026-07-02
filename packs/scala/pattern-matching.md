---
title: "Pattern Matching"
source: https://docs.scala-lang.org/tour/pattern-matching.html
domain: scala
license: CC-BY-SA-4.0
tags: scala, scala 3, sbt
fetched: 2026-07-02
---

# Pattern Matching

Tour of Scala

# Pattern Matching

Language

Pattern matching is a mechanism for checking a value against a pattern. A successful match can also deconstruct a value into its constituent parts. It is a more powerful version of the `switch` statement in Java and it can likewise be used in place of a series of if/else statements.

## Syntax

A match expression has a value, the `match` keyword, and at least one `case` clause.

```scala
import scala.util.Random

val x: Int = Random.nextInt(10)

x match {
  case 0 => "zero"
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
}
```

```scala
import scala.util.Random

val x: Int = Random.nextInt(10)

x match
  case 0 => "zero"
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
```

The `val x` above is a random integer between 0 and 9. `x` becomes the left operand of the `match` operator and on the right is an expression with four cases. The last case `_` is a “catch all” case for any other possible `Int` values. Cases are also called *alternatives*.

Match expressions have a value.

```scala
def matchTest(x: Int): String = x match {
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
}
matchTest(3)  // returns other
matchTest(1)  // returns one
```

```scala
def matchTest(x: Int): String = x match
  case 1 => "one"
  case 2 => "two"
  case _ => "other"

matchTest(3)  // returns other
matchTest(1)  // returns one
```

This match expression has a type String because all of the cases return String. Therefore, the function `matchTest` returns a String.

## Matching on case classes

Case classes are especially useful for pattern matching.

```scala
sealed trait Notification

case class Email(sender: String, title: String, body: String) extends Notification

case class SMS(caller: String, message: String) extends Notification

case class VoiceRecording(contactName: String, link: String) extends Notification
```

`Notification` is a sealed trait which has three concrete Notification types implemented with case classes `Email`, `SMS`, and `VoiceRecording`. (A sealed trait can be extended only in the same file as its declaration.) Now we can do pattern matching on these case classes:

```scala
def showNotification(notification: Notification): String = {
  notification match {
    case Email(sender, title, _) =>
      s"You got an email from $sender with title: $title"
    case SMS(number, message) =>
      s"You got an SMS from $number! Message: $message"
    case VoiceRecording(name, link) =>
      s"You received a Voice Recording from $name! Click the link to hear it: $link"
  }
}
val someSms = SMS("12345", "Are you there?")
val someVoiceRecording = VoiceRecording("Tom", "voicerecording.org/id/123")

println(showNotification(someSms))  // prints You got an SMS from 12345! Message: Are you there?

println(showNotification(someVoiceRecording))  // prints You received a Voice Recording from Tom! Click the link to hear it: voicerecording.org/id/123
```

```scala
def showNotification(notification: Notification): String =
  notification match
    case Email(sender, title, _) =>
      s"You got an email from $sender with title: $title"
    case SMS(number, message) =>
      s"You got an SMS from $number! Message: $message"
    case VoiceRecording(name, link) =>
      s"You received a Voice Recording from $name! Click the link to hear it: $link"

val someSms = SMS("12345", "Are you there?")
val someVoiceRecording = VoiceRecording("Tom", "voicerecording.org/id/123")

println(showNotification(someSms))  // prints You got an SMS from 12345! Message: Are you there?

println(showNotification(someVoiceRecording))  // prints You received a Voice Recording from Tom! Click the link to hear it: voicerecording.org/id/123
```

The function `showNotification` takes as a parameter the abstract type `Notification` and matches on the type of `Notification` (i.e. it figures out whether it’s an `Email`, `SMS`, or `VoiceRecording`). In the `case Email(sender, title, _)` the fields `sender` and `title` are used in the return value but the `body` field is ignored with `_`.

## Matching on string

The `s`-interpolator allows embedding variables in strings and is also useful for pattern matching.

```scala
val input: String = "Alice is 25 years old"

input match {
  case s"$name is $age years old" => s"$name's age is $age"
  case _ => "No match"
}
// Result: "Alice's age is 25"
```

```scala
val input: String = "Alice is 25 years old"

input match
  case s"$name is $age years old" => s"$name's age is $age"
  case _ => "No match"
// Result: "Alice's age is 25"
```

In this example, name and age extract parts of the string based on the pattern. This is helpful for parsing structured text.

We can also use extractor objects for string pattern matching.

```scala
object Age {
  def unapply(s: String): Option[Int] = s.toIntOption
}

val input: String = "Alice is 25 years old"

val (name, age) = input match {
  case s"$name is ${Age(age)} years old" => (name, age)
}
// name: String = Alice
// age: Int = 25
```

```scala
object Age:
  def unapply(s: String): Option[Int] = s.toIntOption

val input: String = "Alice is 25 years old"

val (name, age) = input match
  case s"$name is ${Age(age)} years old" => (name, age)
// name: String = Alice
// age: Int = 25
```

## Pattern guards

Pattern guards are boolean expressions which are used to make cases more specific. Just add `if <boolean expression>` after the pattern.

```scala
def showImportantNotification(notification: Notification, importantPeopleInfo: Seq[String]): String = {
  notification match {
    case Email(sender, _, _) if importantPeopleInfo.contains(sender) =>
      "You got an email from special someone!"
    case SMS(number, _) if importantPeopleInfo.contains(number) =>
      "You got an SMS from special someone!"
    case other =>
      showNotification(other) // nothing special, delegate to our original showNotification function
  }
}

val importantPeopleInfo = Seq("867-5309", "[email protected]")

val someSms = SMS("123-4567", "Are you there?")
val someVoiceRecording = VoiceRecording("Tom", "voicerecording.org/id/123")
val importantEmail = Email("[email protected]", "Drinks tonight?", "I'm free after 5!")
val importantSms = SMS("867-5309", "I'm here! Where are you?")

println(showImportantNotification(someSms, importantPeopleInfo)) // prints You got an SMS from 123-4567! Message: Are you there?
println(showImportantNotification(someVoiceRecording, importantPeopleInfo)) // prints You received a Voice Recording from Tom! Click the link to hear it: voicerecording.org/id/123
println(showImportantNotification(importantEmail, importantPeopleInfo)) // prints You got an email from special someone!

println(showImportantNotification(importantSms, importantPeopleInfo)) // prints You got an SMS from special someone!
```

```scala
def showImportantNotification(notification: Notification, importantPeopleInfo: Seq[String]): String =
  notification match
    case Email(sender, _, _) if importantPeopleInfo.contains(sender) =>
      "You got an email from special someone!"
    case SMS(number, _) if importantPeopleInfo.contains(number) =>
      "You got an SMS from special someone!"
    case other =>
      showNotification(other) // nothing special, delegate to our original showNotification function

val importantPeopleInfo = Seq("867-5309", "[email protected]")

val someSms = SMS("123-4567", "Are you there?")
val someVoiceRecording = VoiceRecording("Tom", "voicerecording.org/id/123")
val importantEmail = Email("[email protected]", "Drinks tonight?", "I'm free after 5!")
val importantSms = SMS("867-5309", "I'm here! Where are you?")

println(showImportantNotification(someSms, importantPeopleInfo)) // prints You got an SMS from 123-4567! Message: Are you there?
println(showImportantNotification(someVoiceRecording, importantPeopleInfo)) // prints You received a Voice Recording from Tom! Click the link to hear it: voicerecording.org/id/123
println(showImportantNotification(importantEmail, importantPeopleInfo)) // prints You got an email from special someone!

println(showImportantNotification(importantSms, importantPeopleInfo)) // prints You got an SMS from special someone!
```

In the `case Email(sender, _, _) if importantPeopleInfo.contains(sender)`, the pattern is matched only if the `sender` is in the list of important people.

## Matching on type only

You can match on the type like so:

```scala
sealed trait Device
case class Phone(model: String) extends Device {
  def screenOff = "Turning screen off"
}
case class Computer(model: String) extends Device {
  def screenSaverOn = "Turning screen saver on..."
}

def goIdle(device: Device): String = device match {
  case p: Phone => p.screenOff
  case c: Computer => c.screenSaverOn
}
```

```scala
sealed trait Device
case class Phone(model: String) extends Device:
  def screenOff = "Turning screen off"

case class Computer(model: String) extends Device:
  def screenSaverOn = "Turning screen saver on..."

def goIdle(device: Device): String = device match
  case p: Phone => p.screenOff
  case c: Computer => c.screenSaverOn
```

`def goIdle` has a different behavior depending on the type of `Device`. This is useful when the case needs to call a method on the pattern. It is a convention to use the first letter of the type as the case identifier (`p` and `c` in this case).

## Binding matched patterns to variables

You can use variable binding to get type-dependent behavior while simultaneously extracting fields from the matched pattern.

```scala
def goIdleWithModel(device: Device): String = device match {
  case p @ Phone(model) => s"$model: ${p.screenOff}" 
  case c @ Computer(model) => s"$model: ${c.screenSaverOn}"
}
```

```scala
def goIdleWithModel(device: Device): String = device match
  case p @ Phone(model) => s"$model: ${p.screenOff}"
  case c @ Computer(model) => s"$model: ${c.screenSaverOn}"
```

## Sealed types

You may have noticed that in the examples above the base types are qualified with the keyword `sealed`. This provides extra safety because the compiler checks that the `cases` of a `match` expression are exhaustive when the base type is `sealed`.

For instance, in the method `showNotification` defined above, if we forget one case, say, `VoiceRecording`, the compiler emits a warning:

```scala
def showNotification(notification: Notification): String = {
  notification match {
    case Email(sender, title, _) =>
      s"You got an email from $sender with title: $title"
    case SMS(number, message) =>
      s"You got an SMS from $number! Message: $message"
  }
}
```

```scala
def showNotification(notification: Notification): String =
  notification match
    case Email(sender, title, _) =>
      s"You got an email from $sender with title: $title"
    case SMS(number, message) =>
      s"You got an SMS from $number! Message: $message"
```

This definition produces the following warning:

```plaintext
match may not be exhaustive.

It would fail on pattern case: VoiceRecording(_, _)
```

The compiler even provides examples of input that would fail!

On the flip side, exhaustivity checking requires you to define all the subtypes of the base type in the same file as the base type (otherwise, the compiler would not know what are all the possible cases). For instance, if you try to define a new type of `Notification` outside of the file that defines the `sealed trait Notification`, it will produce a compilation error:

```plaintext
case class Telepathy(message: String) extends Notification
           ^
        Cannot extend sealed trait Notification in a different source file
```

## More resources

- More details on match expressions in the Scala Book

←

previous

next

→

### Contributors to this page:
