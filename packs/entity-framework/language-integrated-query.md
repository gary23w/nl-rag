---
title: "Language Integrated Query"
source: https://en.wikipedia.org/wiki/Language_Integrated_Query
domain: entity-framework
license: CC-BY-SA-4.0
tags: entity framework, ef core, linq to entities, dotnet orm
fetched: 2026-07-02
---

# Language Integrated Query

**Language Integrated Query** (**LINQ**, pronounced "link") is a Microsoft .NET framework component that adds native data querying abilities to .NET languages, originally released as a major part of .NET Framework 3.5 in 2007.

LINQ extends the language by the addition of query expressions, which are akin to SQL statements, and can be used to conveniently extract and process data from arrays, enumerable classes, XML documents, relational databases, and third-party data sources. Other uses, which utilize query expressions as a general framework for readably composing arbitrary computations, include the construction of event handlers or monadic parsers. It also defines a set of method names (called *standard query operators*, or *standard sequence operators*), along with translation rules used by the compiler to translate query syntax expressions into expressions using fluent-style (called method syntax by Microsoft) with these method names, lambda expressions and anonymous types.

## Architecture

### Standard query operator API

In what follows, the descriptions of the operators are based on the application of working with collections. Many of the operators take other functions as arguments. These functions may be supplied in the form of a named method or anonymous function.

The set of query operators defined by LINQ is exposed to the user as the Standard Query Operator (SQO) application programming interface (API). The query operators supported by the API are:

#### `Select`

The `Select` operator performs a projection on the collection to select interesting aspects of the elements. The user supplies an arbitrary function, in the form of a named or lambda expression, which projects the data members. The function is passed to the operator as a delegate. This implements the Map higher-order function.

#### `Where`

The `Where` operator allows the definition of a set of predicate rules that are evaluated for each object in the collection, while objects that do not match the rule are filtered away. The predicate is supplied to the operator as a delegate. This implements the Filter higher-order function.

#### `SelectMany`

For a user-provided mapping from collection elements to collections, semantically two steps are performed. First, every element is mapped to its corresponding collection. Second, the result of the first step is flattened by one level. `Select` and `Where` are both implementable in terms of `SelectMany`, as long as singleton and empty collections are available. The translation rules mentioned above still make it mandatory for a LINQ provider to provide the other two operators. This implements the Bind higher-order function.

#### `Sum`, `Min`, `Max`, `Average`

These operators optionally take a function that retrieves a certain numeric value from each element in the collection and uses it to find the sum, minimum, maximum or average values of all the elements in the collection, respectively. Overloaded versions take no function and act as if the identity is given as the lambda.

#### `Aggregate`

A generalized `Sum`/`Min`/`Max`. This operator takes a function that specifies how two values are combined to form an intermediate or the final result. Optionally, a starting value can be supplied, enabling the result type of the aggregation to be arbitrary. Furthermore, a finalization function, taking the aggregation result to yet another value, can be supplied. This implements the Fold higher-order function.

#### `Join`, `GroupJoin`

The `Join` operator performs an inner join on two collections, based on matching keys for objects in each collection. It takes two functions as delegates, one for each collection, that it executes on each object in the collection to extract the key from the object. It also takes another delegate in which the user specifies which data elements, from the two matched elements, should be used to create the resultant object. The `GroupJoin` operator performs a group join. Like the `Select` operator, the results of a join are instantiations of a different class, with all the data members of both the types of the source objects, or a subset of them.

#### `Take`, `TakeWhile`

