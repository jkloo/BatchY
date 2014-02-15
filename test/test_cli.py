#!/usr/bin/python

import os
import unittest

from . import TESTFILES
from batchy.cli import main, _list_files, _generate_args


class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_args(self):
        self.assertRaises(SystemExit, main, [])


class TestBatchyFind(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_args(self):
        self.assertRaises(SystemExit, main, ['find'])

    def test_no_flags(self):
        self.assertIs(None, main(['find', 'a']))


class TestBatchyUpdate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_args(self):
        self.assertRaises(SystemExit, main, ['update'])        

    def test_no_flags(self):
        self.assertIs(None, main(['update', 'a', 'b']))        


class TestBatchyView(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_args(self):
        self.assertIs(None, main(['view']))


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
