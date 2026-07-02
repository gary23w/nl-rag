---
title: "PHP: The Basics"
source: https://www.php.net/manual/en/language.oop5.basic.php
domain: php-manual
license: PHP-3.01 (docs CC-BY-3.0)
tags: php, php manual, php function, php script
fetched: 2026-07-02
---

# PHP: The Basics

PHP 8.2.32 Released!

## The Basics

### class

Basic class definitions begin with the keyword `class`, followed by a class name, followed by a pair of curly braces which enclose the definitions of the properties and methods belonging to the class.

The class name can be any valid label, provided it is not a PHP reserved word. As of PHP 8.4.0, using a single underscore `_` as a class name is deprecated. A valid class name starts with a letter or underscore, followed by any number of letters, numbers, or underscores. As a regular expression, it would be expressed thus: `^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$`.

A class may contain its own constants, variables (called "properties"), and functions (called "methods").

**Example #1 Simple Class definition**

The pseudo-variable *$this* is available when a method is called from within an object context. *$this* is the value of the calling object.

Warning

Calling a non-static method statically throws an Error. Prior to PHP 8.0.0, this would generate a deprecation notice, and *$this* would be undefined.

**Example #2 Some examples of the *$this* pseudo-variable**

#### Readonly classes

As of PHP 8.2.0, a class can be marked with the readonly modifier. Marking a class as readonly will add the readonly modifier to every declared property, and prevent the creation of dynamic properties. Moreover, it is impossible to add support for them by using the AllowDynamicProperties attribute. Attempting to do so will trigger a compile-time error.

As neither untyped nor static properties can be marked with the `readonly` modifier, readonly classes cannot declare them either:

A readonly class can be extended if, and only if, the child class is also a readonly class.

### new

To create an instance of a class, the `new` keyword must be used. An object will always be created unless the object has a constructor defined that throws an exception on error. Classes should be defined before instantiation (and in some cases this is a requirement).

If a variable containing a string with the name of a class is used with `new`, a new instance of that class will be created. If the class is in a namespace, its fully qualified name must be used when doing this.

> **Note**:
> 
> If there are no arguments to be passed to the class's constructor, parentheses after the class name may be omitted.

**Example #3 Creating an instance**

As of PHP 8.0.0, using `new` with arbitrary expressions is supported. This allows more complex instantiation if the expression produces a string. The expressions must be wrapped in parentheses.

**Example #4 Creating an instance using an arbitrary expression**

In the class context, it is possible to create a new object by `new self` and `new parent`.

When assigning an already created instance of a class to a new variable, the new variable will access the same instance as the object that was assigned. This behaviour is the same when passing instances to a function. A copy of an already created object can be made by cloning it.

**Example #5 Object Assignment**

It's possible to create instances of an object in a couple of ways:

**Example #6 Creating new objects**

It is possible to access a member of a newly created object in a single expression:

**Example #7 Access member of newly created object**

> **Note**: Prior to PHP 7.1, the arguments are not evaluated if there is no constructor function defined.

### Properties and methods

Class properties and methods live in separate "namespaces", so it is possible to have a property and a method with the same name. Referring to both a property and a method has the same notation, and whether a property will be accessed or a method will be called, solely depends on the context, i.e. whether the usage is a variable access or a function call.

**Example #8 Property access vs. method call**

That means that calling an anonymous function which has been assigned to a property is not directly possible. Instead the property has to be assigned to a variable first, for instance. It is possible to call such a property directly by enclosing it in parentheses.

**Example #9 Calling an anonymous function stored in a property**

### extends

A class can inherit the constants, methods, and properties of another class by using the keyword `extends` in the class declaration. It is not possible to extend multiple classes; a class can only inherit from one base class.

The inherited constants, methods, and properties can be overridden by redeclaring them with the same name defined in the parent class. However, if the parent class has defined a method or constant as final, they may not be overridden. It is possible to access the overridden methods or static properties by referencing them with parent::.

> **Note**: As of PHP 8.1.0, constants may be declared as final.

**Example #10 Simple Class Inheritance**

#### Signature compatibility rules

