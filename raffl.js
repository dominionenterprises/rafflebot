var app = angular.module("hackUApp", []); 
app.controller("socialRaffle", function($scope,$window) {
$scope.openTwitter = function(){
	console.log("sjhsw");
 $window.open('//twitter.com');
};

$scope.openFacebook = function(){
	console.log("sjhsw");
 $window.open('//facebook.com');
};
$scope.openInstagram = function(){
	console.log("sjhsw");
 $window.open('//instagram.com');
};
$scope.openGoogle = function(){
	console.log("sjhsw");
 $window.open('//google.com');
};

	});


    