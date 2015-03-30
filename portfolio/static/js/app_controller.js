/**
 * Created by Xuefeng Zhu on 3/29/15.
 */

function CommentController($scope) {
    $scope.comments = [
        {
            id: 1,
            author: "Frank",
            content: "Bla Bla",
            date: "12/12/2012",
            children: [
                {
                    id: 2,
                    author: "Mike",
                    content: "Bla Bla",
                    data: "12/12/2012"
                },
                {
                    id: 3,
                    author: "Tim",
                    content: "Bla Bla",
                    data: "12/12/2012"
                }
            ]
        }
    ]

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
        if (parent_comment.children == undefined) {
            parent_comment.children = [];
        }

        $scope.new_reply.date = new Date().toDateString();
        parent_comment.children.push(angular.copy($scope.new_reply));
        $scope.new_reply = {};
        $scope.reply_comment = null;
    }

    $scope.makeComment = function (project) {
        $scope.new_comment.date = new Date().toDateString();
        $scope.comments.push(angular.copy($scope.new_comment));
        $scope.new_comment = {};
    }
}
