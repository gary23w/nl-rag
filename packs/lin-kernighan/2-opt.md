---
title: "2-opt"
source: https://en.wikipedia.org/wiki/2-opt
domain: lin-kernighan
license: CC-BY-SA-4.0
tags: lin kernighan heuristic, local search tsp, k opt move, tour improvement
fetched: 2026-07-02
---

# 2-opt

In optimization, **2-opt** is a simple local search algorithm for solving the traveling salesman problem. The 2-opt algorithm was first proposed by Croes in 1958, although the basic move had already been suggested by Flood. The main idea behind it is to take a route that crosses over itself and reorder it so that it does not. A complete 2-opt local search will compare every possible valid combination of the swapping mechanism. This technique can be applied to the traveling salesman problem as well as many related problems. These include the vehicle routing problem (VRP) as well as the capacitated VRP, which require minor modification of the algorithm.

## Pseudocode

Visually, one swap looks like:

```
 - A   B -             - A - B -
     ×         ==>
 - C   D -             - C - D -
```

In pseudocode, the mechanism by which the 2-opt swap manipulates a given route is as follows. Here v1 and v2 are the first vertices of the edges that are to be swapped when traversing through the route:

```
procedure 2optSwap(route, v1, v2) {
    1. take route[start] to route[v1] and add them in order to new_route
    2. take route[v1+1] to route[v2] and add them in reverse order to new_route
    3. take route[v2+1] to route[start] and add them in order to new_route
    return new_route;
}
```

Here is an example of the above with arbitrary input:

- Example route: A → B → E → D → C → F → G → H → A
- Example parameters: v1=1, v2=4 (assuming starting index is 0)
- Contents of new_route by step:
  1. **(A → B)**
  2. A → B → **(C → D → E)**
  3. A → B → C → D → E → **(F → G → H → A)**

This is the complete 2-opt swap making use of the above mechanism:

```
repeat until no improvement is made {
    best_distance = calculateTotalDistance(existing_route)
    start_again:
    for (i = 0; i <= number of nodes eligible to be swapped - 1; i++) {
        for (j = i + 1; j <= number of nodes eligible to be swapped; j++) {
            new_route = 2optSwap(existing_route, i, j)
            new_distance = calculateTotalDistance(new_route)
            if (new_distance < best_distance) {
                existing_route = new_route
                best_distance = new_distance
                goto start_again
            }
        }
    }
}
```

The particular nodes or depots that are at the start and at the end of the path should be removed from the search as an eligible candidates for swapping, as reversing the order would cause an invalid path.

For example, with depot at A:

```
   A → B → C → D → A
```

Swapping using node[0] and node[2] would yield

```
   C → B → A → D → A
```

which is not valid (does not leave from A, the depot).

## Efficient implementation

Building the new route and calculating the distance of the new route can be a very expensive operation, usually $O(n)$ where n is the number of vertices in the route. In a symmetric case (where the distance between A and B is the same as between B and A), this can be skipped by performing a $O(1)$ operation. Since a 2-opt operation involves removing 2 edges and adding 2 different edges we can subtract and add the distances of only those edges.

```
lengthDelta = - dist(route[v1], route[v1+1]) - dist(route[v2], route[v2+1]) + dist(route[v1+1], route[v2+1]) + dist(route[v1], route[v2])
```

If `lengthDelta` is negative that would mean that the new distance after the swap would be smaller. Once it is known that `lengthDelta` is negative, then we perform a 2-opt swap. This saves us a lot of computation.

### C++ code

