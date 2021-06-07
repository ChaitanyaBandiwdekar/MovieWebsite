var app = angular.module('myApp', []);
app.controller('celebCtrl', function($scope) {
    $scope.list=["My Favourite Celebs"];
    $scope.addNewCeleb=function(){
        $scope.errortext = "";
        if (!$scope.addNew) {return;}
        if ($scope.list.indexOf($scope.addNew) == -1) {
			$scope.list.push($scope.addNew);
        } else {
			$scope.errortext ="This Celebrity is already in the list.";
        }
    }
});