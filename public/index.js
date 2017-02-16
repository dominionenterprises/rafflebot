// You can require() this file in a CommonJS environment.
//require('./dist/js/flat-ui.js');
var app = angular.module("raffl", []); 
app.controller("socialRaffle", function($scope,$window) {

$scope.signin = true;
$scope.rules = false;

$scope.openRules = function(){
	$scope.rules = true;
 	$scope.signin = false;
 	window.location.href = "rules.html";
};

$scope.openTwitter = function(){
	$scope.signin = false;
 //$window.open('//twitter.com');
};

$scope.openFacebook = function(){
	console.log("sjhsw");
	$scope.signin = false;
// $window.open('//facebook.com');
};
$scope.openInstagram = function(){
	$scope.signin = false;
	console.log("sjhsw");
// $window.open('//instagram.com');
};
$scope.openGoogle = function(){
	$scope.signin = false;
	console.log("sjhsw");
// $window.open('//google.com');
};

	});

    
