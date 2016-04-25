Title: Q: Friend Circles
Date: 2016-4-23 10:20
Category:
Tags: 
Slug: FriendsCircles
Authors: Ravin Kumar
javascripts: https://d3js.org/d3.v3.min.js, friends.js, friends_vis.js
Status: published


There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature, i.e., if A is friend of B and B is friend of C,
then A is also friend of C. A friend circle is a group of students who are directly or
indirectly friends.
You have to complete a function int friendCircles(char[][] friends) which returns the
number of friend circles in the class. Its argument, friends, is a NxN matrix which
consists of characters 'Y' or 'N'. If friends[i][j] = 'Y', then i and j students are
friends with each other, otherwise not. You have to return the total number of
friend circles in the class.
Note: The method signature will differ by language. For example, Java will have 'int
friendCircles﴾String[] friends﴿' where "friends" is an array of strings, which can be
viewed as a 2 dimensional array of characters.

Constraints:  
-  1 <= N <= 300  
-  Each element of matrix friends will be 'Y' or 'N'  
-  Number of rows and columns will be equal in friends  
-  friends[i][i] = 'Y', where 0 <= i < N  
-  friends[i][j] = friends[j][i], where 0 <= i < j < N  

##Question Format
Online coding challenge

##Time Constraint
1 of 3 Coding problems 2 Hours given

##Context
This question was a 2nd round automated interview question
given after passing multiple choice statistics question

##Initial thoughts
When I saw this question I made a critical error
in my initial understanding of what a friends circle meant.

I was able to make the first key insight which is that
that the friends and relationships are a structure called
Network Graph. The problem is asking to find the number
of unique relationships that span friends. I first
ran into my first issue here.

Because of the title Friends Circles I became fixated
on the thought that a closed loop is what I was
looking for. Loops in graphs are called cycles
and numerous algorithms exist to find them. However
this is not what this question was asked for and I wasted
pretty much 40 minutes implementing this solution.

##Where I went wrong
### Not understanding the question
During the interview I wasn't able to understand the 
question correctly. Unfortunately since I had no human
interviewer I was unable to ask for clarification

###Too slow to iterate
It became apparent to me that my understanding was
wrong when I failed the majority of the test cases.
But I had already wasted 30 minutes to get to that point
and ran out of time

##The Solution
It was misleading that the problem was titled Friends Circles
because the problem is actually asking How many people
know are connected through their friends and their 
friends friends. In math terms it's asking how many groups
of nodes are connected by their edges.  
  
Given this understanding the problem is extremely simple.
Any graph can be composed into a tree. This is a concept
called tree composition. In this problem all we needed
to do was pick a node, run a depth first search algorithm
to find all the nodes that share a tree, then move onto the
next node and try again. The number of unique trees
is the answer to all the test cases.

##Code
The first order of business is to read in the inputs that look like this  
```
YYNN  
YYYN  
NYYN  
NNNY  
```

into a sparse matrix that looks like this

```python
network = {0:[1]
           1:[0,2],
           2: [1],
           3:[]
           }
```
I chose the sparse matrix because beside being very human readable it also
lends itself to the search process.

Given a sparse matrix we can now find circles by doing a depth first search
of that person's friends as shown below.

```python

def find_circles(friends_dict):
    '''
    Iterate through friends dict to find 
    '''

    def find_friends(person):
        '''
        Recursive function that does Depth First Search of all friends
        '''
        if person not in visited:
            visited.append(person)
            for friend in friends_dict[person]:
                find_friends(friend)
        return

    visited = []
    circle = 0
    for person in friends_dict:
        if person not in visited:
            find_friends(person)
            circle +=1
        
    return circle
```
The algorithm works initially picking a node. It then traverses the tree
to find all others nodes (friends) that are connected with the initial node.
When it exhausts all friends in the chain it tries the next node.

In particular is the the find_friends function. This is the workhouse
of this implementation. It recursively finds the friends of the current node.
The find_circles function mostly acts as an outer wrapper, storing the
friends count and the visited list.

The visited list is particularly important because it ensures two things.
One is that we don't waste computational time finding all the friends of a 
person we've already searched. Additionally it allows the find_friends
function to terminate once all the visited friends in a tree have been found.

##Visualization
Here's a visualization of the search process. You notice that once the algorithm
finds a tree it stays on it until there are no more nodes left.

To make this visualization the algorithm was also reimplemented in javascript which
you can find here. The visualization is possible due to the awesome
d3 javascript library which will get a post of it's own in the future

###Click to start search
<div id="vis"> </div>

