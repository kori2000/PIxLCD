import RPi.GPIO as GPIO ## Import GPIO library
import time             ## Import 'time' library. Allows us to use 'sleep'

########################################################################
# Main Program
print("LCD program : Importing PIN Input")

GPIO.setwarnings(False)  ## Ignore warnings
GPIO.setmode(GPIO.BCM)   ## Use board pin numbering

# HD44780 Controller Commands
CLEARDISPLAY = 0x01
SETCURSOR    = 0x80

# Output LCD Pin Config
LCD_RS = 7   # GPIO7  = Pi pin 26
LCD_E = 8    # GPIO8  = Pi pin 24
LCD_D4 = 17  # GPIO17 = Pi pin 11
LCD_D5 = 18  # GPIO18 = Pi pin 12
LCD_D6 = 27  # GPIO21 = Pi pin 13
LCD_D7 = 22  # GPIO22 = Pi pin 15

GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_E,  GPIO.OUT)
GPIO.setup(LCD_D4, GPIO.OUT)
GPIO.setup(LCD_D5, GPIO.OUT)
GPIO.setup(LCD_D6, GPIO.OUT)
GPIO.setup(LCD_D7, GPIO.OUT)

# Pulse the LCD Enable line; used for clocking in data
def PulseEnableLine():
    mSec = 0.0005                   # use half-millisecond delay
    time.sleep(mSec)                # give time for inputs to settle
    GPIO.output(LCD_E, GPIO.HIGH)   # pulse E high
    time.sleep(mSec)                # wait
    GPIO.output(LCD_E, GPIO.LOW)    # return E low
    time.sleep(mSec)                # wait before doing anything else

# sends upper 4 bits of data byte to LCD data pins D4-D7
def SendNibble(data):    
    GPIO.output(LCD_D4, bool(data & 0x10))
    GPIO.output(LCD_D5, bool(data & 0x20))
    GPIO.output(LCD_D6, bool(data & 0x40))
    GPIO.output(LCD_D7, bool(data & 0x80))

# Send one byte to LCD controller
def SendByte(data, charMode=False):    
    GPIO.output(LCD_RS, charMode)   # set mode: command vs. char
    SendNibble(data)                # send upper bits first
    PulseEnableLine()               # pulse the enable line
    data = (data & 0x0F) << 4       # shift 4 bits to left
    SendNibble(data)                # send lower bits now
    PulseEnableLine()               # pulse the enable line

# Send string of characters to display at current cursor position
def ShowMessage(string):
    for character in string:
        SendByte(ord(character), True)

# initialize the LCD controller & clear display
SendByte(0x33)  # initialize
SendByte(0x32)  # set to 4-bit mode
SendByte(0x28)  # 2 line, 5x7 matrix
SendByte(0x0C)  # turn cursor off (0x0E to enable)
SendByte(0x06)  # shift cursor right
SendByte(CLEARDISPLAY)  # remove any stray characters on display
########################################################################

ShowMessage('Deine Mudda :=)')

print("LCD program : Done")