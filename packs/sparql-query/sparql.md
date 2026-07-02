---
title: "SPARQL"
source: https://en.wikipedia.org/wiki/SPARQL
domain: sparql-query
license: CC-BY-SA-4.0
tags: sparql query language, rdf query language, semantic web query, triple pattern query
fetched: 2026-07-02
---

# SPARQL

**SPARQL** (pronounced "sparkle", a recursive acronym for **SPARQL Protocol and RDF Query Language**) is an RDF query language—that is, a semantic query language for databases—able to retrieve and manipulate data stored in Resource Description Framework (RDF) format. It was made a standard by the *RDF Data Access Working Group* (DAWG) of the World Wide Web Consortium, and is recognized as one of the key technologies of the semantic web. On 15 January 2008, SPARQL 1.0 was acknowledged by W3C as an official recommendation, and SPARQL 1.1 in March, 2013.

SPARQL allows for a query to consist of triple patterns, conjunctions, disjunctions, and optional patterns.

Implementations for multiple programming languages exist. There exist tools that allow one to connect and semi-automatically construct a SPARQL query for a SPARQL endpoint, for example ViziQuer. In addition, tools exist to translate SPARQL queries to other query languages, for example to SQL and to XQuery.

## Features

SPARQL allows users to write queries that follow the RDF specification of the W3C. Thus, the entire dataset is "subject-predicate-object" triples. Subjects and predicates are always URI identifiers, but objects can be URIs or literal values. This single physical schema of three "columns" is hypernormalized in that what would be one relational record with (for example) four columns is now four triples with the subject being repeated over and over, the predicate essentially being the column name, and the object being the column value. The SPARQL syntax offers these features:

**1. Subjects and Objects can be used to find the other including transitively.**

Below is a set of triples. It should be clear that `ex:sw001` and `ex:sw002` link to `ex:sw003`, which itself has links:

```mw
ex:sw001        ex:linksWith    ex:sw003 .
ex:sw002        ex:linksWith    ex:sw003 .
ex:sw003        ex:linksWith    ex:sw004 , ex:sw006 .
ex:sw004        ex:linksWith    ex:sw005 .
```

In SPARQL, the first time a variable is encountered in the expression pipeline, it is populated with result. The second and subsequent times it is seen, it is used as an input. If we assign ("bind") the URI `ex:sw003` to the `?targets` variable, then it drives a result into `?src`; this tells us all the things that link *to* `ex:sw003` (upstream dependency):

```mw
SELECT *
WHERE {
    BIND(ex:sw003 AS ?targets)
    ?src  ex:linksWith ?targets .  # ?src populated with ex:sw001, ex:sw002
}
```

But with a simple switch of the binding variable, the behavior is reversed. This will produce all the things upon which `ex:sw003` depends (downstream dependency):

```mw
SELECT *
WHERE {
    BIND(ex:sw003 AS ?src)
    ?src  ex:linksWith ?targets .    # NOTICE!  No syntax change! ?targets populated with ex:sw004, ex:sw006
}
```

Even more attractive is that we can easily instruct SPARQL to transitively follow the path:

```mw
SELECT *
WHERE {
    BIND(ex:sw003 AS ?src)

    # Note the +; now SPARQL will also find ex:sw005 transitively via ex:sw004; ?targets is ex:sw004, ex:sw005, ex:sw006
    ?src  ex:linksWith+ ?targets .
}
```

Bound variables can therefore also be lists and will be operated upon without complicated syntax. The effect of this is similar to the following pseudocode:

```mw
If ?S is bound to (ex:A, ex:B) and ?O is UNbound then
    ?S ex:linksWith ?O
behaves like a forward chain:
    for each s in ?S:
        for each fetch (s, ex:linksWith):
            capture o
            append o to ?O

If ?O is bound to (ex:A, ex:B) and ?S is UNbound then
    ?S ex:linksWith ?O
behaves like a backward chain:
    for each o in ?O:
        for each fetch (ex:linksWith, o):
            capture s
            append s to ?S
```

**2. SPARQL expressions are a pipeline**

Unlike SQL which has subqueries and CTEs, SPARQL is much more like MongoDB or SPARK. Expressions are evaluated exactly in the order they are declared including filtering and joining of data. The programming model becomes what a SQL statement would be like with multiple WHERE clauses. The combination of list-aware subjects and objects plus a pipeline approach can yield extremely expressive queries spanning many different domains of data. JOIN as used in RDBMS and understanding the dynamics of the JOIN (e.g. what column in what table is suitable to join to another, inner vs. outer, etc.) is not relevant in SPARQL (and in some ways simpler) because objects, if an URI and not a literal, implicitly can be used *only* to find a subject. Here is a more comprehensive example that illustrates the pipeline using some syntax shortcuts.

