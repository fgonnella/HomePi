#!/usr/bin/python
import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi software SPI config:
SCLK = 17
DIN = 18
DC = 27
CS = 22
RST = 23
# Software SPI usage (defaults to bit-bang SPI interface):
disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white filled box to clear the image.

# Draw some shapes.
#draw.ellipse((2,2,22,22), outline=0, fill=255)
#draw.rectangle((24,2,44,22), outline=0, fill=255)
#draw.polygon([(46,22), (56,2), (66,22)], outline=0, fill=255)
#draw.line((68,22,81,2), fill=0)
#draw.line((68,2,81,22), fill=0)

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

while True:
        file = open("lcd.txt", "r")
        lines=file.readlines()
        file.close()
        #Clear screen
        draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
        for i in range(0, len(lines)):
#                print lines[i]
                draw.text((0,(i-1)*8+6), lines[i], font=font)
        # Display image.
        disp.image(image)
        disp.display()
        #sleep
        time.sleep(0.5)
