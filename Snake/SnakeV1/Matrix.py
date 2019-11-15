#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import copy
LSBFIRST = 1
MSBFIRST = 2
#define the pins connect to 74HC595
dataPin   = 11      #DS Pin of 74HC595(Pin14)
latchPin  = 13      #ST_CP Pin of 74HC595(Pin12)
clockPin = 15       #SH_CP Pin of 74HC595(Pin11)

def setup():
    GPIO.setmode(GPIO.BOARD)    # Number GPIOs by its physical location
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)

def shiftOut(dPin,cPin,order,val):
    for i in range(0,8):
        GPIO.output(cPin,GPIO.LOW);
        if(order == LSBFIRST):
            GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin,(0x80&(val<<i)==0x80) and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin,GPIO.HIGH);

def destroy():
    GPIO.cleanup()

def getBlank():
	return ["00000000","00000000","00000000","00000000","00000000","00000000","00000000","00000000"]

#display=[
#	"00000000",
#	"00000000",
#	"00010000",
#	"00101000",
#	"00010100",
#	"00001010",
#	"00000100",
#	"00000000"]

#z = getBlank()
#print(display,"\n",z)

def conv(data): # use binary display, converts to non binary (to numbers)
	for i in range(0,len(data)):
		#print(data[i])
		if type(data[i]) is str:
			data[i] = int(data[i],2)
			#print("=",data[i])
	return data

def setPixel(data,x,y,bit): # use binary display
	s=list(data[y-1])
	#print("before",s)
	s[x-1]=str(bit)
	#print("after ",s)
	data[y-1] = "".join(s)
	return data
	
def getPixel(data,x,y): # use binary display
	s=list(data[y-1])
	bit=s[x-1]
	return bit


def setArea(data,x,y,width,height): # use binary display
	pass # not finished and maybe not needed

def emptyPixels(data): # use binary display
	emptyList=[]
	for y in range(0,len(data)):
		for x in range(0,len(data[y])):
			if getPixel(data,x,y) == "0":
				emptyList+=[[x+1,y+1]]
	return emptyList

def getPixels(data):
	pixelList=[]
	for y in range(0,len(data)):
		for x in range(0,len(data[y])):
			pixelList+=[[x+1,y+1]]
	return pixelList

#display = setPixel(display,5,5,0)
#data = conv(display)



def screen(data,duration): # don't use binary, use the converted display
	for k in range(0,duration):
		x=0x80
		#print("start")
		for i in range(8-1,0-1,-1):
			#print(data[i])
			GPIO.output(latchPin,GPIO.LOW)
			shiftOut(dataPin,clockPin,MSBFIRST,data[i])
			shiftOut(dataPin,clockPin,MSBFIRST,~x)
			GPIO.output(latchPin,GPIO.HIGH)
			time.sleep(0.001)
			x>>=1

def screenShort(data): # don't use binary, use the converted display
	x=0x80
	for i in range(8-1,0-1,-1):
		#print(data[i])
		GPIO.output(latchPin,GPIO.LOW)
		shiftOut(dataPin,clockPin,MSBFIRST,data[i])
		shiftOut(dataPin,clockPin,MSBFIRST,~x)
		GPIO.output(latchPin,GPIO.HIGH)
		#time.sleep(0.001)
		x>>=1