```mw
#  SELECT only the terminal values we need.  If we did SELECT * (which
#  is not nessarily bad), then "intermediate" variables ?vendor and ?owner
#  would be part of the output.
SELECT ?slbl ?vlbl ?lei ?lname
WHERE {
    # ?sw is unbound.  Set predicate to rdf:type and object to ex:Software
    # and collect all software instances.  At same, pull the software
    # label (a terse description) and populate ?slbl and also capture the
    # vendor object into ?vendor.
    ?sw rdf:type  ex:Software ;
        rdfs:label ?slbl ;
        ex:vendor ?vendor .

    # The above in "longhand" reveals the binding process:
    #  ?sw rdf:type  ex:Software .  # ?sw UNBOUND; is set here
    #  ?sw rdfs:label ?slbl . # ?sw bound; set unbound ?slbl
    #  ?sw ex:vendor ?vendor .  # ?sw still bound; set ?vendor

    # Exclude open source software.  Note ex:oss is an URI because it is
    # an UNquoted string:
    FILTER(?vendor NOT IN (ex:oss))

    # Next, dive into ?vendor object and extract legal entity identifier
    # and owner of the data -- where owner is also an object.  ?vendor is
    # bound; ?vlbl, ?lei, and ?owner are unbound and will be populated:
    ?vendor  rdfs:label  ?vlbl ;
             ex:LEI    ?lei ;
             ex:owner  ?owner .

    #  Lastly, from owner object, capture last name:
    ?owner   ex:lastname   ?lname .
}
```

Unlike relational databases, the object column is heterogeneous: the object data type, if not an URI, is usually implied (or specified in the ontology) by the predicate value. Literal nodes carry type information consistent with the underlying XSD namespace including signed and unsigned short and long integers, single and double precision floats, datetime, penny-precise decimal, Boolean, and string. Triple store implementations on traditional relational databases will typically store the value as a string and a fourth column will identify the real type. Polymorphic databases such as MongoDB and SQLite can store the native value directly into the object field.

Thus, SPARQL provides a full set of analytic query operations such as `JOIN`, `SORT`, `AGGREGATE` for data whose schema is intrinsically part of the data rather than requiring a separate schema definition. However, schema information (the ontology) is often provided externally, to allow joining of different datasets unambiguously. In addition, SPARQL provides specific graph traversal syntax for data that can be thought of as a graph.

The example below demonstrates a simple query that leverages the ontology definition `foaf` ("friend of a friend").

Specifically, the following query returns names and emails of every person in the dataset:

```mw
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?name
       ?email
WHERE
  {
    ?person  a          foaf:Person .
    ?person  foaf:name  ?name .
    ?person  foaf:mbox  ?email .
  }
```

This query joins all of the triples with a matching subject, where the type predicate, "`a`", is a person (`foaf:Person`), and the person has one or more names (`foaf:name`) and mailboxes (`foaf:mbox`).

For the sake of readability, the author of this query chose to reference the subject using the variable name "`?person`". Since the first element of the triple is always the subject, the author could have just as easily used any variable name, such as "`?subj`" or "`?x`". Whatever name is chosen, it must be the same on each line of the query to signify that the query engine is to join triples with the same subject.

The result of the join is a set of rows – `?person`, `?name`, `?email`. This query returns the `?name` and `?email` because `?person` is often a complex URI rather than a human-friendly string. Note that any `?person` may have multiple mailboxes, so in the returned set, a `?name` row may appear multiple times, once for each mailbox, duplicating the `?name`.

An important consideration in SPARQL is that when lookup conditions are not met in the pipeline for terminal entities like `?email`, then the *whole row is excluded*, unlike SQL where typically a null column is returned. The query above will return only those `?person` where both at least one `?name` and at least one `?email` can be found. If a `?person` had no email, they would be excluded. To align the output with that expected from an equivalent SQL query, the `OPTIONAL` keyword is required:

```mw
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?name
       ?email
WHERE
  {
    ?person  a          foaf:Person .
    OPTIONAL {
        ?person  foaf:name  ?name .
        ?person  foaf:mbox  ?email .
    }
  }
```

This query can be distributed to multiple SPARQL endpoints (services that accept SPARQL queries and return results), computed, and results gathered, a procedure known as federated query.

