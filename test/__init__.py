#!/usr/bin/python

import os

import yaml

TESTROOT = 'files'
TESTFILES_PEOPLE = ['files/people/bob.yml',
                    'files/people/dave.yml',
                    'files/people/jeff.yml',
                    'files/people/steve.yml']
TESTFILES_PEOPLE.sort()

TESTFILES_ANIMALS = ['files/animals/lion.yml',
                     'files/animals/shark.yml',
                     'files/animals/tiger.yml',
                     'files/animals/wolf.yml']
TESTFILES_ANIMALS.sort()

TESTFILES = TESTFILES_PEOPLE + TESTFILES_ANIMALS
TESTFILES.sort()

TESTDATA = {'files/people/bob.yml': {'first': 'Bob', 'middle': 'James', 'last': 'Stevens', 'pets': ['cat', 'dog']},
             'files/people/dave.yml': {'first': 'David', 'middle': 'James', 'last': 'Davidson', 'pets': ['cat']},
             'files/people/jeff.yml': {'first': 'Jeff', 'middle': 'Lee', 'last': 'Kloosterman'},
             'files/people/steve.yml': {'first': 'Steve', 'middle': 'Herbert', 'last': 'Stevens'},
             'files/animals/tiger.yml': {'type': 'cat', 'legs': 4},
             'files/animals/lion.yml': {'type': 'cat', 'legs': 4}, 
             'files/animals/wolf.yml': {'type': 'dog', 'legs': 4},
             'files/animals/shark.yml': {'type': 'fish', 'legs': 0}}


def write_file(f, data):
    with open(f, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def setup_file_system(files):
    def makefile(path):
        basedir = os.path.dirname(path)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        open(path, 'a').close()

    for f in files:
        makefile(f)


