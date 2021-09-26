Title: Implementing Zoom in D3 4.0 
Date: 2016-8-27
Category: 
Tags: HowTo 
Slug: ImplementingD3Zoom 
Authors: Ravin Kumar
Javascripts: https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js, D3Zoom.js
Stylesheets: svgcenter.css
Status: published

D3 is a fantastic library for sharing and engaging users in visualizations.
One of the best ways it does this is by leveraging user interactions, by means
of clicks, drags, and scrolls to highlight data. We'll be exploring how to 
implement one of these interactions, the zoom interaction in D3 4.0

##The benefits of Zoom
In data visualization zooming is a handy method to allow the user both see the
whole picture but also the minute details. This also means the user can focus 
on the details that personally matter to them. Perhaps the most prevalent 
example of this is with services like Google Maps, where users can seamlessly
transition from a map of the entire world, to a detailed map of their neighborhood.

##Zoom in D3
As with the rest of the library zoom in D3 the API is not immediately obvious,
and potentially frustrating. However as you become more familiar with it you'll
come to realize how well it implements an intuitive response and abstracts away
complicated mathematical but still leaves the ability to change the underlying behavior.

## The One Liner
If you need basic zooming and panning behavior and in D3 it's extremely simple
to implement.  

Let's start by creating an svg with a group and adding a circle to it.
```javascript
var svg = d3.select("#basic_zoom")
   .append("svg")
     .attr("width", 100)
     .attr("height", 100);

var g = svg.append("g");

g.append("circle")
     .attr("cx", 50)
     .attr("cy", 50)
     .attr("r", 10);

svg.append("circle")
     .attr("cx", 50)
     .attr("cy", 50)
     .attr("r", 10);
```

Adding zoom and pan behavior is one additional line

```javascript
svg.call(d3.zoom().on("zoom", function() {g.attr("transform", d3.event.transform)}))
```
<div id="basic_zoom"></div>

**Before you leave** note that the event listener has been applied to the svg
but the transformation is applied to the group.

## Zoom + Margin convention
For the visualization I was building at first I was thrilled having solved
my problem, but I ran into another problem.  

My visualization was using the [margin convention](https://bl.ocks.org/mbostock/3019563)
and something odd was happening. See if you can find the same issue.

Here's the code (bounding box added for reference)
```javascript
var margin = {top: 50, right: 0, bottom: 0, left: 50};
var width = 50 + margin.left + margin.right;
var height = 50 + margin.top + margin.right;

var svg = d3.select("#margin_zoom").append("svg")
   .attr("width", width)
   .attr("height", height);

//Bounding Box
svg.append("rect")
   .attr("width", width)
   .attr("height", height)
   .attr("stroke", "black")
   .attr("stroke-width", "2px")
   .attr("fill", "none");
   

var g = svg.append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")")

g.append("circle")
   .attr("cx", 0)
   .attr("cy", 0)
   .attr("r", 10);

svg.call(d3.zoom().on("zoom", function() {g.attr("transform", d3.event.transform)}))
```
and here's the resulting visualization. Try zooming and panning and see if you
can spot the issue
<div id="margin_zoom"></div>

You may have noticed that on the initial event the circle jumps to the top
left corner (0,0 svg coordinates) but behaves normally after that. In the next
post I'll be explaining why this happens

