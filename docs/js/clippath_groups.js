(function() {
var zoom
var svg
var initial_transform
var r = 10

var unfiltered_g
var clippath_g
var filtered_g


var width = 300
var height = 300

//Create Initial Zoom Behavior
zoom = d3.zoom()

//Set Initial Transform
svg = d3.select("#clipped").append("svg")
   .attr("width", width)
   .attr("height", height);

//Define clip path
svg.append("defs")
    .append("clipPath")
      .attr("id", "cliprect")
    .append("rect")
     .attr("x", 0)
     .attr("y", 0)
     .attr("height", height +2 )
     .attr("width", width/2)


//Bounding Box
svg.append("rect")
   .attr("width", width)
   .attr("height", height)
   .attr("stroke", "black")
   .attr("stroke-width", "2px")
   .attr("fill", "none")
                //.attr("clip-path", "url(#cliprect)")
                //
//Create unfiltered group
unfiltered_g = svg.append("g")
unfiltered_g.append("circle")
   .attr("cx", width/2)
   .attr("cy", height/2 + r)
   .attr("r", 10);

//Filter group
clippath_g = svg.append("g")
               .attr("clip-path", "url(#cliprect)")
                
//Filtered group
filtered_g = clippath_g.append("g")

filtered_g.append("circle")
   .attr("cx", width/2)
   .attr("cy", height/2 - r)
   .attr("r", 10)
   //.attr("clip-path", "url(#cliprect)")

//Set the zoom Behavior, use the one initialized above instead of creating a new one
svg.call(zoom.on("zoom", function() {
        unfiltered_g.attr("transform", d3.event.transform)
        filtered_g.attr("transform", d3.event.transform)
      })
  )

console.log("Clipped function ran")
}())
