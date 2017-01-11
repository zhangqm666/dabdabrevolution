#!/usr/bin/env python
# vim:set ft=python nolist ts=2 sw=2 sts=2 et tw=0:

import math
import os
import sys
import serial
import threading

from bottle import route, run, static_file

SERIAL_PORT = '/dev/tty.usbmodem1412'


# NOTE: This really should have a lock protecting it, but I am abusing the fact
# that lists in python 2 have "atomic" operations.
new_data = []
def wait_on_serial():
  p = serial.Serial(SERIAL_PORT, 115200, timeout=3)
  while True:
    new_data.append(p.readline().rstrip('\n\r'))


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/Users/pipskweak/Desktop/web/')


@route('/get_next_line')
def get_next_line():
  line = None
  try:
    line = new_data.pop(0)
  except IndexError:
    # Do nothing, and just return None
    pass
  return {'data': line}


# Spin the serial code off into its own thread.
t = threading.Thread(target=wait_on_serial)
t.daemon = True
t.start()

run(host='localhost', port=8080)
