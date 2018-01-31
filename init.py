#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml
import os

def mkvdir(): 
    mk_usr_command = 'sudo mkdir /usr/bin/labelprinter'
    cpcommand = 'sudo cp label.py /usr/bin/labelprinter/label'
    p = os.system('echo %s|sudo -S %s' % (sudopw, mk_usr_command))
    p = os.system('echo %s|sudo -S %s' % (sudopw, cpcommand))

def scriptpersistenc():
    print ('This step is not required if you want to use it just in the repository, but it is necessary when you want to use it persistent.')
    print ('Do you want to make the script persistent? Y/n')
    Scriptpersistence = input()
    if Scriptpersistence=='n':
        print('Okay')
    else:
        print ('okay')
        print ('In order to make the script persistent the SUDO password is needed.')
        print ('Please type in below')
        global sudopw
        sudopw=input()
        print("Okay I will make it persistent.")
        mkvdir()
        print("Done")


def temp_dir():
    print ('Define the template directory. The default will be ~/.labelprinter/template')
    template_directory = input()
    global template
    if template_directory=='' or template_dir=='~/.labelprinter/template':
        template = '~/.labelprinter/template'
    else:
        template = template_directory()

def printer_def():
    print ('Define the printer')
    global printer
    printer=input()

def conf():
    print ('The conf file will be placed in ~/.labelprinter ')
    print ('Intialize conf.yml')
    mkcommand = 'mkdir ~/.labelprinter'
    p = os.system(mkcommand)

    data = dict(
        printer = printer,
        debug = 'warning',
        template_dir = template
    )

    with open(os.path.expanduser("~/.labelprinter/conf.yml"), 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

def inst():
    scriptpersistenc()
    temp_dir()
    printer_def()
    conf()

def uninstall():
    print ('In order to uninstall the script the SUDO password is needed.')
    sudopw=input()
    
    rm_command = 'sudo rm -rfv /usr/bin/labelprinter'
    rm_conf_command = 'rm -rfv ~/.labelprinter'
    p = os.system('echo %s|sudo -S %s' % (sudopw, mk_usr_command, cpcommand))
    
print ('Please intialise the labelprinter script')
#print ('Please place the initial and the conf.yml in the same directory with the labelscript.')
#print ('If you wish to place the config and or the initial file somewhere else please specify where the three files are.')
print ('Do you want to install, update or uninstall the labelprinter script? install/update/uninstall')
up_inst = input()
if up_inst=='install':
    inst()

elif up_inst=='update':
    update()

elif up_inst=='uninstall':
    uninstall()