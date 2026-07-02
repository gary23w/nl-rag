---
title: "Vehicle routing problem"
source: https://en.wikipedia.org/wiki/Vehicle_routing_problem
domain: logistics-optimization
license: CC-BY-SA-4.0
tags: logistics optimization, vehicle routing problem, operations research, supply chain optimization
fetched: 2026-07-02
---

# Vehicle routing problem

The **vehicle routing problem** (**VRP**) is a combinatorial optimization and integer programming problem which asks "What is the optimal set of routes for a fleet of vehicles to traverse in order to deliver to a given set of customers?" The problem first appeared, as *the truck dispatching problem*, in a paper by George Dantzig and John Ramser in 1959, in which it was applied to petrol deliveries. Often, the context is that of delivering goods located at a central depot to customers who have placed orders for such goods. However, variants of the problem consider, e.g, collection of solid waste and the transport of the elderly and the sick to and from health-care facilities. The standard objective of the VRP is to minimise the total route cost. Other objectives, such as minimising the number of vehicles used or travelled distance are also considered.

The VRP generalises the travelling salesman problem (TSP), which is equivalent to requiring a single route to visit all locations. As the TSP is NP-hard, the VRP is also NP-hard.

VRP has many direct applications in industry. Vendors of VRP routing tools often claim that they can offer cost savings of 5%–30%. Commercial solvers tend to use heuristics due to the size and frequency of real world VRPs they need to solve.

## Setting up the problem

The VRP concerns the service of a delivery company. How things are delivered from one or more *depots* which has a given set of home *vehicles* and operated by a set of *drivers* who can move on a given *road network* to a set of *customers*. It asks for a determination of a set of *routes*, *S*, (one route for each vehicle that must start and finish at its own depot) such that all customers' requirements and operational constraints are satisfied and the *global transportation cost* is minimized. This cost may be monetary, distance or otherwise.

The road network can be described using a graph where the arcs are roads and vertices are junctions between them. The arcs may be directed or undirected due to the possible presence of one way streets or different costs in each direction. Each arc has an associated cost which is generally its length or travel time which may be dependent on vehicle type.

To know the global cost of each route, the travel cost and the travel time between each customer and the depot must be known. To do this our original graph is transformed into one where the vertices are the customers and depot, and the arcs are the roads between them. The cost on each arc is the lowest cost between the two points on the original road network. This is easy to do as shortest path problems are relatively easy to solve. This transforms the sparse original graph into a complete graph. For each pair of vertices *i* and *j*, there exists an arc *(i,j)* of the complete graph whose cost is written as $C_{ij}$ and is defined to be the cost of shortest path from *i* to *j*. The travel time $t_{ij}$ is the sum of the travel times of the arcs on the shortest path from *i* to *j* on the original road graph.

Sometimes it is impossible to satisfy all of a customer's demands and in such cases solvers may reduce some customers' demands or leave some customers unserved. To deal with these situations a priority variable for each customer can be introduced or associated penalties for the partial or lack of service for each customer given

The objective function of a VRP can be very different depending on the particular application of the result but a few of the more common objectives are:

- Minimize the global transportation cost based on the global distance travelled as well as the fixed costs associated with the used vehicles and drivers
- Minimize the number of vehicles needed to serve all customers
- Least variation in travel time and vehicle load
- Minimize penalties for low quality service
- Maximize a collected profit/score.

## VRP variants

Several variations and specializations of the vehicle routing problem exist:

- Vehicle Routing Problem with Profits (VRPP): A maximization problem with profits attributed to each customer and costs (usually in terms of time) attributed to each arc (travel from customer to customer), and constraints on these profits and costs. The common subproblems of VRPP are:
  - Orienteering Problem (OP), where a price constraint (or time constraint) is given and the goal is to maximize the sum of collected profits while respecting the cost limit. Vehicles are required to start and end at the depot. Among the most known and studied OP are:
    - The Team Orienteering Problem (TOP) which is the most studied variant of the VRPP,
    - The Capacitated Team Orienteering Problem (CTOP),
    - The TOP with Time Windows (TOPTW).
  - Collecting Traveling Salesman Problem (PCTSP), in which The goal is to minimize the total cost, subject to the requirement that the collected profit exceeds a given value.
  - Profitable Tour Problem (PTP), in which the goal is to maximize the difference between profit and cost.
