#!/usr/bin/python

import os

from . import FILETYPES


def _list_files(files, dirs):
    file_list = []
    if dirs:
        for d in dirs:
            if os.path.isdir(d):
                for r, ds, fs in os.walk(d):
                    files.extend([os.path.join(r, f) for f in fs])
    else:
        for r, ds, fs in os.walk(os.getcwd()):
            files.extend([os.path.join(r, f) for f in fs])

    for f in files:
        if os.path.isfile(f):
            if os.path.splitext(f)[1].strip('.') in FILETYPES:
                file_list.append(os.path.relpath(f))
    return list(set(file_list))
