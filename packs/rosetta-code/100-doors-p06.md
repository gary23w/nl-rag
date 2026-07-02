---
title: "100 doors (part 6/10)"
source: https://rosettacode.org/wiki/100_doors
domain: rosetta-code
license: GFDL-1.2
tags: rosetta code, cross-language comparison, polyglot example
fetched: 2026-07-02
part: 6/10
---

## Icon and Unicon

Icon and Unicon don't have a boolean type because most often, logic is expressed in terms of success or failure, which affects flow at run time.

**Unoptimized solution.**

```mw
procedure main()
    door := table(0)    # default value of entries is 0
    every pass := 1 to 100 do
        every door[i := pass to 100 by pass] := 1 - door[i]

    every write("Door ", i := 1 to 100, " is ", if door[i] = 1 then "open" else "closed")
end
```

**Optimized solution.**

```mw
procedure main()
    every write("Door ", i := 1 to 100, " is ", if integer(sqrt(i)) = sqrt(i) then "open" else "closed")
end
```

or

```mw
procedure main(args)
    dMap := table("closed")
    every dMap[(1 to sqrt(100))^2] := "open"
    every write("Door ",i := 1 to 100," is ",dMap[i])
end
```


## Idris

```mw
import Data.Vect

-- Creates list from 0 to n (not including n) 
upTo : (m : Nat) -> Vect m (Fin m)
upTo Z = []
upTo (S n) = 0 :: (map FS (upTo n))

data DoorState = DoorOpen | DoorClosed

toggleDoor : DoorState -> DoorState
toggleDoor DoorOpen = DoorClosed
toggleDoor DoorClosed = DoorOpen

isOpen : DoorState -> Bool
isOpen DoorOpen = True
isOpen DoorClosed = False

initialDoors : Vect 100 DoorState
initialDoors = fromList $ map (\_ => DoorClosed) [1..100]

iterate : (n : Fin m) -> Vect m DoorState -> Vect m DoorState
iterate n doors {m} = 
  map (\(idx, doorState) => 
          if ((S (finToNat idx)) `mod` (S (finToNat n))) == Z 
              then toggleDoor doorState 
              else doorState)  
      (zip (upTo m) doors)

-- Returns all doors left open at the end
solveDoors : List (Fin 100)
solveDoors = 
  findIndices isOpen $ foldl (\doors,val => iterate val doors) initialDoors (upTo 100)

main : IO ()
main = print $ map (\n => S (finToNat n)) solveDoors
```


## Inform 7

Works with

:

Z-machine

version 8

Works with

:

Glulx virtual machine

```mw
Hallway is a room.

A toggle door is a kind of thing.
A toggle door can be open or closed. It is usually closed.
A toggle door has a number called the door number.
Understand the door number property as referring to a toggle door.
Rule for printing the name of a toggle door: say "door #[door number]".

There are 100 toggle doors.

When play begins (this is the initialize doors rule):
	let the next door number be 1;
	repeat with D running through toggle doors:
		now the door number of D is the next door number;
		increment the next door number.

To toggle (D - open toggle door): now D is closed.
To toggle (D - closed toggle door): now D is open.

When play begins (this is the solve puzzle rule):
	let the door list be the list of toggle doors;
	let the door count be the number of entries in the door list;
	repeat with iteration running from 1 to 100:
		let N be the iteration;
		while N is less than the door count:
			toggle entry N in the door list;
			increase N by the iteration;
	say "Doors left open: [list of open toggle doors].";
	end the story.
```


## Informix 4GL

```mw
MAIN
    DEFINE
        i, pass SMALLINT,
        doors ARRAY[100] OF SMALLINT
 
    FOR i = 1 TO 100
        LET doors[i] = FALSE
    END FOR
 
    FOR pass = 1 TO 100
        FOR i = pass TO 100 STEP pass
            LET doors[i] = NOT doors[i]
        END FOR
    END FOR
 
    FOR i = 1 TO 100
        IF doors[i]
          THEN DISPLAY i USING "Door <<& is open"
          ELSE DISPLAY i USING "Door <<& is closed"
        END IF
    END FOR
END MAIN
```


## Insitux

```mw
(var doors (times 100 false))

(for i  (range 1 101)
     i2 (range (dec i) 100 i)
  (var! doors (set-at [i2] (not (i2 doors))))
  (continue))

(-> (xmap vec doors)
    (filter 1)
    (map (comp 0 inc))
    (join ", ")
   @(str "open doors: "))
```

**Output:**

```
open doors: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```


## Io

simple boolean list solution:

```mw
doors := List clone
100 repeat(doors append(false))
for(i,1,100,
    for(x,i,100, i, doors atPut(x - 1, doors at(x - 1) not))
)
doors foreach(i, x, if(x, "Door #{i + 1} is open" interpolate println))
```

Optimized solution:

```mw
(Range 1 to(10) asList) foreach(v, "Door #{v ** 2} is open." interpolate println)
```

Sample output:

```
Door 1 is open.
Door 4 is open.
Door 9 is open.
Door 16 is open.
Door 25 is open.
Door 36 is open.
Door 49 is open.
Door 64 is open.
Door 81 is open.
Door 100 is open.
```


## Ioke

**Unoptimized Object Oriented solution.**

```mw
NDoors = Origin mimic

NDoors Toggle = Origin mimic do(
  initialize = method(toggled?, @toggled? = toggled?)
  toggle! = method(@toggled? = !toggled?. self)
)

NDoors Doors = Origin mimic do(
  initialize = method(n,
    @n = n
    @doors = {} addKeysAndValues(1..n, (1..n) map(_, NDoors Toggle mimic(false)))
  )
  numsToToggle = method(n, for(x <- (1..@n), (x % n) zero?, x))
  toggleThese = method(nums, nums each(x, @doors[x] = @doors at(x) toggle))
  show = method(@doors filter:dict(value toggled?) keys sort println)
)

; Test code
x = NDoors Doors mimic(100)
(1..100) each(n, x toggleThese(x numsToToggle(n)))
x show
```


## Isabelle

