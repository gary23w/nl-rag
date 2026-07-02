---
title: "Jakarta Persistence Query Language"
source: https://en.wikipedia.org/wiki/Java_Persistence_Query_Language
domain: hibernate-orm
license: CC-BY-SA-4.0
tags: hibernate orm, jpa persistence, hql query, java persistence
fetched: 2026-07-02
---

# Jakarta Persistence Query Language

(Redirected from

Java Persistence Query Language

)

The **Jakarta Persistence Query Language** (**JPQL**; formerly Java Persistence Query Language) is a platform-independent object-oriented query language defined as part of the Jakarta Persistence (JPA; formerly Java Persistence API) specification.

JPQL is used to make queries against entities stored in a relational database. It is heavily inspired by SQL, and its queries resemble SQL queries in syntax, but operate against JPA entity objects rather than directly with database tables.

In addition to retrieving objects (`SELECT` queries), JPQL supports set based `UPDATE` and `DELETE` queries.

## Examples

Example JPA Classes, getters and setters omitted for simplicity.

```mw
@Entity
public class Author {
    @Id
    private Integer id;
    private String firstName;
    private String lastName;
 
    @ManyToMany
    private List<Book> books;
}
 
@Entity
public class Book {
    @Id
    private Integer id;
    private String title;
    private String isbn;
 
    @ManyToOne
    private Publisher publisher;
 
    @ManyToMany
    private List<Author> authors;
}
 
@Entity
public class Publisher {
    @Id
    private Integer id;
    private String name;
    private String address;
 
    @OneToMany(mappedBy = "publisher")
    private List<Book> books;
}
```

Then a simple query to retrieve the list of all authors, ordered alphabetically, would be:

```mw
SELECT a FROM Author a ORDER BY a.firstName, a.lastName
```

To retrieve the list of authors that have ever been published by XYZ Press:

```mw
SELECT DISTINCT a FROM Author a INNER JOIN a.books b WHERE b.publisher.name = 'XYZ Press'
```

JPQL supports named parameters, which begin with the colon (`:`). We could write a function returning a list of authors with the given last name as follows:

```mw
import javax.persistence.EntityManager;
import javax.persistence.TypedQuery;

...

public List<Author> getAuthorsByLastName(String lastName) {
    String queryString = "SELECT a FROM Author a " +
                         "WHERE a.lastName IS NULL OR LOWER(a.lastName) = LOWER(:lastName)";

    TypedQuery<Author> query = getEntityManager().createQuery(queryString, Author.class);
    query.setParameter("lastName", lastName);
    return query.getResultList();
}
```

## Hibernate Query Language

JPQL is based on the Hibernate Query Language (HQL), an earlier non-standard query language included in the Hibernate object-relational mapping library.

Hibernate and the HQL were created before the JPA specification. As of Hibernate 3 JPQL is a subset of HQL.
