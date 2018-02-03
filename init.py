#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml
import os
import urllib
import urllib.request
import re

def mkvdir(): 
    mk_usr_command = 'sudo mkdir /usr/bin/labelprinter'
    cpcommand = 'sudo cp -r label.py arguments tex  /usr/bin/labelprinter/'
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
        global sudopw
        sudopw=input()
        print("Okay I will make it persistent.")
        mkvdir()
        print("Done")

def temp_dir():
    print ('Define the template directory. The default will be ~/.labelprinter/template')
    template_directory = input()
    mkcommand = 'mkdir ~/.labelprinter'
    p = os.system(mkcommand)
    global template
    if template_directory=='' or template_dir=='~/.labelprinter/template':
        template = '~/.labelprinter/template'
        mktempdir = 'mkdir ~/.labelprinter/template'
        p = os.system(mktempdir)
    else:
        template = template_directory()
    
def printer_def():
    print ('Define the printer')
    global printer
    printer=input()

def conf():
    print ('The conf file will be placed in ~/.labelprinter ')
    print ('Intialize conf.yml')
    
    data = dict(
        printer = printer,
        debug = 'warning',
        template_dir = template
    )

    with open(os.path.expanduser("~/.labelprinter/conf.yml"), 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

def version():
    p = os.system('wget -q https://priv.ricksha.eu/Update/version.txt')
    p = os.system('mv version.txt ~/.labelprinter/version.txt')
    
def inst():
    scriptpersistenc()
    temp_dir()
    printer_def()
    conf()
    version()
    print('Installation completed')

def uninstall():
    print ('In order to uninstall the script the SUDO password is needed.')
    sudopw=input()
    
    rm_command = 'sudo rm -rf /usr/bin/labelprinter'
    rm_conf_command = 'rm -rf ~/.labelprinter'
    p = os.system('echo %s|sudo -S %s' % (sudopw, rm_conf_command))
    p = os.system('echo %s|sudo -S %s' % (sudopw, rm_command))
    print('Uninstalling completed.')
    
def update_installer():
    print('In order to perform the update I need the SUDO password.')
    sudopw=input()
    rm_cm = 'rm -rf /tmp/label'
    p = os.system('echo %s|sudo -S %s' % (sudopw, rm_cm))
    p = os.system('mkdir -p /tmp/label/')
    p = os.system('git clone -q https://github.com/Ricks-ha/labelprinter.git /tmp/label/git_dir/ ')
    cpcommand = 'cp -rf /tmp/label/git_dir/label.py /tmp/label/git_dir/arguments /tmp/label/git_dir/tex  /usr/bin/labelprinter/'
    p = os.system('echo %s|sudo -S %s' % (sudopw, cpcommand))
    p = os.system('wget -q https://priv.ricksha.eu/Update/version.txt')
    p = os.system('mv version.txt ~/.labelprinter/version.txt')
    #p = os.system('echo %s|sudo -S %s' % (sudopw, rm_cm))
    
def update_checker():
    versionSource = open(os.path.expanduser("~/.labelprinter/version.txt"), 'r')
    versionContents = versionSource.read()
    versionContentDigits = re.sub("[^0123456789\.]","",str(versionContents))
    
    updateSource = urllib.request.urlopen("https://priv.ricksha.eu/Update/version.txt")
    updateContents = updateSource.read()
    updateContentDigits = re.sub("[^0123456789\.]","",str(updateContents))
    
    
    if updateContentDigits==versionContentDigits:
        print("There are no updates available")
        
    else:
        versionLabel = print("There are updates Available")
        print("Do you want me to install them for you? y/n")
        update_value = input()
        if update_value=='y':
            update_installer()
        else: 
            print("Okay I will leave it as it is")

def update():
    update_checker()
    print('Done')
    

print ('Please intialise the labelprinter script')
print ('You need to place the init.py and the conf.yml in the same directory with the label.py.')
#print ('If you wish to place the config and or the initial file somewhere else please specify where the three files are.')
print ('Do you want to install, update or uninstall the labelprinter script? install/update/uninstall')
up_inst = input()
if up_inst=='install':
    inst()

elif up_inst=='update':
    update()

elif up_inst=='uninstall':
    uninstall()
else: 
    print('Please write the statements exactly like they are given.')