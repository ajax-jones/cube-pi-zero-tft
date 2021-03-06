import sys
sys.path.append('/home/pi/cube-pi-zero-tft')
from st7735 import *
def nis(nisnum):
        nistext = "NIS " + str(nisnum)
        DrawRect(   97,35,  157,57,RED)
        DrawRect(   98,36,  156,56,RED)
        PutString2(102,40,nistext,WHITE)

def mb(mibnum):
        mbtext = "MB " + str(mibnum)
        DrawRect(   97,61,  157,83,YELLOW)
        DrawRect(   98,62,  156,82,YELLOW)
        PutString2(102,66,mbtext,WHITE)
def ok(oknum):
         oktext = "OK " + str(oknum)
         DrawRect(   97,87,  157,109,GREEN)
         DrawRect(   98,88,  156,108,GREEN)
         PutString2(102,92,oktext,WHITE)

def acc(accnum):
        acctext = "Acc "+str(accnum)
        DrawRect(17,99,77,121,BLUE)
        DrawRect(18,100,76,120,BLUE)
        PutString2(22,104,acctext,WHITE)

def views(x,y,viewnum,txtcolor):
        str_width=GetStringWidth(str(viewnum))
        str_height=5

        ch_height = font.fontInfo[0]
	ch_width  = GetCharWidth("M")

        viewtext = str(viewnum)

#        print(x,y,str_width,ch_height,	BLACK)
	x1 = x+str_width+2
	y1 = y+ch_height+2
        FillRect(x,y, 	x1,y1,	BLACK)

        DrawRect(x,y,x1,y1,BLUE)
        DrawRect(x+1,y+1,x1-1,y1-1,BLUE)

        PutString2(x+3,y+3,viewtext.strip(),txtcolor)





def daybar(startx, starty, height,width,nis,mb,ok):
        total = nis+mb+ok
        one_percent = float(height) / 100
        nis_per = int((float(nis)/float(total))*height)
        mb_per  = int((float( mb)/float(total))*height)
        ok_per  = int((float( ok)/float(total))*height)

        FillRect (startx,starty, startx+width, starty+nis_per,RED)
        FillRect (startx,starty+nis_per, startx+width, starty+nis_per+mb_per,YELLOW)
        FillRect (startx,starty+nis_per+mb_per, startx+width, starty+height,GREEN)
def cover(coverage):
        covertext = str(coverage)+"%"
        DrawRect(97,3,157,25,TEAL)
        DrawRect(98,4,156,24,TEAL)
        PutString2(102,8,covertext,WHITE)


def titlebox(site,kolor):
        FillRect(4,4,90,26,kolor)
        PutString2(6,6,site,YELLOW)
        HLine(4,90,23,YELLOW)
 

def m1(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-5,        bcolor)
        DrawPixel(x,y-4,        bcolor)
        DrawPixel(x,y-3,        bcolor)
        DrawPixel(x,y-2,        bcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      bcolor)
        DrawPixel(x+1,y-6,      fcolor)
        DrawPixel(x+1,y-5,      bcolor)
        DrawPixel(x+1,y-4,      bcolor)
        DrawPixel(x+1,y-3,      bcolor)
        DrawPixel(x+1,y-2,      bcolor)
        DrawPixel(x+1,y-1,      fcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      fcolor)
        DrawPixel(x+2,y-6,      fcolor)
        DrawPixel(x+2,y-5,      fcolor)
        DrawPixel(x+2,y-4,      fcolor)
        DrawPixel(x+2,y-3,      fcolor)
        DrawPixel(x+2,y-2,      fcolor)
        DrawPixel(x+2,y-1,      fcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      bcolor)
        DrawPixel(x+3,y-6,      bcolor)
        DrawPixel(x+3,y-5,      bcolor)
        DrawPixel(x+3,y-4,      bcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      bcolor)
        DrawPixel(x+3,y-1,      fcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      bcolor)
        DrawPixel(x+4,y-6,      bcolor)
        DrawPixel(x+4,y-5,      bcolor)
        DrawPixel(x+4,y-4,      bcolor)
        DrawPixel(x+4,y-3,      bcolor)
        DrawPixel(x+4,y-2,      bcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)


