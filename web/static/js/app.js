// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.controllers' is found in controllers.js
myapp = angular.module('starter', ['ionic', 'ngCordova', 'starter.controllers', 'nvd3'])

.factory('DATA', function() {
  
  return {}
})



.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);

    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }

  });
})

.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider

  .state('app', {
    url: '/app',
    abstract: true,
    templateUrl: 'templates/sidemenu-left.html',
    controller: 'AppCtrl'
  })


  .state('app.analysis', {
    url: '/analysis',
    //params: {obj:null},
    views: {
      'menuContent': {
        templateUrl: 'templates/analysis.html',
        controller: 'analysisCtrl'
      }
    }
  })

  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/app/analysis');
})

 //angular.module('app.directives')
.directive('ngEnter', function () { //a directive to 'enter key press' in elements with the "ng-enter" attribute

    return function (scope, element, attrs) {

        element.bind("keydown keypress", function (event) {
            if (event.which === 13) {
                scope.$apply(function () {
                    scope.$eval(attrs.ngEnter);
                });
                event.preventDefault();
            }
        });
    };
})
.directive('animateOnChange', function($timeout) {
    return function(scope, element, attr) {
        scope.$watch(attr.animateOnChange, function(nv,ov) {
          
            if (ov=="") {
                
            }
            else if (parseFloat(nv) < parseFloat(ov)) {
                element.addClass('changed_red');
                $timeout(function() {
                    element.removeClass('changed_red');
                }, 500);
            }
            else if (parseFloat(nv) > parseFloat(ov)) {
                element.addClass('changed_green');
                $timeout(function() {
                    element.removeClass('changed_green');
                }, 500);
            }
            
        });
    };  
});