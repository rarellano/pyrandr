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

def increase_display_state():
	display_state = open('/tmp/pyrandr-state', 'w') 
	n = get_display_state(read_display_state())
	display_state.write((n+1)+'\n')
	display_state.close()

def read_display_state():
	display_state = open('/tmp/pyrandr-state') 
	number_state = display_state.readlines()
	display_state.close()
	return number_state[0]

def get_display_state(s):
	return  int(read_display_state())


def check_file_state():
	if os.path.isfile('/tmp/pyrandr-state') == False:
		display_state = open('/tmp/pyrandr-state', 'w') 
		display_state.write('0\n')
		display_state.close()

def xrandr_exec(devices):
	
	check_file_state()
	
	if len(devices) == 2:
		a = devices[0]
		b = devices[1]

		if get_display_state == 0:
			print("Opción : " + get_display_state() )
			os.system('xrandr --output '+ a +' --off')
		if get_display_state == 1:
			print("Opción : " + get_display_state() )
			os.system('xrandr --output '+ b +' --off')
		if get_display_state == 2:
			print("Opción : " + get_display_state() )
			os.system('xrandr --output '+ a +' --auto  --output '+ b +' --same-as '+ a)
		if get_display_state == 3:
			print("Opción : " + get_display_state() )
			os.system('xrandr --output '+ a +' --auto  --output '+ b +' --left-of '+ a)
		if get_display_state == 4:
			print("Opción : " + get_display_state() )
			os.system('xrandr --output '+ b +' --auto  --output '+ a +' --left-of '+ b)
		
		increase_display_state()

check_file_state()

#increase_display_state()


print(get_display_state(read_display_state()))

#cmdout = command_out('xrandr').split('\n')

#devs = find_devices(cmdout)

#xrandr_exec(devs)