def m3(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        fcolor)
        DrawPixel(x,y-6,        bcolor)
        DrawPixel(x,y-5,        bcolor)
        DrawPixel(x,y-4,        bcolor)
        DrawPixel(x,y-3,        bcolor)
        DrawPixel(x,y-2,        fcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      fcolor)
        DrawPixel(x+1,y-6,      bcolor)
        DrawPixel(x+1,y-5,      bcolor)
        DrawPixel(x+1,y-4,      bcolor)
        DrawPixel(x+1,y-3,      bcolor)
        DrawPixel(x+1,y-2,      bcolor)
        DrawPixel(x+1,y-1,      fcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      fcolor)
        DrawPixel(x+2,y-6,      bcolor)
        DrawPixel(x+2,y-5,      fcolor)
        DrawPixel(x+2,y-4,      bcolor)
        DrawPixel(x+2,y-3,      bcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      fcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      fcolor)
        DrawPixel(x+3,y-6,      fcolor)
        DrawPixel(x+3,y-5,      bcolor)
        DrawPixel(x+3,y-4,      fcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      bcolor)
        DrawPixel(x+3,y-1,      fcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      fcolor)
        DrawPixel(x+4,y-6,      bcolor)
        DrawPixel(x+4,y-5,      bcolor)
        DrawPixel(x+4,y-4,      bcolor)
        DrawPixel(x+4,y-3,      fcolor)
        DrawPixel(x+4,y-2,      fcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)

def m2(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-6,        fcolor)
        DrawPixel(x,y-5,        bcolor)
        DrawPixel(x,y-4,        bcolor)
        DrawPixel(x,y-3,        bcolor)
        DrawPixel(x,y-2,        bcolor)
        DrawPixel(x,y-1,        fcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      fcolor)
        DrawPixel(x+1,y-6,      bcolor)
        DrawPixel(x+1,y-5,      bcolor)
        DrawPixel(x+1,y-4,      bcolor)
        DrawPixel(x+1,y-3,      bcolor)
        DrawPixel(x+1,y-2,      fcolor)
        DrawPixel(x+1,y-1,      fcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      fcolor)
        DrawPixel(x+2,y-6,      bcolor)
        DrawPixel(x+2,y-5,      bcolor)
        DrawPixel(x+2,y-4,      bcolor)
        DrawPixel(x+2,y-3,      fcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      fcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      fcolor)
        DrawPixel(x+3,y-6,      bcolor)
        DrawPixel(x+3,y-5,      bcolor)
        DrawPixel(x+3,y-4,      fcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      bcolor)
        DrawPixel(x+3,y-1,      fcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      bcolor)
        DrawPixel(x+4,y-6,      fcolor)
        DrawPixel(x+4,y-5,      fcolor)
        DrawPixel(x+4,y-4,      bcolor)
        DrawPixel(x+4,y-3,      bcolor)
        DrawPixel(x+4,y-2,      bcolor)
        DrawPixel(x+4,y-1,      fcolor)
        DrawPixel(x+4,y,        bcolor)

def m4(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-5,        bcolor)
        DrawPixel(x,y-4,        fcolor)
        DrawPixel(x,y-3,        fcolor)
        DrawPixel(x,y-2,        bcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      bcolor)
        DrawPixel(x+1,y-6,      bcolor)
        DrawPixel(x+1,y-5,      fcolor)
        DrawPixel(x+1,y-4,      bcolor)
        DrawPixel(x+1,y-3,      fcolor)
        DrawPixel(x+1,y-2,      bcolor)
        DrawPixel(x+1,y-1,      bcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      bcolor)
        DrawPixel(x+2,y-6,      fcolor)
        DrawPixel(x+2,y-5,      bcolor)
        DrawPixel(x+2,y-4,      bcolor)
        DrawPixel(x+2,y-3,      fcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      bcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      fcolor)
        DrawPixel(x+3,y-6,      fcolor)
        DrawPixel(x+3,y-5,      fcolor)
        DrawPixel(x+3,y-4,      fcolor)
        DrawPixel(x+3,y-3,      fcolor)
        DrawPixel(x+3,y-2,      fcolor)
        DrawPixel(x+3,y-1,      fcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      bcolor)
        DrawPixel(x+4,y-6,      bcolor)
        DrawPixel(x+4,y-5,      bcolor)
        DrawPixel(x+4,y-4,      bcolor)
        DrawPixel(x+4,y-3,      fcolor)
        DrawPixel(x+4,y-2,      bcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)