- Vehicle Routing Problem with Backhauling (VRPB): Disjoint sets of delivery and pickup customers are given. Goods have to be delivered from the depot to the delivery customer and from the pickup customers to the depot. Vehicles may be forbidden from picking up goods from customers until all carried goods have been delivered to delivery customers or allowed interchanging pickups with deliveries at a potential cost.
- Vehicle Routing Problem with Pickup and Delivery (VRPPD): A number of goods need to be moved from certain pickup locations to other delivery locations. The goal is to find optimal routes for a fleet of vehicles to visit the pickup and drop-off locations.
- Vehicle Routing Problem with LIFO: Similar to the VRPPD, except an additional restriction is placed on the loading of the vehicles: at any delivery location, the item being delivered must be the item most recently picked up. This scheme reduces the loading and unloading times at delivery locations because there is no need to temporarily unload items other than the ones that should be dropped off.
- Vehicle Routing Problem with Time Windows (VRPTW): The delivery locations have time windows within which the deliveries (or visits) must be made.
- Capacitated Vehicle Routing Problem: CVRP or CVRPTW. The vehicles have a limited carrying capacity of the goods that must be delivered.
- Vehicle Routing Problem with Multiple Trips (VRPMT): The vehicles can do more than one route.
- Open Vehicle Routing Problem (OVRP): Vehicles are not required to return to the depot.
- Inventory Routing Problem (IRP): Vehicles are responsible for satisfying the demands in each delivery point
- Multi-Depot Vehicle Routing Problem (MDVRP): Multiple depots exist from which vehicles can start and end.
- Vehicle Routing Problem with Transfers (VRPWT): Goods can be transferred between vehicles at specially designated transfer hubs.
- Electric Vehicle Routing Problem (EVRP): A variant in which electric vehicles are used, requiring additional considerations such as limited battery range and charging decisions.

Several software vendors have built software products to solve various VRP problems. Numerous articles are available for more detail on their research and results.

Although VRP is related to the Job Shop Scheduling Problem, the two problems are typically solved using different techniques.

## Exact solution methods

There are three main approaches to modelling the VRP using mixed-integer linear programming (MILP):

1. **Vehicle flow formulations**—this uses integer variables associated with each arc that count the number of times that the edge is traversed by a vehicle. It is generally used for basic VRPs. This is good for cases where the solution cost can be expressed as the sum of any costs associated with the arcs. However it can't be used to handle many practical applications.
2. **Commodity flow formulations**—additional integer variables are associated with the arcs or edges which represent the flow of commodities along the paths travelled by the vehicles. This has only recently been used to find an exact solution.
3. **Set-partitioning**—This approach models the VRP as a set cover problem, in which the locations make up the universe and the set of all feasible routes (cycles) make up the collection of sets to choose from. The problem can then be modelled using a linear programming model for the weighted set cover problem, with the weight of a route set to its cost. Modelling the VRP in this way will possibly result in an exponential number of binary variables in the linear program, as one is associated with each of a potentially exponential number of feasible routes.

### Vehicle flow formulations

The formulation of the TSP by Dantzig, Fulkerson and Johnson was extended to create the two index vehicle flow formulations for the VRP

${\text{min}}\sum _{i\in V}\sum _{j\in V}c_{ij}x_{ij}$

subject to

| $\sum _{i\in V}x_{ij}=1\quad \forall j\in V\backslash \left\{0\right\}$ |   | 1 |
|---|---|---|

| $\sum _{j\in V}x_{ij}=1\quad \forall i\in V\backslash \left\{0\right\}$ |   | 2 |
|---|---|---|

| $\sum _{i\in {V\backslash \left\{0\right\}}}x_{i0}=K$ |   | 3 |
|---|---|---|

| $\sum _{j\in {V\backslash \left\{0\right\}}}x_{0j}=K$ |   | 4 |
|---|---|---|

| $\sum _{i\notin S}\sum _{j\in S}x_{ij}\geq r(S),~~\forall S\subseteq V\setminus \{0\},S\neq \emptyset$ |   | 5 |
|---|---|---|

| $x_{ij}\in \{0,1\}\quad \forall i,j\in V$ |   | 6 |
|---|---|---|

In this formulation $c_{ij}$ represents the cost of going from node i to node j , $x_{ij}$ is a binary variable that has value 1 if the arc going from i to j is considered as part of the solution and 0 otherwise, K is the number of available vehicles and $r(S)$ corresponds to the minimum number of vehicles needed to serve set S . We are also assuming that 0 is the depot node.

Constraints **1** and **2** state that exactly one arc enters and exactly one leaves each vertex associated with a customer, respectively. Constraints **3** and **4** say that the number of vehicles leaving the depot is the same as the number entering. Constraints **5** are the capacity cut constraints, which impose that the routes must be connected and that the demand on each route must not exceed the vehicle capacity. Finally, constraints **6** are the integrality constraints.

