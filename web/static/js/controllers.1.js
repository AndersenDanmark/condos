angular.module('starter.controllers', [])

.controller('AppCtrl', function($scope, $rootScope, $ionicModal, $timeout, DATA) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  $scope.$on('$ionicView.enter', function(e) {
    console.log('AppCtrl: $ionicView.enter')
  });

  
  

})

.controller('analysisCtrl', function($scope, $ionicModal, $ionicPopup, $timeout, $http, $state, DATA) {

  $scope.$on('$ionicView.enter', function(e) {
    
    
    ff();
    
    
  });

  $scope.analysis_params = {years:10, rate:4, principle:300000} // default values
  $scope.analysis_results = '';
  
  $scope.calc = function() {
     
    var url = "https://maui-api-riskmanagerjeff.c9users.io/API/v1/calc"
    var params = null  //{ params: { "email": DATA.loginData.email, "password": DATA.loginData.password, "name": name, "message": $scope.popup.toggle.newMessage } }
    
    //alert(JSON.stringify($scope.analysis_params))
    params = $scope.analysis_params
    
    // check that the 3 parameters are numbers and not null
    if (!(isNaN(params.years) || isNaN(params.rate)|| isNaN(params.principle)) 
        && (params.years!=null && params.rate!=null && params.principle!=null)) {
       
       
        $http.get(url, {'params':params})
            .success(function(data) {
              $scope.analysis_results = JSON.stringify(data)
              
             
              $scope.data = [
                {
                  id:'New York',
                  values:[
                    {'date':'20090901', 'temperature':53.4}, 
                    {'date':'20111002', 'temperature':78.0},
                    {'date':'20121103', 'temperature':43.3},
                    {'date':'20121204', 'temperature':55.7}
                    ]
                },
                {
                  id:'New York2',
                  values:[
                    {'date':'20090901', 'temperature':363.4}, 
                    {'date':'20111002', 'temperature':158.0},
                    {'date':'20121103', 'temperature':53.3},
                    {'date':'20121204', 'temperature':155.7}
                    ]
                }
                
              ]
              
              //data = $scope.data
              

              //ff.updateData($scope.data);
              var svg = d3.select("body").transition();
              var margin = {top: 50, right: 50, bottom: 50, left: 50},
                  width = svg.attr("width") - margin.left - margin.right,
                  height = svg.attr("height") - margin.top - margin.bottom
              
              var parseTime = d3.timeParse("%Y%m%d");
              var line = d3.line()
                .curve(d3.curveBasis)
                .x(function(d) { return x(parseTime(d.date)); })
                .y(function(d) { return y(d.temperature); });
                
                
              var x = d3.scaleTime().range([0, width]),
                  y = d3.scaleLinear().range([height, 0])
      
          // Make the changes
              svg.select(".line")   // change the line
                  .duration(750)
                  .attr("d", function(d) { return line(d.values); });
              svg.select(".axis .axis--x") // change the x axis
                  .duration(750)
                  .call(x);
              svg.select(".axis .axis--y") // change the y axis
                  .duration(750)
                  .call(y);
    

              
            })
              .error(function(data) {
            });
        
    }
    else {
        alert('error in input(s)')
    }
  }  
  
  
  
  
  
$scope.data = [
    {
      id:'New York',
      values:[
        {'date':'20090901', 'temperature':63.4}, 
        {'date':'20111002', 'temperature':78.0},
        {'date':'20121103', 'temperature':53.3},
        {'date':'20121204', 'temperature':55.7}
        ]
    },
    {
      id:'New York2',
      values:[
        {'date':'20090901', 'temperature':163.4}, 
        {'date':'20111002', 'temperature':158.0},
        {'date':'20121103', 'temperature':153.3},
        {'date':'20121204', 'temperature':155.7}
        ]
    }
    
  ]
  

var ff = function() {

var svg = d3.select("svg")
var cc = d3.select(".chart-container")

   

var margin = {top: 50, right: 50, bottom: 50, left: 50},
    width = svg.attr("width") - margin.left - margin.right,
    height = svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//alert(d3.select("#chart-container").attr("width"))
svg.attr("width", '100%')
    .attr("height", '100%')
    .attr('viewBox','0 0 '+(Math.min(960,600)+400)+' '+(Math.min(960,600)+0))
    .append("g")
    .attr("transform", "translate(" + Math.min(width,height) / 2 + "," + Math.min(width,height) / 2 + ")");
    
/*
svg.attr("width", '100%')
    .attr("height", '70%')
    .attr('viewBox','0 0 '+Math.min(width,height)+' '+Math.min(width,height))
    .attr('preserveAspectRatio','xMinYMin')
    .append("g")
    .attr("transform", "translate(" + Math.min(width,height) / 2 + "," + Math.min(width,height) / 2 + ")");
*/



var parseTime = d3.timeParse("%Y%m%d");

var x = d3.scaleTime().range([0, width]),
    y = d3.scaleLinear().range([height, 0]),
    z = d3.scaleOrdinal(d3.schemeCategory10);

var line = d3.line()
    .curve(d3.curveBasis)
    .x(function(d) { return x(parseTime(d.date)); })
    .y(function(d) { return y(d.temperature); });

//d3.json("data.tsv", type, function(error, data) {
//  if (error) throw error;

  /*var cities = data.columns.slice(1).map(function(id) {
    return {
      id: id,
      values: data.map(function(d) {
        return {date: d.date, temperature: d[id]};
      })
    };
  });*/
  var data = $scope.data
  var cities = $scope.data

  x.domain(d3.extent($scope.data[0].values, function(d) { return parseTime(d.date); }));

  y.domain([
    d3.min($scope.data, 
      function(c) { 
        return d3.min(c.values, 
          function(d) { 
            return d.temperature; 
          }); 
      }),
    d3.max($scope.data, function(c) { return d3.max(c.values, function(d) { return d.temperature; }); })
  ]);

  z.domain($scope.data.map(function(c) { return c.id; }));

  g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      //.style("font", "18px sans-serif")
      .style("font-size","10px") //To change the font size of texts
      .call(d3.axisBottom(x));

  g.append("g")
      .attr("class", "axis axis--y")
      .style("font", "18px sans-serif")
      .call(d3.axisLeft(y))
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      //.style("font", "18px sans-serif")
      .attr("fill", "#000")
      .text("Temperature, ºF");

  var city = g.selectAll(".city")
    .data($scope.data)
    .enter().append("g")
      .attr("class", "city");

  city.append("path")
      .attr("class", "line")
      .attr("d", function(d) { return line(d.values); })
      .style("stroke", function(d) { return z(d.id); });

  city.append("text")
      .datum(function(d) { return {id: d.id, value: d.values[d.values.length - 1]}; })
      .attr("transform", function(d) { return "translate(" + x(parseTime(d.value.date)) + "," + y(d.value.temperature) + ")"; })
      .attr("x", 3)
      .attr("dy", "0.35em")
      .style("font", "18px sans-serif")
      .text(function(d) { return d.id; });
//});
}


     
      
          // Select the section we want to apply our changes to
         
          
   


/*function type(d, _, columns) {
  d.date = parseTime(d.date);
  for (var i = 1, n = columns.length, c; i < n; ++i) d[c = columns[i]] = +d[c];
  return d;
}*/



  
})

