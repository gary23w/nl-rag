---
title: "M-tree"
source: https://en.wikipedia.org/wiki/M-tree
domain: metric-space-tree
license: CC-BY-SA-4.0
tags: ball tree, vantage-point tree, metric tree, cover tree, nearest neighbor search
fetched: 2026-07-02
---

# M-tree

In computer science, **M-trees** are tree data structures that are similar to R-trees and B-trees. It is constructed using a metric and relies on the triangle inequality for efficient range and k-nearest neighbor (k-NN) queries. While M-trees can perform well in many conditions, the tree can also have large overlap and there is no clear strategy on how to best avoid overlap. In addition, it can only be used for distance functions that satisfy the triangle inequality, while many advanced dissimilarity functions used in information retrieval do not satisfy this.

## Overview

As in any tree-based data structure, the M-tree is composed of nodes and leaves. In each node there is a data object that identifies it uniquely and a pointer to a sub-tree where its children reside. Every leaf has several data objects. For each node there is a radius r that defines a Ball in the desired metric space. Thus, every node n and leaf l residing in a particular node N is at most distance r from N , and every node n and leaf l with node parent N keep the distance from it.

## M-tree construction

### Components

An M-tree has these components and sub-components:

1. Non-leaf nodes
  1. A set of routing objects N*RO*.
  2. Pointer to Node's parent object O*p*.
2. Leaf nodes
  1. A set of objects N*O*.
  2. Pointer to Node's parent object O*p*.
3. Routing Object
  1. (Feature value of) routing object O*r*.
  2. Covering radius r(O*r*).
  3. Pointer to covering tree T(O*r*).
  4. Distance of O*r* from its parent object d(O*r*,P(O*r*))
4. Object
  1. (Feature value of the) object O*j*.
  2. Object identifier oid(O*j*).
  3. Distance of O*j* from its parent object d(O*j*,P(O*j*))

### Insert

The main idea is first to find a leaf node N where the new object O belongs. If N is not full then just attach it to N. If N is full then invoke a method to split N. The algorithm is as follows:

```
Algorithm Insert
  Input: Node N of M-Tree MT, Entry 
  
    
      
        
          O
          
            n
          
        
      
    
    {\displaystyle O_{n}}
  

  Output: A new instance of MT containing all entries in original MT plus 
  
    
      
        
          O
          
            n
          
        
      
    
    {\displaystyle O_{n}}
  
```

```
  
  
    
      
        
          N
          
            e
          
        
        ←
        N
      
    
    {\displaystyle N_{e}\gets N}
  
's routing objects or objects
  if N is not a leaf then
  {
       /* Look for entries that the new object fits into */
       let 
  
    
      
        
          N
          
            i
            n
          
        
      
    
    {\displaystyle N_{in}}
  
 be routing objects from 
  
    
      
        
          N
          
            e
          
        
      
    
    {\displaystyle N_{e}}
  
's set of routing objects 
  
    
      
        
          N
          
            R
            O
          
        
      
    
    {\displaystyle N_{RO}}
  
 such that 
  
    
      
        d
        (
        
          O
          
            r
          
        
        ,
        
          O
          
            n
          
        
        )
        ≤
        r
        (
        
          O
          
            r
          
        
        )
      
    
    {\displaystyle d(O_{r},O_{n})\leq r(O_{r})}
  

       if 
  
    
      
        
          N
          
            i
            n
          
        
      
    
    {\displaystyle N_{in}}
  
 is not empty then
       {
          /* If there are one or more entry, then look for an entry such that is closer to the new object */
          
  
    
      
        
          O
          
            r
          
          
            ∗
          
        
        ←
        
          min
          
            
              O
              
                r
              
            
            ∈
            
              N
              
                i
                n
              
            
          
        
        d
        (
        
          O
          
            r
          
        
        ,
        
          O
          
            n
          
        
        )
      
    
    {\displaystyle O_{r}^{*}\gets \min _{O_{r}\in N_{in}}d(O_{r},O_{n})}
  

       }
       else
       {
          /* If there are no such entry, then look for an object with minimal distance from */ 
          /* its covering radius's edge to the new object */
          
  
    
      
        
          O
          
            r
          
          
            ∗
          
        
        ←
        
          min
          
            
              O
              
                r
              
            
            ∈
            
              N
              
                i
                n
              
            
          
        
        d
        (
        
          O
          
            r
          
        
        ,
        
          O
          
            n
          
        
        )
        −
        r
        (
        
          O
          
            r
          
        
        )
      
    
    {\displaystyle O_{r}^{*}\gets \min _{O_{r}\in N_{in}}d(O_{r},O_{n})-r(O_{r})}
  

          /* Upgrade the new radii of the entry */
          
  
    
      
        r
        (
        
          O
          
            r
          
          
            ∗
          
        
        )
        ←
        d
        (
        
          O
          
            r
          
          
            ∗
          
        
        ,
        
          O
          
            n
          
        
        )
      
    
    {\displaystyle r(O_{r}^{*})\gets d(O_{r}^{*},O_{n})}
  

       }
       /* Continue inserting in the next level */
       return insert(
  
    
      
        T
        (
        
          O
          
            r
          
          
            ∗
          
        
        )
        ,
        
          O
          
            n
          
        
      
    
    {\displaystyle T(O_{r}^{*}),O_{n}}
  
);
  else
  {
       /* If the node has capacity then just insert the new object */
       if N is not full then
       { store(
  
    
      
        N
        ,
        
          O
          
            n
          
        
      
    
    {\displaystyle N,O_{n}}
  
) }
       /* The node is at full capacity, then it is needed to do a new split in this level */
       else
       { split(
  
    
      
        N
        ,
        
          O
          
            n
          
        
      
    
    {\displaystyle N,O_{n}}
  
) }
  }
```

