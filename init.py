#!/usr/bin/env python3
import yaml
import subprocess

print ('Please intialise the labelprinter script')
print ('Please place the initial and the conf.yml in the same directory with the labelscript.')
print ('If you wish to place the config and or the initial file somewhere else please specify where the three files are.')

print ('The system may ask you to write the SUDO password in the next few steps')

print ('Where should I place the conf file?')

#print ('Do you want to make the script persistent? Y/n')
Scriptpersistence = input("So you want the script to be persistent? (y/n:)")
    if Scriptpersistence=='n':
        print("Okay dann nicht")
    else:
        print("Okay I will make it persistent.") # was auch immer du dann noch fragen willst
#        subprocess.Popen("sudo cp ./label.py /usr/local/bin/")
        print("Done")
print ('Should I create more than one conf file?')
