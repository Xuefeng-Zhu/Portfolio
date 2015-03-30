/**
 * Created by Xuefeng Zhu on 3/29/15.
 */

var url = location.origin;

function CommentController($scope, $http) {
    var project = location.pathname.slice(1);
    $http.get([url, "comment", project].join("/"))
        .success(function (response) {
            $scope.comments = response.data;
        })

    $scope.new_comment = {};

    $scope.replyTo = function (comment) {
        if ($scope.reply_comment == comment) {
            $scope.reply_comment = null;
        }
        else {
            $scope.reply_comment = comment;
        }
        $scope.new_reply = {};
    }

    $scope.reply = function (parent_comment) {
        $scope.new_reply.parent = parent_comment.id;
        $http.post([url, "comment", project].join("/"), angular.copy($scope.new_reply))
            .success(function (response) {
                if (parent_comment.children == undefined) {
                    parent_comment.children = [];
                    $scope.$apply();
                }
                parent_comment.children.push(response);
                console.log(parent_comment)
                $scope.new_reply = {};
                $scope.reply_comment = null;
            });
    }

    $scope.makeComment = function () {
        $http.post([url, "comment", project].join("/"), angular.copy($scope.new_comment))
            .success(function (response) {
                $scope.comments.push(response);
            });
        $scope.new_comment = {};
    }

}
