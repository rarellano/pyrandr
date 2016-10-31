#!/usr/bin/python3.5
from subprocess import PIPE,run
import os

# PyRandr Project

def command_out(cmd):
	c = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
	return c.stdout

def find_devices():
	cmdout = command_out('xrandr').split('\n')
	return [i.split(' ')[0] for i in cmdout if 'connected' in i and not 'disconnected' in i]

def increase_display_state():
	current_state = get_display_state()
	display_state = open('/tmp/pyrandr-state', 'w') 
	if current_state == '0':
		next_state = '1'
	if current_state == '1':
		next_state = '2'
	if current_state == '2':
		next_state = '3'
	if current_state == '3':
		next_state = '4'
	if current_state == '4':
		next_state = '0'		
	display_state.write(next_state)
	display_state.close()

def get_display_state():
	display_state = open('/tmp/pyrandr-state') 
	number_state = display_state.readlines()
	display_state.close()
	return number_state[0]

def check_file_state():
	if os.path.isfile('/tmp/pyrandr-state') == False:
		display_state = open('/tmp/pyrandr-state', 'w') 
		display_state.write('0')
		display_state.close()

def xrandr_exec(devices):
	check_file_state()
	if len(devices) == 2:
		a,b = devices[0],devices[1]
		if get_display_state() == '0':
			os.system('xrandr --output ' + b + ' --off' + ' --output ' + a + ' --auto')
		if get_display_state() == '1':
			os.system('xrandr --output ' + a + ' --off' + ' --output ' + b + ' --auto')
		if get_display_state() == '2':
			os.system('xrandr --output ' + a + ' --auto  --output ' + b + ' --right-of ' + a)
		if get_display_state() == '3': 
			os.system('xrandr --output ' + a + ' --auto  --output ' + b + ' --left-of ' + a)
		if get_display_state() == '4':
			os.system('xrandr --output ' + a + ' --auto  --output ' + b + ' --same-as ' + a)	
		increase_display_state()

if __name__ == '__main__':
	devs = find_devices()
	xrandr_exec(devs)

