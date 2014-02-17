#!/usr/bin/python

import yaml

from . import RESERVED_FILE_KEY
from .utils import _list_files, _read_files


def batchy_view(files, keys):
    docs = _read_files(files)
    # filter on the desired keys
    if keys:
        for doc in docs:
            for k in doc.keys():
                if k not in keys + [RESERVED_FILE_KEY]:
                    del doc[k]

    return yaml.dump_all(docs, default_flow_style=False)
