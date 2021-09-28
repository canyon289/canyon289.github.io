Title: D3 4.0 Zoom demystified
Date: 2016-9-25
Category: Visualization
Tags: Visualization
Slug: D3ZoomDemystified 
Authors: Ravin Kumar
Javascripts: https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js, D3Zoom.js
Stylesheets: svgcenter.css
Status: published

In the [last post]({filename}ImplementingD3Zoom.md) we covered how to implement
basic zoom and pan in a D3 svg with one line but also left ourselves with an example
of an unexpected behavior.

In this post will dig deeper to see what's happening under the hood and how we 
can get around our issue. Before we get into D3 let's start with the basics.

## What is Zoom and Pan in an SVG?
SVG stands for Scalable Vector Graphics. Vectors are mathematical
of a magnitude and direction in a coordinate space. So when we're zooming, panning,
or rotating and skewing, an SVG we are **applying coordinate transformations
to the vector space** that our computer eventually turns into graphics.

In SVGs these coordinate transforms are defined by attributes such as matrix,
translate,scale,rotate etc. So for example if we wanted to "pan" a rectangle
SVG element we would add an attribute tag as so

```
<rect width="100" height="100" transform ="translate(50,50) scale(2)"></rect>
```

The render inteprets this as move "50px right and 50px down from the origin and
double all the linear dimensions". For further details on the SVG spec take a look
at the [Mozillla Foundation Documentation](https://developer.mozilla.org/en/docs/Web/SVG/Attribute/transform)
or visit this blog post by [Sara Soueidan](https://sarasoueidan.com/blog/svg-transformations/)

## What are DOM Events and Event handlers?
We won't get too far into this one but take a moment to think about the mechanics
of event handlers. If you're reading this blog you're likely aware that nothing
is "magic" in programming, but instead a well-structured set of rules has been implemented.

In the case of zoom when the user clicks and drags an element, or a user scrolls
their mousewheel, in d3 we see that the SVG correspondingly reacts.

Mozilla Foundation once again comes through and [lists nearly all](https://developer.mozilla.org/en-US/docs/Web/Events)
the event handlers available. For those paying close attention you'll notice zoom
isn't listed, we'll cover that in a second.

## How does D3 Implement Zoom 
With an understanding how SVGs work with zoom and with how browsers handle events
we can now focus on D3 itself.
D3 implements zoom in two major piece, mostly encapsulated in two objects.
There's the **d3.zoom** object, which creates a zoom behavior and applies
the zoom event handler to selections. This is where d3 also implements
its [custom event handler](https://github.com/d3/d3-zoom#api-reference) "zoom"

There's also the **d3.ZoomTransform** element which stores the zoom transform
for a certain element. It is important to note at time of writing d3 does not support
rotate or any of the other SVG transforms in the Zoom API.

## The One Liner explanation
With all this newfound knowledge let's dissect the one liner from the previous post,
here again for reference

```javascript
svg.call(d3.zoom().on("zoom", function() {g.attr("transform", d3.event.transform)}))
```
Working our way from the outside in

```javascript
svg.call
```
If you recall the svg variable here is a refernce to our svg. The call is a d3
method for applying a function to a selection

```javascript
svg.call(d3.zoom().on("zoom"
```
In the next statement we are doing a couple of things. We're creating a zoom object,
[which is also a function](https://github.com/d3/d3-zoom#zoom) and applying it
to svg through the call method. We also are binding the zoom behavior to the 
d3 zoom event handler

```javascript
svg.call(d3.zoom().on("zoom", function() {g.attr("transform", d3.event.transform)}))
```
In this last set of code we are telling d3 change the attribute "transform" on the svg
group g, whenever the zoom event is invoked. d3.event.transform returns
an svg string that details the current transform.

## Why the initial visualization jumps
To answer our question from last week here's why the visualization jumps.

When we initially create the svg group, we manually code the transformed
position as an attribute on the svg group, copied here for reference

```javascript
.attr("transform", "translate(" + margin.left + "," + margin.top + ")")
```
when we do this d3 has no "knowledge" of the state of the SVG, but the svg
"knows" and subsequently so does the browser rendering engine.

After this when we initially try to drag or pan the element if you pay close
attention to the svg group attribute, you'll notice that the *translate* 
attribute jumps to somewhere near (0,0). Since d3 is now adjusting
the transform attribute and since it still thinks everything is referenced
from an identity position, that's where the zoom starts.

If the wording is confusing take a look at the adjusted code.
Starting with line 11 and 14, notice that we're creating an initial zoom object
and a zoomTransform object that we're offsetting.

In line 29 were setting this zoomTransform object on svg. This is the key
line, the one that "tells" d3 the initial state of the transform.  
  
We then go on to use this object to write the svg attribute string for us on line
34 and finally we set the event handler on the svg selection on line 42 and 43.
```javascript
var zoom
var svg
var initial_transform
var g

var margin = {top: 50, right: 0, bottom: 0, left: 50};
var width = 50 + margin.left + margin.right;
var height = 50 + margin.top + margin.right;

//Create Initial Zoom Behavior
zoom = d3.zoom()

//Set Initial Transform
initial_transform = d3.zoomIdentity.translate(margin.top,margin.left)

svg = d3.select("#margin_zoom").append("svg")
   .attr("width", width)
   .attr("height", height);

//Bounding Box
svg.append("rect")
   .attr("width", width)
   .attr("height", height)
   .attr("stroke", "black")
   .attr("stroke-width", "2px")
   .attr("fill", "none");
   
//Replace initial SVG zoomTransform object with our previously transformed one
svg.call(zoom.transform, initial_transform)


g = svg.append("g")
  //Rather than manually write transform string let d3 do the work for us
  .attr("transform", initial_transform.toString())

g.append("circle")
   .attr("cx", 0)
   .attr("cy", 0)
   .attr("r", 10);

//Set the zoom Behavior, use the one initialized above instead of creating a new one
svg
.call(zoom.on("zoom", function() {g.attr("transform", d3.event.transform)}))
```

## What we covered
In the previous post we covered how to implement zoom and pan easily in one
line of code. In this post we covered how d3 controls zoom behavior with the 
d3.zoom() object/function and how d3 "remembers" zoom states by setting 
d3.zoomTransform objects on elements where transforms have been applied.  

