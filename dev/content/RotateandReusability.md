Title: SVG Rotation and Reusability
Date: 2016-10-15 10:20
Category: SVG 
Tags: Software, Visualization
Slug: RotationAndReusability 
Authors: Ravin Kumar
Javascripts: https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js 
Status: published

SVGs aren't always the most straightforward to work it and also are deceptively
simple but as you'll get more familiar with the API you'll be able to
combine SVG "methods" to more easily get what you need.  
In this post we'll cover rotation and reuseability of SVG elements as well
as the practical problem this solved for me

# The Backstory
At SpaceX I'm currently writing a program that will calculate a timeline
of activities and am using D3 for the visualization portion. For this particular
business process there were activities, thing that happen over a period of time,
and milestones, significant dates that occured after the completion of
a series of activities

# Gantt Charts
Schedules are nothing new, over a 100 years ago 
[the Gantt Chart](https://en.wikipedia.org/wiki/Gantt_chart) was developed
to visualize and communicate project timelines
![test]( https://upload.wikimedia.org/wikipedia/commons/0/0b/ConceptDraw_Project_Gantt_Chart.png)

There's now numerous visual encodings but the two that are most used are
the rectangle, displaying activity duration, and diamonds, which signify milestones
or completion times of important events.
<div id="unclipped"></div>

# Creating a diamond
SVG supports a number of 
[basic shapes]( https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Basic_Shapes)
Rectangles are oneof these and creating one just requires easily understood parameters
such as x,y location of te top left corner and width and height.

```xml
<svg>
  <rect x="10" y="10" height="20" width="40"/>
  <rect x="20" y="20" height="20" width="40"></rect>
</svg>
```
They can be repsented in either of the formats above, the only difference
being the closing block for the svg element.The resulting SVG looks like this.
Seemingly unspectacular but actually pretty cool for only 4 lines of code.  
<svg>
  <rect x="10" y="10" height="20" width="40"/>
  <rect x="20" y="40" height="20" width="40"></rect>
</svg>

Our next challenge is reprsenting a diamond. There is no basic shape for a
diamond in the SVG library. Given that we can't just "tell" the renderer
to draw a diamond we could instead manually "draw" the lines like this

<svg width=100 height=100>
  <path d="M50 15 L15 50 L50 85 L85 50 Z"></path>
</svg>
But this feels like a bit much, we really just want a diamond.

#Rotation
Taking a step back though if we think about it a diamond really is just 
a rotated rectangle. Luckily there is a simple method to rotate elements in SVGs.

```xml
transform = "rotate(degrees, x,y)"
```
In the string above degrees are the degree of rotation, and x and y are
rotation center. If not specified the rotation center defaults to the origin
of the svg.

Let's go through an example. Below is a basic rectangle like we saw above.
```xml
<svg width ="100" height ="100">
  <rect x="25" y="25" height="50" width="50"/>
</svg>
```
<svg width ="100" height ="100">
  <rect x="25" y="25" height="50" width="50"></rect>
</svg>  

If we specify the rotation as so

```xml
<svg width ="100" height ="100">
  <rect x="25" y="25" height="50" width="50 "transform="rotate(45, 50,50)"></rect>
</svg>
```
we get the diamond with much less work!

<svg width ="100" height ="100">
  <rect x="25" y="25" height="50" width="50" transform="rotate(45, 50,50)"></rect>
</svg>

We had to specify the center of the relative to the SVG origin however. If we
translate the diamond slightly, without changing the rotate x and y coordinates
we end up with effects like what you see below. We still got a diamond
but it's not at the coordinates we wanted it to be.
```xml
<svg width ="400" height ="400">
  <rect x="200" y="200" height="50" width="50" fill="blue"></rect>
  <rect x="200" y="200" height="50" width="50" transform="rotate(45, 50,50)"></rect>
</svg>
```

<svg width ="400" height ="400">
  <rect x="200" y="200" height="50" width="50" fill="blue"></rect>
  <rect x="200" y="200" height="50" width="50" transform="rotate(45, 50,50)"></rect>
  <circle cx="50" cy="50" r="10" fill="red"></circle>
</svg>
The blue square and the black diamond share the same x and y attribute, but since
the center of rotation is at red dot, the diamond isn't in the position as the
black square.

# SVG Reusability
SVG has another trick up it's sleeve though. Take a guess what the following
SVG will look like.

```xml
<svg width ="100" height ="100">
  <defs>
      <rect id="myshape" x="0" y="0" height="50" width="50"/>
  </defs>
</svg>
```
<svg width ="100" height ="100">
  <defs>
      <rect id="myshape" x="0" y="0" height="50" width="50"/>
  </defs>
</svg>
If you guessed nothing you were right. However there is geometry defined
and similar to the [clip paths]({filename}ClipPaths.md) tutorial it's wrapped
in [defs](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/defs) tags.

Anything in defs tags can be reused by use of the "use" tag and referencing
the id of the element.

```xml
<svg width ="100" height ="100">
  <defs>
      <rect id="myshape" x="0" y="0" height="50" width="50"/>
  </defs>
  <use xlink:href="#myshape" x="10" y="10"/>
      <rect x="0" y="0" height="50" width="50"/>
</svg>
```
<svg width ="100" height ="100">
  <defs>
      <rect id="myshape" x="0" y="0" height="50" width="50"/>
  </defs>
  <use xlink:href="#myshape" x="10" y="10"/>
</svg>

So for our diamond we can declare once and then use it anywhere with minimal effort.
```xml
<svg width ="100" height ="100">
  <defs>
      <rect id="myshape" x="0" y="0" height="50" width="50"/>
  </defs>
  <use xlink:href="#myshape" x="10" y="10"/>
      <rect x="0" y="0" height="50" width="50"/>
</svg>
```
<svg width ="200" height ="200">
  <defs>
      <rect id="diamond" height="50" width="50" transform="rotate(45)">
  </defs>
  <use xlink:href="#diamond" x="50" y="50"/>
  <use xlink:href="#diamond" x="100" y="100"/>
</svg>

# In Closing
Declaring elements in the defs tag is how DRY, Don't Repeat Yourself, is 
implemented in SVGs. As you can see they're also extremely useful in
very practical situations. If you have any questions feel free to contact
me either through my Linkedin or Github. I hope this was helpful!
