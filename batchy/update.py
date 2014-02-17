#!/usr/bin/python

import re

import yaml

from . import RESERVED_FILE_KEY
from .utils import _list_files, _read_files, _write_files


def batchy_update(key, value, files, add=False, append=False):
    if add and append:
        raise ValueError('conflicting keyword arguments \'add\' and \'append\' cannot both be true')
    docs = _read_files(files)
    if add:
        # create a new key with value, do nothing if key already exists
        for doc in docs:
            if key not in doc.keys():
                doc[key] = value
    elif append:
        # append the value to the exisiting key, converting to a list if necessary
        for doc in docs:
            if key in doc.keys():
                if isinstance(doc[key], list):
                    doc[key].append(value)
                else:
                    doc[key] = [doc[key], value]
    else:
        # default is overwrite
        for doc in docs:
            if key in doc.keys():
                doc[key] = value

    _write_files(docs)
    return docs
