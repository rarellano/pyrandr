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

def display_state(n):
	# fstate = open('/home/rarellano/.config/','w')
	pass

def get_display_state(n):
	pass

def xrandr_exec(devices):
	a = devices[0]
	b = devices[1]
	
	display_state(0)
	
	if len(devices) == 2:
		if get_display_state == 0:
			os.system('xrandr --output '+ a +' --off')
		if get_display_state == 1:
			os.system('xrandr --output '+ b +' --off')
		if get_display_state == 2:
			os.system('xrandr --output '+ a +' --auto  --output '+ b +' --same-as '+ a)
		if get_display_state == 3:
			os.system('xrandr --output '+ a +' --auto  --output '+ b +' --left-of '+ a)
		if get_display_state == 4:
			os.system('xrandr --output '+ b +' --auto  --output '+ a +' --left-of '+ b)
		
		display_state(1)


cmdout = command_out('xrandr').split('\n')

devs = find_devices(cmdout)

xrandr_exec(devs)







