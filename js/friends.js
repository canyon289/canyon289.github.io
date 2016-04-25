/*Solution for Friends Algorithm written in JavaScript

Painful lessons learned
Javascript keys are always strings
 */

var relationships 
var raw_data

//Turn strings into sparse array for search
function format_input(file_data) {
  var friends_matrix = {}
  for (person in file_data) {
    var friends = file_data[person]
    var friends_list = []
    for (var friend_num = 0; friend_num < friends.length; friend_num++ ) {
      if (friends[friend_num] === 'Y' && friend_num !== +person) {
        friends_list.push(+friend_num);
      };
    };
   friends_matrix[+person] = friends_list
  }
return friends_matrix;
};

function find_circles(relationships) {
  //Function that finds total numbers of circles
  var visited
  var circles
  visited = []
  
  //Recursive function that performs depth first search of friends
  function find_friends(person){
    if (visited.indexOf(person) === -1){
        visited.push(+person)
        
        //D3 function to visualize search
        if (typeof(d3) !== null) {
              d3.select("svg")
                .select("#num_" + person)
            .transition()
              .delay(750 * visited.length)
              .style("fill", "red")
            .transition()
              .delay(750 * (visited.length + 1))
              .style("fill", "green")
            
        };      
        for (var i = 0; i < relationships[person].length; i++){
            find_friends(relationships[person][i]);
           };
        
        return;
    };
    return;
  };

  circles = 0 
  for (person in relationships){
    if (visited.indexOf(parseInt(person)) === -1) {
        find_friends(person)
        circles++
    };
  };

console.log(circles)
};


//Load data and go through functions
d3.text("data/friends/input07.txt", function(error, file_data) {
  
  //Split into array and drop first item
  raw_data = file_data.split("\n").splice(1)
  relationships = format_input(raw_data)
  draw_network()
  //find_circles(relationships) 
});

