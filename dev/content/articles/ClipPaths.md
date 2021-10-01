Title: Clip Paths and Transforms
Date: 2016-10-09 10:20
Category: Data Science
Tags: Visualization
Slug: clippaths 
Authors: Ravin Kumar
Javascripts: https://cdnjs.cloudflare.com/ajax/libs/d3/4.2.2/d3.min.js, unclipped.js, clippath_groups.js, clippath.js
Status: published

When creating visualizations sometimes we want an element to be visible 
in one portion of the SVG but perhaps in another. An example would be a chart
with axes that also implements zoom and pan. As we move the chart elements
into the axes area we don't wany any overlap.

# An example
In the visualization below zoom and pan have been applied using the method in
the [zoom and pan post]({filename}ImplementingD3Zoom.md). We only want the blue
dot to be visible in the blue region but it's clearly visible everywhere.

<div id="unclipped"></div>

# Clip Paths
Luckily the SVGs support a concept called clip-path. The idea is simple,
essentially defining an area where elements are visible, however the implementation
is a bit more convoluted.  
  
In our example above we only wanted the blue circle to be visible in the blue 
region. As with nearly everything in SVG we'll have to define the geometry.
However unlike other svg geometry it needs to be defined in the **defs**
section of the svg.
```SVG
<svg>
  <defs>
    <clipPath id="bluerect">
      <!--Geometry goes here-->
    </clipPath>
  </defs> 
</svg>
```

[defs](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/defs)
are a tag for reuseable elements in SVGs. In this case 
[clipPath](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/clipPath)
element needs to be defined in this block.


```SVG
<svg>
  <defs>
    <clipPath id="bluerect">
      <rect x=0 y=0 height=300 width=150></rect>
    </clipPath>
  </defs> 
</svg>
```

Once defined in the defs section the clip path can be applied to an element
by adding a **clip-path** attribute on the element. The blue is removed
from the example code for code clarity. 
[ref] While sample bl.ocks are great sometimes when going through them
it's hard to isolate the specific feature I'm trying to learn
from all the other functionality[/ref]

```javascript
g.append("circle")
   .attr("cx", width/2)
   .attr("cy", height/2 - r)
   .attr("r", 10)
   .attr("clip-path", "url(#cliprect)")
```

<div id="staticclipped"></div>
The clip path clearly worked but unfortunately it stick with the element
regardless of position. What we really want is the circle to be visible
depending on where it is in the svg.

# Clip Path Groups
Before fixing the issue above it should be mentioned that clip paths 
can also be applied to groups. There are a lot of uses for it but in our 
case this is EXTREMELY handy as it allows us to do two major things

* Apply a clip group to one circle but not another
* Apply the clip group to a group that is not transformed

The simplified SVG structure looks like this.

```SVG
<svg>
<g id="alwaysvisiblecircle" class="pan_and_zoom_class">
  <circle>
</g>
<g id="url(#clippathdef)">
  <g class="pan_and_zoom_class">
    <circle>
  </g>
</g>
</svg>
```

<div id="clipped"></div>

This structure results in this visualization which does everything we want it
to! If you try dragging the circles, you'll notice that one of them starts
disapearing as it's location moves to the right, but start appearing again
if you move left

# References
The code for these visualizations are available on my Github. Additionally
there is a much more extensive writeup on clip paths written by
[Sara Soueidan](https://sarasoueidan.com/blog/css-svg-clipping/) which
I highly recommend. 



