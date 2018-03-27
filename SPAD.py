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



#
# UPLOAD TO WEB APP
#


#
# INSTALL TO WEB AP 
#

### Import libraries ###
import RPi.GPIO as GPIO

### Setup ###
GPIO.setmode(GPIO.BCM)

# READ PIN
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #The pull_up_down
# argument controls the state of the internal pull-up/down resistors.
# A pull-down adds an additional resistor between the pin and ground, or
# put simply forces the voltage when the button is not pressed to be 0.
# Pin assigned is '4' as 'input'.

# print GPIO.input(4)GPIO.setmode(GPIO.BCM)

GPIO.add_event_detect(4, GPIO.RISING)# Read PIN
        def my_callback():
        print 'Start'
        GPIO.add_event_callback(4, my_callback)
        # starts a background thread that watches for low to high (0-3.3V)
        # May want to add something for debouncing.
# Write PIN
GPIO.output(25, GPIO.HIGH)

### SEND 'START' TO FARMBOT###


### RECIEVE S.P.A.D. NUMBER ###


### DISPLAY S.P.A.D. NUMBER IN LOGS ###
