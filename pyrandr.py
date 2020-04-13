#!/usr/bin/python3
from subprocess import PIPE, run
import argparse
import os

# PyRandr Project

text = """  
    It is a small script that uses xrandr to change the configuration of 2 screens.
    It is designed to be a shortcut and not have to open more complex applications such as: arandr or others.
    Maximum use with two screens, in case there are more than two screens, you should use the --exclude option.
"""

parser = argparse.ArgumentParser(description=text)
parser.add_argument("--exclude", "-e", help="To exclude a display or a list. Usage example: -e eDP-1,HDMI-1 ")

args = parser.parse_args()

states = [
    'xrandr --output {b} --off --output {a} --auto {devices_off}',
    'xrandr --output {a} --off --output {b} --auto {devices_off}',
    'xrandr --output {a} --auto --output {b} --right-of {a} {devices_off}',
    'xrandr --output {a} --auto --output {b} --left-of {a} {devices_off}',
    'xrandr --output {a} --auto --output {b} --same-as {a} {devices_off}',
]


def command_out(cmd):
    command_out = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return command_out


def exclude_devices(devices, exclude_devices_list):
    clean_devices_list = list()
    for device in devices:
        if not device in exclude_devices_list:
            clean_devices_list.append(device)
    return clean_devices_list


def find_devices():
    cmdout = command_out('xrandr').stdout.split('\n')
    devices = [i.split(' ')[0] for i in cmdout if 'connected' in i and not 'disconnected' in i]
    return devices


def increase_display_state():
    current_state = get_display_state()
    next_state = (current_state + 1) % len(states)

    with open('/tmp/pyrandr-state', 'w') as display_state_file:
        display_state_file.write(str(next_state))


def get_display_state():
    with open('/tmp/pyrandr-state') as display_state_file:
        number_state = display_state_file.read()

    return int(number_state)


def check_file_state():
    if not os.path.isfile('/tmp/pyrandr-state'):
        with open('/tmp/pyrandr-state', 'w') as display_state_file:
            display_state_file.write('0')


def exclude_devices_str(exc_devs):
    command = [f" --output {d} --off " for d in exc_devs]
    return "".join(command)


def xrandr_exec(devices, exc_devs):
    check_file_state()
    if len(devices) == 2:
        a, b, devices_off = devices[0], devices[1], exclude_devices_str(exc_devs)

        current_state = get_display_state()
        command = states[current_state]
        os.system(command.format(**{"a" : a, "b" : b, "devices_off": devices_off}))

        increase_display_state()
    else:
        print("More than two screens have been detected. Use the option -e (--exclude)")

if __name__ == '__main__':
    all_connected_devices = find_devices()
    devices_to_exclude = args.exclude.split(",") if args.exclude else list()
    devices = exclude_devices(all_connected_devices, devices_to_exclude)
    xrandr_exec(devices, devices_to_exclude)
