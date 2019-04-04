!/usr/bin/env python
#'''
#Trigger script
#'''
#=======================================================================
#
#
#           ~~~~~~~~~~~~~~~   TRIGGER   ~~~~~~~~~~~~~~~    
#
#                        UNHFarmbot Farmware        
#
#=======================================================================
# Written by: Alfred Odierno, Amadou Tall, 
#             Issam Benabdelkrim
#
# Created: Ver. 0.1 04/04/19
# Updated: ver. 0.2 
#
#-----------------------------------------------------------------------
# This program is designed to be implemented as Farmware for the FarmBot 
# web-app. 
#
# The "Trigger" Farmware will launch the script "Data Transfer" installed
# on the a second raspberry pi connected to the Farmbot pi through serial
# A call is recieved from the web-app. The Farmbot will send a 'start' 
# signal to the Image processor. 
#------------------------------------------------------------------------

import serial
from time import sleep
port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=None)

while True:
    pin = input("").strip()
    port.write(str.encode(pin))
    sleep(0.1)