- "←" denotes assignment. For instance, "*largest* ← *item*" means that the value of *largest* changes to the value of *item*.
- "**return**" terminates the algorithm and outputs the following value.

### Split

If the split method arrives to the root of the tree, then it choose two routing objects from N, and creates two new nodes containing all the objects in original N, and store them into the new root. If split methods arrives to a node N that is not the root of the tree, the method choose two new routing objects from N, re-arrange every routing object in N in two new nodes $N_{1}$ and $N_{2}$ , and store these new nodes in the parent node $N_{p}$ of original N. The split must be repeated if $N_{p}$ has not enough capacity to store $N_{2}$ . The algorithm is as follow:

```
Algorithm Split
  Input: Node N of M-Tree MT, Entry 
  
    
      
        
          O
          
            n
          
        
      
    
    {\displaystyle O_{n}}
  

  Output: A new instance of MT containing a new partition.
```

```
  /* The new routing objects are now all those in the node plus the new routing object */
  let be NN entries of 
  
    
      
        N
        ∪
        O
      
    
    {\displaystyle N\cup O}
  

  if N is not the root then
  {
     /*Get the parent node and the parent routing object*/
     let 
  
    
      
        
          O
          
            p
          
        
      
    
    {\displaystyle O_{p}}
  
 be the parent routing object of N
     let 
  
    
      
        
          N
          
            p
          
        
      
    
    {\displaystyle N_{p}}
  
 be the parent node of N
  }
  /* This node will contain part of the objects of the node to be split */
  Create a new node N'
  /* Promote two routing objects from the node to be split, to be new routing objects */
  Create new objects 
  
    
      
        
          O
          
            p
            1
          
        
      
    
    {\displaystyle O_{p1}}
  
 and 
  
    
      
        
          O
          
            p
            2
          
        
      
    
    {\displaystyle O_{p2}}
  
.
  Promote(
  
    
      
        N
        ,
        
          O
          
            p
            1
          
        
        ,
        
          O
          
            p
            2
          
        
      
    
    {\displaystyle N,O_{p1},O_{p2}}
  
)
  /* Choose which objects from the node being split will act as new routing objects */
  Partition(
  
    
      
        N
        ,
        
          O
          
            p
            1
          
        
        ,
        
          O
          
            p
            2
          
        
        ,
        
          N
          
            1
          
        
        ,
        
          N
          
            2
          
        
      
    
    {\displaystyle N,O_{p1},O_{p2},N_{1},N_{2}}
  
)
  /* Store entries in each new routing object */
  Store 
  
    
      
        
          N
          
            1
          
        
      
    
    {\displaystyle N_{1}}
  
's entries in N and 
  
    
      
        
          N
          
            2
          
        
      
    
    {\displaystyle N_{2}}
  
's entries in N'
  if N is the current root then
  {
      /* Create a new node and set it as new root and store the new routing objects */
      Create a new root node 
  
    
      
        
          N
          
            p
          
        
      
    
    {\displaystyle N_{p}}
  

      Store 
  
    
      
        
          O
          
            p
            1
          
        
      
    
    {\displaystyle O_{p1}}
  
 and 
  
    
      
        
          O
          
            p
            2
          
        
      
    
    {\displaystyle O_{p2}}
  
 in 
  
    
      
        
          N
          
            p
          
        
      
    
    {\displaystyle N_{p}}
  

  }
  else
  {
      /* Now use the parent routing object to store one of the new objects */
      Replace entry 
  
    
      
        
          O
          
            p
          
        
      
    
    {\displaystyle O_{p}}
  
 with entry 
  
    
      
        
          O
          
            p
            1
          
        
      
    
    {\displaystyle O_{p1}}
  
 in 
  
    
      
        
          N
          
            p
          
        
      
    
    {\displaystyle N_{p}}
  

      if 
  
    
      
        
          N
          
            p
          
        
      
    
    {\displaystyle N_{p}}
  
 is no full then
      {
          /* The second routing object is stored in the parent only if it has free capacity */
          Store 
  
    
      
        
          O
          
            p
            2
          
        
      
    
    {\displaystyle O_{p2}}
  
 in 
  
    
      
        
          N
          
            p
          
        
      
    
    {\displaystyle N_{p}}
  

      }
      else
      {
           /*If there is no free capacity then split the level up*/
           split(
  
    
      
        
          N
          
            p
          
        
        ,
        
          O
          
            p
            2
          
        
      
    
    {\displaystyle N_{p},O_{p2}}
  
)
      }
  }
```