When overriding a method, its signature must be compatible with the parent method. Otherwise, a fatal error is emitted, or, prior to PHP 8.0.0, an **`E_WARNING`** level error is generated. A signature is compatible if it respects the variance rules, makes a mandatory parameter optional, adds only optional new parameters and doesn't restrict but only relaxes the visibility. This is known as the Liskov Substitution Principle, or LSP for short. The constructor, and `private` methods are exempt from these signature compatibility rules, and thus won't emit a fatal error in case of a signature mismatch.

**Example #11 Compatible child methods**

The following examples demonstrate that a child method which removes a parameter, or makes an optional parameter mandatory, is not compatible with the parent method.

**Example #12 Fatal error when a child method removes a parameter**

**Example #13 Fatal error when a child method makes an optional parameter mandatory**

Warning

Renaming a method's parameter in a child class is not a signature incompatibility. However, this is discouraged as it will result in a runtime Error if named arguments are used.

**Example #14 Error when using named arguments and parameters were renamed in a child class**

### ::class

The `class` keyword is also used for class name resolution. To obtain the fully qualified name of a class `ClassName` use `ClassName::class`. This is particularly useful with namespaced classes.

**Example #15 Class name resolution**

> **Note**:
> 
> The class name resolution using `::class` is a compile time transformation. That means at the time the class name string is created no autoloading has happened yet. As a consequence, class names are expanded even if the class does not exist. No error is issued in that case.
> 
> **Example #16 Missing class name resolution**

As of PHP 8.0.0, `::class` may also be used on objects. This resolution happens at runtime, not compile time. Its effect is the same as calling get_class() on the object.

**Example #17 Object name resolution**

### Nullsafe methods and properties

As of PHP 8.0.0, properties and methods may also be accessed with the "nullsafe" operator instead: `?->`. The nullsafe operator works the same as property or method access as above, except that if the object being dereferenced is **`null`** then **`null`** will be returned rather than an exception thrown. If the dereference is part of a chain, the rest of the chain is skipped.

The effect is similar to wrapping each access in an is_null() check first, but more compact.

**Example #18 Nullsafe Operator**

> **Note**:
> 
> The nullsafe operator is best used when null is considered a valid and expected possible value for a property or method return. For indicating an error, a thrown exception is preferable.

### Found A Problem?

＋

add a note

### User Contributed Notes 15 notes

up

down

666

aaron at thatone dot com

¶

18 years ago

```
I was confused at first about object assignment, because it's not quite the same as normal assignment or assignment by reference. But I think I've figured out what's going on.

First, think of variables in PHP as data slots. Each one is a name that points to a data slot that can hold a value that is one of the basic data types: a number, a string, a boolean, etc. When you create a reference, you are making a second name that points at the same data slot. When you assign one variable to another, you are copying the contents of one data slot to another data slot.

Now, the trick is that object instances are not like the basic data types. They cannot be held in the data slots directly. Instead, an object's "handle" goes in the data slot. This is an identifier that points at one particular instance of an obect. So, the object handle, although not directly visible to the programmer, is one of the basic datatypes. 

What makes this tricky is that when you take a variable which holds an object handle, and you assign it to another variable, that other variable gets a copy of the same object handle. This means that both variables can change the state of the same object instance. But they are not references, so if one of the variables is assigned a new value, it does not affect the other variable.

<?php
Class Object{
   public $foo="bar";
};

$objectVar = new Object();
$reference =& $objectVar;
$assignment = $objectVar

?>

$assignment has a different data slot from $objectVar, but its data slot holds a handle to the same object. This makes it behave in some ways like a reference. If you use the variable $objectVar to change the state of the Object instance, those changes also show up under $assignment, because it is pointing at that same Object instance.

<?php
$objectVar->foo = "qux";
print_r( $objectVar );
print_r( $reference );
print_r( $assignment );

?>

But it is not exactly the same as a reference. If you null out $objectVar, you replace the handle in its data slot with NULL. This means that $reference, which points at the same data slot, will also be NULL. But $assignment, which is a different data slot, will still hold its copy of the handle to the Object instance, so it will not be NULL.

<?php
$objectVar = null;
print_r($objectVar);
print_r($reference);
print_r($assignment);

?>
```

