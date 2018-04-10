#!/usr/bin/env python
#'''
#Take get SPAD Number
#'''


#=======================================================================
#
#
#           ~~~~~~~~~~~~~~~   S.P.A.D.   ~~~~~~~~~~~~~~~    
#
#                        UNHFarmbot Farmware        
#
#=======================================================================
# Written by: Alfred Odierno, Sean Cronin, Ezequiel Abreu, 
#             Issam Benabdelkrim
#
# Created: Ver. 0.1 11/16/17
# Updated: ver. 0.2 11/16/17 by Alfred Odierno
#
#-----------------------------------------------------------------------
# This program is designed to be implemented as Farmware for the FarmBot 
# web-app. 
#
# The SPAD Farmware will take a picture of a plant being managed by the
# bot. The image will be analysed and a SPAD number will be generated. A
# report will be outputed to the web-app. A call is recieved from the
# web-app. The Farmbot will send a 'start' signal to the Image processor. 
#------------------------------------------------------------------------

### Import libraries ###
import os
import json
import requests
#import serial

### Define Functions ###

#ser =serial.Serial(
 #   "/dev/tty4",
 #   baudrate=9600,
 #   parity=serial.PARITY_NONE,
 #   stopbits=serial.STOPBITS_ONE,
 #   bytesize=serial.EIGHTBITS,
 #   writeTimeout = 0,
 #   timeout = 10,
 #   rtscts=False,
 #   dsrdtr=False,
#    xonxoff=False)
#init = '0xBF'

#def initiate():
 #   log("Serial Initiated...","success")
 #   ser.write(init)
  #  print(ser.read())
   # log("Message Sent", "success")
    
#def farmware_api_url():
#    major_version = int(os.getenv('FARMBOT_OS_VERSION', '0.0.0')[0])
#    base_url = os.environ['FARMWARE_URL']
  #  return base_url + 'api/v1/' if major_version > 5 else base_url
def log(message, message_type):
    'Send a send_message command to post a log to the Web App.'
    requests.post(
        os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
        headers={'Authorization': 'Bearer ' + os.environ['FARMWARE_TOKEN'],
                 'content-type': 'application/json'},
        data=json.dumps({
            'kind': 'send_message',
            'args': {
                'message': message,
                'message_type': message_type}}))
#def log(message, message_type):
#    'Send a message to the log.'
#    try:
 #       os.environ['FARMWARE_URL']
 #   except KeyError:
  #      print(message)
  #  else:
   #     log_message = str(message)
   #     headers = {
    #        'Authorization': 'bearer {}'.format(os.environ['FARMWARE_TOKEN']),
    #        'content-type': "application/json"}
    #    payload = json.dumps(
     #       {"kind": "send_message",
     #        "args": {"message": log_message, "message_type": message_type}})
       # requests.post(farmware_api_url() + 'celery_script',
     #                 data=payload, headers=headers)
  
        #### EXECUTE ####

if __name__ == '__main__':
        log("Started Program", "success")
        #initiate()
       
