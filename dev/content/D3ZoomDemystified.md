Title: D3 4.0 Zoom demystified
Date: 2016-8-27
Category: 
Tags: HowTo 
Slug: D3ZoomDemystified 
Authors: Ravin Kumar
Javascripts: https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js, D3Zoom.js
Stylesheets: svgcenter.css
Status: draft

#Demystifying D3 Zoom
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

##Zoom Transform objects
Zoom Transform objects are set on every object.  
I can set them manually by calling d3.zoom().transform, initial_transform
although I need to learn this magic more

##Zoom Objects
These hold the zoom behavior. I know less about them, Keep studying these



#Demystifying D3 zoom
D3 4.0 changed zoom behavior. Zoom is now stored on element itself and not on the behavior


##Complex Zoom
Gory details of what happens when I only want to apply it to one element
Show how you do it only modifying the attribute
Also how to do it modifying each objects zoo

#Deprecated
When working with data it's going to come in a lot of sources. If you're
unlucky it will be a unstructured text or a network folder full of 
Excel files. If you're really lucky it will be in a a
[Tidy](http://vita.had.co.nz/papers/tidy-data.pdf) format. Somewhere inbetween
are databases.

#Databases structure 
Databases are great, the data is structured, types are well represented,
and the data is available for all. What's not great is the data is not
always structured in the way a data scientist would like to use it.

After deciding to use a [Statically Generated Site]({filename}WhyIChoseASSG.md)
I needed to pick a template. Trouble was that I had already found a template for
WordPress that I had liked.

![WordPressTheme]({filename}/images/PelicanTemplate/WordPressTemplate.png)
*The Wordpress theme* 

Luckily there was a [GitHubRepo](https://github.com/getpelican/pelican-themes)
that had many prexisting themes and even more luckily there was one 
that was already a [close fit](https://github.com/jvanz/pelican-hyde)
![WordPressTheme]({filename}/images/PelicanTemplate/PelicanHydeTheme.png)
*The Pelican-Hyde theme* 

There were some things I didn't like though. I didn't like the sidebar size,
the links to social media, and the font, or that the sidebar was focused
on the bottom. Additionally I wanted the horizontal line element from the 
WordPress theme. Given that this theme was so close though, rather than
start from scratch I decided to modify the existing one instead.

#Peeking under the hood
Given that this is a Statically Generated Site everything you see can be
traced back to a single file quite easily. However given this is still web
technology there is still the possibility that the formatting could be coming
from an html file and multiple css stylesheets. Bluntly put figuring out why
certain things are laid out a certain way, or why they're a certain color, can
still be a pain. Luckily though the Chrome Team developed awesome dev tools
which make figuring out what's going on much easier
![ChromeDevTools]({filename}/images/PelicanTemplate/ChromeDevTools.png)
*Chrome Dev Tools*

In the screenshot above you can see a couple of awesome things. One is that
by highlighting over an element I can both see the code in the Document
Object Model and the full tree of CSS stylers that are changing it's appearance
and position. While I won't go into all the tools here, there are numerous
other tabs and functions to dive even deeper into more complex applications.
However in generality using the dev tools is what I used in the following
steps to deconstruct the Wordpress and Pelican themes

![ChromeDevTools]({filename}/images/PelicanTemplate/CSSModifications.png)
*Adding a Dark Green Class*  
For the most part this modifying the CSS to reflect the styles we want.
For instance above an addition was made the CSS style sheets to allow for
a Dark Green class that uses the same green in the original WordPress Theme.

#Modifying the template
I also wanted links to be added for the static pages to include pages 
such as About This Blog and References. Luckily Pelican decided to use 
the jinja2 templating engine which is simple to use.

![Template Modifications]({filename}/images/PelicanTemplate/TemplateModification.png)

By adding the above loop in white, links will now be added for each sidebar link.

#Why does this matter for Data Science
As a data scientist part of the job is being able to present information
seamlessly and quickly. The Web was built for this 
Using it to be able to quickly and effectively use this medium is an extremely
useful skill to have in your communication toolset, and things like
the Chrome Devtools and jinja2 templating engine are extremely powerful
to template and style reusable webpages for reports and internal facing
dashboards.
