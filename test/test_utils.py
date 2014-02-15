#!/usr/bin/python

import os
import unittest

from . import TESTFILES
from batchy.utils import _list_files


class TestListFiles(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        os.chdir(os.path.dirname(__file__))

    def tearDown(self):
        os.chdir(self.cwd)

    def test__list_files_empty_lists(self):
        files = _list_files([], [])
        files.sort()
        self.assertEqual(files, TESTFILES)