```mw
theory Scratch
  imports Main
begin

section‹100 Doors›

  datatype doorstate = Open | Closed
  
  fun toggle :: "doorstate ⇒ doorstate" where
    "toggle Open   = Closed"
  | "toggle Closed = Open"
  
  fun walk :: "('a ⇒ 'a) ⇒ nat ⇒ nat ⇒ 'a list ⇒ 'a list" where
    "walk f _     _       []     = []"
  | "walk f every 0       (x#xs) = (f x) # walk f every every xs"
  | "walk f every (Suc n) (x#xs) = x # walk f every n xs"
  
  text‹Example: \<^const>‹toggle› every second door. (second = 1, because of 0 indexing)›
  lemma "walk toggle 1 1 [Open, Open, Open, Open, Open, Open] =
                         [Open, Closed, Open, Closed, Open, Closed]" by code_simp
  
  text‹Example: \<^const>‹toggle› every third door.›
  lemma "walk toggle 2 2 [Open, Open, Open, Open, Open, Open] =
                         [Open, Open, Closed, Open, Open, Closed]" by code_simp
  
  text‹Walking each door is essentially the same as the common \<^const>‹map› function.›
  lemma "walk f 0 0 xs = map f xs"
    by(induction xs) (simp)+
  
  lemma walk_beginning:
    "walk f every n xs = (walk f every n (take (Suc n) xs)) @ (walk f every every (drop (Suc n) xs))"
    by(induction f every n xs rule:walk.induct) (simp)+
  
  text‹A convenience definition to take the off-by-one into account and setting the starting position.›
  definition visit_every :: "('a ⇒ 'a) ⇒ nat ⇒ 'a list ⇒ 'a list" where
    "visit_every f every xs ≡ walk f (every - 1) (every - 1) xs"
  
  
  fun iterate :: "nat ⇒ (nat ⇒ 'a ⇒ 'a) ⇒ nat ⇒ 'a ⇒ 'a" where
    "iterate 0       _ _ a = a"
  | "iterate (Suc i) f n a = iterate i f (Suc n) (f n a)"
  
  text‹The 100 doors problem.›
  definition "onehundred_doors ≡ iterate 100 (visit_every toggle) 1 (replicate 100 Closed)"
  
  lemma "onehundred_doors =
    [Open, Closed, Closed, Open, Closed, Closed, Closed,
     Closed, Open, Closed, Closed, Closed, Closed, Closed,
     Closed, Open, Closed, Closed, Closed, Closed, Closed,
     Closed, Closed, Closed, Open, Closed, Closed, Closed,
     Closed, Closed, Closed, Closed, Closed, Closed, Closed,
     Open, Closed, Closed, Closed, Closed, Closed, Closed,
     Closed, Closed, Closed, Closed, Closed, Closed, Open,
     Closed, Closed, Closed, Closed, Closed, Closed, Closed,
     Closed, Closed, Closed, Closed, Closed, Closed, Closed,
     Open, Closed, Closed, Closed, Closed, Closed, Closed,
     Closed, Closed, Closed, Closed, Closed, Closed, Closed,
     Closed, Closed, Closed, Open, Closed, Closed, Closed,
     Closed, Closed, Closed, Closed, Closed, Closed, Closed,
     Closed, Closed, Closed, Closed, Closed, Closed, Closed,
     Closed, Open]" by code_simp
  
  text‹Filtering for the open doors, we get the same result as the Haskell implementation.›
  lemma
    "[(i, door) ← enumerate 1 onehundred_doors. door = Open] =
     [(1,Open),(4,Open),(9,Open),(16,Open),(25,Open),(36,Open),(49,Open),(64,Open),(81,Open),(100,Open)]"
    by code_simp

section‹Equivalence to Haskell Implementation›
text‹
We will now present an alternative implementation, which is similar to the Haskell implementation
on 🌐‹https://rosettacode.org/wiki/100_doors#Haskell›. We will prove, that the two behave the same;
in general, not just for a fixed set of 100 doors.
›

  definition map_every_start :: "('a ⇒ 'a) ⇒ nat ⇒ nat ⇒ 'a list ⇒ 'a list" where
    "map_every_start f every start xs ≡
      map (λ(i, x). if i mod every = 0 then f x else x) (enumerate start xs)"

  definition visit_every_alt :: "('a ⇒ 'a) ⇒ nat ⇒ 'a list ⇒ 'a list" where
    "visit_every_alt f every xs ≡ map_every_start f every 1 xs"
  
  text‹Essentially, \<^term>‹start› and \<^term>‹start mod every› behave the same.›
  lemma map_every_start_cycle:
    "map_every_start f every (start + k*every) xs = map_every_start f every start xs"
    proof(induction xs arbitrary: start)
      case Nil
      show "map_every_start f every (start + k * every) [] = map_every_start f every start []"
        by(simp add: map_every_start_def)
    next
      case (Cons x xs)
      from Cons.IH[of "Suc start"]
        show "map_every_start f every (start + k * every) (x # xs) =
              map_every_start f every start (x # xs)"
        by(simp add: map_every_start_def)
    qed
  corollary map_every_start_cycle_zero:
    "map_every_start f every every xs = map_every_start f every 0 xs"
    using map_every_start_cycle[where k=1 and start=0, simplified] by blast
  
  lemma map_every_start_fst_zero:
    "map_every_start f every 0 (x # xs) = f x # map_every_start f every (Suc 0) xs"
    by(simp add: map_every_start_def)
  
  text‹
  The first \<^term>‹n› elements are not processed by \<^term>‹f›,
  as long as \<^term>‹n› is less than the \<^term>‹every› cycle.
  ›
  lemma map_every_start_skip_first: "Suc n < every ⟹
         map_every_start f every (every - (Suc n)) (x # xs) = 
         x # map_every_start f every (every - n) xs"
    by(simp add: map_every_start_def Suc_diff_Suc)

  lemma map_every_start_append:
    "map_every_start f n s (ds1 @ ds2) =
     map_every_start f n s ds1 @ map_every_start f n (s + length ds1) ds2"
    by(simp add: map_every_start_def enumerate_append_eq)

  text‹
  The \<^const>‹walk› function and \<^const>‹map_every_start› behave the same,
  as long as the starting \<^term>‹n› is less than the \<^term>‹every› cycle,
  because \<^const>‹walk› allows pushing the start arbitrarily far and
  \<^const>‹map_every_start› only allows deferring the start within
  the \<^term>‹every› cycle.
  This generalization is needed to strengthen the induction hypothesis
  for the proof.
  ›
  lemma walk_eq_map_every_start:
    "n ≤ every ⟹ walk f every n xs = map_every_start f (Suc every) (Suc every - n) xs"
    proof(induction xs arbitrary: n)
      case Nil
      show "walk f every n [] = map_every_start f (Suc every) (Suc every - n) []"
        by(simp add: map_every_start_def)
    next
      case (Cons x xs)
      then show "walk f every n (x # xs) = map_every_start f (Suc every) (Suc every - n) (x # xs)"
      proof(cases n)
        case 0
        with Cons.IH show ?thesis 
          by(simp add: map_every_start_cycle_zero map_every_start_fst_zero)
      next
        case (Suc n2)
        with Cons.prems map_every_start_skip_first[of n2 "Suc every"] have
          "map_every_start f (Suc every) (Suc every - Suc n2) (x # xs) =
           x # map_every_start f (Suc every) (Suc every - n2) xs"
          by fastforce
        with Suc Cons show ?thesis
          by(simp)
      qed
    qed
  
  corollary walk_eq_visit_every_alt:
    "walk f every every xs = visit_every_alt f (Suc every) xs"
    unfolding visit_every_alt_def
    using walk_eq_map_every_start by fastforce

  text‹
  Despite their very different implementations, our alternative visit function behaves the same
  as our original visit function.
  Text the theorem includes \<^term>‹Suc every› to express that we exclude \<^term>‹every = 0›.
  ›
  theorem visit_every_eq_visit_every_alt:
    "visit_every f (Suc every) xs = visit_every_alt f (Suc every) xs"
    unfolding visit_every_def
    using walk_eq_visit_every_alt by fastforce

  text‹Also, the \<^const>‹iterate› function we implemented above can be implemented by a simple \<^const>‹fold›.›
  lemma fold_upt_helper: assumes n_geq_1: "Suc 0 ≤ n"
    shows "fold f [Suc s..<n + s] (f s xs) = fold f [s..<n + s] xs"
  proof -
    from n_geq_1 have "[s..<n + s] = s#[Suc s..<n + s]" by (simp add: Suc_le_lessD upt_rec)
    from this have "fold f [s..<n + s] xs = fold f (s#[Suc s..<n + s]) xs" by simp
    also have "fold f (s#[Suc s..<n + s]) xs = fold f [Suc s..<n + s] (f s xs)" by(simp)
    ultimately show ?thesis by simp
  qed
  
  theorem iterate_eq_fold: "iterate n f s xs = fold f [s ..< n+s] xs"
  proof(induction n arbitrary: s xs)
    case 0
    then show "iterate 0 f s xs = fold f [s..<0 + s] xs" by simp
  next
    case (Suc n)
    from Suc show "iterate (Suc n) f s xs = fold f [s..<Suc n + s] xs" 
      by(simp add: fold_upt_helper not_less_eq_eq)
  qed

section‹Efficient Implementation›
text ‹
As noted on this page, the only doors that remain open are those whose numbers are perfect squares.
Yet, rosettacode does not want us to take this shortcut, since we want to compare implementations
across programming languages. But we can prove that our code computes the same result as reporting
all doors with a perfect square number as open:
›
  theorem "[(i, door) ← enumerate 1 onehundred_doors. door = Open] =
           [(i*i, Open). i ← [1..<11]]"
    by code_simp
end
```