```mw
#include <random>
#include <stdio.h>
#include <vector>

using namespace std;

class Point {
public:
  float x, y;

  Point(float x, float y) {
    this->x = x;
    this->y = y;
  }
  Point() {
    this->x = 0.0;
    this->y = 0.0;
  }

  // Distance between two points
  inline float dist(const Point &other) const {
    float diffx = x - other.x;
    float diffy = y - other.y;
    return sqrt(diffx * diffx + diffy * diffy);
  }
};

// Calculate the distance of the whole circuit
float pathLength(vector<Point> &path) {
  int n = path.size();
  float length = path[n - 1].dist(path[0]);
  for (int i = 0; i < n - 1; i++) {
    length += path[i].dist(path[i + 1]);
  }
  return length;
}

// Replace edges path[i]->path[i+1] and path[j]->path[j+1]
// with path[i]->path[j] and path[i+1]->path[j+1]
void swap_edges(vector<Point> &path, int i, int j) {
  i += 1;
  while (i < j) {
    Point temp = path[i];
    path[i] = path[j];
    path[j] = temp;
    i++;
    j--;
  }
}

// Print the path.
void printPath(string pathName, vector<Point> &path) {
  printf("%s = [", pathName.c_str());
  for (int i = 0; i < path.size(); i++) {
    if (i % 10 == 0) {
      printf("\n  ");
    }
    if (i < path.size() - 1) {
      printf("[%.1f, %.1f], ", path[i].x, path[i].y);
    } else {
      printf("[%.1f, %.1f]", path[i].x, path[i].y);
    }
  }
  printf("\n];\n");
}

// Create a path of length n with random points between 0 and 1000
vector<Point> createRandomPath(int n) {
  vector<Point> path;
  for (int i = 0; i < n; i++) {
    float x = (float)rand() / (float)(RAND_MAX / 1000);
    float y = (float)rand() / (float)(RAND_MAX / 1000);
    path.push_back(Point(x, y));
  }
  return path;
}

int main() {
  vector<Point> path = createRandomPath(100);
  printPath("path1", path);
  float curLength = pathLength(path);
  printf("path1len = %.1f;\n\n", curLength);

  int n = path.size();
  bool foundImprovement = true;
  while (foundImprovement) {
    foundImprovement = false;
    for (int i = 0; i < n - 1; i++) {
      for (int j = i + 2; j < n; j++) {
        float lengthDelta =
            -path[i].dist(path[i + 1]) - path[j].dist(path[(j + 1) % n]) +
            path[i].dist(path[j]) + path[i + 1].dist(path[(j + 1) % n]);

        // If the length of the path is reduced, do a 2-opt swap
        if (lengthDelta < 0) {
          swap_edges(path, i, j);
          curLength += lengthDelta;
          foundImprovement = true;
        }
      }
    }
  }

  printPath("path2", path);
  printf("path2len = %.1f;\n", curLength);

  return 0;
}
```

### Output

