
import colorsys
import time
from blinkt import *#set_brightness, set_pixel, show, clear

spacing = 360.0 / 16.0
hue = 0
set_brightness(0.05)
def level1():
        set_pixel(0,0,255,0)
def level2():
        set_pixel(0,0,255,0)
        set_pixel(1,0,255,0)
def level3():
        set_pixel(0,0,255,0)
        set_pixel(1,0,255,0)
        set_pixel(2,0,255,0)
def level4():
        set_pixel(0,0,255,0)
        set_pixel(1,0,255,0)
        set_pixel(2,0,255,0)
        set_pixel(3,0,255,0)
def level5():
        set_pixel(0,0,255,0)
        set_pixel(1,0,255,0)
        set_pixel(2,0,255,0)
        set_pixel(3,0,255,0)
        set_pixel(4,255,150,0)
def level6():
        set_pixel(0,0,255,0)
        set_pixel(1,0,255,0)
        set_pixel(2,0,255,0)
        set_pixel(3,0,255,0)
        set_pixel(4,255,150,0)
        set_pixel(5,255,150,0)
def level7():
        set_pixel(0,0,255,0)
        set_pixel(1,0,255,0)
        set_pixel(2,0,255,0)
        set_pixel(3,0,255,0)
        set_pixel(4,255,150,0)
        set_pixel(5,255,150,0)
        set_pixel(6,255,150,0)
def level8():
        set_pixel(0,0,255,0)
        set_pixel(1,0,255,0)
        set_pixel(2,0,255,0)
        set_pixel(3,0,255,0)
        set_pixel(4,255,150,0)
        set_pixel(5,255,150,0)
        set_pixel(6,255,150,0)
        set_pixel(7,255,0,0)

while True:
	clear()
	file = 'speedump.txt'
	data_file = open(file)
	file_data = data_file.read()
	data_file.close()
	if len(file_data)>0:
		speed = float(file_data)
		print speed
	
		traffic = speed
		if traffic >= 0 and traffic  < 50:
			level1()
		elif traffic > 50 and traffic < 100 :
        		level2()
		elif traffic > 100 and traffic < 200:
        		level3()
		elif traffic > 200 and traffic < 350:
        		level4()
		elif traffic > 350 and traffic < 700:
        		level5()
		elif traffic > 700 and traffic < 1500:
        		level6()
		elif traffic > 1500 and traffic < 3000:
        		level7()
		elif traffic > 3000:
        		level8()
		show()
        time.sleep(1)