## J

**unoptimized**

```mw
   ~:/ (100 $ - {. 1:)"0 >:i.100
1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ...
   ~:/ 0=|/~ >:i.100  NB. alternative
1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ...
   (*/"1)2|>:_ q:>:i.100 NB. alternative
```

**optimized**

```mw
   (e. *:) 1+i.100
1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ...
   1 (<:*:i.10)} 100$0  NB. alternative
1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ...
```

**with formatting**

```mw
   'these doors are open: ',": I. (i.101) e. *: 1+i.10
these doors are open: 1 4 9 16 25 36 49 64 81 100
```


## Janet

```mw
(def doors (seq [_ :range [0 100]] false))

(loop [pass :range [0 100]
       door :range [pass 100 (inc pass)]]
  (put doors door (not (doors door))))

(print "open doors: " ;(seq [i :range [0 100] :when (doors i)] (string (inc i) " ")))
```

Output:

```
open doors: 1 4 9 16 25 36 49 64 81 100
```


## Java

### With an array of boolean

```mw
class HundredDoors {
    public static void main(String[] args) {
        boolean[] doors = new boolean[101];

        for (int i = 1; i < doors.length; i++) {
            for (int j = i; j < doors.length; j += i) {
                doors[j] = !doors[j];
            }
        }

        for (int i = 1; i < doors.length; i++) {
            if (doors[i]) {
                System.out.printf("Door %d is open.%n", i);
            }
        }
    }
}
```

### With a BitSet

```mw
import java.util.BitSet;

public class HundredDoors {
    public static void main(String[] args) {
        final int n = 100;
        var a = new BitSet(n);
        for (int i = 1; i <= n; i++) {
            for (int j = i - 1; j < n; j += i) {
                a.flip(j);
            }
        }
        a.stream().map(i -> i + 1).forEachOrdered(System.out::println);
    }
}
```

### Only print the result

```mw
class HundredDoors {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++)
            System.out.printf("Door %d is open.%n", i * i);
    }
}
```

Output:

```
Door 1 is open.
Door 4 is open.
Door 9 is open.
Door 16 is open.
Door 25 is open.
Door 36 is open.
Door 49 is open.
Door 64 is open.
Door 81 is open.
Door 100 is open.
```

**If only printing the result is required, using streams.**

```mw
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class HundredDoors {
    public static void main(String args[]) {
        String openDoors = IntStream.rangeClosed(1, 100)
                .filter(i -> Math.pow((int) Math.sqrt(i), 2) == i)
                .mapToObj(Integer::toString)
                .collect(Collectors.joining(", "));
        System.out.printf("Open doors: %s%n", openDoors);
    }
}
```

Output:

```
Open doors: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```


## JavaScript

### ES5

#### Iterative

```mw
var doors=[];
for (var i=0;i<100;i++)
    doors[i]=false;
for (var i=1;i<=100;i++)
    for (var i2=i-1;i2<100;i2+=i)
        doors[i2]=!doors[i2];
for (var i=1;i<=100;i++)
    console.log("Door %d is %s",i,doors[i-1]?"open":"closed")
```

#### Functional Composition

Naive search

```mw
(function (n) {
    "use strict";
    function finalDoors(n) {
        var lstRange = range(1, n);
        return lstRange
            .reduce(function (a, _, k) {
                var m = k + 1;
                return a.map(function (x, i) {
                    var j = i + 1;
                    return [j, j % m ? x[1] : !x[1]];
                });
            }, zip(
                lstRange,
                replicate(n, false)
            ));
    };
    function zip(xs, ys) {
        return xs.length === ys.length ? (
            xs.map(function (x, i) {
                return [x, ys[i]];
            })
        ) : undefined;
    }
    function replicate(n, a) {
        var v = [a],
            o = [];
        if (n < 1) return o;
        while (n > 1) {
            if (n & 1) o = o.concat(v);
            n >>= 1;
            v = v.concat(v);
        }
        return o.concat(v);
    }
    function range(m, n, delta) {
        var d = delta || 1,
            blnUp = n > m,
            lng = Math.floor((blnUp ? n - m : m - n) / d) + 1,
            a = Array(lng),
            i = lng;
        if (blnUp)
            while (i--) a[i] = (d * i) + m;
        else
            while (i--) a[i] = m - (d * i);
        return a;
    }
    return finalDoors(n)
        .filter(function (tuple) {
            return tuple[1];
        })
        .map(function (tuple) {
            return {
                door: tuple[0],
                open: tuple[1]
            };
        });

})(100);
```

#### Optimized (iterative)

```mw
for (var door = 1; door <= 100; door++) {
  var sqrt = Math.sqrt(door);
  if (sqrt === (sqrt | 0)) {
    console.log("Door %d is open", door);
  }
}
```

Simple for loop. Optimizing the optimized?

