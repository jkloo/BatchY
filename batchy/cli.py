#!/usr/bin/python

import argparse

from batchy import CLI


def batchy_find(args):
    print('BatchY find!')


def batchy_update(args):
    print('BatchY update!')


def batchy_view(args):
    print('BatchY view!')


def generate_args(args=None):
    parser = argparse.ArgumentParser(prog=CLI)

    subparser = parser.add_subparsers(title='subcommands')

    find = subparser.add_parser('find')
    find.set_defaults(func=batchy_find)
    find.add_argument('pattern', help='Pattern to search files for.')
    find.add_argument('--keys', nargs='+', help='')
    find.add_argument('--replace', nargs='+', help='')
    find.add_argument('--files', nargs='+', help='List of files to limit the scope to.')
    find.add_argument('--dirs', nargs='+', help='List of directories to limit the scope to.')

    update = subparser.add_parser('update')
    update.set_defaults(func=batchy_update)
    update.add_argument('key', help='')
    update.add_argument('value', help='')
    group = update.add_mutually_exclusive_group()
    group.add_argument('--add', action='store_true')
    group.add_argument('--append', action='store_true')
    update.add_argument('--files', nargs='+', help='List of files to limit the scope to.')
    update.add_argument('--dirs', nargs='+', help='List of directories to limit the scope to.')

    view = subparser.add_parser('view')
    view.set_defaults(func=batchy_view)
    view.add_argument('--keys', nargs='+')
    view.add_argument('--files', nargs='+', help='List of files to limit the scope to.')
    view.add_argument('--dirs', nargs='+', help='List of directories to limit the scope to.')

    args = parser.parse_args(args)
    return args


def main():
    args = generate_args()
    args.func(args)
