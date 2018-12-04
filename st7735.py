#!/usr/bin/python
##
import sys
sys.path.append('/home/pi/web')

#import cooper14 as font
import monotxt12 as font
#import gothic as font
#import four as font0
#import small8 as font
#import small12 as font
#import font as font0
#import mono14 as font
#import font5x7 as font0

import RPi.GPIO as GPIO
import time
import os #for popen
import socket
import fcntl
import struct
import spidev #hardware SPI
from random import randint
from math import sqrt

#TFT to RPi connections
# PIN TFT RPi
# 1 backlight 3v3
# 2 MISO <none>
# 3 CLK SCLK (GPIO 11)
# 4 MOSI MOSI (GPIO 10)
# 5 CS-TFT GND
# 6 CS-CARD <none>
# 7 D/C GPIO 25
# 8 RESET <none>
# 9 VCC 3V3
# 10 GND GND
DC = 25
RST = 18
DEBUG = False

XSIZE = 128
YSIZE = 160
XMAX = XSIZE-1
YMAX = YSIZE-1
X0 = XSIZE/2
Y0 = YSIZE/2
#Color constants
BLACK = 0x0000
BLUE = 0x001F
RED = 0xF800
GREEN = 0x0400
LIME = 0x07E0
CYAN = 0x07FF
MAGENTA = 0xF81F
YELLOW = 0xFFE0
WHITE = 0xFFFF
PURPLE = 0x8010
NAVY = 0x0010
TEAL = 0x0410
OLIVE = 0x8400
MAROON = 0x8000
SILVER = 0xC618
GRAY = 0x8410
bColor = BLACK
fColor = YELLOW
COLORSET = [BLACK,BLUE,RED,GREEN,LIME,CYAN,MAGENTA,YELLOW, WHITE,PURPLE,NAVY,TEAL,OLIVE,MAROON,SILVER,GRAY]

#TFT display constants
SWRESET = 0x01
SLPIN = 0x10
SLPOUT = 0x11
PTLON = 0x12
NORON = 0x13
INVOFF = 0x20
INVON = 0x21
DISPOFF = 0x28
DISPON = 0x29
CASET = 0x2A
RASET = 0x2B
RAMWR = 0x2C
RAMRD = 0x2E
PTLAR = 0x30
COLMOD = 0x3A

#MADCTL = 0xC0
MADCTL = 0x36

MADCTL_MY  = 0x80
MADCTL_MX  = 0x40
MADCTL_MV  = 0x20
MADCTL_ML  = 0x10
MADCTL_RGB = 0x00
MADCTL_BGR = 0x08
MADCTL_MH  = 0x04

########################################################################
#
# Low-level routines
#
#
def SetPin(pinNumber,value):
 #sets the GPIO pin to desired value (1=on,0=off)
 GPIO.output(pinNumber,value)

def InitGPIO():
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(DC,GPIO.OUT)
 GPIO.setup(RST,GPIO.OUT)
 SetPin(RST,1)

def InitSPI():
        spiObject = spidev.SpiDev()
        spiObject.open(0,0)
        spiObject.mode = 0
        return spiObject
########################################################################
#
# ST7735 TFT controller routines:
#
#
def WriteByte(value):   #"sends an 8-bit value to the display as data"
        SetPin(DC,1)
        spi.writebytes([value])
def WriteWord (value):#"sends a 16-bit value to the display as data"
        SetPin(DC,1)
        spi.writebytes([value>>8, value&0xFF])
def Command(cmd, *bytes):
        SetPin(DC,0) #command follows
        spi.writebytes([cmd]) #send the command byte
        if len(bytes)>0: #is there data to follow command?
                SetPin(DC,1) #data follows
                spi.writebytes(list(bytes)) #send the data bytes
def InitDisplay():
        Command (SWRESET) #reset TFT controller
        time.sleep(0.2) #wait 200mS for controller init
        Command (SLPOUT) #wake from sleep
        Command (COLMOD, 0x05) #set color mode to 16 bit
        Command (DISPON) #turn on display

def SetOrientation(degrees):
        if degrees==90: arg=0x60
        elif degrees==180: arg=0xC0
        elif degrees==270: arg=0xA0
        else: arg=0x00
        #print ("MADCTL="),
        #print MADCTL
        #print ("arg="),
        #print arg

#       arg1 = MADCTL_MX | MADCTL_MY | MADCTL_RGB
#       arg2 = MADCTL_MY | MADCTL_MV | MADCTL_RGB
#       arg3 = MADCTL_RGB
#       arg4 = MADCTL_MX | MADCTL_MV | MADCTL_RGB

#       print ("arg="),#        print arg1,
#       print arg2,#    print arg3,#    print arg4,

        Command (MADCTL,arg)