```mw
for(var door=1;i<10/*Math.sqrt(100)*/;i++){
 console.log("Door %d is open",i*i);
}
```

#### Optimized (functional)

The question of which doors are flipped an odd number of times reduces to the question of which numbers have an odd number of integer factors. We can simply search for these:

```mw
(function (n) {
    "use strict";
    return range(1, 100)
        .filter(function (x) {
            return integerFactors(x)
                .length % 2;
        });
    function integerFactors(n) {
        var rRoot = Math.sqrt(n),
            intRoot = Math.floor(rRoot),
            lows = range(1, intRoot)
            .filter(function (x) {
                return (n % x) === 0;
            });
        return lows.concat(lows.map(function (x) {
                return n / x;
            })
            .reverse()
            .slice((rRoot === intRoot) | 0));
    }
    function range(m, n, delta) {
        var d = delta || 1,
            blnUp = n > m,
            lng = Math.floor((blnUp ? n - m : m - n) / d) + 1,
            a = Array(lng),
            i = lng;
        if (blnUp)
            while (i--) a[i] = (d * i) + m;
        else
            while (i--) a[i] = m - (d * i);
        return a;
    }
})(100);
```

Or we can note, on inspection and further reflection, that only perfect squares have odd numbers of integer factors - all other numbers have only matched pairs of factors - low factors below the non-integer square root, and the corresponding quotients above the square root. In the case of perfect squares, the additional integer square root (not paired with any other factor than itself) makes the total number of distinct factors odd.

```mw
(function (n) {
    "use strict";
    return perfectSquaresUpTo(100);
    function perfectSquaresUpTo(n) {
        return range(1, Math.floor(Math.sqrt(n)))
            .map(function (x) {
                return x * x;
            });
    }
    function range(m, n, delta) {
        var d = delta || 1,
            blnUp = n > m,
            lng = Math.floor((blnUp ? n - m : m - n) / d) + 1,
            a = Array(lng),
            i = lng;
        if (blnUp)
            while (i--) a[i] = (d * i) + m;
        else
            while (i--) a[i] = m - (d * i);
        return a;
    }
})(100);
```

### ES6

```mw
Array.apply(null, { length: 100 })
  .map((v, i) => i + 1)
    .forEach(door => { 
      var sqrt = Math.sqrt(door); 

      if (sqrt === (sqrt | 0)) {
        console.log("Door %d is open", door);
      } 
    });
```

Works with

:

SpiderMonkey

(Firefox) But not most (if any) other JavaScript engines. Array comprehension (`[ for... ]`) is non-standard.

```mw
// Array comprehension style
[ for (i of Array.apply(null, { length: 100 })) i ].forEach((_, i) => { 
  var door = i + 1
  var sqrt = Math.sqrt(door); 

  if (sqrt === (sqrt | 0)) {
    console.log("Door " + door + " is open");
  } 
});
```

The result is always:

```
Door 1 is open
Door 4 is open
Door 9 is open
Door 16 is open
Door 25 is open
Door 36 is open
Door 49 is open
Door 64 is open
Door 81 is open
Door 100 is open
```

Or using a more general function for listing perfect squares:

```mw
(function (n) {
 
 
    // ONLY PERFECT SQUARES HAVE AN ODD NUMBER OF INTEGER FACTORS
    // (Leaving the door open at the end of the process) 
 
    return perfectSquaresUpTo(n);
 
 
    // perfectSquaresUpTo :: Int -> [Int]
    function perfectSquaresUpTo(n) {
        return range(1, Math.floor(Math.sqrt(n)))
            .map(x => x * x);
    }
 
 
    // GENERIC
 
    // range(intFrom, intTo, optional intStep)
    // Int -> Int -> Maybe Int -> [Int]
    function range(m, n, step) {
        let d = (step || 1) * (n >= m ? 1 : -1);
 
        return Array.from({
            length: Math.floor((n - m) / d) + 1
        }, (_, i) => m + (i * d));
    }
 
})(100);
```

**Output:**

```mw
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

#### School example

Works with

:

JavaScript

version Node.js 16.13.0 (LTS)

```mw
"use strict";

// Doors can be open or closed.
const open = "O";
const closed = "C";

// There are 100 doors in a row that are all initially closed.
const doorsCount = 100;
const doors = [];
for (let i = 0; i < doorsCount; doors[i] = closed, i++);

// You make 100 passes by the doors, visiting every door and toggle the door (if
// the door is closed, open it; if it is open, close it), according to the rules
// of the task.
for (let pass = 1; pass <= doorsCount; pass++)
    for (let i = pass - 1; i < doorsCount; i += pass)
        doors[i] = doors[i] == open ? closed : open;

// Answer the question: what state are the doors in after the last pass?
doors.forEach((v, i) =>
    console.log(`Doors ${i + 1} are ${v == open ? 'opened' : 'closed'}.`));

// Which are open, which are closed?
let openKeyList = [];
let closedKeyList = [];
for (let door of doors.entries())
    if (door[1] == open)
        openKeyList.push(door[0] + 1);
    else
        closedKeyList.push(door[0] + 1);
console.log("These are open doors: " + openKeyList.join(", ") + ".");
console.log("These are closed doors: " + closedKeyList.join(", ") + ".");

// Assert:
const expected = [];
for (let i = 1; i * i <= doorsCount; expected.push(i * i), i++);
if (openKeyList.every((v, i) => v === expected[i]))
    console.log("The task is solved.")
else
    throw "These aren't the doors you're looking for.";
```


## jq

jq arrays have 0 as their index origin, but in the following, the 100 doors are numbered from 1 to 100.

**Solution by simulation**

```mw
# Solution for n doors:
def doors(n):

  def print:
    . as $doors
    | range(1; length+1)
    | if $doors[.] then "Door \(.) is open" else empty end;

    [range(n+1)|null] as $doors
  | reduce range(1; n+1) as $run
      ( $doors; reduce range($run; n+1; $run ) as $door
                  ( .; .[$door] = (.[$door] | not) ) )
  | print ;
```

**Analytical solution**

```mw
# Solution for 100 doors:
def solution:
  range(1;11) | "Door \(. * .) is open";
```


## Julia

**Simple**:

- falses(100) creates a 100-element Bool array filled with false values,
- 'b in a:a:100' translates to 'start:step:end',
- string concatenation by '*'.

```mw
doors = falses(100)
for a in 1:100, b in a:a:100
    doors[b] = !doors[b]
end
for a = 1:100
    println("Door $a is " * (doors[a] ? "open." : "closed.")) 
