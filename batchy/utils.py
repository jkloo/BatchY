#!/usr/bin/python

import os

from . import FILETYPES, RESERVED_FILE_KEY


def _list_files(files, dirs):
    def _walk(d):
        output = []
        if os.path.isdir(d):
            for r, _, fs in os.walk(d):
                output.extend([os.path.join(r, f) for f in fs])
        return output

    output = []
    # get all the files from the CWD
    if not files and not dirs:
        output.extend(_walk(os.getcwd()))
    else:
        # get all of the files from the given dirs
        for d in dirs:
            output.extend(_walk(d))
        # make sure that the given files are YAML files and exist.
        output.extend([f for f in files if os.path.isfile(f)])

    return list(set([os.path.relpath(f) for f in output if os.path.splitext(f)[1].strip('.') in FILETYPES]))


def _read_files(files):
    docs = []
    for f in files:
        with open(f, 'r') as g:
            docs.append(yaml.load(g))
            # keep a reference to the file the data came from
            docs[-1][RESERVED_FILE_KEY] = f
    return docs