def SetAddrWindow(x0,y0,x1,y1):
        Command (CASET,0,x0,0,x1) #set column range (x0,x1)
        Command (RASET,0,y0,0,y1) #set row range (y0,y1)
def WriteBulk (value,reps,count=1):
        SetPin(DC,0) #command follows
        spi.writebytes([RAMWR]) #issue RAM write command
        SetPin(DC,1) #data follows
        valHi = value >> 8 #separate color into two bytes
        valLo = value & 0xFF
        byteArray = [valHi,valLo]*reps #create buffer of multiple pixels
        for a in range(count):
                spi.writebytes(byteArray) #send this buffer multiple times
def WritePixels (byteArray):
        SetPin(DC,0) #command follows
        spi.writebytes([RAMWR]) #issue RAM write command
        SetPin(DC,1) #data follows
        spi.writebytes(byteArray) #send data to the TFT
########################################################################
#
# Graphics routines:
#
#
def DrawPixel(x,y,color):               # "draws a pixel on the TFT display"
        SetAddrWindow(x,y,x,y)                  #set display window to x,y
        Command (RAMWR, color>>8, color&0xFF)   #send pixel color (2 bytes)

def FastDrawPixel(x,y,color):           #"draws a pixel on the TFT display; increases speed by inlining"
        GPIO.output(DC,0)
        spi.writebytes([CASET])
        GPIO.output(DC,1)
        spi.writebytes([0,x,0,x])
        GPIO.output(DC,0)
        spi.writebytes([RASET])
        GPIO.output(DC,1)
        spi.writebytes([0,y,0,y])
        GPIO.output(DC,0)
        spi.writebytes([RAMWR])
        GPIO.output(DC,1)
        spi.writebytes([color>>8, color&0xFF])

def FillRect(x0,y0,x1,y1,color):
        width = x1-x0+1
        height = y1-y0+1
        SetAddrWindow(x0,y0,x1,y1)
        WriteBulk(color,width,height)
def FillScreen(color):
        FillRect(0,0,YMAX,XMAX,color)
        FillRect(0,0,XMAX,YMAX,color)
def ClearScreen():
        FillScreen(BLACK)
def HLine (x0,x1,y,color):      # "draws a horizontal line in given color"
        width = x1-x0+1
        SetAddrWindow(x0,y,x1,y)
        WriteBulk(color,width)

def VLine (x,y0,y1,color):      #  "draws a verticle line in given color"
        height = y1-y0+1
        SetAddrWindow(x,y0,x,y1)
        WriteBulk(color,height)


def Line (x0,y0,x1,y1,color):   #"draws a line in given color"
        if (x0==x1):
                VLine(x0,y0,y1,color)
        elif (y0==y1):
                HLine(x0,x1,y0,color)
        else:
                slope = float(y1-y0)/(x1-x0)
                if (abs(slope)< 1):
                        for x in range(x0,x1+1):
                                y = (x-x0)*slope + y0
                                FastDrawPixel(x,int(y+0.5),color)
                else:
                        for y in range(y0,y1+1):
                                x = (y-y0)/slope + x0
                                FastDrawPixel(int(x+0.5),y,color)

def DrawRect(x0,y0,x1,y1,color):        # "Draws a rectangle in specified color"
        HLine(x0,x1,y0,color)
        HLine(x0,x1,y1,color)
        VLine(x0,y0,y1,color)
        VLine(x1,y0,y1,color)

def Circle(xPos,yPos,radius,color):     #"draws circle at x,y with given radius & color"
        xEnd = int(0.7071*radius)+1
        for x in range(xEnd):
                y = int(sqrt(radius*radius - x*x))
                FastDrawPixel(xPos+x,yPos+y,color)
                FastDrawPixel(xPos+x,yPos-y,color)
                FastDrawPixel(xPos-x,yPos+y,color)
                FastDrawPixel(xPos-x,yPos-y,color)
                FastDrawPixel(xPos+y,yPos+x,color)
                FastDrawPixel(xPos+y,yPos-x,color)
                FastDrawPixel(xPos-y,yPos+x,color)
                FastDrawPixel(xPos-y,yPos-x,color)

def FillCircle(xPos,yPos,radius,color): #"draws filled circle at x,y with given radius & color"
        r2 = radius * radius
        for x in range(radius):
                y = int(sqrt(r2-x*x))
                y0 = yPos-y
                y1 = yPos+y
                VLine(xPos+x,y0,y1,color)
                VLine(xPos-x,y0,y1,color)