The `Take` operator selects the first `n` objects from a collection, while the `TakeWhile` operator, which takes a predicate, selects those objects that match the predicate (stopping at the first object that doesn't match it).

#### `Skip`, `SkipWhile`

The `Skip` and `SkipWhile` operators are complements of `Take` and `TakeWhile` - they skip the first `n` objects from a collection, or those objects that match a predicate (for the case of `SkipWhile`).

#### `OfType`

The `OfType` operator is used to select the elements of a certain type.

#### `Concat`

The `Concat` operator concatenates two collections.

#### `OrderBy`, `ThenBy`

The `OrderBy` operator is used to specify the primary sort ordering of the elements in a collection according to some key. The default ordering is in ascending order, to reverse the order, the `OrderByDescending` operator is to be used. `ThenBy` and `ThenByDescending` specifies subsequent ordering of the elements. The function to extract the key value from the object is specified by the user as a delegate.

#### `Reverse`

The `Reverse` operator reverses a collection.

#### `GroupBy`

The `GroupBy` operator takes a function that extracts a key value and returns a collection of `System.Linq.IGrouping<K, V>` objects, for each distinct key value. The `System.Linq.IGrouping<K, V>` objects can then be used to enumerate all the objects for a particular key value.

#### `Distinct`

The `Distinct` operator removes duplicate instances of an object from a collection. An overload of the operator takes an equality comparator object which defines the criteria for distinctness.

#### `Union`, `Intersect`, `Except`

These operators are used to perform a union, intersection and difference operation on two sequences, respectively. Each has an overload which takes an equality comparator object which defines the criteria for element equality.

#### `SequenceEqual`

The `SequenceEqual` operator determines whether all elements in two collections are equal and in the same order.

#### `First`, `FirstOrDefault`, `Last`, `LastOrDefault`

These operators take a predicate. The `First` operator returns the first element for which the predicate yields true, or, if nothing matches, throws an exception. The `FirstOrDefault` operator is like the `First` operator except that it returns the default value for the element type (usually a null reference) in case nothing matches the predicate. The `Last` operator retrieves the last element to match the predicate, or throws an exception in case nothing matches. The `LastOrDefault` returns the default element value if nothing matches.

#### `Single`, `SingleOrDefault`

The `Single` operator takes a predicate and returns the element that matches the predicate. An exception is thrown, if none or more than one element match the predicate.

The `SingleOrDefault` operator takes a predicate and return the element that matches the predicate. If more than one element matches the predicate, an exception is thrown. If no element matches the predicate, a default value is returned.

#### `ElementAt`

The `ElementAt` operator retrieves the element at a given index in the collection.

#### `Any`, `All`

The `Any` operator checks, if there are any elements in the collection matching the predicate. It does not select the element, but returns true if at least one element is matched. An invocation of any without a predicate returns true if the collection non-empty. The `All` operator returns true if all elements match the predicate.

#### `Contains`

The `Contains` operator checks, if the collection contains a given element.

#### `Count`

The `Count` operator counts the number of elements in the given collection. An overload taking a predicate, counts the number of elements matching the predicate.

The standard query operator API also specifies certain operators that convert a collection into another type:

- `AsEnumerable`: Statically types the collection as an `System.Collections.Generic.IEnumerable<T>`.
- `AsQueryable`: Statically types the collection as an `System.Linq.IQueryable<T>`.
- `ToArray`: Creates an array `T[]` from the collection.
- `ToList`: Creates a `System.Collections.Generic.List<T>` from the collection.
- `ToDictionary`: Creates a `System.Collections.Generic.Dictionary<K, V>` from the collection, indexed by the key `K`. A user supplied projection function extracts a key from each element.
- `ToLookup`: Creates a `System.Linq.Lookup<K, V>` from the collection, indexed by the key `K`. A user supplied projection function extracts a key from each element.
- `Cast`: converts a non-generic `System.Collections.IEnumerable` collection to one of `System.Collections.Generic.IEnumerable<T>` by casting each element to type `T`. Alternately converts a generic `System.Collections.Generic.IEnumerable<T>` to another generic `System.Collections.Generic.IEnumerable<R>` by casting each element from type `T` to type `R`. Throws an exception in any element cannot be cast to the indicated type.
- `OfType`: converts a non-generic `System.Collections.IEnumerable` collection to one of `System.Collections.Generic.IEnumerable<T>`. Alternately converts a generic `System.Collections.Generic.IEnumerable<T>` to another generic `System.Collections.Generic.IEnumerable<R>` by attempting to cast each element from type `T` to type `R`. In both cases, only the subset of elements successfully cast to the target type are included. No exceptions are thrown.

### Language extensions

While LINQ is mainly implemented as a library for .NET Framework 3.5, it also defines optional language extensions that make queries a first-class language construct and provide syntactic sugar for writing queries. These language extensions have initially been implemented in C# 3.0, VB 9.0, F# and Oxygene, with other languages like Nemerle having announced preliminary support. The language extensions include:

- Query syntax: A language is free to choose a query syntax that it will recognize natively. These language keywords must be translated by the compiler to appropriate LINQ method calls.
- Implicitly typed variables: This enhancement allows variables to be declared without specifying their types. The languages C# 3.0 and Oxygene declare them with the `var` keyword. In VB9.0, the `Dim` keyword without type declaration accomplishes the same. Such objects are still strongly typed; for these objects the compiler infers the types of variables via type inference, which allows the results of the queries to be specified and defined without declaring the type of the intermediate variables.
- Anonymous types: Anonymous types allow classes that contain only data-member declarations to be inferred by the compiler. This is useful for the Select and Join operators, whose result types may differ from the types of the original objects. The compiler uses type inference to determine the fields contained in the classes and generates accessors and mutators for these fields.
- Object initializer: Object initializers allow an object to be created and initialized in a single scope, as required for Select and Join operators.
- Lambda expressions: Lambda expressions allow predicates and other projection functions to be written inline with a concise syntax, and support full lexical closure. They are captured into parameters as delegates or expression trees depending on the Query Provider.

For example, in the query to select all the objects in a collection with `SomeProperty` less than 10,

```mw
using System;
using System.Collections.Generic;

IEnumerable<MyObject> SomeCollection = /* something here */;

IEnumerable<MyObject> results = from c in SomeCollection
                                where c.SomeProperty < 10
                                select new {c.SomeProperty, c.OtherProperty};

foreach (MyObject result in results)
{
    Console.WriteLine(result);
}
```

the types of variables `result`, `c` and `results` all are inferred by the compiler in accordance to the signatures of the methods eventually used. The basis for choosing the methods is formed by the query expression-free translation result

```mw
using System;
using System.Collections.Generic;

IEnumerable<MyObject> results = SomeCollection
    .Where(c => c.SomeProperty < 10)
    .Select(c => new {c.SomeProperty, c.OtherProperty});

results.ForEach(x => {Console.WriteLine(x.ToString());})
```

### LINQ providers

The C#3.0 specification defines a Query Expression Pattern along with translation rules from a LINQ expression to an expression in a subset of C# 3.0 without LINQ expressions. The translation thus defined is actually un-typed, which, in addition to lambda expressions being interpretable as either delegates or expression trees, allows for a great degree of flexibility for libraries wishing to expose parts of their interface as LINQ expression clauses. For example, **LINQ to Objects** works on `System.Collections.Generic.IEnumerable<T>`s and with delegates, whereas **LINQ to SQL** makes use of the expression trees.

The expression trees are at the core of the LINQ extensibility mechanism, by which LINQ can be adapted for many data sources. The expression trees are handed over to LINQ Providers, which are data source-specific implementations that adapt the LINQ queries to be used with the data source. If they choose so, the LINQ Providers analyze the expression trees contained in a query in order to generate essential pieces needed for the execution of a query. This can be SQL fragments or any other completely different representation of code as further manipulatable data. LINQ comes with LINQ Providers for in-memory object collections, Microsoft SQL Server databases, ADO.NET datasets and XML documents. These different providers define the different flavors of LINQ:

#### LINQ to Objects

The LINQ to Objects provider is used for in-memory collections, using the local query execution engine of LINQ. The code generated by this provider refers to the implementation of the standard query operators as defined on the `Sequence` pattern and allows `System.Collections.Generic.IEnumerable<T>` collections to be queried locally. Current implementation of LINQ to Objects perform interface implementation checks to allow for fast membership tests, counts, and indexed lookup operations when they are supported by the runtime type of the `System.Collections.Generic.IEnumerable<T>`.

#### LINQ to XML (formerly named XLINQ)

The LINQ to XML provider converts an XML document to a collection of `System.Linq.Xml.XElement` objects, which are then queried against using the local execution engine that is provided as a part of the implementation of the standard query operator. The LINQ to XML provider converts an XML document to a collection of `System.Linq.Xml.XElement` objects, which are then queried against using the local execution engine that is provided as a part of the implementation of the standard query operator.

#### LINQ to SQL (formerly named DLINQ)

The LINQ to SQL provider allows LINQ to be used to query Microsoft SQL Server databases, including SQL Server Compact databases. Since SQL Server data may reside on a remote server, and because SQL Server has its own query engine, LINQ to SQL does not use the query engine of LINQ. Instead, it converts a LINQ query to a SQL query that is then sent to SQL Server for processing. However, since SQL Server stores the data as relational data and LINQ works with data encapsulated in objects, the two representations must be mapped to one another. For this reason, LINQ to SQL also defines a mapping framework. The mapping is done by defining classes that correspond to the tables in the database, and containing all or a subset of the columns in the table as data members. The correspondence, along with other relational model attributes such as primary keys, are specified using LINQ to SQL-defined attributes. For example,

```mw
using System.Data.Linq;

[Table(Name="Customers")]
public class Customer
{
     [Column(IsPrimaryKey = true)]
     public int CustID;

     [Column]
     public string CustName;
}
```

This class definition maps to a table named `Customers` and the two data members correspond to two columns. The classes must be defined before LINQ to SQL can be used. Visual Studio 2008 includes a mapping designer that can be used to create the mapping between the data schemas in the object as well as the relational domain. It can automatically create the corresponding classes from a database schema, as well as allow manual editing to create a different view by using only a subset of the tables or columns in a table.

The mapping is implemented by the `System.Data.Linq.DataContext` that takes a connection string to the server, and can be used to generate a `System.Data.Linq.Table<T>` where `T` is the type to which the database table will be mapped. The `System.Data.Linq.Table<T>` encapsulates the data in the table, and implements the `System.Linq.IQueryable<T>` interface, so that the expression tree is created, which the LINQ to SQL provider handles. It converts the query into T-SQL and retrieves the result set from the database server. Since the processing happens at the database server, local methods, which are not defined as a part of the lambda expressions representing the predicates, cannot be used. However, it can use the stored procedures on the server. Any changes to the result set are tracked and can be submitted back to the database server.

#### LINQ to DataSets

Since the LINQ to SQL provider (above) works only with Microsoft SQL Server databases, in order to support any generic database, LINQ also includes the LINQ to DataSets. It uses ADO.NET to handle the communication with the database. Once the data is in ADO.NET Datasets, LINQ to DataSets execute queries against these datasets.

## Performance

Non-professional users may struggle with subtleties in the **LINQ to Objects** features and syntax. Naive LINQ implementation patterns can lead to a catastrophic degradation of performance.

**LINQ to XML** and **LINQ to SQL** performance compared to ADO.NET depends on the use case.

## PLINQ

Version 4 of the .NET framework includes Parallel Extensions for *Parallel LINQ* (PLINQ), a parallel execution engine for LINQ queries. It defines the `System.Linq.ParallelQuery<T>` class. Any implementation of the `System.Collections.Generic.IEnumerable<T>` interface can take advantage of the PLINQ engine by calling the `AsParallel<T>(this IEnumerable<T>)` extension method defined by the `System.Linq.ParallelEnumerable` class namespace of the .NET framework. The PLINQ engine can execute parts of a query concurrently on multiple threads, providing faster results.

## Predecessor languages

Many of the concepts that LINQ introduced were originally tested in Microsoft's **Cω** research project, formerly known by the codenames **X#** (X Sharp) and **Xen**. It was renamed to Cω after **Polyphonic C#** (another research language based on join calculus principles) was integrated into it.

Cω attempts to make datastores (such as databases and XML documents) accessible with the same ease and type safety as traditional types like strings and arrays. Many of these ideas were inherited from an earlier incubation project within the WebData XML team called X# and Xen. Cω also includes new constructs to support concurrent programming; these features were largely derived from the earlier Polyphonic C# project.

First available in 2004 as a compiler preview, Cω's features were subsequently used by Microsoft in the creation of the LINQ features released in 2007 in .NET version 3.5 The concurrency constructs have also been released in a slightly modified form as a library, named *Joins Concurrency Library*, for C# and other .NET languages by Microsoft Research.
