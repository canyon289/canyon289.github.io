Title: Q: Finding a match
Date: 2016-4-25 10:20
Category:
Tags: 
Slug: pickingadjectives
Authors: Ravin Kumar
Status: published


Two people join a dating site independently. Upon signing up they pick 5 words to
describe themselves out of 25 given words. If 4 out of 5 of the words are the
same the dating site declares they're a match. What's the probability
those couples match?


##Question Format
Online text input box

##Time Constraint
1 of 20 problems on a one hour test

##Context
This question was a 1st round automated interview test.

##Standard Assumptions
Given problems like this it's safe to assume the picks are independent
both between the people, and even between the words themselves. In real life
if the adjectives "vegetarian" and "steak eater" were in the same list
it's unlikely the same person would pick both and the choices. Would not 
entirely be independent. Likewise if the two people were already dating it
that also would not be independent. But this is a probability 
multiple choice test so assume independence.

Another trick which greatly simplifies the problem
is to assume one person already picked 5 words so find 
the probability the other person picks 4 out of the 5 words.
Mathematically it's the same but conceptually it helps
me work with the problem more easily.


##Solution 1
If you're unlucky there's a chance you'll blank on the elegant
way to solve this.  
However if you're partially lucky you'll be sitting in 
front of a computer with no one around.

As it turns out I was partially lucky.

```python
#Python Monte Carlo Simulation
import numpy as np
import pandas as pd

s = pd.Series(list(range(24)))
number_of_trials, matches = (0,0)

while number_of_trials < 1000000:
    c1 = s[np.random.choice(24,5, replace = False)]
    c2 = s[np.random.choice(24,5, replace = False)]
    if c2.isin(c1).sum() >= 4:
        matches +=1
        
    number_of_trials +=1
    print(matches/number_of_trials)
```
The above code is as crude as it gets. Python
randomly picks 5 integers out of 24 with no replacement twice.
It turns compares it's picks. If 4 match the numerator
increments by one. For each pair of random picks the 
denominator increments by one. 

If we do this a million times we get a number really close
to the closed form solution. It actually turns out that
this simulation gets close to the real answer really quickly
in close to 1000 iterations which is less than 2 seconds 
on my laptop.

This type of solution is called the Monte Carlo method.
It's actually very useful for a wide range of problems
that are too complicated for closed form solutions.
But for this problem there are better solutions.

##Solution 2
But before we get to the better solution let's say you're
really unlucky.  You both forgot the elegant method
and don't have a computer. This problem can be brute forced.  

To restate the problem this individual needs to pick 
4 specific words out of 25 with no replacement with 5 picks.
Let's call this individual Sam.  

Limiting this to two picks on the first pick there's a 
5 out of 24 chance that Sam will pick a "match" word
and a 19 out of 24 that the person will pick a "non match" word.

However on the second pick the probability is dependent on
the first pick. If the first pick was a "match" word
there is now a 4 out of 23 chance that Sam will pick
a "match" word. Likewise there is a 19/23 chance Sam
will pick a non match word.

Since each pick is independent we can multiply the probabilities
to get the chance of a sequence of picks. We also can add
each way the picks could play out to get the total chance
at least 4 match. To save yourself a lot of multiplication
and division here's the math in Python.

```python
print(
#All five match
(5/24)*(4/23)*(3/22)*(2/21)*(1/20) + 

#First four are match words, last one isn't
(5/24)*(4/23)*(3/22)*(2/21)*(19/20) +

#First 3 are match words, 4th doesn't, last does
(5/24)*(4/23)*(3/22)*(19/21)*(2/20)  +

#First 2 are match words, 3rd doesn't, last 2 do
(5/24)*(4/23)*(19/22)*(3/21)*(2/20)  +

#First matches words, 2nd doesn't, last 3 do
(5/24)*(19/23)*(4/22)*(3/21)*(2/20)  +

#First doesn't match, last 4 do
(19/24)*(5/23)*(4/22)*(3/21)*(2/20)
)
```
If you multiplied and divided by hand it would be a pain
but you would get the exact answer.

If you typed the above by hand into Python
it would also be a pain and you'd get almost
the right answer.
(You don't because of floating point error)

##Solution 3
If you were really on your game though you'd realize
that this is a combinatorics problem. Essentially we need to pick
X winning combinations out of Y possible combinations.

In combination notation it looks like this.
$${{5 \choose 4}{19 \choose 1} + {5 \choose 5}{19 \choose 0}}
  \over {25 \choose 5}$$  

In python we can use the Combinations function to get the answer

```python
from itertools import combinations

def cl(n,k):
    '''
    k combination of out length n set
    '''
    return len(list(combinations(range(n),k)))
    
numerator =  cl(5,4) * cl(19,1) + cl(5,5)*cl(19,0)
denominator = cl(24, 5)
numerator/denominator
```

There are some additional tricks that would allow you to simplify the calculation
even further but I leave it up to you to explore combinatorics further
