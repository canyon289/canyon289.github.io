
//Visualization for basic zoom
(function basic_zoom(){
var svg = d3.select("#basic_zoom")
           .append("svg")
             .attr("width", 100)
             .attr("height", 100);

var g = svg.append("g");

g.append("circle")
   .attr("cx", 50)
   .attr("cy", 50)
   .attr("r", 10);

svg.call(d3.zoom().on("zoom", function() {g.attr("transform", d3.event.transform)}));
console.log("Function Ran")
}());

(function margin_convention(){

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
console.log("Function Ran")
}());
