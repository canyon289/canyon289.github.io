(function() {
var zoom
var svg
var g
var initial_transform
var r = 10




var width = 300
var height = 300

//Create Initial Zoom Behavior
zoom = d3.zoom()

//Set Initial Transform
svg = d3.select("#staticclipped").append("svg")
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

g = svg.append("g")

g.append("circle")
   .attr("cx", width/2)
   .attr("cy", height/2 + r)
   .attr("r", 10);

                

g.append("circle")
   .attr("cx", width/2)
   .attr("cy", height/2 - r)
   .attr("r", 10)
   .attr("clip-path", "url(#cliprect)")

//Set the zoom Behavior, use the one initialized above instead of creating a new one
svg.call(zoom.on("zoom", function() {
        g.attr("transform", d3.event.transform)
      })
  )

console.log("Clipped function ran")
}())