```mw
path1 = [
  [0.0, 131.5], [755.6, 458.7], [532.8, 219.0], [47.0, 678.9], [679.3, 934.7], [383.5, 519.4], [831.0, 34.6], [53.5, 529.7], [671.1, 7.7], [383.4, 66.8], 
  [417.5, 686.8], [589.0, 930.4], [846.2, 526.9], [92.0, 653.9], [416.0, 701.2], [910.3, 762.2], [262.5, 47.5], [736.1, 328.2], [632.6, 756.4], [991.0, 365.3], 
  [247.0, 982.6], [722.7, 753.4], [651.5, 72.7], [631.6, 884.7], [272.7, 436.4], [766.5, 477.7], [237.8, 274.9], [359.3, 166.5], [486.5, 897.7], [909.2, 60.6], 
  [904.7, 504.5], [516.3, 319.0], [986.6, 494.0], [266.1, 90.7], [947.8, 73.7], [500.7, 384.1], [277.1, 913.8], [529.7, 464.4], [941.0, 50.1], [761.5, 770.2], 
  [827.8, 125.4], [15.9, 688.5], [868.2, 629.5], [736.2, 725.4], [999.5, 888.6], [233.2, 306.3], [351.0, 513.3], [591.1, 846.0], [412.1, 841.5], [269.3, 415.4], 
  [537.3, 467.9], [287.2, 178.3], [153.7, 571.7], [802.4, 33.1], [534.4, 498.5], [955.4, 748.3], [554.6, 890.7], [624.8, 842.0], [159.8, 212.8], [714.7, 130.4], 
  [91.0, 274.6], [3.0, 414.3], [26.9, 709.8], [937.9, 239.9], [180.9, 317.5], [887.0, 652.1], [150.3, 681.3], [385.8, 387.7], [499.7, 147.5], [587.2, 845.6], 
  [590.1, 955.4], [556.1, 148.2], [983.3, 408.8], [141.8, 564.9], [252.1, 488.5], [464.0, 961.1], [126.0, 199.8], [319.2, 629.3], [126.7, 651.3], [621.6, 803.1], 
  [247.8, 476.4], [389.3, 203.3], [28.4, 901.7], [426.5, 142.0], [947.5, 410.3], [131.2, 885.6], [92.2, 162.2], [71.1, 365.3], [253.1, 135.1], [783.2, 455.3], 
  [349.5, 452.3], [808.9, 931.7], [651.6, 215.2], [679.6, 908.9], [250.1, 860.9], [471.3, 506.0], [600.4, 817.6], [755.8, 462.2], [951.4, 632.7], [439.3, 824.7]
];
path1len = 55723.0;

path2 = [
  [0.0, 131.5], [91.0, 274.6], [71.1, 365.3], [3.0, 414.3], [53.5, 529.7], [92.0, 653.9], [47.0, 678.9], [15.9, 688.5], [26.9, 709.8], [28.4, 901.7], 
  [131.2, 885.6], [247.0, 982.6], [277.1, 913.8], [464.0, 961.1], [486.5, 897.7], [439.3, 824.7], [412.1, 841.5], [250.1, 860.9], [150.3, 681.3], [126.7, 651.3], 
  [141.8, 564.9], [153.7, 571.7], [247.8, 476.4], [252.1, 488.5], [319.2, 629.3], [416.0, 701.2], [417.5, 686.8], [534.4, 498.5], [537.3, 467.9], [529.7, 464.4], 
  [516.3, 319.0], [500.7, 384.1], [471.3, 506.0], [383.5, 519.4], [351.0, 513.3], [349.5, 452.3], [385.8, 387.7], [272.7, 436.4], [269.3, 415.4], [180.9, 317.5], 
  [233.2, 306.3], [237.8, 274.9], [287.2, 178.3], [389.3, 203.3], [532.8, 219.0], [736.1, 328.2], [783.2, 455.3], [755.6, 458.7], [755.8, 462.2], [766.5, 477.7], 
  [846.2, 526.9], [904.7, 504.5], [868.2, 629.5], [736.2, 725.4], [761.5, 770.2], [722.7, 753.4], [632.6, 756.4], [621.6, 803.1], [600.4, 817.6], [624.8, 842.0], 
  [631.6, 884.7], [591.1, 846.0], [587.2, 845.6], [554.6, 890.7], [589.0, 930.4], [590.1, 955.4], [679.3, 934.7], [679.6, 908.9], [808.9, 931.7], [999.5, 888.6], 
  [955.4, 748.3], [910.3, 762.2], [887.0, 652.1], [951.4, 632.7], [986.6, 494.0], [947.5, 410.3], [983.3, 408.8], [991.0, 365.3], [937.9, 239.9], [827.8, 125.4], 
  [947.8, 73.7], [941.0, 50.1], [909.2, 60.6], [831.0, 34.6], [802.4, 33.1], [671.1, 7.7], [651.5, 72.7], [714.7, 130.4], [651.6, 215.2], [556.1, 148.2], 
  [499.7, 147.5], [426.5, 142.0], [359.3, 166.5], [383.4, 66.8], [262.5, 47.5], [266.1, 90.7], [253.1, 135.1], [159.8, 212.8], [126.0, 199.8], [92.2, 162.2]
];
path2len = 8586.2;
```

### Visualization