def m5(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        fcolor)
        DrawPixel(x,y-7,        fcolor)
        DrawPixel(x,y-5,        fcolor)
        DrawPixel(x,y-4,        bcolor)
        DrawPixel(x,y-3,        bcolor)
        DrawPixel(x,y-2,        fcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      fcolor)
        DrawPixel(x+1,y-6,      bcolor)
        DrawPixel(x+1,y-5,      fcolor)
        DrawPixel(x+1,y-4,      bcolor)
        DrawPixel(x+1,y-3,      bcolor)
        DrawPixel(x+1,y-2,      bcolor)
        DrawPixel(x+1,y-1,      fcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      fcolor)
        DrawPixel(x+2,y-6,      bcolor)
        DrawPixel(x+2,y-5,      fcolor)
        DrawPixel(x+2,y-4,      bcolor)
        DrawPixel(x+2,y-3,      bcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      fcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      fcolor)
        DrawPixel(x+3,y-6,      bcolor)
        DrawPixel(x+3,y-5,      fcolor)
        DrawPixel(x+3,y-4,      bcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      bcolor)
        DrawPixel(x+3,y-1,      fcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      fcolor)
        DrawPixel(x+4,y-6,      bcolor)
        DrawPixel(x+4,y-5,      bcolor)
        DrawPixel(x+4,y-4,      fcolor)
        DrawPixel(x+4,y-3,      fcolor)
        DrawPixel(x+4,y-2,      fcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)
def m6(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-5,        fcolor)
        DrawPixel(x,y-4,        fcolor)
        DrawPixel(x,y-3,        fcolor)
        DrawPixel(x,y-2,        fcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      bcolor)
        DrawPixel(x+1,y-6,      fcolor)
        DrawPixel(x+1,y-5,      bcolor)
        DrawPixel(x+1,y-4,      fcolor)
        DrawPixel(x+1,y-3,      bcolor)
        DrawPixel(x+1,y-2,      bcolor)
        DrawPixel(x+1,y-1,      fcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      fcolor)
        DrawPixel(x+2,y-6,      bcolor)
        DrawPixel(x+2,y-5,      bcolor)
        DrawPixel(x+2,y-4,      fcolor)
        DrawPixel(x+2,y-3,      bcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      fcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      fcolor)
        DrawPixel(x+3,y-6,      bcolor)
        DrawPixel(x+3,y-5,      bcolor)
        DrawPixel(x+3,y-4,      fcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      bcolor)
        DrawPixel(x+3,y-1,      fcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      bcolor)
        DrawPixel(x+4,y-6,      bcolor)
        DrawPixel(x+4,y-5,      bcolor)
        DrawPixel(x+4,y-4,      bcolor)
        DrawPixel(x+4,y-3,      fcolor)
        DrawPixel(x+4,y-2,      fcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)