########################################################################
#
# Text routines:
#
#
def GetCharData (ch):
        pIndex = ord(ch)-ord(' ')
        lastDescriptor = len(font.descriptor)-1
        charIndex = font.descriptor[pIndex][1]
        if (DEBUG):
                print "\r\nGET CHARDATA\r\nch",
                print ch,
                print " pindex",
                print pIndex,
                print " lastdescriptor",
                print lastDescriptor,
                print " charindex",
                print charIndex,
        if (pIndex >= lastDescriptor):
                return font.rasterData[charIndex:]
                #return font.bitmaps[charIndex:]
        else:
                nextIndex = font.descriptor[pIndex+1][1]
                if (DEBUG):
                        print (" nextIndex="),
                        print nextIndex
                return font.rasterData[charIndex:nextIndex]
                #return font.bitmaps[charIndex:nextIndex]

def GetCharWidth(ch):
        pIndex = ord(ch)-ord(' ')
        return font.descriptor[pIndex][0]
def GetCharHeight(ch):
        return font.fontInfo[0]

def GetStringWidth(st):
        width = 0
        for ch in st:
                width += GetCharWidth(ch) + 1
        return width
def PutCh (ch,xPos,yPos,color=fColor):
        #charData = font0.data[ord(ch)-32]
        charData = GetCharData(ch)
        SetAddrWindow(xPos,yPos,xPos+4,yPos+6)
        SetPin(DC,0)
        spi.writebytes([RAMWR])
        SetPin(DC,1)
        buf = []
        mask = 0x01
        for row in range(7):
                for col in range(5):
                        bit = charData[col] & mask
                        if (bit==0):
                                pixel = bColor
                        else:
                                pixel = color
                        buf.append(pixel>>8)
                        buf.append(pixel&0xFF)
                mask <<= 1
        spi.writebytes(buf)
def PutCharV2 (ch,xPos,yPos,color=fColor):
        charData = GetCharData(ch)
        xLen = GetCharWidth(ch)
        numRows = GetCharHeight(ch)
        #numRows = 19
        bytesPerRow = 1+((xLen-1)/8)
        numBytes = numRows*bytesPerRow
        if (DEBUG):
                print ("-----------------------------------------------\r\nPCV__Chardata="),
                print charData,
                print ("ch="),
                print ch,
                print (" Xlen="),
                print xLen,
                print " numrows=",
                print numRows,
                print " numbytes=",
                print numBytes

        SetAddrWindow(xPos,yPos,xPos+xLen-1,yPos+numRows-1)
        SetPin(DC,0)
        spi.writebytes([RAMWR])
        SetPin(DC,1)
        i= 0
        while (i< numBytes):
                mask = 0x01
                rowBits = 0
                for b in range(bytesPerRow):
                        rowBits <<= 8
                        mask <<= 8
                        rowBits += charData[i]
                        i += 1
                mask >>= 1
                rowBuf = []
                for a in range(xLen):
                        bit = rowBits & mask
                        mask >>= 1
                        if (bit==0):
                                pixel = bColor
                        else:
                                pixel = color
                        rowBuf.append(pixel>>8)
                        rowBuf.append(pixel&0xFF)
                spi.writebytes(rowBuf)

def PutChar (ch,xPos,yPos,color=fColor):
        charData = GetCharData(ch)

        xLen = GetCharWidth(ch) #char width, in pixels
        numRows = GetCharHeight(ch)

        #numRows = 19
        bytesPerRow = 1+((xLen-1)/8) #char width, in bytes
        numBytes = numRows*bytesPerRow
        SetAddrWindow(xPos,yPos,xPos+xLen-1,yPos+numRows-1)
        if (DEBUG):
                print ("XY="),
                print xPos,
                print " ",
                print yPos,
                print (" Chardata="),
                print charData,
                print (" Xlen="),
                print xLen,
                print " numrows=",
                print numRows,
                print " numbytes=",
                print numBytes

        SetPin(DC,0)
        spi.writebytes([RAMWR]) #pixel data to follow
        SetPin(DC,1)
        index = 0
        buf = []
        for a in range(numRows): #row major
                bitNum = 0
                for b in range(bytesPerRow): #do whole row
                        mask = 0x80 #msb first
                        for c in range(8): #do all bits in this byte
                                if (bitNum<xLen): #still within char width?
                                        bit = charData[index] & mask
                                        if (bit==0): #check the bit
                                                pixel = bColor #0: background color
                                        else:
                                                pixel = color #1: foreground color
                                        buf.append(pixel>>8) #add pixel to buffer
                                        buf.append(pixel&0xFF)
                                        mask >>= 1 #goto next bit in byte
                                bitNum += 1 #goto next bit in row
                        index += 1 #goto next byte of data
                spi.writebytes(buf) #send char data to TFT

def PutString(xPos,yPos,st,color=fColor):
        for ch in st:
                if (DEBUG):
                        print ch,
                width = GetCharWidth(ch)+1
                PutCh(ch,xPos,yPos,color)
                xPos += width

