#!/usr/bin/python
########################################################################
# A Python script for controlling the Adafruit 1.8" TFT LCD module based on the work by 
# Author : Bruce E. Hall, W8BH <bhall66@gmail.com>
# Date : 25 Feb 2014
# For more information, see w8bh.net
########################################################################
import sys
import math
import time
import datetime as dt

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


		clockCentreX = 32
		clockCentreY = 65
		clockradius  = 30
		clockhr	     = clockradius-10
		clockmin     = clockradius-5
                FillCircle(clockCentreX,clockCentreY,clockradius,WHITE)
                FillCircle(clockCentreX,clockCentreY,clockradius-2,MFB4)
                FillCircle(clockCentreX,clockCentreY,clockradius-4,BLACK)


  		for z in range(0,360,30):
  			#Begin at 0 and stop at 360
    			angle = z 
    			angle=(angle/57.29577951) 		#Convert degrees to radians
    			x2=int((clockCentreX+(math.sin(angle)*clockradius)))
    			y2=int((clockCentreY-(math.cos(angle)*clockradius)))
    			x3=int((clockCentreX+(math.sin(angle)*(clockradius-5))))
    			y3=int((clockCentreY-(math.cos(angle)*(clockradius-5))))
			Line(x2,y2,x3,y3,WHITE)
			Line(x3,y3,x2,y2,WHITE)


		htime =  dt.datetime.now().hour
		mtime =  dt.datetime.now().minute
		# Hour Hand
		angle = htime  * 30 + int((mtime / 12) * 6 )
		angle=(angle/57.29577951) # Convert degrees to radians  
  		x3=int((clockCentreX+(math.sin(angle)*(clockhr))))
  		y3=int((clockCentreY-(math.cos(angle)*(clockhr))))
  		Line(clockCentreX,clockCentreY,x3,y3,WHITE)

		# Minute Hand
		angle = mtime * 6
  		angle=(angle/57.29577951) # Convert degrees to radians  
  		x3=int((clockCentreX+(math.sin(angle)*(clockmin))))
  		y3=int((clockCentreY-(math.cos(angle)*(clockmin))))
  		Line(clockCentreX,clockCentreY,x3,y3,WHITE)
  		Line(x3,y3,clockCentreX,clockCentreY,WHITE)
#  		print(clockCentreX,clockCentreY,x3,y3,WHITE)

#		FillRect (18,100,76,120,BLACK)
		instruct = Run("cat instruct.csv")
		views(70,8,"Instr",WHITE)
		views(72,32,instruct,WHITE)

		views(70,60,"Thing",WHITE)
		views(72,84,822,WHITE)

		DemiCircle(95,130,20,MFB1)
		Circle(95,130,21,MFB2)
		Circle(95,130,22,MFB2)
		Circle(95,130,23,MFB2)



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