Whether in a federated manner or locally, additional triple definitions in the query could allow joins to different subject types, such as automobiles, to allow simple queries, for example, to return a list of names and emails for people who drive automobiles with a high fuel efficiency.

## Query forms

In the case of queries that read data from the database, the SPARQL language specifies four different query variations for different purposes.

**`SELECT` query**

Used to extract raw values from a SPARQL endpoint, the results are returned in a table format.

**`CONSTRUCT` query**

Used to extract information from the SPARQL endpoint and transform the results into valid RDF.

**`ASK` query**

Used to provide a simple True/False result for a query on a SPARQL endpoint.

**`DESCRIBE` query**

Used to extract an RDF graph from the SPARQL endpoint, the content of which is left to the endpoint to decide, based on what the maintainer deems as useful information.

Each of these query forms takes a `WHERE` block to restrict the query, although, in the case of the `DESCRIBE` query, the `WHERE` is optional.

SPARQL 1.1 specifies a language for updating the database with several new query forms.

## Example

Another SPARQL query example that models the question "What are all the country capitals in Africa?":

```mw
PREFIX ex: <http://example.com/exampleOntology#>
SELECT ?capital
       ?country
WHERE
  {
    ?x  ex:cityname       ?capital   ;
        ex:isCapitalOf    ?y         .
    ?y  ex:countryname    ?country   ;
        ex:isInContinent  ex:Africa  .
  }
```

Variables are indicated by a `?` or `$` prefix. Bindings for `?capital` and the `?country` will be returned. When a triple ends with a semicolon, the subject from this triple will implicitly complete the following pair to an entire triple. So for example `ex:isCapitalOf ?y` is short for `?x ex:isCapitalOf ?y`.

The SPARQL query processor will search for sets of triples that match these four triple patterns, binding the variables in the query to the corresponding parts of each triple. Important to note here is the "property orientation" (class matches can be conducted solely through class-attributes or properties – see Duck typing).

To make queries concise, SPARQL allows the definition of prefixes and base URIs in a fashion similar to Turtle. In this query, the prefix "`ex`" stands for “`http://example.com/exampleOntology#`”.

SPARQL has native dateTime operations as well. Here is a query that will return all pieces of software where the EOL date is greater than or equal to 1000 days from the release date and the release year is 2020 or greater:

```mw
SELECT ?lbl ?version ?released ?eol ?duration
WHERE {
    ?software a ex:Software ;
              rdfs:label  ?lbl ;
              ex:EOL  ?eol ;   # is xsd:dateTime
              ex:version ?version ;  # string
              ex:released ?released ; # is xsd:dateTime

    # After this stage,	?duration is bound as xsd:duration type
    # (in Java implementations, org.apache.jena.datatypes.xsd.XSDDuration)
    # and is available in the pipeline,	in the SELECT, and in
    # GROUP or ORDER operators,	etc.:
    BIND(?eol - ?released AS ?duration)

    # toString representation of Duration is of format PnYnMnDTnHnMnS.  
    # We must use ^^ casting to tell the engine this is to be treated as a duration.
    # SPARQL (and RDF) literal syntax has built-in numeric shortcuts to simplify 
    # expressions without casts:
    #   16         xsd:int       java.lang.Integer
    #   16.7       xsd:decimal   java.math.BigDecimal   preserves precision
    #   16.700     xsd:decimal   java.math.BigDecimal   preserves precision
    #   1.0632e6   xsd:double    java.lang.Double   true double float; be careful
    #   2147483649 xsd:long      java.lang.Long  >32 bit int automatically detected
    #
    # Most castings work as expected e.g. "16.700"^^xsd:double.   
    # Note in the FILTER below we use the shortcut for integer 2020:

    FILTER(?duration >= "P1000D"^^xsd:duration && YEAR(?released) >= 2020)
}
ORDER BY DESC(?duration)
LIMIT 5
```

## Extensions

GeoSPARQL defines filter functions for geographic information system (GIS) queries using well-understood OGC standards (GML, WKT, etc.).

SPARUL is another extension to SPARQL. It enables the RDF store to be updated with this declarative query language, by adding `INSERT` and `DELETE` methods.

XSPARQL is an integrated query language combining XQuery with SPARQL to query both XML and RDF data sources at once.

## Implementations

Open source, reference SPARQL implementations

- Eclipse RDF4J, formerly OpenRDF Sesame
- Apache Jena
- OpenLink Virtuoso

See List of SPARQL implementations for more comprehensive coverage, including triplestore, APIs, and other storages that have implemented the SPARQL standard.
