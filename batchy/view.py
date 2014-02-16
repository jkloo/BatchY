#!/usr/bin/python

import yaml

from . import RESERVED_FILE_KEY
from .utils import _list_files


def _batchy_view(args):
    docs = []
    for f in args.files:
        with open(f, 'r') as g:
            docs.append(yaml.load(g))
            # keep a reference to the file the data came from
            docs[-1][RESERVED_FILE_KEY] = f

    # filter on the desired keys
    if args.keys:
        for doc in docs:
            for k in doc.keys():
                if k not in args.keys + [RESERVED_FILE_KEY]:
                    del doc[k]

    return yaml.dump_all(docs, default_flow_style=False)
