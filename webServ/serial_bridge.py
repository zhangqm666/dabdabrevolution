#!/usr/bin/env python
# vim:set ft=python nolist ts=2 sw=2 sts=2 et tw=0:

import math
import os
import sys
# import serial
import threading

from time import sleep

# run(host='0.0.0.0', port=8080, server='gevent')

from bottle import route, run, static_file

# SERIAL_PORT = '/dev/tty.usbmodem1412'


# NOTE: This really should have a lock protecting it, but I am abusing the fact
# that lists in python 2 have "atomic" operations.
new_data = []
def wait_on_serial():
  p = serial.Serial(SERIAL_PORT, 115200, timeout=3)
  while True:
    new_data.append(p.readline().rstrip('\n\r'))


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


a = [0]

@route('/result')
def result():
	a[0] += 1
	if a[0] == 7:
		a[0] = 0
	sleep(0.5)
	return ['tr', 'tl', 'br', 'bl', 'tick', 'cross', 'clear'][a[0]]


# Spin the serial code off into its own thread.
t = threading.Thread(target=wait_on_serial)
t.daemon = True
t.start()

run(host='localhost', port=8080)
