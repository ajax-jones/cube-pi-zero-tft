#!/usr/bin/python
########################################################################
#
# A Python script for controlling the Adafruit 1.8" TFT LCD module based on the work by 
# Author : Bruce E. Hall, W8BH <bhall66@gmail.com>
# Date : 25 Feb 2014
# For more information, see w8bh.net
########################################################################
import sys
# the mock-0.3.1 dir contains testcase.py, testutils.py & mock.py
sys.path.append('/home/pi/cube-pi-zero-tft')

from st7735 import *
import MySQLdb

## color palette for the stats screens
MFB1            = 0x0D3A
MFB2            = 0x0435
MFB3            = 0x0CD8
MFB4            = 0x026C
MFW1            = 0xFFFF


########################################################################
#
# Main Program
#
import math
from cubefunc import *

print "Maker stats "
#SetOrientation(180) #upside-down
#ClearScreen()
SetOrientation(0) #upside-down
#ColorBars()
ClearScreen()
#SetPin(LED,0)

try:
        while (not DEBUG):

		FillRect ( 4,  4,  64,157,MFB1)

		FillRect (65,  4,  123, 29,MFB2)
		FillRect (65,  30, 123, 54,MFB3)

		FillRect (65,  55,  123, 79,MFB2)
		FillRect (65,  80, 123, 104,MFB3)

		FillRect (65,  105, 123, 155,MFB4)

		DrawRect(0,0,127 ,159,WHITE)
		DrawRect(1,1,126 ,158,WHITE)
		DrawRect(2,2,125 ,157,WHITE)
		DrawRect(3,3,124 ,156,WHITE)


                FillCircle(52,65,25,WHITE)
                FillCircle(52,65,23,RED)
                FillCircle(52,65,20,BLACK)
		FillRect (18,100,76,120,BLACK)
		instruct = Run("cat instruct.csv")
		acc(instruct)

                time.sleep(12)


        GPIO.cleanup()  # clean exit
        spi.close() #close down SPI interface
        print "Done."
except KeyboardInterrupt:
        GPIO.cleanup()  # clean exit
        spi.close() #close down SPI interface
        print "keyboard close"

#except:#
#       GPIO.cleanup()  # clean exit
#       spi.close() #close down SPI interface
#       print "some other error happened here"

finally:
        GPIO.cleanup()  # clean exit
        spi.close() #close down SPI interface

# END ###############################################################
