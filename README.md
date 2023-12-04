# Santa's Optimal Transportation Network, a not too serious approach

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
\end{equation}
Currently there are very efficient software solutions for this problem []. However, we have identified several insurmountable obstacles:
$$

 \item The TSP solution would require an impossible large sled to build (bigger than Noah's arch) in order to carry all the gifts, since in the TSP framework once the 
 delivery beggins, the sled must follow the optimal tour and it cannot return to the base. 
 \item The reindeer team has a limited horsepower and it cannot pull such a large sled.  
 \end{itemize} 
We should mention that with each delivery the cargo becomes lighter, and at the last delivery it would be very light. 
This observation may provide a theoretical incentive to adopt the TSP solution, however the question that remains unsolved so far is how to make the first delivery, since 
at the beginning the cargo is so heavy, and it cannot be moved by the reindeers? 
Therefore, we quickly abandoned this approach, as unrealistic and unfeasible. 
