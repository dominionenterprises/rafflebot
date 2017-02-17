// You can require() this file in a CommonJS environment.
//require('./dist/js/flat-ui.js');
var app = angular.module("raffl", []); 
app.controller("socialRaffle", function($scope,$window,$http) {

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

$scope.viewRaffles = function(){
	window.location.href = "admin_results_page.html";
};
$scope.newRaffle = function(){
	console.log("111");
	window.location.href = "index.html";
};

$http.get("/getRaffles")
    .then(function(response) {
        $scope.myWelcome = response.data;
        console.log("111",$scope.myWelcome);
    });


	});
app.controller("viewRaffleCtrl", function($scope,$window,$http) {

	$http.get("/getRaffles")
    .then(function(response) {
        $scope.raffleDetails = response.data;
        console.log("111",$scope.raffleDetails);
        $scope.raffleDetailsArray = [];
        var count=0;
        var winner = false;
 		var raffleCounter =0;
        angular.forEach($scope.raffleDetails, function(value, key){
        	raffleCounter++;
        	
        		//console.log(12,$scope.raffleDetails);
        		angular.forEach(value.tweets, function(tweets, key){
        			count++;
        			//console.log(123,value.tweets)
        			if(tweets.drawn == true){
        				winner = true;
        			}

        		});
        		$scope.raffleDetailsObject = {'hashtag':value.hashtag,'count':count,'winner':winner};
        		$scope.raffleDetailsArray.push($scope.raffleDetailsObject);
        		console.log(11,$scope.raffleDetailsObject);

        	

        });
    });

});
    
