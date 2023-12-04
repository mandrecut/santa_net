# Santa's Optimal Transportation Network 

## Abstract
We discuss the problem of computing Santa's optimal transportation network. 
That is, starting from the North Pole we intend to find the optimal network for transporting the Christmas gifts to each city around the World.
This is a hard NP-complete problem, and here we only provide a sub-optimal heuristic approach. A software solution is also included, and 
freely accessible as a web application at: www.santa.com 

## Introduction

Christmas is approaching quickly and Santa Claus Organization (SCO) requires a flawless solution for its world-wide transportation and delivery problem. 
That is, every Christmas the SCO must transport and deliver the gifts to the people in each city around the World, starting from its North Pole undisclosed location:) 
This is a challenging problem which requires maximum scalability from the elves team and the reindeer fleet, and so far the SCO has managed to keep the optimal transportation 
plan secret for more than 1750 years.

Here we make a first attempt to unravel the SCO secret transportation network, however this is a hard NP-complete problem, and our solution is only based on a sub-optimal 
heuristic approach. Initially we thought that the Traveling Salesman Problem (TSP) could provide an adequate framework, 
however we quickly dismissed this approach since it raises several logistic questions which we could not solve. 
Finally we settled for a Branching Optimal Transportation (BOT) solution [1]. While this solution 
is obviously sub-optimal, it has the advantage that it is relatively easy to compute and avoids the previously mentioned obstacles. We provide the details of our sub-optimal solution 
and we illustrate our findings by developing a web application freely accessible at: www.santa.com 

## The TSP approach
Let us assume that $X=\{x_n \mid n=0,1,...,N-1\}$ is the set of all cities to be visited. Any permutation $\pi$ of the set of indexes $I=\{0,1,...,N-1\}$ is a 
tour visiting all the cities. In the TSP framework the problem is to find the optimal permutation (tour) $\pi^*$ that minimizes the distance $d$ required to visit all the cities:

$$
\pi^* = \text{arg}\min_{\pi} \sum_{n=0}^{N-2} d(x_{\pi(n)},x_{\pi(n+1)}) + d(x_{\pi(N-1),\pi(0)}).
$$

Currently there are very efficient software solutions for this problem. However, we have identified several insurmountable obstacles:
 \item The TSP solution would require an impossible large sled to build (bigger than Noah's arch) in order to carry all the gifts, since in the TSP framework once the 
 delivery beggins, the sled must follow the optimal tour and it cannot return to the base. 
 \item The reindeer team has a limited horsepower and it cannot pull such a large sled.  
 \end{itemize} 
We should mention that with each delivery the cargo becomes lighter, and at the last delivery it would be very light. 
This observation may provide a theoretical incentive to adopt the TSP solution, however the question that remains unsolved so far is how to make the first delivery, since 
at the beginning the cargo is so heavy, and it cannot be moved by the reindeers? 
Therefore, we quickly abandoned this approach, as unrealistic and unfeasible. 

## The BOT approach

This approach is based on the algorithm developed in our previous work, which is a combination of greedy and tabu search [1]. 
This algorithm has the advantage that it is deterministic and finite, and with each branching node added to the network the overall cost is guaranteed to decrease,   
showing very good results in practical simulations. 

The remaining question is therefore how to select the initial set of sources (distribution centers) for each country? 
We consider a national distribution center which is at the center of (population) mass of the country. This can be easily computed since 
we have the position and the population of the cities:

$$
x^*_0 = \frac{\sum_i p_i x_i}{\sum_i p_i},
$$

here $x_i$ is the location of the city and $p_i$ is the population. 
In addition we also define several regional distribution centers $\{x^*_1,x^*_2,...,x^*_K\}$. Again, this is possible since we have 
the location and population of each city. The number of centroids is empirically set to $K=\sqrt{N}+1$, and their position is given by the centroids solution of the weighted K-means clustering:

$$
\text{arg}\min_{\{x^*_1,x^*_2,...,x^*_K\}} \sum_k \sum_i p_i\Vert x_i - x^*_k\Vert^2,
$$

where the centroids $x^*_k$ are the center of mass of the clusters $C_k$:

$$
x^*_k = \frac{\sum_i p_i x_i}{\sum_i p_i}, \quad i \in C_k.
$$

After we have computed the location of the national and regional distribution centers, we can use the BOT algorithm \cite{key-1} to compute the branching points and to find a sub-optimal distribution network. 
The results are quite good as one can see in the web application demo at: www.santa.com

While the above approach does find a plausible sub-optimal distribution network, it also creates some more or less amusing "political" problems. 
For example, the national distribution center of some countries may be located in other countries, or in non-territorial waters. 
For example the national distribution center for Canada is located close to Marquette, Wisconsin, United States. 
But this is OK, since most of the stuff Canadians buy is from Costco or Walmart anyway, so adding SCO to the suppliers list will not cause too much of a commotion. 

## Conclusion

We have described a heuristic branching method approach for the SCO distribution network. 
The method is based on a deterministic algorithm implementing a combination of (regularized) linear programming in the first stage, followed by a greedy tabu search in the second stage, exploiting 
a local branching optimization approach \cite{key-1}. 
An application illustrating the method is also provided at: www.santa.com

## References

1. M. Andrecut, \textit{Heuristic Optimal Transport in Branching Networks}, Optimization and Control https://arxiv.org/abs/2311.06650 (2023).
