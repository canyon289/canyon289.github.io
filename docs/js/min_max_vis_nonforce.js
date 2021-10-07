/* D3 Visualization of min max network creation
and how solution is found
*/

var height = 500
var width = 500
var radius = 20
var initial_radius = 225
var in_progress = false

//Data sources for suboptimal networks
var sub_optimal1 = {"nodes":[
                    {name:"Node0", number:0},
                    {name:"Node1", number:1},
                    {name:"Node2", number:2},
                    {name:"Node3", number:3}
                    ],
                    "edges":[
                    {source:0, target:1},
                    {source:1, target:2},
                    {source:2, target:3},
                    {source:3, target:1}
                    ]};

var sub_optimal2 = {"nodes":[
                    {name:"Node0", number:0},
                    {name:"Node1", number:1},
                    {name:"Node2", number:2},
                    {name:"Node3", number:3}
                    ],
                    "edges":[
                    {source:0, target:1},
                    {source:1, target:2},
                    {source:2, target:3},
                    {source:3, target:0}
                    ]};

//Draw both example networks immediately
draw_network("#wronglyconnectedgraph", sub_optimal1)
draw_network("#betterconnectedgraph", sub_optimal2)

//Click Header to start animation
d3.select("body").select("#click-to-start-visualization")
        .on("click", function() {
            if (in_progress){
                console.log("Visualisation already running")
                return;
            }
            else {
            //Click header to start animation
            draw_network("#vis", d3_data)
            in_progress = true
            }
        });

function draw_network(div, data){

    function xy_array_generator(){
        //Returns array of xy positions
        var x
        var y
        var int_angle = 0
        var xy_array = []
        var angle = (2*Math.PI)/data["nodes"].length

        if (data["nodes"].length % 2 === 0){
            int_angle = angle/2 + Math.PI/2
        }

        for (var i=0; i < data["nodes"].length; i++) {
            x = width/2 + Math.cos(int_angle - angle*i)*initial_radius
            y = height/2 - Math.sin(int_angle - angle*i)*initial_radius
            //debugger
            xy_array.push({"x":x, "y":y})
        }
        return xy_array;
    }

    var xy_array = xy_array_generator()
    var drawn_links = [];

    var svg = d3.select("body").select(div)
            .append("svg")
            .attr("width", width)
            .attr("height", height);

    var node = svg.selectAll(".node")
            .data(data["nodes"])
            .enter()
            .append("g")

        node.append("circle")
            .attr("class", "node")
            .attr("id", function(d, i) {return(i);})
            .attr("r", radius)
            .attr("cx", function(d,i) {return xy_array[i].x;})
            .attr("cy", function(d,i) {return xy_array[i].y;});

        node.append("text")
            .text(function(d,i) {return d["number"]})
            .attr("x", function(d,i) {return xy_array[i].x;})
            .attr("y", function(d,i) {return xy_array[i].y;})
            .attr("dy", ".3em")
            .attr("text-anchor", "middle")

    // magic is here
    run();
    function run() {
        // use the set time out to wait a second between steps
        setTimeout(function() {
            // append the next link
            var res = appendLink();
            // but only step forward if there are more links
            if (res) {
                run();
            }
        }, 1000);
    }

    function appendLink() {
        // get the next edge
        var newedge = data.edges.shift();
        drawn_links.push(newedge);
        console.log(newedge)

        // now add the links to the svg element
        link = svg.selectAll(".edge")
            .data(drawn_links);

        link.enter()
            .insert("line", ":first-child")
            .attr("class", "edge") // make sure that the class is the same as the selector
            .style("stroke-width", 2)
            .attr("x1", function(d) { return xy_array[d.source].x;})
            .attr("y1", function(d) { return xy_array[d.source].y; })
            .attr("x2", function(d) { return xy_array[d.target].x; })
            .attr("y2", function(d) { return xy_array[d.target].y; })
        link.exit().remove();

        // return true if there are more links to append
        return data.edges.length > 0;
    }
}
