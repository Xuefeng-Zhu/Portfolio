__author__ = 'Frank'

import unittest
from portfolio.utils.parser import *


class TestParser(unittest.TestCase):
    def test_parse_svn_list(self):
        project_dict = parse_svn_list()
        self.assertEqual(6, len(project_dict))

        assignment0 = project_dict["Assignment0"]
        self.assertEqual("Assignment0", assignment0.title)
        self.assertEqual('221', assignment0.revision)
        self.assertEqual(32, len(assignment0.file_list))
        self.assertEqual(32, len(assignment0.file_dict))

    def test_parse_svn_log(self):
        project_dict = parse_svn_list()
        log_dict = parse_svn_log(project_dict)

        self.assertEqual(138, len(log_dict))

        log = log_dict["221"]
        self.assertEqual("221", log.revision)
        self.assertEqual("commit assignment0", log.msg)
        self.assertEqual("xzhu15", log.author)
        self.assertEqual("2015-02-04 21:57:12.156363", str(log.date))

        assignment2 = project_dict["Assignment2.0"]
        self.assertEqual(2, len(assignment2.file_dict["Assignment2.0/module/__init__.py"]))


if __name__ == '__main__':
    unittest.main()