def PutString2(xPos,yPos,st,color=fColor):
        for ch in st:
                if (DEBUG):
                        print ch,
                width = GetCharWidth(ch)+1
                PutCharV2(ch,xPos,yPos,color)
                xPos += width

########################################################################
#
# Testing routines:
#
#

# This function allows us to grab any of our IP addresses
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def PrintElapsedTime(function,startTime):
        elapsedTime=time.time()-startTime
        print "%15s: %8.3f seconds" % (function,elapsedTime)
        time.sleep(1)
def ColorBars():
        for a in range(8):
                FillRect(0,a*20,XMAX,a*20+19,COLORSET[a+1])
def ScreenTest():
        startTime=time.time()
        FillScreen(LIME)
        FillScreen(MAGENTA)
        ColorBars()
        PrintElapsedTime('ScreenTest',startTime)

def PortaitChars():
#font is 5x7 with 1 pixel spacing
        CHARS_PER_ROW = 21
        FillRect(0,0,XMAX,YMAX,bColor) #clear screen
        for i in range(120):
                x= i % CHARS_PER_ROW
                y= i / CHARS_PER_ROW
                ascii = (i % 21)+32
                PutCharV2(chr(ascii),x*6,y*8)
        time.sleep(1)

def LandscapeChars():
        CHARS_PER_ROW = 26
        FillRect(0,0,YMAX,XMAX,bColor) #clear screen
        for i in range(122):
                x= i % CHARS_PER_ROW
                y= i / CHARS_PER_ROW
                ascii = (i % 12)+32
                PutCharV2(chr(ascii),x*6,y*8,CYAN)
        time.sleep(1)
def LargeFontTest():
        title = 'Large Font'
        startTime = time.time()
        for i in range(90):
                x= i % 10
                y= i / 10
                ascii = (i % 96)+32

                PutCharV2(chr(ascii),x*12,y*18,LIME)
        PrintElapsedTime(title,startTime)
def RandColor():
        index = randint(0,len(COLORSET)-1)
        return COLORSET[index]
def SmallFontTest():
        title = 'Small Font'
        startTime = time.time()
        for i in range(2000):
                x= randint(0,20)
                y= randint(0,19)
                color = RandColor()
                ascii = (i % 96)+32
                PutCh(chr(ascii),x*6,y*8,color)
        PrintElapsedTime(title,startTime)
def OrientationTest():
        title = 'Orientation'
        startTime = time.time()
        PortaitChars()
        SetOrientation(90) #display-top on right
        LandscapeChars()
        SetOrientation(180) #upside-down
        PortaitChars()
        SetOrientation(270) #display-top on left
        LandscapeChars()
        SetOrientation(0) #return to 0 deg.
        PrintElapsedTime(title,startTime)

def GetTempCPU():
        tPath = '/sys/class/thermal/thermal_zone0/temp'
        tFile = open(tPath)
        temp = tFile.read()
        tFile.close()
        #return (float(temp)*0.0018 + 32)
        return (float(temp)/1000)
def Run(cmd):
        return os.popen(cmd).read()
def GetIPAddr():
        cmd = "ifconfig | awk '/192/ {print $2}'"
        res = Run(cmd).replace('\n','') #remove end of line char
        return res.replace('addr:','') #remove addr: prefix

def InfoTest():
        title = 'Info'
        startTime = time.time()
        PutString2(5,0,'IP addr',WHITE)
        try:
                n_TEXT = get_ip_address('wlan0') # WiFi address of WiFi$
        except IOError:
                try:
                        n_TEXT = get_ip_address('eth0') # WiFi address $
                except IOError:
                        n_TEXT = ('NO INTERNET!')

        PutString2(5,100,GetIPAddr())
        PutString2(5,20,n_TEXT)
        PutString2(5,60,'CPU temp',WHITE)
        temp = GetTempCPU()
        PutString2(5,80,'{:5.1f} deg F'.format(temp))
        tStr = time.strftime("%I:%M:%S ")
        PutString2(5,120,'Time',WHITE)
        PutString2(5,140,tStr)
        PrintElapsedTime(title,startTime)
def RunTextTests():
        startTime = time.time() #keep track of test duration
        ScreenTest()
        LargeFontTest()
        SmallFontTest()
        OrientationTest()

        FillScreen(RED)
        FillScreen(GREEN)
        FillScreen(BLUE)
        FillScreen(WHITE)

        ClearScreen()
        InfoTest()
        PrintElapsedTime('Full Suite',startTime)


InitGPIO() #initialize GPIO interface
time.sleep(.15)
spi = InitSPI() #initialize SPI interface
time.sleep(.15)
InitDisplay() #initialize TFT controller
time.sleep(.15)
ClearScreen()
