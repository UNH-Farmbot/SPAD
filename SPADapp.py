#!/usr/bin/env python
'''SPAD'''


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
# Created: Ver. 0.1.0 11/16/17
# Updated: ver. 1.0.0  13/27 by Alfred Odierno
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

import os
import ImageCapture as IC
import ImageProcessing as IP
import ImageAnalysis as IA
import json
import requests


def get_token():
# Inputs:
	global EMAIL
	EMAIL = raw_input("FarmBot Email: ")
	global PASSWORD
	PASSWORD = raw_input("WebApp Password: ")
# Get your FarmBot Web App token.
	headers = {'content-type': 'application/json'}
	user = {'user': {'email': EMAIL, 'password': PASSWORD}}
	payload = json.dumps(user)
	response = requests.post('https://my.farmbot.io/api/tokens',headers=headers, data=payload)
	global TOKEN
	TOKEN = response.json()['token']['encoded']



def Run_Routines():
### Call Image Capture subroutine ###
	image=IC.capture()      # Takes picture with raspicamera. Saves 
							# to local folder 'images' as current 
							# '%datetime' +.jpg. Returns file+path.
### Call Pipeline ###
	data=IP.process(image)  # Creates color data from plant image. 
							# Saves to local folder 'plantdata' as 
							# current '%datetime' +.txt. Returns 
							# file+path.
### Call DataAnalysis.py ###
	spad_number=IA.analysis(data)   # Estimates SPAD number using  
									# saves nuber to a txt file
									# returns SPAD number
	return (spad_number)


# Send the number to the FarmBot Web App logs.
def send_it(s_number):
	headers = {'Authorization': 'Bearer ' + TOKEN,'content-type': 'application/json'}
	data = json.dumps({'message': 'SPAD number:' + str(s_number)})
	response = requests.post('https://my.farmbot.io/api/logs', headers=headers, data=data)
	print "sent it!"


def main():
	get_token()
	s_number = Run_Routines()
	send_it(s_number)
	
if __name__ == '__main__':
	main()
