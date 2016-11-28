/*Example code for Double Data join*/
var data = {"Jack":["Tall", "Athletic"],
            "Jill":["Smart"]}

// How did I get it to append into the div not h3
var doubledatajoin = function() {
         d3.select("#example")
           .selectAll("div")
           .data(Object.keys(data))
           .enter()
             .append("div")
             .append("h3")
             .text(function(d) {return d})
           .selectAll("p")
           .data(function(d) {return data[d]})
           .enter() 
             .append("p")
             .text(function(d) {return d})

        } 

