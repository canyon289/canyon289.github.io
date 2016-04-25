/* D3 Visualization that should be used in 
conjunction with the DFS program found in the
adjacent file
*/

var height = 600
var width = 600
var radius = 5
var d3_data

function d3_parser(raw_data){
    d3_data = {"nodes":[], "edges":[]}
    
    for (person in raw_data) {
        //Seems like I need to pass objects as nodes for d3 to work
        
        d3_data.nodes.push({"number":"num_" + person});
        var friends = raw_data[person]
        for (var i = +person+1; i < friends.length; i++){
            if (friends[i] === "Y") {
                d3_data.edges.push({"source":+person, "target":i})
            };
        };
    };
    return d3_data
};

//Click Header to start animiation
d3.select("#click-to-start-search")
        .on("click", function() {find_circles(relationships)})
        
 
function draw_network(){ 
    d3_data = d3_parser(raw_data)
    
    var svg = d3.select("#vis").append("svg")
           .attr("width", width)
           .attr("height", height);
    
   
    var force = d3.layout.force()
        .size([width,height])
        .nodes(d3_data["nodes"])
        .links(d3_data["edges"])
        .linkDistance([30])
        .charge([-30])
        .start();
    
    var link = svg.selectAll(".link")
            .data(d3_data["edges"])
            .enter()
            .append("line")
            .attr("class", "edge")
            .style("stroke-width", 2)
                
    var node = svg.selectAll(".node")
                .data(d3_data["nodes"])
                .enter()
                .append("circle")
                .attr("class", "node")
                .attr("id", function(d) {return(d["number"])})
                .attr("r", radius)
                //.call(force.drag)
    


    force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
        .attr("cy", function(d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });
      });
}
