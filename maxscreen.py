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
sys.path.append('/home/pi/web')

from st7735 import *
import MySQLdb

########################################################################
#
# Main Program
#
import math
from cubefunc import *

print "Adafruit 1.8 TFT max screeb "
#SetOrientation(180) #upside-down
#ClearScreen()
SetOrientation(90) #upside-down
#ColorBars()
ClearScreen()

try:
        while (not DEBUG):
                db = MySQLdb.connect(host="localhost", user="root",passwd="navalpower55", db="signal")
                cur = db.cursor()
                #       InfoTest()

#                PPCMarkets = ['UK_Sports','Italy','Italy_Sports','Portugal','Romania','Spain','Spain_Sports','UK','UK_Casino','Ireland','Greece','Belgium','Bulgaria','Czech','Denmark','France','France_Sports','Full_Tilt_UK']
                PPCMarkets = ['France','Spain','UK','UK_Sports','Portugal','Romania','Czech','Greece','Spain_Sports','Belgium','Denmark','Bulgaria']
                for Country in PPCMarkets:
                        sql = "SELECT realdate,country,na,ok,mb,nis, ROUND((((ok)*100.0)/na),1) as coverage FROM signalsfeedtotal where country = '{0}' order by realdate desc limit 5".format(Country)
#                        print (sql)
                        # Execute the SQL command
                        cur.execute(sql)
                        rowcount = 1
                        for row in cur.fetchall():
                                #print "row=",rowcount, " date=",row[0]," ",row[1], " NA=" ,row[2]," NIS=",row[5]," MB=",row[4]," OK=",row[3], " coverage=" , row[6],"%"
                                #theday  = thedate[-2:]
                                tt = "New Accounts {}".format(row[2])
                                NIS = row[5]
                                OK  = row[3]
                                MB  = row[4]
                                CV  = row[6]

                                if (rowcount == 5):
                                        daybar( 4,40,50,15,  NIS, MB,OK)
                                if (rowcount == 4):
                                        daybar(21,40,50,15,  NIS, MB,OK)
                                if (rowcount == 3):
                                        daybar(38,40,50,15,  NIS,MB,OK)
                                if (rowcount == 2):
                                        daybar(55,40,50,15,  NIS,MB,OK)
                                if (rowcount == 1):
                                        daybar(72,40,50,15,  NIS,MB,OK)
                                        thedate=str(row[0])
                                        theday=thedate[6:8]
                                        theday1=int(thedate[6:7])
                                        theday2=int(thedate[7:8])

                                        themonth=thedate[4:6]
                                        themonth1=int(thedate[4:5])
                                        themonth2=int(thedate[5:6])

#                                       print(" DATE ",theday1,theday2,"/",themonth1,themonth2)

                                        ss = "{}".format(Country)
                                        stitle=ss[0:8]
                                        uu = "{}".format(OK)
                                        vv = "{}".format(NIS)
                                        ww = "{}".format(MB)
                                        xx = "{}%".format(CV)
                                        cover(CV)
                                        if (CV < 50 ):
                                                DrawRect(0,0,159,127,RED)
                                                titlebox(stitle,RED)
                                        elif (CV > 70):
                                                DrawRect(0,0,159,127,BLUE)
                                                titlebox(stitle,BLUE)
                                        else:
                                                DrawRect(0,0,159,127,MAROON)
                                                titlebox(stitle,MAROON)


#                                       five()
#                                       four()
                                        nis(vv)
                                        mb(ww)
                                        ok(uu)
                                        accounts = NIS+OK+MB
                                        acc(accounts)
#                               DrawPixel(90,40,YELLOW)
#                               DrawPixel(91,41,YELLOW)
#                               DrawPixel(92,42,YELLOW)
#                               DrawPixel(93,43,TEAL)


#                               Circle(30,30,10,YELLOW)
#                               FillCircle(118,117,5,GREEN)

                                DSX = 97
                                DSY = 121
                                DrawRect(DSX,DSY-11,DSY+10,DSY+2,RED)
                                smallchar(theday1,DSX+3,DSY,GREEN,BLACK)
                                smallchar(theday2,DSX+9,DSY,GREEN,BLACK)
                                mslash(DSX+15,DSY,GREEN,BLACK)
                                smallchar(themonth1,DSX+21,DSY,GREEN,BLACK)
                                smallchar(themonth2,DSX+27,DSY,GREEN,BLACK)


#                               FillCircle(130,117,5,GREEN)
                                FillCircle(142,117,5,GREEN)
#                               Line(30,30,80,80,BLUE)
                                rowcount+=1

                        time.sleep(20)
                        ClearScreen()


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
