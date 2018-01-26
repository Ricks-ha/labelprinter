#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#import yaml
#import subprocess

print ('Please intialise the labelprinter script')
print ('Please place the initial and the conf.yml in the same directory with the labelscript.')
print ('If you wish to place the config and or the initial file somewhere else please specify where the three files are.')
print ('This step is not required if you want to use it just in the repository, but it is necessary when you want to use it persistent.')

print ('Do you wdant to make the script persistent? Y/n')
Scriptpersistence = input()
if Scriptpersistence=='n':
    print('Okay')
else:
    print ('okay')
    print ('In order to make the script persistent the SUDO password is needed.')
    print ('Please type in below')
    sudot=input()

#        print("Okay I will make it persistent.") # was auch immer du dann noch fragen willst
#        subprocess.Popen("sudo cp ./label.py /usr/local/bin/")
#        print("Done")
#print ('Should I create more than one conf file?')

print ('Where should I place the conf file? The default will be ~/.labelprinter.')
conf_dir=input()
if conf_dir=='' or conf_dir=='n' or conf_dir=='no':
    print ('I will use the default')
else: 
        print ('Set')