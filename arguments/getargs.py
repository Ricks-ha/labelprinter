"""Get the commandline options."""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


def get_args():
    """Read the parsed arguments."""
    parser = argparse.ArgumentParser(description='', prog='label.py')
    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version='%(prog)s {}'.format('version'))

    parser.add_argument('-t',
                        '--template',
                        metavar='<template>',
                        type=str,
                        help='')

    parser.add_argument('--printer',
                        help='Printer')

    parser.add_argument('-s',
                        '--string',
                        action='store',
                        help='Label Content')

    parser.add_argument('--listprinter',
                        required=False,
                        action='store_true',
                        # metavar='',
                        help='List Printer')
    parser.add_argument('--listtemplates',
                        required=False,
                        action='store_true',
                        # metavar='',
                        help='List templates')

    parser.add_argument('-p',
                        action='store_true',
                        help='preview')

    parser.add_argument('-P',
                        '--printit',
                        action='store_true',
                        help='Print Label')

    parser.add_argument('-d',
                        '--debug',
                        action='store',
                        # choices=['info', 'warning'],
                        help='Debug mode')

    parser.add_argument('-a',
                        '--amount',
                        action='store',
                        type=int,
                        metavar='int',
                        help='Print label n times')

    parser.add_argument('-c',
                        required=False,
                        action='store_true',
                        help='clean up temp files')
    args = parser.parse_args()

    printer = args.printer
    textemplate = args.template
    string = args.string
    printers = args.listprinter
    preview = args.p
    printit = args.printit
    debug = args.debug
    amount = args.amount
    cleanup = args.c
    templates = args.listtemplates

    return printer, textemplate, string, printers, preview, printit, debug, amount, cleanup, templates
