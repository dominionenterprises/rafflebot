// You can require() this file in a CommonJS environment.
//require('./dist/js/flat-ui.js');
var app = angular.module("raffl", []); 
app.controller("socialRaffle", function($scope,$window,$http) {

$scope.signin = true;
$scope.rules = false;
$scope.winners = [];

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


$http.get("/getRaffles")
    .then(function(response) {
        $scope.myWelcome = response.data;
        console.log("111",$scope.myWelcome);
    });


	});
app.controller("viewRaffleCtrl", function($scope,$window,$http) {
    $scope.getRaffles = function() {
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
        		var winObject = {};
                var winnerArray = [];
                var joinedRaffle = [];
        		//console.log(12,$scope.raffleDetails);
        		angular.forEach(value.tweets, function(tweets, key){
        			count++;
        			//console.log(123,value.tweets)
        			if(tweets.drawn == true){
        				winner = true;
                        winObject = {'username':tweets.username,'twitter_id':tweets.user_id,'profile_img':tweets.profile_img};
                        winnerArray.push(winObject);
        			}
                    joinedRaffle.push(tweets);

        		});
        		$scope.raffleDetailsObject = {'raffle_id':value.id,'hashtag':value.hashtag,'count':count,'winner':winner,'winnerDetails':winnerArray,'joinedRaffle':joinedRaffle};
        		$scope.raffleDetailsArray.push($scope.raffleDetailsObject);
        		console.log(11,$scope.raffleDetailsObject);

        	

        });
        setTimeout(function() {

        $('[data-toggle="tooltip"]').tooltip(); 
    }, 500)
    });
};
 	$scope.pickUpWinner = function(raffleId){
 		//alert("Hurray!!")
 		$http({
    method: 'POST',
    url: "/pickWinner",
    data: $.param({'raffle_id' : raffleId}),
    headers: {'Content-Type': 'application/x-www-form-urlencoded'}
})
 		//$http.post("/pickWinner", {'raffle_id' : raffleId})
     .then(function(response) {
     	
     	$scope.winnerDetails = {'raffleId':raffleId,'details':response};
        if($scope.winnerDetails)
     	$scope.winners.push($scope.winnerDetails);
     });
     $scope.getRaffles();
	};

	$scope.newRaffle = function(){
	console.log("111");
	window.location.href = "index.html";
};
$scope.getRaffles();
$scope.stopRaffle = function(raffleId){
    $scope.pickUpWinner(raffleId);

};

});
    
