__author__ = 'Xuefeng Zhu'

import unittest
from portfolio.app import app


class TestProjectView(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_project_list(self):
        """
        Test if the project list can display required information
        """
        rv = self.app.get("/")
        self.assertIn("Assignment0", rv.data)
        self.assertIn("Assignment1.0", rv.data)
        self.assertIn("Assignment2.0", rv.data)

    def test_project_detail(self):
        """
        Test if the project detail page can display required information
        """
        rv = self.app.get("/Assignment0")
        self.assertIn("Assignment0", rv.data)
        self.assertIn("2015-02-04 21:57:12.156363", rv.data)
        self.assertIn("221", rv.data)
        self.assertIn("commit assignment0", rv.data)

        self.assertIn("Assignment0/Procfile", rv.data)
        self.assertIn("Assignment0/README.md", rv.data)

if __name__ == '__main__':
    unittest.main()
