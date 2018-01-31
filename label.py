#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main script."""

# import subprocess

import logging

import os
import string

import cups

import yaml

from arguments.getargs import get_args

home = os.path.expanduser('~')

# Wir braauchen eine abfrage ob ein config file mit in den parser geschmissen wird.

# workaround 

#with open("/.labelprinter/conf.yml", 'r') as conf:
with open(os.path.expanduser("~/.labelprinter/conf.yml"), 'r') as conf:
    cfg = yaml.load(conf)


class LaTeXTemplate(string.Template):
    """Change the variable delimiter."""

    delimiter = "%%"


def list_templates():
#    template_dir = os.listdir("~/bin/label/templates") # Wir koennten diesen eintrag von der conf.yml holen und den vorher vom init script reinschreiben lassen
#    template_dir = os.listdir("~/bin/label/templates")
#    template_dir = os.listdir("~/.labelprinter/templates")
    list_template_dir = os.listdir(template_dir)
    print('\t')
    for template in list_template_dir:
        print('{}{}'.format('   ', template))
    print('\t')


def list_printers():

    con = cups.Connection()
    print('\t')
    for printer in con.getPrinters():
        print('{}{}'.format('   ', printer))
    print('\t')


def main():
    """Main function."""

    printer, textemplate, string, printers, preview, printit, debug, amount, cleanup, templates = get_args()

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

    if not textemplate and not cleanup:
        logging.error('No template selected. Parameter --template used?')

    if not string:
        logging.error('No data selected --string parameter used.')
        exit(0)

    else:
        #file = open(home + '/.labelprinter/templates/data.tex', 'w')
        #logging.info('Content writen…')
        #file.write(string)
        #file.close()
        logging.info('…done')

    if preview and printit:
        logging.ERROR('Dont use --preview and --printit together')
        exit(0)

    with open('~/.labelprinter/templates/template_' + textemplate, 'r') as template:
        data = template.read()
        with open('~/.labelprinter/templates/' + textemplate, 'w') as letter:
            letter.write(LaTeXTemplate(data).substitute(string=string))
        letter.close()
    template.close()


    #if not debug:
    #    latex = subprocess.Popen(['pdflatex', home + '/.labelprinter/templates/' + template], stdout=open(os.devnull, 'wb'))
    #else:
    #    latex = subprocess.Popen(['pdflatex', home + '/.labelprinter/templates/' + template])

    #logging.info('Compiling Latex…')

    #for x in range(3):
    #    latex.communicate()

    #logging.info('Compiling Latex done')

    #pdffile = template.replace('.tex', '.pdf')

    #if preview:
    #    if not debug:
    #        pdfview = subprocess.Popen(['xreader', pdffile], stderr=open(os.devnull, 'wb'))
    #    else:
    #        pdfview = subprocess.Popen(['xreader', pdffile])

    #   logging.info('Opening preview PDF file')
    #    pdfview.communicate()

    if not amount:
        amount = 1

    #if printit:
    #    for x in range(amount):
    #        con = cups.Connection()
     ##       logging.info('Print PDF file')
     #       con.printFile(printer, pdffile, template, {})

    #os.rename(pdffile, pdffile.replace('.pdf', '') + '--' + string + '.pdf')

    if cleanup:
        for file in os.listdir(os.getcwd()):
            suffix = file.split('.')[-1]
            if suffix == "aux" or suffix == 'log':
                os.remove(file)
        logging.info('Temp files deleted')
        exit(0)


if __name__ == '__main__':

    main()