up

down

98

kStarbe at gmail point com

¶

9 years ago

```
You start using :: in second example although the static concept has not been explained. This is not easy to discover when you are starting from the basics.
```

up

down

134

Doug

¶

15 years ago

```
What is the difference between  $this  and  self ?

Inside a class definition, $this refers to the current object, while  self  refers to the current class.

It is necessary to refer to a class element using  self ,
and refer to an object element using  $this .
Note also how an object variable must be preceded by a keyword in its definition.

The following example illustrates a few cases:

<?php
class Classy {

const       STAT = 'S' ; static     $stat = 'Static' ;
public     $publ = 'Public' ;
private    $priv = 'Private' ;
protected  $prot = 'Protected' ;

function __construct( ){  }

public function showMe( ){
    print '<br> self::STAT: '  .  self::STAT ; print '<br> self::$stat: ' . self::$stat ; print '<br>$this->stat: '  . $this->stat ; print '<br>$this->publ: '  . $this->publ ; print '<br>' ;
}
}
$me = new Classy( ) ;
$me->showMe( ) ;

?>
```

up

down

10

johannes dot kingma at gmail dot com

¶

4 years ago

```
BEWARE! 

Like Hayley Watson pointed out class names are not case sensitive. 

<?php
class Foo{}
class foo{} ?>
As well as
<?php
class BAR{}
$bar = new Bar();
echo get_class($bar);
?> 

Is perfectly fine and will return 'BAR'.

This has implications on autoloading classes though. The standard spl_autoload function will strtolower the class name to cope with case in-sensitiveness and thus the class BAR can only be found if the file name is bar.php (or another variety if an extension was registered with spl_autoload_extensions(); ) not BAR.php for a case sensitive file and operating system like linux. Windows file system is case sensitive but the OS is not  and there for autoloading BAR.php will work.
```

up

down

73

wbcarts at juno dot com

¶

17 years ago

```
CLASSES and OBJECTS that represent the "Ideal World"

Wouldn't it be great to get the lawn mowed by saying $son->mowLawn()? Assuming the function mowLawn() is defined, and you have a son that doesn't throw errors, the lawn will be mowed. 

In the following example; let objects of type Line3D measure their own length in 3-dimensional space. Why should I or PHP have to provide another method from outside this class to calculate length, when the class itself holds all the neccessary data and has the education to make the calculation for itself?

<?php

class Point3D
{
    public $x;
    public $y;
    public $z;                  public function __construct($xCoord=0, $yCoord=0, $zCoord=0)
    {
        $this->x = $xCoord;
    $this->y = $yCoord;
        $this->z = $zCoord;
    }

    public function __toString()
    {
        return 'Point3D(x=' . $this->x . ', y=' . $this->y . ', z=' . $this->z . ')';
    }
}

class Line3D
{
    $start;
    $end;

    public function __construct($xCoord1=0, $yCoord1=0, $zCoord1=0, $xCoord2=1, $yCoord2=1, $zCoord2=1)
    {
        $this->start = new Point3D($xCoord1, $yCoord1, $zCoord1);
        $this->end = new Point3D($xCoord2, $yCoord2, $zCoord2);
    }

    public function getLength()
    {
        return sqrt(
            pow($this->start->x - $this->end->x, 2) +
            pow($this->start->y - $this->end->y, 2) +
            pow($this->start->z - $this->end->z, 2)
        );
    }

    public function __toString()
    {
        return 'Line3D[start=' . $this->start .
            ', end=' . $this->end .
            ', length=' . $this->getLength() . ']';
    }
}

echo '<p>' . (new Line3D()) . "</p>\n";
echo '<p>' . (new Line3D(0, 0, 0, 100, 100, 0)) . "</p>\n";
echo '<p>' . (new Line3D(0, 0, 0, 100, 100, 100)) . "</p>\n";

?>

  <--  The results look like this  -->

Line3D[start=Point3D(x=0, y=0, z=0), end=Point3D(x=1, y=1, z=1), length=1.73205080757]

Line3D[start=Point3D(x=0, y=0, z=0), end=Point3D(x=100, y=100, z=0), length=141.421356237]

Line3D[start=Point3D(x=0, y=0, z=0), end=Point3D(x=100, y=100, z=100), length=173.205080757]

My absolute favorite thing about OOP is that "good" objects keep themselves in check. I mean really, it's the exact same thing in reality... like, if you hire a plumber to fix your kitchen sink, wouldn't you expect him to figure out the best plan of attack? Wouldn't he dislike the fact that you want to control the whole job? Wouldn't you expect him to not give you additional problems? And for god's sake, it is too much to ask that he cleans up before he leaves?

I say, design your classes well, so they can do their jobs uninterrupted... who like bad news? And, if your classes and objects are well defined, educated, and have all the necessary data to work on (like the examples above do), you won't have to micro-manage the whole program from outside of the class. In other words... create an object, and LET IT RIP!
```

