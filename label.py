#!/usr/bin/env python3

import argparse
import os
import subprocess
import cups
import logging
import yaml

with open("conf.yml", 'r') as conf:
    cfg = yaml.load(conf)

def list_templates():
    template_dir = os.listdir("~/bin/label/templates")
    print('\t')
    for template in template_dir:
        print('{}{}'.format('   ', template))
    print('\t')


def list_printers():

    con = cups.Connection()
    print('\t')
    for printer in con.getPrinters():
        print('{}{}'.format('   ', printer))
    print('\t')

def get_args():

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
                        #metavar='',
                        help='List Printer')
    parser.add_argument('--listtemplates',
                        required=False,
                        action='store_true',
                        #metavar='',
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
                        choices=['info', 'warning'],
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

    if cfg['printer']:
        printer = cfg['printer']
    elif not cfg['printer']:
        printer = args.printer
    else:
        logging.error('No printer selected. Parameter --printer used?')
        printer = None

    template = args.template
    string = args.string
    printers = args.listprinter
    preview = args.p
    printit = args.printit
    debug = args.debug
    amount = args.amount
    cleanup = args.c
    templates = args.listtemplates

    return printer, template, string, printers, preview, printit, debug, amount, cleanup, templates


def main():

    printer, template, string, printers, preview, printit, debug, amount, cleanup, templates = get_args()

    logging.basicConfig(format='%(message)s')

    if templates:
        list_templates()
        exit(0)

    if printers:
        list_printers()
        exit(0)

    if not debug:
        logging.getLogger().setLevel(logging.INFO)
    elif debug == 'warning':
        logging.getLogger().setLevel(logging.WARNING)

    if not template and not cleanup:
        logging.error('No template selected. Parameter --template used?')

    if not string:
        logging.error('No data selected --string parameter used.')
        exit(0)

    else:
        file = open('templates/data.tex', 'w')
        logging.info('Content writen…')
        file.write(string)
        file.close()
        logging.info('…done')

    if preview and printit:
        logging.ERROR('Dont use --preview and --printit together')
        exit(0)

    if not debug:
        latex = subprocess.Popen(['pdflatex', 'templates/' + template], stdout=open(os.devnull, 'wb'))
    else:
        latex = subprocess.Popen(['pdflatex', 'templates/' + template])

    logging.info('Compiling Latex…')

    for x in range(3):
        latex.communicate()

    logging.info('Compiling Latex done')

    pdffile = template.replace('.tex', '.pdf')

    if preview:
        if not debug:
            pdfview = subprocess.Popen(['xreader', pdffile], stderr=open(os.devnull, 'wb'))
        else:
            pdfview = subprocess.Popen(['xreader', pdffile])

        logging.info('Opening preview PDF file')
        pdfview.communicate()

    if not amount:
        amount = 1

    if printit:
        for x in range(amount):
            con = cups.Connection()
            logging.info('Print PDF file')
            con.printFile(printer, pdffile, template, {})

    os.rename(pdffile, pdffile.replace('.pdf', '') + '--' + string + '.pdf')

    if cleanup:
        for file in os.listdir(os.getcwd()):
            suffix = file.split('.')[-1]
            if suffix == "aux" or suffix == 'log':
                os.remove(file)
        logging.info('Temp files deleted')
        exit(0)


if __name__ == '__main__':

    main()