- "←" denotes assignment. For instance, "*largest* ← *item*" means that the value of *largest* changes to the value of *item*.
- "**return**" terminates the algorithm and outputs the following value.

## M-tree queries

### Range query

A range query is where a minimum similarity/maximum distance value is specified. For a given query object ⁠ $Q\in D$ ⁠ and a maximum search distance ⁠ $r(Q)$ ⁠, the range query **range**(Q, r(Q)) selects all the indexed objects ⁠ $O_{j}$ ⁠ such that ⁠ $d(O_{j},Q)\leq r(Q)$ ⁠.

Algorithm RangeSearch starts from the root node and recursively traverses all the paths which cannot be excluded from leading to qualifying objects.

```
Algorithm RangeSearch
Input: Node N of M-Tree MT,  Q: query object, 
  
    
      
        r
        (
        Q
        )
      
    
    {\displaystyle r(Q)}
  
: search radius
```

```
Output: all the DB objects such that 
  
    
      
        d
        (
        O
        j
        ,
        Q
        )
        ≤
        r
        (
        Q
        )
      
    
    {\displaystyle d(Oj,Q)\leq r(Q)}
  
```

```
{ 
  let 
  
    
      
        
          O
          
            p
          
        
      
    
    {\displaystyle O_{p}}
  
 be the parent object of node N;

  if N is not a leaf then { 
    for each entry(
  
    
      
        
          O
          
            r
          
        
      
    
    {\displaystyle O_{r}}
  
) in N do {
          if 
  
    
      
        
          |
        
        d
        (
        
          O
          
            p
          
        
        ,
        Q
        )
        −
        d
        (
        
          O
          
            r
          
        
        ,
        
          O
          
            p
          
        
        )
        
          |
        
        ≤
        r
        (
        Q
        )
        +
        r
        (
        
          O
          
            r
          
        
        )
      
    
    {\displaystyle |d(O_{p},Q)-d(O_{r},O_{p})|\leq r(Q)+r(O_{r})}
  
 then { 
            Compute 
  
    
      
        d
        (
        
          O
          
            r
          
        
        ,
        Q
        )
      
    
    {\displaystyle d(O_{r},Q)}
  
;
            if 
  
    
      
        d
        (
        
          O
          
            r
          
        
        ,
        Q
        )
        ≤
        r
        (
        Q
        )
        +
        r
        (
        
          O
          
            r
          
        
        )
      
    
    {\displaystyle d(O_{r},Q)\leq r(Q)+r(O_{r})}
  
 then
              RangeSearch(*ptr(
  
    
      
        T
        (
        
          O
          
            r
          
        
      
    
    {\displaystyle T(O_{r}}
  
)),Q,
  
    
      
        r
        (
        Q
        )
      
    
    {\displaystyle r(Q)}
  
); 
          }
    }
  }
  else { 
    for each entry(
  
    
      
        
          O
          
            j
          
        
      
    
    {\displaystyle O_{j}}
  
) in N do {
          if 
  
    
      
        
          |
        
        d
        (
        
          O
          
            p
          
        
        ,
        Q
        )
        −
        d
        (
        
          O
          
            j
          
        
        ,
        
          O
          
            p
          
        
        )
        
          |
        
        ≤
        r
        (
        Q
        )
      
    
    {\displaystyle |d(O_{p},Q)-d(O_{j},O_{p})|\leq r(Q)}
  
 then { 
            Compute 
  
    
      
        d
        (
        
          O
          
            j
          
        
        ,
        Q
        )
      
    
    {\displaystyle d(O_{j},Q)}
  
;
            if 
  
    
      
        d
        (
        
          O
          
            j
          
        
        ,
        Q
        )
      
    
    {\displaystyle d(O_{j},Q)}
  
 ≤ 
  
    
      
        r
        (
        Q
        )
      
    
    {\displaystyle r(Q)}
  
 then
              add 
  
    
      
        o
        i
        d
        (
        
          O
          
            j
          
        
        )
      
    
    {\displaystyle oid(O_{j})}
  
 to the result;
          }
    }
  }
}
```

- "←" denotes assignment. For instance, "*largest* ← *item*" means that the value of *largest* changes to the value of *item*.
- "**return**" terminates the algorithm and outputs the following value.

- $oid(O_{j})$ is the identifier of the object which resides on a separate data file.
- $T(O_{r})$ is a sub-tree – the covering tree of $O_{r}$

### *k*-NN queries

*k*-nearest neighbor (*k*-NN) query takes the cardinality of the input set as an input parameter. For a given query object Q ∈ D and an integer *k* ≥ 1, the *k*-NN query NN(Q, k) selects the *k* indexed objects which have the shortest distance from Q, according to the distance function d.
