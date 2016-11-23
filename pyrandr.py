#!/usr/bin/python3.5
from subprocess import PIPE, run
import os

# PyRandr Project

states = None

def command_out(cmd):
    c = run(cmd, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return c.stdout


def find_devices():
    cmdout = command_out('xrandr').split('\n')
    return [i.split(' ')[0] for i in cmdout if 'connected' in i and not 'disconnected' in i]


def get_config_file():
    check_file_state()
    if os.path.isfile(os.environ['HOME'] + '/.config/pyrandr'):
        with open(os.environ['HOME']+'/.config/pyrandr') as config_file:
            res = [x.replace('\n','') for x in config_file.readlines()]
            if get_display_state() >= len(res):
                with open('/tmp/pyrandr-state', 'w') as display_state_file:
                    display_state_file.write('0')
        return res
    else:
        return [
            'xrandr --output {b} --off --output {a} --auto',
            'xrandr --output {a} --off --output {b} --auto',
            'xrandr --output {a} --auto --output {b} --right-of {a}',
            'xrandr --output {a} --auto --output {b} --left-of {a}',
            'xrandr --output {a} --auto --output {b} --same-as {a}',
        ]


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


def xrandr_exec(devices):
    states = get_config_file()
    check_file_state()
    if len(devices) == 2:
        a, b = devices[0], devices[1]
        current_state = get_display_state()
        command = states[current_state]
        os.system(command.format(**{"a" : a, "b" : b}))
        increase_display_state()

if __name__ == '__main__':
    devs = find_devices()
    xrandr_exec(devs)