up

down

25

Hayley Watson

¶

8 years ago

```
Class names are case-insensitive:
<?php
class Foo{}
class foo{} ?>

Any casing can be used to refer to the class
<?php
class bAr{}
$t = new Bar();
$u = new bar();
echo ($t instanceof $u) ? "true" : "false"; echo ($t instanceof BAR) ? "true" : "false"; echo is_a($u, 'baR') ? "true" : "false"; ?>

But the case used when the class was defined is preserved as "canonical":
<?php
echo get_class($t); ?>

And, as always, "case-insensitivity" only applies to ASCII.
<?php
class пасха{}
class Пасха{} $p = new ПАСХА(); ?>
```

up

down

32

moty66 at gmail dot com

¶

16 years ago

```
I hope that this will help to understand how to work with static variables inside a class

<?php

class a {

    public static $foo = 'I am foo';
    public $bar = 'I am bar';
    
    public static function getFoo() { echo self::$foo;    }
    public static function setFoo() { self::$foo = 'I am a new foo'; }
    public function getBar() { echo $this->bar;    }            
}

$ob = new a();
a::getFoo();     $ob->getFoo();    $ob->getBar();    a::setFoo();    $ob = new a();     $ob->getFoo();    ?>

Regards
Motaz Abuthiab
```

up

down

40

Notes on stdClass

¶

16 years ago

```
stdClass is the default PHP object. stdClass has no properties, methods or parent. It does not support magic methods, and implements no interfaces.

When you cast a scalar or array as Object, you get an instance of stdClass. You can use stdClass whenever you need a generic object instance.
<?php
$x = new stdClass;
$y = (object) null;        $z = (object) 'a';         $a = (object) array('property1' => 1, 'property2' => 'b');
?>

stdClass is NOT a base class! PHP classes do not automatically inherit from any class. All classes are standalone, unless they explicitly extend another class. PHP differs from many object-oriented languages in this respect.
<?php
class CTest {
    public $property1;
}
$t = new CTest;
var_dump($t instanceof stdClass);            var_dump(is_subclass_of($t, 'stdClass'));    echo get_class($t) . "\n";                   echo get_parent_class($t) . "\n";            ?>

You cannot define a class named 'stdClass' in your code. That name is already used by the system. You can define a class named 'Object'.

You could define a class that extends stdClass, but you would get no benefit, as stdClass does nothing.

(tested on PHP 5.2.8)
```

up

down

7

pawel dot zimnowodzki at gmail dot com

¶

4 years ago

```
Although there is no null-safe operator for not existed array keys I found workaround for it: ($array['not_existed_key'] ?? null)?->methodName()
```

up

down

21

Jeffrey

¶

17 years ago

```
A PHP Class can be used for several things, but at the most basic level, you'll use classes to "organize and deal with like-minded data". Here's what I mean by "organizing like-minded data". First, start with unorganized data.

<?php
$customer_name;
$item_name;
$item_price;
$customer_address;
$item_qty;
$item_total;
?>

Now to organize the data into PHP classes:

<?php
class Customer {
  $name;          $address;       }

class Item {
  $name;          $price;         $qty;           $total;         }
?>

Now here's what I mean by "dealing" with the data. Note: The data is already organized, so that in itself makes writing new functions extremely easy.

<?php
class Customer {
  public $name, $address;                   }

class Item {
  public $name, $price, $qty, $total;        }
?>

Imagination that each function you write only calls the bits of data in that class. Some functions may access all the data, while other functions may only access one piece of data. If each function revolves around the data inside, then you have created a good class.
```

