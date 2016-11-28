/*Example code for Double Data join*/
var data = {"red":["Strawberries", "Apple"],
            "blue":["BlueBerries"]}

var doubledatajoin = function() {
         d3.select("#example")
           .selectAll("div")
           .data(Object.keys(data))
           .enter()
             .append("div")
             .style("color", function(d) {return d})
           .selectAll("p")
           .data(function(d) {return data[d]})
           .enter() 
             .append("p")
             .text(function(d) {return d})
        } 

d3.select("#button")
  .on("click", doubledatajoin)
