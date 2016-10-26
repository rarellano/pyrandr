#!/usr/bin/python3.5
from subprocess import PIPE,run
import os

# PyRandr Project

def command_out(cmd):
	c = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
	return c.stdout

def find_devices(stdout):
	devices=[]
	for i in cmdout:
		if 'connected' in i and not 'disconnected' in i:
			aux=i.split(' ')
			devices.append(aux[0])
	return devices

def xrandr_exec(devices):
	a = devices[0]
	b = devices[1]
	os.system('xrandr --output '+ a +' --auto  --output '+ b +' --right-of '+ a)

cmdout = command_out('xrandr').split('\n')

devs = find_devices(cmdout)

xrandr_exec(devs)