up

down

2

Dimona at gmx dot net

¶

1 month ago

```
I programmed two classes in PHP that use inheritance. The class Kind extends the class Person, which means that Kind inherits the properties and methods of Person. This allows me to reuse existing code from the parent class and add specific functionality for the child class. For example, the Kind class can store an additional group and can change this group with a separate method.

<?php

abstract class person {

    protected $name;
    protected $gebdat;

    public function __construct(string $name,string $gebdat)
    {
        $this->name = $name;
        $this->gebdat = $gebdat;

    }

    public function holeDaten(): string
    {
     return "Name: $this->name, geb. am $this->gebdat<br>";
    }

}

?>

__________________________________________

<?php

require_once "person.php";
class erzieher extends person {

    private $watz;
    public static $minWaz = 12;
    public static $maxWaz = 35;

  public function __construct(string $name,string $gebdat,int $waz)
    {
        parent::__construct($name,$gebdat);
        $this->setWaz($waz);
    }

    public function setWaz(int $wo)
    {
        if($wo > self::$minWaz && $wo< self::$maxWaz){
        $this->watz = $wo; 
        echo "Wochenarbeitszeit für $this->name gesetztet";
        }
        elseif($wo < self::$minWaz && $wo> self::$maxWaz){
            echo "wochenzeit auf minimum gesetztet";

        }
    }

    public function holeDaten(): string
    {
        $str = parent::holeDaten();
        $str.="Erzeiher mit einer wöchentlichen Arbeitszeit von  $this->watz <br>";
        return $str;
    }

}

?>

______________________________________

for testing i use : 

<?php

    require_once "kind.php";
    require_once "erzieher.php";

$k1 = new Kind("luid Lurch","12.12.20","Lurche");

$e = new erzieher("edi mudda","2.2.2","35");

echo "<h1>Test Kind</h1>";
echo "<h2>Test holeDaten</h2>";

echo $k1->holeDaten();

echo "<h2>Test umGruppieren Gruppe exisitiert</h2>";

 $k1 -> umGruppieren("Lurche");

echo $k1->holeDaten();

echo "<h2>Test umGruppieren Gruppe exisitiert</h2>";

 $k1 -> umGruppieren("Mause");

echo $k1->holeDaten();

$e->setWaz(20);

?>
```

up

down

0

anisgazira at gmail dot com

¶

1 month ago

```
<?php
class John{
    public  string $address = "Bangladesh";
    public function myAddress(){
         return get_class($this);
    }
}
$a = new John;
echo $a->myAddress();
echo "\n";
echo get_class($a);
```

up

down

0

anvilaight at gmail dot com

¶

1 month ago

````
Hi everyone,

I’m currently practicing PHP, especially splitting strings with `explode()` and looping through arrays with `foreach`.

I have one string that contains several employees. 
Each employee is separated by `;`, and 
the individual values of each employee are separated by `,`.

Example:

```php
$employees = "Weber,Lisa,Warehouse,36.5,13.20;Klein,
Markus,Assembly,42,16.50;Hoffmann,Sarah,
Quality,28.5,15.80;Yilmaz,Emre,Shipping,39,14.40";
```

My goal is to first split the string into individual 
employees and then output the last name, first name, department, working hours and hourly wage
 for each employee.

My current approach looks like this:

```php
<?php

$employees = "Weber,Lisa,Warehouse,36.5,13.20;Klein,
Markus,Assembly,42,16.50;Hoffmann,
Sarah,Quality,28.5,15.80;Yilmaz,Emre,Shipping,39,14.40";

$persons = explode(";", $employees);

foreach ($persons as $person) {

    echo "<h3>Employee record:</h3>";
    echo $person . "<br>";

    $employeeData = explode(",", $person);

    echo "Last name: " . $employeeData[0] . "<br>";
    echo "First name: " . $employeeData[1] . "<br>";
    echo "Department: " . $employeeData[2] . "<br>";
    echo "Hours: " . $employeeData[3] . "<br>";
    echo "Hourly wage: " . $employeeData[4] . "<br>";

    echo "--------------------<br>";
}

?>
```

