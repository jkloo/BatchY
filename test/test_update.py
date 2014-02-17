#!/usr/bin/python

import os
import shutil
import unittest

from . import TESTDATA, TESTROOT
from . import TESTFILES, TESTFILES_ANIMALS, TESTFILES_PEOPLE
from . import setup_file_system, write_file

from batchy import RESERVED_FILE_KEY
from batchy.utils import _list_files, _read_files
from batchy.update import batchy_update


class TestBatchyUpdate(unittest.TestCase):
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
        self.docs = _read_files(TESTFILES)
    
    def tearDown(self):
        pass

    def test__batchy_update__overwrite_key_data(self):
        batchy_update('middle', 'TEST', TESTFILES)
        docs = _read_files(TESTFILES)
        self.assertEqual(len(TESTFILES_PEOPLE), len([x for x in docs if 'middle' in x.keys()]))
        for doc in docs:
            if 'middle' in doc.keys():
                self.assertEqual('TEST', doc['middle'])

    def test__batchy_update__append_key_data(self):
        batchy_update('pets', 'TEST', TESTFILES, append=True)
        docs = _read_files(TESTFILES)
        for doc in docs:
            if 'pets' in doc.keys():
                old_docs = [x for x in self.docs if x[RESERVED_FILE_KEY] == doc[RESERVED_FILE_KEY]]
                self.assertEqual(1, len(old_docs))
                old = old_docs[0]
                self.assertEqual(doc['pets'], old['pets'] + ['TEST'])

    def test__batchy_update__append_to_non_list(self):
        batchy_update('middle', 'TEST', ['files/people/jeff.yml'], append=True)
        doc = _read_files(['files/people/jeff.yml'])[0]
        self.assertTrue(isinstance(doc['middle'], list))
        self.assertEqual(doc['middle'], ['Lee', 'TEST'])

    def test__batchy_update__add_key(self):
        files = _list_files(dirs=['files/people'])
        batchy_update('thing', 'TEST', files, add=True)
        docs = _read_files(TESTFILES)
        for doc in docs:
            if doc[RESERVED_FILE_KEY] in TESTFILES_PEOPLE:
                self.assertTrue('thing' in doc.keys())
                self.assertEqual(doc['thing'], 'TEST')
            else:
                self.assertFalse('thing' in doc.keys())

    def test__batchy_update__add_and_append(self):
        self.assertRaises(ValueError, batchy_update, *['a', 's', TESTFILES], **{'add':True, 'append':True})
