#!/usr/bin/python

import os
import unittest

from . import TESTFILES
from batchy.cli import main


class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__cli__no_args(self):
        self.assertRaises(SystemExit, main, [])


class TestBatchyFind(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__cli__batchy_find__no_args(self):
        self.assertRaises(SystemExit, main, ['find'])

    def test__cli__batchy_find__no_flags(self):
        self.assertIs(None, main(['find', 'a']))


class TestBatchyUpdate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__cli__batchy_update__no_args(self):
        self.assertRaises(SystemExit, main, ['update'])        

    def test__cli__batchy_update__no_flags(self):
        self.assertIs(None, main(['update', 'a', 'b']))        


class TestBatchyView(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__cli__batchy_view__no_args(self):
        self.assertIs(None, main(['view']))