end
```

**Gimmicky-optimized**:

```mw
for i in 1:10 println("Door $(i^2) is open.") end
```


## K

### K3

Works with

:

Kona

Converted from Q:

```mw
   doors:{`closed`open![;2]@#:'1_=,/&:'0=t!\:/:t:!101}
```

Optimized 1-based indices:

```mw
   (1+!10)^2
1 4 9 16 25 36 49 64 81 100
```

Indices as a parameterized function:

```mw
   {(1+!_ x^%2)^2}100
1 4 9 16 25 36 49 64 81 100
```


## KatLang

```mw
ToggleAccum(passNum, (doorNum, doorState)) =
    (doorNum, if(doorNum mod passNum == 0, 1 - doorState, doorState))

DoorStateAfterAllPasses = range(1, 100).reduce(ToggleAccum, (doorNum, 0))

range(1, 100).map(DoorStateAfterAllPasses).filter{x:1}.map{x:0}
```


## Klingphix

```mw
include ..\Utilitys.tlhy

%n 100 !n
0 $n repeat

$n [dup sqrt int dup * over
== ( [1 swap set] [drop] ) if] for

$n [ ( "The door " over  " is " ) lprint get ( ["OPEN"] ["closed"] ) if print nl] for

( "Time elapsed: " msec " seconds" ) lprint nl

pstack
" " input
```


## Klong

### unoptimized

```mw
flip::{,/{(1-*x),1_x}'x:#y}
i::0;(100{i::i+1;flip(i;x)}:*100:^0)?1
```

### optimized

```mw
(1+!9)^2
```


## Koka

Iterative version

```mw
type state
  Open
  Closed

fun toggle(self: state): state
  match self
    Open   -> Closed
    Closed -> Open

inline extern unsafe-assign : forall<a> ( v : vector<a>, i : ssize_t, x : a ) -> total ()
  c "kk_vector_unsafe_assign"

fun main()
  val doors = vector(100, Closed)
  for(0,99) fn(pass)
    var door := pass
    while { door < 99 }
      doors.unsafe-assign(door.ssize_t, doors[door].toggle)
      door := door + (pass+1)
  doors.foreach-indexed fn(idx, it)
    match it
      Open   -> println("door " ++ (idx + 1).show ++ " is open")
      Closed -> println("door " ++ (idx + 1).show ++ " is closed")
```

Functional Version (Same definitions as above with different main)

```mw
fun main()
  val doors = list(0,99,1,fn(i) Closed)
  val transformed = list(1,99).foldl(doors) fn(drs, pass)
    drs.map-indexed fn(i, door)
      if ((i + 1) % pass) == 0 then door.toggle else door
  transformed.foreach-indexed fn(idx, it)
    match it
      Open   -> println("door " ++ (idx + 1).show ++ " is open")
      Closed -> println("door " ++ (idx + 1).show ++ " is closed")
```


## KonsolScript

```mw
function main() {
    Array:New doors[100]:Boolean;
    Var:Number pass;
    Var:Number door;

    for (pass = 1; pass <= 100; pass++) {
        door = pass;
        while (door <= 100) {
            if (doors[door - 1]) { doors[door - 1] = false; }
            else                  { doors[door - 1] = true; }
            door = door + pass;
        }
    }

    for (door = 1; door <= 100; door++) {
        if (doors[door - 1]) {
            Konsol:Print("Door ${door} is open");
        } else {
            Konsol:Print("Door ${door} is close");
        }
    }
}
```


## Kotlin

```mw
fun oneHundredDoors(): List<Int> {
    val doors = BooleanArray(100) { false }

    repeat(doors.size) { i ->
        for (j in i until doors.size step (i + 1)) {
            doors[j] = !doors[j]
        }
    }

    return doors
        .foldIndexed(emptyList()) { i, acc, door ->
            if (door) acc + (i + 1) else acc
        }
}
```


## KQL

```mw
range InitialDoor from 1 to 100 step 1
| extend DoorsVisited=range(InitialDoor, 100, InitialDoor)
| mvexpand DoorVisited=DoorsVisited to typeof(int)
| summarize VisitCount=count() by DoorVisited
| project Door=DoorVisited, IsOpen=(VisitCount % 2) == 1
```


## LabVIEW

This image is a VI Snippet, an executable image of LabVIEW code. The LabVIEW version is shown on the top-right hand corner. You can download it, then drag-and-drop it onto the LabVIEW block diagram from a file browser, and it will appear as runnable, editable code.

**Optimized**

This image is a VI Snippet, an executable image of LabVIEW code. The LabVIEW version is shown on the top-right hand corner. You can download it, then drag-and-drop it onto the LabVIEW block diagram from a file browser, and it will appear as runnable, editable code.


## Lambdatalk

Translation from Python

```mw
1) unoptimized version

{def doors
 {A.new
  {S.map {lambda {} false} {S.serie 1 100}}}}
-> doors

{def toggle
 {lambda {:i :a}
  {let { {_ {A.set! :i {not {A.get :i :a}} :a} }}}}}
-> toggle

{S.map {lambda {:b} 
 {S.map {lambda {:i} {toggle :i {doors}}} 
  {S.serie :b 99 {+ :b 1}}}}
   {S.serie 0 99}} 
->

{S.replace \s by space in 
 {S.map {lambda {:i} {if {A.get :i {doors}} then {+ :i 1} else}} 
  {S.serie 0 99}}}

-> 1 4 9 16 25 36 49 64 81 100

2.2) optimized version

{S.replace \s by space in 
 {S.map {lambda {:i}
         {let { {:root {sqrt :i}} } 
              {if {= :root {round :root}} 
               then {* :root :root}
               else}}}
        {S.serie 1 100}}}

-> 1 4 9 16 25 36 49 64 81 100
```


## Lang

```mw
&doors = fn.arrayGenerateFrom(fn.inc, 100)
fp.mapper = ($i) -> {
	$n
	$open = 0
	repeat($[n], 100) {
		$open $= $i % +|$n?!$open:$open
	}
	
	return $open
}
fn.arrayMap(&doors, fp.mapper)

fn.print(Open doors:)
$i
repeat($[i], @&doors) {
	if(&doors[$i]) {
		fn.printf(\s%03d, parser.op(+|$i))
	}
}
fn.println()
```

**Output:**

```
Open doors: 001 004 009 016 025 036 049 064 081 100
```


## langur

### not optimized

```mw
var doors = [false] * 100

for i of doors {
    for j = i; j <= len(doors); j += i {
        doors[j] = not doors[j]
    }
}

