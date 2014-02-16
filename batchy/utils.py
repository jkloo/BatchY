#!/usr/bin/python

import os

from . import FILETYPES


def _list_files(files, dirs):
    file_list = []

    # get all the files from the CWD
    if not files and not dirs:
        for r, _, fs in os.walk(os.getcwd()):
            files.extend([os.path.join(r, f) for f in fs])

    # get all of the files from the given dirs
    for d in dirs:
        if os.path.isdir(d):
            for r, ds, fs in os.walk(d):
                files.extend([os.path.join(r, f) for f in fs])

    # make sure that the given files are YAML files and exist.
    for f in files:
        if os.path.isfile(f):
            if os.path.splitext(f)[1].strip('.') in FILETYPES:
                file_list.append(os.path.relpath(f))

    return list(set(file_list))
