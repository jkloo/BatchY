#!/usr/bin/python

import os
import shutil
import unittest

from . import TESTDATA, TESTROOT
from . import TESTFILES, TESTFILES_ANIMALS, TESTFILES_PEOPLE
from . import setup_file_system, write_file
from batchy.utils import _list_files


class TestListFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # setup the test files
        cls.cwd = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        setup_file_system(TESTFILES)

    @classmethod
    def tearDownClass(cls):
        # remove the test files
        shutil.rmtree(TESTROOT)
        os.chdir(cls.cwd)

    def setUp(self):
        # make sure that each test starts with the same data
        for f, data in TESTDATA.items():
            write_file(f, data)
    
    def tearDown(self):
        pass

    def test__utils__list_files__empty_lists(self):
        files = _list_files([], [])
        files.sort()
        self.assertEqual(files, TESTFILES)

    def test__utils__list_files__given_dirs(self):
        files = _list_files([], ['files/people'])
        files.sort()
        self.assertEqual(files, TESTFILES_PEOPLE)

    def test__utils__list_files__given_files(self):
        focus = ['files/people/bob.yml', 'files/people/jeff.yml']
        files = _list_files(focus, [])
        files.sort()
        self.assertEqual(files, focus)

    def test__utils__list_files__given_files_and_dirs(self):
        focus = ['files/people/bob.yml', 'files/people/jeff.yml']
        output = _list_files(focus, ['files/animals'])
        output.sort()
        files = focus + TESTFILES_ANIMALS
        files.sort()
        print TESTFILES_ANIMALS
        print files
        print output
        self.assertEqual(files, output)

