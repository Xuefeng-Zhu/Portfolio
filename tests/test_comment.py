__author__ = 'Xuefeng Zhu'

import unittest
import json
from portfolio.app import app
from portfolio.models.comment import Comment


class TestComment(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.comment1 = {
            "author": "Frank",
            "content": "Hello"
        }

        self.comment2 = {
            "author": "Mike",
            "content": "Hi"
        }

        self.comment3 = {
            "author": "Tim",
            "content": "Fuck you"
        }

    def post_comment_helper(self, data):
        """
        Helper function to post comment
        :return json_data from server
        """
        json_data = json.dumps(data)
        return self.app.post('/comment/Assignment0', data=json_data, content_type='application/json')

    def test_post_comment(self):
        """
        Test if the user can post comment
        """
        rv = self.post_comment_helper(self.comment1)
        self.assertIn(self.comment1["author"], rv.data)
        self.assertIn(self.comment1["content"], rv.data)
        Comment.objects(id=json.loads(rv.data)["id"]).delete()

    def test_reply_comment(self):
        """
        Test if the user can post reply comment
        """
        rv1 = self.post_comment_helper(self.comment1)
        data1 = json.loads(rv1.data)
        self.comment2["parent"] = data1["id"]
        rv2 = self.post_comment_helper(self.comment2)
        data2 = json.loads(rv2.data)

        self.assertIn(self.comment2["author"], rv2.data)
        self.assertIn(self.comment2["content"], rv2.data)
        Comment.objects(id=data1["id"]).delete()
        Comment.objects(id=data2["id"]).delete()

    def test_post_filter_comment(self):
        """
        Test if the comment containing red flag words will be filtered
        """
        rv = self.post_comment_helper(self.comment3)
        self.assertIn(self.comment3["author"], rv.data)
        self.assertNotIn(self.comment3["content"], rv.data)
        self.assertIn("bi", rv.data)
        Comment.objects(id=json.loads(rv.data)["id"]).delete()


    def test_get_comment(self):
        """
        Test if the user can get comments posted
        """
        rv1 = self.post_comment_helper(self.comment1)
        data1 = json.loads(rv1.data)
        self.comment2["parent"] = data1["id"]
        rv2 = self.post_comment_helper(self.comment2)
        data2 = json.loads(rv2.data)

        rv = self.app.get("/comment/Assignment0")
        self.assertIn(self.comment1["author"], rv.data)
        self.assertIn(self.comment1["content"], rv.data)
        self.assertIn(self.comment2["author"], rv.data)
        self.assertIn(self.comment2["content"], rv.data)

        Comment.objects(id=data1["id"]).delete()
        Comment.objects(id=data2["id"]).delete()


if __name__ == '__main__':
    unittest.main()