def m7(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        fcolor)
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-5,        bcolor)
        DrawPixel(x,y-4,        bcolor)
        DrawPixel(x,y-3,        bcolor)
        DrawPixel(x,y-2,        bcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      fcolor)
        DrawPixel(x+1,y-6,      bcolor)
        DrawPixel(x+1,y-5,      bcolor)
        DrawPixel(x+1,y-4,      bcolor)
        DrawPixel(x+1,y-3,      fcolor)
        DrawPixel(x+1,y-2,      fcolor)
        DrawPixel(x+1,y-1,      fcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      fcolor)
        DrawPixel(x+2,y-6,      bcolor)
        DrawPixel(x+2,y-5,      bcolor)
        DrawPixel(x+2,y-4,      fcolor)
        DrawPixel(x+2,y-3,      bcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      bcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      fcolor)
        DrawPixel(x+3,y-6,      bcolor)
        DrawPixel(x+3,y-5,      fcolor)
        DrawPixel(x+3,y-4,      bcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      bcolor)
        DrawPixel(x+3,y-1,      bcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      fcolor)
        DrawPixel(x+4,y-6,      fcolor)
        DrawPixel(x+4,y-5,      bcolor)
        DrawPixel(x+4,y-4,      bcolor)
        DrawPixel(x+4,y-3,      bcolor)
        DrawPixel(x+4,y-2,      bcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)
def m8(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-7,        fcolor)
        DrawPixel(x,y-5,        fcolor)
        DrawPixel(x,y-4,        bcolor)
        DrawPixel(x,y-3,        fcolor)
        DrawPixel(x,y-2,        fcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      fcolor)
        DrawPixel(x+1,y-6,      bcolor)
        DrawPixel(x+1,y-5,      bcolor)
        DrawPixel(x+1,y-4,      fcolor)
        DrawPixel(x+1,y-3,      bcolor)
        DrawPixel(x+1,y-2,      bcolor)
        DrawPixel(x+1,y-1,      fcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      fcolor)
        DrawPixel(x+2,y-6,      bcolor)
        DrawPixel(x+2,y-5,      bcolor)
        DrawPixel(x+2,y-4,      fcolor)
        DrawPixel(x+2,y-3,      bcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      fcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      fcolor)
        DrawPixel(x+3,y-6,      bcolor)
        DrawPixel(x+3,y-5,      bcolor)
        DrawPixel(x+3,y-4,      fcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      bcolor)
        DrawPixel(x+3,y-1,      fcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      bcolor)
        DrawPixel(x+4,y-6,      fcolor)
        DrawPixel(x+4,y-5,      fcolor)
        DrawPixel(x+4,y-4,      bcolor)
        DrawPixel(x+4,y-3,      fcolor)
        DrawPixel(x+4,y-2,      fcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)
def m9(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-7,        fcolor)
        DrawPixel(x,y-5,        fcolor)
        DrawPixel(x,y-4,        bcolor)
        DrawPixel(x,y-3,        bcolor)
        DrawPixel(x,y-2,        bcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      fcolor)
        DrawPixel(x+1,y-6,      bcolor)
        DrawPixel(x+1,y-5,      bcolor)
        DrawPixel(x+1,y-4,      fcolor)
        DrawPixel(x+1,y-3,      bcolor)
        DrawPixel(x+1,y-2,      bcolor)
        DrawPixel(x+1,y-1,      fcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      fcolor)
        DrawPixel(x+2,y-6,      bcolor)
        DrawPixel(x+2,y-5,      bcolor)
        DrawPixel(x+2,y-4,      fcolor)
        DrawPixel(x+2,y-3,      bcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      fcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      fcolor)
        DrawPixel(x+3,y-6,      bcolor)
        DrawPixel(x+3,y-5,      bcolor)
        DrawPixel(x+3,y-4,      fcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      fcolor)
        DrawPixel(x+3,y-1,      bcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      bcolor)
        DrawPixel(x+4,y-6,      fcolor)
        DrawPixel(x+4,y-5,      fcolor)
        DrawPixel(x+4,y-4,      fcolor)
        DrawPixel(x+4,y-3,      fcolor)
        DrawPixel(x+4,y-2,      bcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)
