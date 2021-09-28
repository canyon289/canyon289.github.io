Title: Interview Question: Minimum Strongly Connected Network
Date: 2016-5-22
Category: Interview
Tags: Intervi
Slug: MinStrongNetwork
Authors: Ravin Kumar
Javascripts: https://d3js.org/d3.v3.min.js, min_max_generator.js, min_max_vis_nonforce.js
Stylesheets: min_max_vis.css
Status: published

A group of software engineers want to develop an algorithm for finding strongly
connected groups among members of a social networking site. A group of people
are considered to be strongly connected if each person knows each other person
within the group.

Given M nodes and N edges develop an algorithm that determines
the minimum size of the largest strongly connected group.

Constraints:  
-  `1 <= N <= 100000`  
-  `2 <= M <= 10000`  
-  `1 <= M <= N*(N-1)/2`  

##Question Format
Online coding challenge

##Time Constraint
* 1 of 3 coding problems 
* 2 hours given

##Context
This question was a 2nd round automated interview question
given after passing multiple choice statistics question

##Initial thoughts

There exist algorithms that can efficiently find strongly groups in
directed graphs such as 
[Tarjan's Algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)
or
[Kosaraju's Algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm).

Similar to the other coding questions the initial prompt
initially led me astray. I spent a couple of minutes  trying to determine the
best way to find all the strongly connected groups in an existing network.

However this is not what the problem is asking. Instead of **finding**
the sizes of the strongly connected groups, it's actually asking
**how can you make the least strongly connected graph**

To illustrate this point here are some visualizations.
If we needed to construct a graph of 4 nodes and 4 edges it could look like this.
  
<div id="wronglyconnectedgraph"></div>  

However, this solution is suboptimal. We can see that there are 3 strongly
connected groups of 2 and 1 strongly connected group of three.  

Instead, if we place 4 edges like this, the largest connected
group is 2 even though the number of edges and nodes are the same.
<div id="betterconnectedgraph"></div>  


##Experimental Solution
The trick to this problem is to construct the most weakly connected
network possible. This can intuitively be done in stages. At first the edges
are placed to connect the nodes "around the edges".
Up until this point the minimum strongly connected network size is 2. In code this is done by connecting
the N index node with the N+1 index node.

After this we can continue by connecting the N index node with the N + 3
indexed node. We do this because if we connected the N node with the N+2 node
at this point we would end up with a strongly connected group of 3. Connecting
the N indexed node with the N+3 indexed node we can continue placing edges
while maintaining a strongly connected group of 2.

Eventually it becomes the case that adding more edges will create strongly
connected groups of three but the above algorithm avoids this case as
long as possible.

In words this is challenging to describe but the algorithm is quite visually
intuitive as shown below.

###Click to start visualization

<div id="vis"></div>


```python

def add_edge(self, source, target):
        if target >= self.max_n:
            target = target % (self.max_n)

        if target not in self.relationships[source]:
            self.relationships[source].add(target)
            self.relationships[target].add(source)

            self.edges_placed +=1
        return self.relationships


    def create_network(self):
        base_adder = 1
        loop_adder = 0
        n =0

        # Add all the loops
        while self.edges_placed < self.max_edges:
            # While adder is less than max n
            while (base_adder + loop_adder)  < self.max_n:
                #While the node being iterated is less than the maximum
                while n < self.max_n:

                    #Stop adding edges if all are placed
                    if self.edges_placed == self.max_edges:
                        break
                    else:
                        self.add_edge(n, n+(loop_adder+base_adder))
                        n+=1

                # Continue connecting nodes
                loop_adder += 2
                n = 0
            #Strong Connections Start
            base_adder += 1
            loop_adder = 0
```



