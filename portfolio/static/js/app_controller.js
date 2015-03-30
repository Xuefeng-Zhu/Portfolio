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
        if ($scope.new_reply.author == undefined || $scope.new_reply.author == "" ||
            $scope.new_reply.content == undefined || $scope.new_reply.content == "") {
            alert("Author or Content cannot be empty");
            return;
        }

        $scope.new_reply.parent = parent_comment.id;
        $http.post([url, "comment", project].join("/"), angular.copy($scope.new_reply))
            .success(function (response) {
                if (parent_comment.children == undefined) {
                    parent_comment.children = [];
                }
                parent_comment.children.push(response);
                $scope.new_reply = {};
                $scope.reply_comment = null;
            });
    }

    $scope.makeComment = function () {
        if ($scope.new_comment.author == undefined || $scope.new_comment.author == "" ||
            $scope.new_comment.content == undefined || $scope.new_comment.content == "") {
            alert("Author or Content cannot be empty");
            return;
        }

        $http.post([url, "comment", project].join("/"), angular.copy($scope.new_comment))
            .success(function (response) {
                $scope.comments.push(response);
            });
        $scope.new_comment = {};
    }

}