def m0(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-7,        fcolor)
        DrawPixel(x,y-5,        fcolor)
        DrawPixel(x,y-4,        fcolor)
        DrawPixel(x,y-3,        fcolor)
        DrawPixel(x,y-2,        fcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      fcolor)
        DrawPixel(x+1,y-6,      bcolor)
        DrawPixel(x+1,y-5,      bcolor)
        DrawPixel(x+1,y-4,      bcolor)
        DrawPixel(x+1,y-3,      fcolor)
        DrawPixel(x+1,y-2,      bcolor)
        DrawPixel(x+1,y-1,      fcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      fcolor)
        DrawPixel(x+2,y-6,      bcolor)
        DrawPixel(x+2,y-5,      bcolor)
        DrawPixel(x+2,y-4,      fcolor)
        DrawPixel(x+2,y-3,      bcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      fcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      fcolor)
        DrawPixel(x+3,y-6,      bcolor)
        DrawPixel(x+3,y-5,      fcolor)
        DrawPixel(x+3,y-4,      bcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      bcolor)
        DrawPixel(x+3,y-1,      fcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      bcolor)
        DrawPixel(x+4,y-6,      fcolor)
        DrawPixel(x+4,y-5,      fcolor)
        DrawPixel(x+4,y-4,      fcolor)
        DrawPixel(x+4,y-3,      fcolor)
        DrawPixel(x+4,y-2,      fcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)

def mslash(x,y,fcolor,bcolor):
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-7,        bcolor)
        DrawPixel(x,y-5,        bcolor)
        DrawPixel(x,y-4,        bcolor)
        DrawPixel(x,y-3,        bcolor)
        DrawPixel(x,y-2,        fcolor)
        DrawPixel(x,y-1,        bcolor)
        DrawPixel(x,y,  bcolor)

        DrawPixel(x+1,y-7,      bcolor)
        DrawPixel(x+1,y-6,      bcolor)
        DrawPixel(x+1,y-5,      bcolor)
        DrawPixel(x+1,y-4,      bcolor)
        DrawPixel(x+1,y-3,      fcolor)
        DrawPixel(x+1,y-2,      bcolor)
        DrawPixel(x+1,y-1,      bcolor)
        DrawPixel(x+1,y,        bcolor)

        DrawPixel(x+2,y-7,      bcolor)
        DrawPixel(x+2,y-6,      bcolor)
        DrawPixel(x+2,y-5,      bcolor)
        DrawPixel(x+2,y-4,      fcolor)
        DrawPixel(x+2,y-3,      bcolor)
        DrawPixel(x+2,y-2,      bcolor)
        DrawPixel(x+2,y-1,      bcolor)
        DrawPixel(x+2,y,        bcolor)

        DrawPixel(x+3,y-7,      bcolor)
        DrawPixel(x+3,y-6,      bcolor)
        DrawPixel(x+3,y-5,      fcolor)
        DrawPixel(x+3,y-4,      bcolor)
        DrawPixel(x+3,y-3,      bcolor)
        DrawPixel(x+3,y-2,      bcolor)
        DrawPixel(x+3,y-1,      bcolor)
        DrawPixel(x+3,y,        bcolor)

        DrawPixel(x+4,y-7,      bcolor)
        DrawPixel(x+4,y-6,      fcolor)
        DrawPixel(x+4,y-5,      bcolor)
        DrawPixel(x+4,y-4,      bcolor)
        DrawPixel(x+4,y-3,      bcolor)
        DrawPixel(x+4,y-2,      bcolor)
        DrawPixel(x+4,y-1,      bcolor)
        DrawPixel(x+4,y,        bcolor)

def smallchar(charac,x,y,fcolor,bcolor):
        if (charac==1):
                m1(x,y,fcolor,bcolor)
        if (charac==2):
                m2(x,y,fcolor,bcolor)
        if (charac==3):
                m3(x,y,fcolor,bcolor)
        if (charac==4):
                m4(x,y,fcolor,bcolor)
        if (charac==5):
                m5(x,y,fcolor,bcolor)
        if (charac==6):
                m6(x,y,fcolor,bcolor)
        if (charac==7):
                m7(x,y,fcolor,bcolor)
        if (charac==8):
                m8(x,y,fcolor,bcolor)
        if (charac==9):
                m9(x,y,fcolor,bcolor)
        if (charac==0):
                m0(x,y,fcolor,bcolor)

