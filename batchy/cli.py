#!/usr/bin/python

import argparse

from . import CLI
from .utils import _list_files
from .find import _batchy_find
from .update import _batchy_update
from .view import _batchy_view


def _generate_args(args=None):
    parser = argparse.ArgumentParser(prog=CLI)

    subparser = parser.add_subparsers(title='subcommands')

    find = subparser.add_parser('find')
    find.set_defaults(func=_batchy_find)
    find.add_argument('pattern', help='Pattern to search files for.')
    find.add_argument('--keys', nargs='+', help='')
    find.add_argument('--replace', nargs='+', help='')
    find.add_argument('--files', nargs='+', help='List of files to limit the scope to.', default=[])
    find.add_argument('--dirs', nargs='+', help='List of directories to limit the scope to.', default=[])

    update = subparser.add_parser('update')
    update.set_defaults(func=_batchy_update)
    update.add_argument('key', help='')
    update.add_argument('value', help='')
    group = update.add_mutually_exclusive_group()
    group.add_argument('--add', action='store_true')
    group.add_argument('--append', action='store_true')
    update.add_argument('--files', nargs='+', help='List of files to limit the scope to.', default=[])
    update.add_argument('--dirs', nargs='+', help='List of directories to limit the scope to.', default=[])

    view = subparser.add_parser('view')
    view.set_defaults(func=_batchy_view)
    view.add_argument('--keys', nargs='+')
    view.add_argument('--files', nargs='+', help='List of files to limit the scope to.', default=[])
    view.add_argument('--dirs', nargs='+', help='List of directories to limit the scope to.', default=[])

    args = parser.parse_args(args)
    args.files = _list_files(args.files, args.dirs)
    return args


def main(args=None):
    args = _generate_args(args)
    return args.func(args)