My question:

Is this generally the correct approach, 
first using `explode(";", ...)` to split the 
employee records and then using `
explode(",", ...)` inside the `foreach` 
loop to split the individual values?

Would it also make sense to store
 the values in separate variables afterwards, for example:

```php
$lastName = $employeeData[0];
$firstName = $employeeData[1];
$department = $employeeData[2];
$hours = (float)$employeeData[3];
$hourlyWage = (float)$employeeData[4];
```

Or is directly accessing `$employeeData[0]`, 
`$employeeData[1]`, etc. good enough for a 
simple example like this?

Thanks in advance!
````

up

down

0

cedstyler22 at gmail dot com

¶

1 month ago

```
<?php
abstract class Basis {
    protected string $a1;   protected string $a2;   private static int $anzahl = 0;

    public function __construct(string $a1, string $a2) {
        $this->a1 = $a1;
        $this->a2 = $a2;
        self::$anzahl++;
    }

    public function getA1(): string       { return $this->a1; }
    public function setA1(string $v): void { $this->a1 = $v; }
    public static function getAnzahl(): int { return self::$anzahl; }

    public function holeDaten(): string {
        return $this->a1 . "<br>" . $this->a2;
    }
}

class KindA extends Basis {
    private string $gruppe;
    public static array $gruppen = ["X", "Y", "Z"]; public function __construct(string $a1, string $a2, string $g) {
        parent::__construct($a1, $a2);
        $this->gruppe = $g;
    }

    public function umGruppieren(string $neu): void {
        if (in_array($neu, self::$gruppen)) {
            $this->gruppe = $neu;
            echo $this->a1 . " → " . $neu . "<br>";
        } else {
            echo $neu . " existiert nicht<br>";
        }
    }
    
    public function holeDaten(): string {
        return parent::holeDaten() . "<br>Gruppe: " . $this->gruppe;
    }
}
class KindB extends Basis {
    private int $wert;
    public int $min = 0;    public int $max = 100;
    private bool $status = true;

    public function __construct(string $a1, string $a2, int $w) {
        parent::__construct($a1, $a2);
        $this->setWert($w); }

    public function setWert(int $v): void {
        if ($v < $this->min)      $this->wert = $this->min;
        elseif ($v > $this->max)  $this->wert = $this->max;
        else                      $this->wert = $v;
    }

    public function getWert(): int { return $this->wert; }

    public function aktion(): bool {
        if (!$this->status) return false;
        $this->status = false;
        return true;
    }

    public function erhoeheLevel(): bool {
        if ($this->wert < $this->max) { $this->wert++; return true; }
        return false;
    }
    public function berechne(float $a, float $b): float {
        return $a / ($b * $b);
    }

    public function getBewertung(float $v): string {
        if ($v < 18.5)      return "Untergewicht";
        elseif ($v <= 24.9) return "Normalgewicht";
        else                return "Übergewicht";
    }

    private array $werte = [];

    public function add(float $v): void { $this->werte[] = $v; }

    public function berechneMittelwert(): float {
        if (empty($this->werte)) return 0.0;
        $s = 0;
        foreach ($this->werte as $w) $s += $w;
        return $s / count($this->werte);
    }
```

up

down

-4

Anonymous

¶

8 years ago

```
At first I was also confused by the assignment vs referencing but here's how I was finally able to get my head around it. This is another example which is somewhat similar to one of the comments but can be helpful to those who did not understand the first example. Imagine object instances as rooms where you can store and manipulate your properties and functions.  The variable that contains the object simply holds 'a key' to this room and thus access to the object. When you assign this variable to another new variable, what you are doing is you're making a copy of the key and giving it to this new variable. That means these two variable now have access to the same 'room' (object) and can thus get in and manipulate the values. However, when you create a reference, what you doing is you're making the variables SHARE the same key. They both have access to the room. If one of the variable is given a new key, then the key that they are sharing is replaced and they now share a new different key. This does not affect the other variable with a copy of the old key...that variable still has access to the first room
```

＋

add a note
