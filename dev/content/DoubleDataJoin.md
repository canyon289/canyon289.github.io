Title: Double Data Joins
Date: 2016-11-21 
Category: D3 
Tags: Software, Visualization
Slug: DoubleDataJoin 
Authors: Ravin Kumar
Javascripts: d3.v4.js, doubledatajoin.js
Status: published 

Perhaps the most fundamental concept of D3 is the data join **insert link here**
which shortly summarized compares a dataset in memory with the data in a selection.
New elements are **entered**  where no matched data exists in the selection, 
current elements are **updated** and missing elements are **exited**.

One aspect that's easy to miss though is that the results of a data join
are also a selection. This means you can chain data joins on top of each other. 

## An example
Say we have data that has a nested structure like this
```javascript

var data = {}
```
<div id="example"></div>

by using two data joins we can add the corresponding adjectives to into the 
dom where it makes sense. The above example is quite trivial but where this
can become extremely useful is nested groups. By being able to create
hierarchial groups like this it becomes easy to transform, hide, and modify
like groups of elements. If you want an example of this feel free to contact me
and I can add one to this post. Otherwise I hope you see the power of this
and just how powerful combining concepts in D3 can be.

