#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml
#import subprocess
import os

print ('Please intialise the labelprinter script')
#print ('Please place the initial and the conf.yml in the same directory with the labelscript.')
#print ('If you wish to place the config and or the initial file somewhere else please specify where the three files are.')
print ('This step is not required if you want to use it just in the repository, but it is necessary when you want to use it persistent.')
print ('Do you want to make the script persistent? Y/n')
Scriptpersistence = input()
if Scriptpersistence=='n':
    print('Okay')
else:
    print ('okay')
    print ('In order to make the script persistent the SUDO password is needed.')
    print ('Please type in below')
    sudopw=input()
    print("Okay I will make it persistent.")
    cpcommand = 'sudo cp label.py /usr/bin/label'
    p = os.system('echo %s|sudo -S %s' % (sudopw, cpcommand))
    print("Done")
#print ('Should I create more than one conf file?')

print ('The conf file will be placed in ~/.labelprinter ')

print ('Intialize conf.yml')
mkcommand = 'mkdir ~/.labelprinter'
p = os.system(mkcommand)
print ('Define the printer')
printer=input()
print ('Define the template directory. The default will be ~/.labelprinter/template')
template_directory = input()
if template_directory=='' or template_dir=='~/.labelprinter/template':
    template = '~/.labelprinter/template'
else:
    template = template_directory

data = dict(
    printer = printer,
    debug = 'warning',
    template_dir = template
)

with open(os.path.expanduser("~/.labelprinter/conf.yml"), 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