One arbitrary constraint among the $2|V|$ constraints is actually implied by the remaining $2|V|-1$ ones so it can be removed. Each cut defined by a customer set S is crossed by a number of arcs not smaller than ⁠ $r(S)$ ⁠(minimum number of vehicles needed to serve set S ).

An alternative formulation may be obtained by transforming the capacity cut constraints into generalised subtour elimination constraints (GSECs).

$\sum _{i\in S}\sum _{j\in S}x_{ij}\leq |S|-r(S)$

which imposes that at least ⁠ $r(S)$ ⁠arcs leave each customer set S .

GCECs and CCCs have an exponential number of constraints so it is practically impossible to solve the linear relaxation. A possible way to solve this is to consider a limited subset of these constraints and add the rest if needed. Identification of the needed constraints is done via a separation procedure. Efficient exact separation methods for such constraints (based on mixed integer programming) have been developed.

A different method again is to use a family of constraints which have a polynomial cardinality which are known as the MTZ constraints, they were first proposed for the TSP and subsequently extended by Christofides, Mingozzi and Toth.

$u_{j}-u_{i}\geq d_{j}-C(1-x_{ij})~~~~~~\forall i,j\in V\backslash \{0\},i\neq j~~~~{\text{s.t. }}d_{i}+d_{j}\leq C$

$0\leq u_{i}\leq C-d_{i}~~~~~~\forall i\in V\backslash \{0\}$

where $u_{i},~i\in V\backslash \{0\}$ is an additional continuous variable which represents the load left in the vehicle **after** visiting customer i and $d_{i}$ is the demand of customer i . These impose both the connectivity and the capacity requirements. When $x_{ij}=0$ constraint then i is not binding' since $u_{i}\leq C$ and $u_{j}\geq d_{j}$ whereas $x_{ij}=1$ they impose that $u_{j}\geq u_{i}+d_{j}$ .

These have been used extensively to model the basic VRP (CVRP) and the VRPB. However, their power is limited to these simple problems. They can only be used when the cost of the solution can be expressed as the sum of the costs of the arc costs. We cannot also know which vehicle traverses each arc. Hence we cannot use this for more complex models where the cost and or feasibility is dependent on the order of the customers or the vehicles used.

### Manual versus automatic optimum routing

There are many methods to solve vehicle routing problems manually. For example, optimum routing is a big efficiency issue for forklifts in large warehouses. Some of the manual methods to decide upon the most efficient route are: Largest gap, S-shape, Aisle-by-aisle, Combined and Combined +. While Combined + method is the most complex, thus the hardest to be used by lift truck operators, it is the most efficient routing method. Still the percentage difference between the manual optimum routing method and the real optimum route was on average 13%.

## Approximate solutions

Many real-world applications use computational methods that produce approximate solutions, due to the computational complexity of the VRP. These methods are typically heuristic-based and belong to one of two classes:

- **Classical heuristics**–perform a set of relatively simple operations to quickly construct a relatively good solution.
- **Metaheuristics**–classify and explore the most promising parts of the solution space.

### Metaheuristic

Due to the difficulty of solving to optimality large-scale instances of vehicle routing problems, a significant research effort has been dedicated to metaheuristics such as Genetic algorithms, Tabu search, Simulated annealing and Adaptive Large Neighborhood Search (ALNS). Some of the most recent and efficient metaheuristics for vehicle routing problems reach solutions within 0.5% or 1% of the optimum for problem instances counting hundreds or thousands of delivery points. These methods are also more robust in the sense that they can be more easily adapted to deal with a variety of side constraints. As such, the application of metaheuristic techniques is often preferred for large-scale applications with complicating constraints and decision sets.

Many methods are based on optimization. These methods are typically composed of a rapid construction phase of an initial route, for example by means of a greedy algorithm, followed by an iterative improvement phase, in which small modifications that improve the route’s score are sought. Mechanisms are employed to avoid local optima, for example by allowing moves that do not improve the route’s score in the short term.

### Non-metaheuristic methods

Additional methods for solving the VRP have been proposed, some of which depend on the specific problem conditions.

In the case of a VRP with time-dependent profit, various algorithms have been proposed to account for the time dimension. In one such approach, local optimization is applied, whereby the profit of each step incorporates the change in the potential profit of vertices that have not yet been visited.

Another algorithm, which does not rely on optimization, begins with a discretization of time. The two-dimensional graph of vertices of the form $(x,y)$ is replaced by a three-dimensional graph of vertices of the form $(x,y,t)$ , where t represents a point in time. Each vertex in the new graph is assigned a corresponding profit, and directed edges between vertices represent the possibility of traveling from one location at a given time to another location at a different time. Dynamic programming is then applied in order to identify a high-scoring path in the resulting directed acyclic graph.
