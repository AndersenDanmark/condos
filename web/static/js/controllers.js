angular.module('starter.controllers', [])

.controller('AppCtrl', function($scope, $rootScope, $ionicModal, $timeout, $ionicSideMenuDelegate, DATA) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  $scope.$on('$ionicView.enter', function(e) {
    console.log('AppCtrl: $ionicView.enter')
  });


  

})



.controller('analysisCtrl', function($scope, $stateParams, $ionicModal, $ionicPopup, $timeout, $http, $state, $location, $ionicSideMenuDelegate, DATA) {

    
  
  $scope.toggleLeftSideMenu = function() {
      
    $ionicSideMenuDelegate.toggleLeft();
  };
   
   
  $scope.propertyName = 'Sample Property'    
  $scope.params = {}
  $scope.analysis_params = {}
  
  $scope.params['monthlyRates'] = [
        {'month':'Jan', 'nightly':220, 'occupancy':90},
        {'month':'Feb', 'nightly':250, 'occupancy':90},
        {'month':'Mar', 'nightly':185, 'occupancy':90},
        {'month':'Apr', 'nightly':185, 'occupancy':80},
        {'month':'May', 'nightly':170, 'occupancy':80},
        {'month':'Jun', 'nightly':170, 'occupancy':70},
        {'month':'Jul', 'nightly':170, 'occupancy':70},
        {'month':'Aug', 'nightly':170, 'occupancy':70},
        {'month':'Sep', 'nightly':170, 'occupancy':80},
        {'month':'Oct', 'nightly':170, 'occupancy':80},
        {'month':'Nov', 'nightly':185, 'occupancy':90},
        {'month':'Dec', 'nightly':200, 'occupancy':90}
    ] 
  $scope.analysis_params = {
        years:20, 
        rate:4, 
        price:400000, 
        downpayment:100000,
        propertyTax:0.00456,
        condoFees:784,
        appreciationRate:0.04,
        monthlyRates: JSON.stringify($scope.params['monthlyRates'])
        //monthlyRates: $scope.params['monthlyRates']
    }

  $scope.data = []
  $scope.analysis_results = '';
  $scope.chartsArray = [1,2]
        
    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
    
  $scope.$on('$ionicView.enter', function(e) {
      
    var paramValue = $location.search().property; 
    if (paramValue == undefined) {
        $scope.propertyName = 'Sample Property'  
        $scope.calc()
    }
    else {
        //alert('Load params for ' + paramValue.toString())
        $scope.propertyName = capitalizeFirstLetter(paramValue.toString().toLowerCase())
        $scope.loadParams(paramValue.toString(), $scope.calc)
    }
    
  });
  
  
  
  $scope.change = function(d) {
      // d = d.toString() + '%'
       //$scope.params['monthlyRates'][0].occupancy = d.toString() + '%'
       //alert($scope.params['monthlyRates'][0].occupancy)
  }
  
  
  
  $scope.keyEnter = function() {
      $scope.calc()
  }
  
  
  
  $scope.loadParams = function(property, callback) {
      
    if (property.toUpperCase() == 'MAUI') {
        //$scope.params = {}
        $scope.params['monthlyRates'] = [
            {'month':'Jan', 'nightly':620, 'occupancy':90},
            {'month':'Feb', 'nightly':450, 'occupancy':90},
            {'month':'Mar', 'nightly':485, 'occupancy':90},
            {'month':'Apr', 'nightly':385, 'occupancy':80},
            {'month':'May', 'nightly':270, 'occupancy':80},
            {'month':'Jun', 'nightly':270, 'occupancy':70},
            {'month':'Jul', 'nightly':270, 'occupancy':70},
            {'month':'Aug', 'nightly':270, 'occupancy':70},
            {'month':'Sep', 'nightly':370, 'occupancy':80},
            {'month':'Oct', 'nightly':370, 'occupancy':80},
            {'month':'Nov', 'nightly':485, 'occupancy':90},
            {'month':'Dec', 'nightly':500, 'occupancy':90}
        ] 
        $scope.analysis_params = {
            years:20, 
            rate:4, 
            price:600000, 
            downpayment:180000,
            propertyTax:0.00456,
            condoFees:784,
            appreciationRate:0.04,
            monthlyRates: JSON.stringify($scope.params['monthlyRates'])
        }
    }
    else {
        $scope.propertyName = 'Sample Property'  
        alert(property + ' wasnt found')
    }
    callback()
      
  }
  
  
  $scope.calc = function() {
     
    //var url = "https://maui-api-riskmanagerjeff.c9users.io/API/v1/calc"
    var url = "API/v1/calc"
    var params = null 
            
    // this loop changes the 'textbox' parameters into floats for the API, since the type=number format css is ugly
    for (i=0; i<$scope.params['monthlyRates'].length; i++) {
        $scope.params['monthlyRates'][i].nightly = Number($scope.params['monthlyRates'][i].nightly)
        $scope.params['monthlyRates'][i].occupancy = Number($scope.params['monthlyRates'][i].occupancy)
    }       
              
    $scope.analysis_params.monthlyRates = JSON.stringify($scope.params['monthlyRates'])
    params = $scope.analysis_params
    
    // check that the 3 parameters are numbers and not null
    if (!(isNaN(params.years) || isNaN(params.rate) || isNaN(params.price) || isNaN(params.downpayment)) 
        && (params.years!=null && params.rate!=null && params.price!=null && params.downpayment!=null)) {
       
       
        $http.get(url, {'params':params})
            .success(function(data) {
              
              $scope.analysis_results = (data.monthly_payment.toFixed(2))
              $scope.nYears_with_rental = data.nMonths_with_rental
              $scope.nYears_without_rental = data.nMonths_without_rental
              $scope.npv_cashflow = data.npv_cashflow.toFixed(2)
              $scope.futureValue = data.futureValue.toFixed(2)
              $scope.presentValue = data.presentValue.toFixed(2)
              $scope.IRR = (100*data.IRR).toFixed(2)
              $scope.avgRentalIncome = data.avgRentalIncome.toFixed(2)
              $scope.totalMonthly_payment = data.totalMonthly_payment.toFixed(2)
              
              $scope.nYears_saved = ((data.nMonths_without_rental - data.nMonths_with_rental)/12).toFixed(2)
              
              $scope.data = data.schedules
              $scope.data[0].type = 'line'
              $scope.data[0].yAxis = 1
              $scope.data[1].type = 'line'
              $scope.data[1].yAxis = 2
             
              $scope.data_bar = {}
              $scope.data_bar = [$scope.data[0]]
              $scope.data_bar[0].values[0].cashflow = 0
              
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
                "type":"line",
                "yAxis":2,
                "key" : "Mortgage with rental" ,
                "values" : [ ]
            },
            {
                "type":"line",
                "yAxis":1,
                "key" : "Mortgage " ,
                "values" : [  ]
            }
            ]
  
  $scope.options = {
            chart: {
                type: 'lineChart',  //lineChart
                lines: { // for line chart
                    forceY: [0]
                    //yDomain: [0,1],
                    //yRange: [0,10]
                },
                height: 320,
                margin : {
                    top: 20,
                    right: 40,
                    bottom: 40,
                    left: 70
                },
                x: function(d){return d3.time.format("%Y-%m-%d").parse(d.date);}, //var format = d3.time.format("%Y-%m-%d");
                //x: function(d){return d[0];}, //var format = d3.time.format("%Y-%m-%d");
                y: function(d){return d.remaining;},
                useVoronoi: false,
                //clipEdge: true,
                duration: 500,
                useInteractiveGuideline: false,
                xScale : d3.time.scale(),
                xAxis: {
                    ticks: d3.time.year,
                    tickFormat: function(d) {
                        return d3.time.format('%Y')(new Date(d));
                    }
                },
                yAxis: {
                    tickFormat: function(d){
                        return d3.format(',.0f')(d);
                    }
                }
            }
        };
        


  $scope.options2 = {
            chart: {
                type: 'multiChart',  //lineChart
                /*lines: { // for line chart
                    forceY: [0]
                    //yDomain: [0,1],
                    //yRange: [0,10]
                },*/
                color: ['#2ca02c', 'darkred'],
                height: 400,
                margin : {
                    top: 20,
                    right: 40,
                    bottom: 40,
                    left: 70
                },
                x: function(d){return d3.time.format("%Y-%m-%d").parse(d.date);}, //var format = d3.time.format("%Y-%m-%d");
                //x: function(d){return d[0];}, //var format = d3.time.format("%Y-%m-%d");
                y: function(d){return d.remaining;},
                //useVoronoi: false,
                //clipEdge: true,
                duration: 500,
                useInteractiveGuideline: false,
                xAxis: {
                    showMaxMin: true,
                    ticks: d3.time.months,
                    tickFormat: function(d) {
                        return d3.time.format('%y')(new Date(d));
                    }
                },
                yAxis1: {
                    tickFormat: function(d){
                        return d3.format(',.1f')(d);
                    }
                },
                yAxis2: {
                    tickFormat: function(d){
                        return d3.format(',.1f')(d);
                    }
                },
                /*yAxis: {
                    tickFormat: function(d){
                        return d3.format(',.0f')(d);
                    }
                },*/
                zoom: {
                    enabled: false,
                    scaleExtent: [0, 10],
                    useFixedDomain: false,
                    useNiceScale: false,
                    horizontalOff: false,
                    verticalOff: true,
                    unzoomEventType: 'dblclick.zoom'
                }
            }
        };  
   

$scope.options_bar = {
            chart: {
                type: 'historicalBarChart',
                height: 200,
                margin : {
                    top: 20,
                    right: 40,
                    bottom: 40,
                    left: 60
                },
                //x: function(d){return d[0];},
                x: function(d){return d3.time.format("%Y-%m-%d").parse(d.date);}, //var format = d3.time.format("%Y-%m-%d");
                //y: function(d){return d[1]/100000;},
                y: function(d){return d.cashflow},
                showValues: false,
                valueFormat: function(d){
                    return d3.format(',.1f')(d);
                },
                //yDomain: [0,1],
                duration: 500,
                useInteractiveGuideline: false,
                xScale : d3.time.scale(),
                xAxis: {
                    //axisLabel: 'X Axis',
                    //showMaxMin: true,
                    /*tickFormat: function(d) {
                        return d3.time.format('%b %Y')(new Date(d))  //%b-%y   %x
                    }*/
                    //showMaxMin: true,
                    ticks: d3.time.year,
                    tickFormat: function(d) {
                        return d3.time.format('%Y')(new Date(d));
                    }
                    //rotateLabels: 90,
                    //showMaxMin: true
                },
                yAxis: {
                    axisLabel: 'Cashflow',
                    axisLabelDistance: -10,
                    tickFormat: function(d){
                        return d3.format(',.0f')(d);
                    },
                    showMaxMin: true
                },
                tooltip: {
                    enabled: false,
                    keyFormatter: function(d) {
                        return d3.time.format('%x')(new Date(d));
                    }
                },
                zoom: {
                    enabled: false,
                    scaleExtent: [1, 10],
                    useFixedDomain: false,
                    useNiceScale: false,
                    horizontalOff: false,
                    verticalOff: true,
                    unzoomEventType: 'dblclick.zoom'
                }
            }
        };

        $scope.data_bar = [$scope.data[1]]
        
        
        
    $scope.buttons = [
        {text: 'Airbnb'},
        {text: 'Home Away'},
        {text: 'Long Term'}
    ];
      
    $scope.activeButton = 0;
    
    $scope.setActiveButton = function(index) {
        $scope.activeButton = index;
    };  
  
})

