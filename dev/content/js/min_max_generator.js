//Min Max network Generator implemented in Javascript

var max_n
var max_edges
var relationships
var edges_placed

var d3_data = {
            nodes:[],
            edges:[]
            };

function min_max_generator(max_n, max_edges){
    /**
     * Creates network for min and max relationship
     */
  
    var target
    var base_adder = 1
    var loop_adder = 0
    var n = 0
    edges_placed = 0 
    
    while (edges_placed < max_edges) {
      while ((base_adder + loop_adder) < max_n) {
        while(n < max_n){
          if (edges_placed <= max_edges){
            target = n + (base_adder + loop_adder)
            add_edge(n, target)
            n++
          }

          else {
            break
          };
        };
        loop_adder += 2
        n = 0 
      };
      loop_adder = 0
     base_adder ++
    };
 
  console.log("All edges placed")
  console.log("Last Edges Placed " + n.toString() +":" + target.toString()) 
  
  return
}; 


function make_relations_dict(max_n){
  /** 
   * Makes object which contains relations between nodes and edges
   */
  relationships = {}
  
  for (var i = 0; i < max_n; i++){
    relationships[i] = new Set()
    d3_data["nodes"].push({'name':"Node" + i.toString(),'number':i})
  };
  return relationships;
};


function add_edge(source, int_target){
  var target = int_target % max_n
  if (relationships[source].has(target)){
    return;
  }

  else {
    relationships[source].add(target)
    relationships[target].add(source)
    d3_data["edges"].push({"source":source,"target":target})
    edges_placed++ 
  };
};

//Run function
max_n = 7
max_edges = 20
make_relations_dict(max_n);
min_max_generator(max_n, max_edges)