writeln for[=[]] i of doors { if doors[i]: _for = more(_for, i) }
```

Or, we could use the fold() function to produce the output.

```mw
writeln fold(doors, series(1..len(doors)), by=fn(a, b, c) { if(b: a & [c]; a) }, init=[])
```

### optimized

```mw
writeln map(1..10, by=fn{^2})
```

**Output:**

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


## Lasso

### Loop

```mw
loop(100) => {^
	local(root = math_sqrt(loop_count))
	local(state = (#root == math_ceil(#root) ? '<strong>open</strong>' | 'closed'))
	#state != 'closed' ? 'Door ' + loop_count + ': ' + #state + '<br>'
^}
```

**Output:**

```
Door 1: open
Door 4: open
Door 9: open
Door 16: open
Door 25: open
Door 36: open
Door 49: open
Door 64: open
Door 81: open
Door 100: open
```


## Latitude

```mw
use 'format importAllSigils.

doors := Object clone.
doors missing := { False. }.
doors check := {
  self slot ($1 ordinal).
}.
doors toggle := {
  self slot ($1 ordinal) = self slot ($1 ordinal) not.
}.
1 upto 101 do {
  takes '[i].
  local 'j = i.
  while { j <= 100. } do {
    doors toggle (j).
    j = j + i.
  }.
}.
$stdout printf: ~fmt "The open doors are: ~A", 1 upto 101 filter { doors check. } to (Array).
```


## Lhogho

This implementation defines 100 variables, named "1 through "100, rather than using a list. Thanks to Pavel Boytchev, the author of Lhogho, for help with the code.

```mw
to doors
	;Problem 100 Doors 
	;Lhogho

	for "p [1 100] 
	[
		make :p "false
	]

	for "a [1 100 1]
	[
		for "b [:a 100 :a]
		[
			if :b < 101 
			[
				make :b not thing :b
			]
		]
	]

	for "c [1 100]
	[
		if thing :c 
		[ 
			(print "door :c "is "open) 
		]
	] 
end

doors
```


## Liberty BASIC

Works with

:

Just BASIC

Works with

:

Run BASIC

```mw
dim doors(100)
for pass = 1 to 100
    for door = pass to 100 step pass
        doors(door) = not(doors(door))
    next door
next pass
print "open doors ";
for door = 1 to 100
    if doors(door) then print door;"  ";
next door
```


## Lily

```mw
var doors = List.fill(100, false)

for i in 0...99:
    for j in i...99 by i + 1:
        doors[j] = !doors[j]

# The type must be specified since the list starts off empty.
var open_doors: List[Integer] = []

doors.each_index{|i|
    if doors[i]:
        open_doors.push(i + 1)
}

print($"Open doors: ^(open_doors)")
```

**Output:**

```
Open doors: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


## LiveCode

### xTalk

Works with

:

HyperCard

Works with

:

LiveCode

```mw
on mouseUp   
   repeat with tStep = 1 to 100
      repeat with tDoor = tStep to 100 step tStep
         put not tDoors[tDoor] into tDoors[tDoor]
      end repeat
      if tDoors[tStep] then put "Door " & tStep & " is open" & cr after tList
   end repeat
   set the text of field "Doors" to tList
end mouseUp
```


## Logo

```mw
to doors
;Problem 100 Doors 
;FMSLogo
;lrcvs 2010

make "door (vector 100 1) 
for [p 1 100][setitem :p :door 0] 
  
for [a 1 100 1][for [b :a 100 :a][make "x item :b :door 
	                          ifelse :x  = 0 [setitem :b :door 1][setitem :b :door 0] ] ] 
  
for [c 1 100][make "y item :c :door 
	      ifelse :y = 0 [pr (list :c "Close)] [pr (list :c "Open)] ] 
end
```


## LOLCODE

```mw
HAI 1.3

I HAS A doors ITZ A BUKKIT
IM IN YR hallway UPPIN YR door TIL BOTH SAEM door AN 100
    doors HAS A SRS door ITZ FAIL BTW, INISHULIZE ALL TEH DOORZ AS CLOZD
IM OUTTA YR hallway

IM IN YR hallway UPPIN YR pass TIL BOTH SAEM pass AN 100
    I HAS A door ITZ pass
    IM IN YR passer
        doors'Z SRS door R NOT doors'Z SRS door
        door R SUM OF door AN SUM OF pass AN 1
        DIFFRINT door AN SMALLR OF door AN 99, O RLY?
            YA RLY, GTFO
        OIC
    IM OUTTA YR passer
IM OUTTA YR hallway

IM IN YR printer UPPIN YR door TIL BOTH SAEM door AN 100
    VISIBLE "Door #" SUM OF door AN 1 " is "!
    doors'Z SRS door, O RLY?
        YA RLY, VISIBLE "open."
        NO WAI, VISIBLE "closed."
    OIC
IM OUTTA YR printer

KTHXBYE
```


## Lua

```
local is_open = {}

for pass = 1,100 do
    for door = pass,100,pass do
        is_open[door] = not is_open[door]
    end
end

for i,v in pairs(is_open) do
    if v then io.write( string.format( " %d", i ) ) end
end
```


## M2000 Interpreter

Second dim preserve values except explicit assign a value for each item using = or a different value using << and a lambda function as generator.

Here we use =false to make all items false (which is a double value of 0).

M2000 use True and False as -1 and 0 (type of double), but from comparisons return Boolean True and False, which used as -1 and 0 also. Using =1=1 we get Boolean True and =1=0 we get Boolean False. We can check type from a variable using Type$(), so x=1=1 : Print Type$(x)="Boolean". We can chack type of an expression using a function: Def ExpressionType$(x)=Type$(x)

```mw
Module Doors100 {
      Dim Doors(1 to 100)
      For i=1 to 100
            For j=i to 100 step i
                  Doors(j)~
            Next j
      Next i
      DispAll()
      ' optimization
      Dim Doors(1 to 100)=False
      For i=1 to 10
            Doors(i**2)=True
      Next i
      Print
      DispAll()
      Sub DispAll()
            Local i
            For i=1 to 100
                  if Doors(i) then print i,
            Next i
            Print
      End Sub
}
Doors100
```


## M4

```mw
define(`_set', `define(`$1[$2]', `$3')')dnl
define(`_get', `defn(`$1[$2]')')dnl
define(`for',`ifelse($#,0,``$0'',`ifelse(eval($2<=$3),1,
`pushdef(`$1',$2)$5`'popdef(`$1')$0(`$1',eval($2+$4),$3,$4,`$5')')')')dnl
define(`opposite',`_set(`door',$1,ifelse(_get(`door',$1),`closed',`open',`closed'))')dnl
define(`upper',`100')dnl
for(`x',`1',upper,`1',`_set(`door',x,`closed')')dnl
for(`x',`1',upper,`1',`for(`y',x,upper,x,`opposite(y)')')dnl
for(`x',`1',upper,`1',`door x is _get(`door',x)
')dnl
```


## MACRO-11

```mw
        .TITLE  DOORS
        .MCALL  .TTYOUT,.EXIT
NDOORS  =       ^D100
DOORS::
        ; CLOSE ALL DOORS
        MOV     #DOORBF+1,R0
CLOSE:  CLR     (R0)+
        CMP     R0,#BUFTOP
        BLT     CLOSE

        ; VISIT DOORS
        MOV     #1,R1                   ; R1 = PASS
PASS:   MOV     R1,R2                   ; R2 = DOOR
DOOR:   COMB    DOORBF(R2)              ; VISIT DOOR
        ADD     R1,R2
        CMP     R2,#NDOORS              ; NEXT DOOR
        BLE     DOOR
        INC     R1
        CMP     R1,R2                   ; NEXT PASS
        BLE     PASS

        ; DISPLAY DOORS AS ASCII 0 OR 1
        MOV     #DOORBF+1,R1
DISP:   MOVB    (R1)+,R0
        BICB    #^C1,R0
        BISB    #^D48,R0
        .TTYOUT
        CMP     R1,#BUFTOP
        BLT     DISP

        .EXIT
DOORBF: .BLKB   NDOORS+1
BUFTOP  =       .
        .END    DOORS
```

**Output:**

```
1001000010000001000000001000000000010000000000001000000000000001000000000000000010000000000000000001
```


## MAD

```mw
            NORMAL MODE IS INTEGER
            DIMENSION OPEN(100)
            PRINT COMMENT $ $
           
          R MAKE SURE ALL DOORS ARE CLOSED AT BEGINNING
            THROUGH CLOSE, FOR DOOR=1, 1, DOOR.G.100
CLOSE       OPEN(DOOR) = 0

          R MAKE 100 PASSES
            THROUGH TOGGLE, FOR PASS=1, 1, PASS.G.100
            THROUGH TOGGLE, FOR DOOR=PASS, PASS, DOOR.G.100
TOGGLE      OPEN(DOOR) = 1 - OPEN(DOOR) 

          R PRINT THE DOORS THAT ARE OPEN
            THROUGH SHOW, FOR DOOR=1, 1, DOOR.G.100
SHOW        WHENEVER OPEN(DOOR).E.1, PRINT FORMAT ISOPEN, DOOR
           
            VECTOR VALUES ISOPEN = $5HDOOR ,I3,S1,8HIS OPEN.*$     
            END OF PROGRAM
```

**Output:**

```
DOOR   1 IS OPEN.
DOOR   4 IS OPEN.
DOOR   9 IS OPEN.
DOOR  16 IS OPEN.
DOOR  25 IS OPEN.
DOOR  36 IS OPEN.
DOOR  49 IS OPEN.
DOOR  64 IS OPEN.
DOOR  81 IS OPEN.
DOOR 100 IS OPEN.
```


## make

Make does not have any built-in arithmetic. It does have easy access to the shell and plug-ins for other languages but using them would be 'cheating' because the real work would not be done by make. Instead of doing arithmetic with numbers, the number of passes is encoded as the number of X's in $(pass). The door to toggle is encoded as the number of X's in $(count) and toggling a door is achieved by adding a dependency to the door number. To prevent $(count) from containing a huge number of X's the 'if' in $(loop) short circuits the inner loop.

```mw
.DEFAULT_GOAL:=100
digit=1 2 3 4 5 6 7 8 9
doors:=$(digit) $(foreach i,$(digit),$(foreach j,0 $(digit),$i$j)) 100
$(doors):;@: $(if $(filter %1 %3 %5 %7 %9,$(words $^)),$(info $@))
$(foreach i,$(doors),$(eval $i: $(word $i,0 $(doors))))
0 $(addprefix pass,$(doors)):
pass:=X
dep=$(eval count+=$(pass))$(eval $(words $(count)):pass$(words $(pass)))
loop=$(foreach inner,$(doors),$(if $(word 101,$(count)),,$(dep)))
$(foreach outer,$(doors),$(eval pass+=X)$(eval count:=)$(loop))
```


## Maple

```mw
NDoors := proc( N :: posint )
        # Initialise, using 0 to represent "closed"
        local pass, door, doors := Array( 1 .. N, 'datatype' = 'integer'[ 1 ] );
        # Now do N passes
        for pass from 1 to N do
                for door from pass by pass while door <= N do
                        doors[ door ] := 1 - doors[ door ]
                end do
        end do;
        # Output
        for door from 1 to N do
                printf( "Door %d is %s.\n", door, `if`( doors[ door ] = 0, "closed", "open" ) )
        end do;
        # Since this is a printing routine, return nothing.
        NULL
end proc:
```

To solve the problem, call it with 100 as argument (output not shown here).

```mw
> NDoors( 100 );
```

Here is the optimised version, which outputs only the open doors.

```mw
> seq( i^2, i = 1 .. isqrt( 100 ) );
                  1, 4, 9, 16, 25, 36, 49, 64, 81, 100
```

Alternatively,

```mw
> [seq]( 1 .. 10 )^~2;
                 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


## Mathematica /Wolfram Language

**unoptimized 1**

```mw
n=100;
tmp=ConstantArray[-1,n];
Do[tmp[[i;;;;i]]*=-1;,{i,n}];
Do[Print["door ",i," is ",If[tmp[[i]]==-1,"closed","open"]],{i,1,Length[tmp]}]
```

**unoptimized 2**

```mw
f[n_] = "Closed"; 
Do[Do[If[f[n] == "Closed", f[n] = "Open", f[n] = "Closed"], {n, k, 100, k}], {k, 1, 100}]; 
Table[f[n], {n, 1, 100}]
```

**unoptimized 3**

Mathematica also supports immutable data paradigms, like so:

```mw
Fold[
 ReplacePart[#1, (i_ /; Mod[i, #2] == 0) :> (-#1[[i]])] &,
 ConstantArray[-1, {100}],
 Range[100]
] /. {1 -> "Open", -1 -> "Closed"}
```

**optimized 1**

```mw
Do[Print["door ",i," is ",If[IntegerQ[Sqrt[i]],"open","closed"]],{i,100}]
```

**optimized 2**

```mw
n=100;
a=Range[1,Sqrt[n]]^2
Do[Print["door ",i," is ",If[MemberQ[a,i],"open","closed"]],{i,100}]
```

**optimized 3**

```mw
n=100
nn=1
a=0
For[i=1,i<=n,i++,
 If[i==nn,
  Print["door ",i," is open"];
  a++;
  nn+=2a+1;
 ,
  Print["door ",i," is closed"];
 ];
]
```

These will only give the indices for the open doors: **unoptimized 2**

```mw
Pick[Range[100], Xor@@@Array[Divisible[#1,#2]&, {100,100}]]
```

**optimized 4**

```mw
Range[Sqrt[100]]^2
```


## MATLAB / Octave

### Iterative Method

**Unoptimized**

```mw
a = false(1,100);
for b=1:100
  for i = b:b:100
    a(i) = ~a(i);
  end
end
a
```

**Optimized**

```mw
for x=1:100;
  if sqrt(x) == floor(sqrt(x))
    a(i)=1;
  end
end
a
```

**Optimized - Alternative**

```mw
doors   = zeros(1,100); // 0: closed 1: open
for i = 1:100
    doors(i:i:100) = 1-doors(i:i:100)
end
doors
```

**More Optimized**

```mw
a = zeros(100,1);
for counter = 1:sqrt(100);
  a(counter^2) = 1;
end
a
```

### Vectorized Method

```mw
function [doors,opened,closed] = hundredDoors()

    %Initialize the doors, make them booleans for easy vectorization
    doors = logical( (1:1:100) );
    
    %Go through the flipping process, ignore the 1 case because the doors
    %array is already initialized to all open
    for initialPosition = (2:100)
        doors(initialPosition:initialPosition:100) = not( doors(initialPosition:initialPosition:100) );
    end
    
    opened = find(doors); %Stores the numbers of the open doors
    closed = find( not(doors) ); %Stores the numbers of the closed doors
    
end
```

### Known-Result Method

```mw
doors((1:10).^2) = 1;

doors
```


## Maxima

```mw
doors(n) := block([v], local(v),
  v: makelist(true, n),
  for i: 2 thru n do
  for j: i step i thru n do v[j]: not v[j],
  sublist_indices(v, 'identity));
```

Usage:

```mw
doors(100);
/* [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] */
```


## MAXScript

**unoptimized**

```mw
doorsOpen = for i in 1 to 100 collect false

for pass in 1 to 100 do
(
    for door in pass to 100 by pass do
    (
        doorsOpen[door] = not doorsOpen[door]
    )
)

for i in 1 to doorsOpen.count do
(
    format ("Door % is open?: %\n") i doorsOpen[i]
)
```

**optimized**

```mw
for i in 1 to 100 do
(
    root = pow i 0.5
    format ("Door % is open?: %\n") i (root == (root as integer))
)
```


## Mercury

```mw
:- module doors.
:- interface.
:- import_module io.
:- pred main(io::di, io::uo) is det.
:- implementation.
:- import_module bitmap, bool, list, string, int.

:- func doors = bitmap.
doors = bitmap.init(100, no).

:- pred walk(int, bitmap, bitmap).
:- mode walk(in, bitmap_di, bitmap_uo) is det.
walk(Pass, !Doors) :-
    walk(Pass, Pass, !Doors).

:- pred walk(int, int, bitmap, bitmap).
:- mode walk(in, in, bitmap_di, bitmap_uo) is det.
walk(At, By, !Doors) :-
    ( if bitmap.in_range(!.Doors, At - 1) then
        bitmap.unsafe_flip(At - 1, !Doors),
        walk(At + By, By, !Doors)
    else
        true
    ).

:- pred report(bitmap, int, io, io).
:- mode report(bitmap_di, in, di, uo) is det.
report(Doors, N, !IO) :-
    ( if is_set(Doors, N - 1) then
        State = "open"
    else
        State = "closed"
    ),
    io.format("door #%d is %s\n",
        [i(N), s(State)], !IO).

main(!IO) :-
    list.foldl(walk, 1 .. 100, doors, Doors),
    list.foldl(report(Doors), 1 .. 100, !IO).
```


## Metafont

```mw
boolean doors[];
for i = 1 upto 100: doors[i] := false; endfor
for i = 1 upto 100:
  for j = 1 step i until 100:
    doors[j] := not doors[j];
  endfor
endfor
for i = 1 upto 100:
  message decimal(i) & " " & if doors[i]: "open" else: "close" fi;
endfor
end
```


## Microsoft Small Basic

Translation of

:

GW-BASIC

```mw
For offset = 1 To 100
  For i = 0 To 100 Step offset
    a[i] = a[i] + 1
  EndFor
EndFor
' Print "opened" doors
For i = 1 To 100
  If math.Remainder(a[i], 2) = 1 Then 
    TextWindow.WriteLine(i)
  EndIf  
EndFor
```

**Output**:

```
1
4
9
16
25
36
49
64
81
100
```


## MiniScript

Using a map to hold the set of open doors:

```mw
d = {}
for p in range(1, 100)
    for t in range(p, 100, p)
        if d.hasIndex(t) then d.remove t else d.push t
    end for
end for

print d.indexes.sort
```

**Output:**

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Using an array of boolean values to keep track of door state, and a separate list of indexes of the open doors:

```mw
d = [false] * 101
open = []
for p in range(1, 100)
    for t in range(p, 100, p)
        d[t] = not d[t]
    end for
    if d[p] then open.push p
end for

print open
```

(Output same as above.)


## MIPS Assembly

```mw
.data
  doors:     .space 100
  num_str:   .asciiz "Number "
  comma_gap: .asciiz " is "
  newline:   .asciiz "\n"

.text
main:
# Clear all the cells to zero
  li $t1, 100
  la $t2, doors
clear_loop:
  sb $0, ($t2)
  add $t2, $t2, 1
  sub $t1, $t1, 1
  bnez $t1, clear_loop

# Now start the loops
  li $t0, 1         # This will the the step size
  li $t4, 1         # just an arbitrary 1
loop1:
  move $t1, $t0      # Counter
  la $t2, doors      # Current pointer
  add $t2, $t2, $t0
  addi $t2, $t2, -1
loop2:
  lb $t3, ($t2)
  sub $t3, $t4, $t3
  sb $t3, ($t2)
  add $t1, $t1, $t0
  add $t2, $t2, $t0
  ble $t1, 100, loop2

  addi $t0, $t0, 1
  ble $t0, 100, loop1

  # Now display everything
  la $t0, doors
  li $t1, 1
loop3:
  li $v0, 4
  la $a0, num_str
  syscall
  
  li $v0, 1
  move $a0, $t1
  syscall

  li $v0, 4
  la $a0, comma_gap
  syscall

  li $v0, 1
  lb $a0, ($t0)
  syscall

  li $v0, 4,
  la $a0, newline
  syscall

  addi $t0, $t0, 1
  addi $t1, $t1, 1
  bne $t1, 101 loop3
```


## Mirah

```mw
import java.util.ArrayList

class Door
	:state

	def initialize
		@state=false
	end
 
	def closed?; !@state; end
	def open?; @state; end

	def close; @state=false; end
	def open; @state=true; end
 
	def toggle
		if closed?
			open
		else
			close
		end
	end
 
	def toString; Boolean.toString(@state); end
end
 
doors=ArrayList.new
1.upto(100) do
    doors.add(Door.new)
end 

1.upto(100) do |multiplier|
    index = 0
    doors.each do |door|
        Door(door).toggle if (index+1)%multiplier == 0
        index += 1
    end
end

i = 0
doors.each do |door| 
    puts "Door #{i+1} is #{door}."
    i+=1
end
```


## Miranda

```mw
main :: [sys_message]
main = [Stdout (show (openDoors 100)), 
        Stdout "\n"]    

openDoors :: num->[num]
openDoors doors =
    map snd (filter fst (zip2 (doorStates doors) [1..]))

doorStates :: num->[bool]
doorStates doors =
    take doors (foldr (zipWith (~=)) (repeat False) (map pass [1..doors]))

pass :: num->[bool]
pass n = tl (concat (repeat (take n (True:repeat False))))

zipWith f x y = map f' (zip2 x y)
                where f' (x,y) = f x y
```

**Output:**

```
[1,4,9,16,25,36,49,64,81,100]
```
