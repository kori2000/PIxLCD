import RPi.GPIO as GPIO ## Import GPIO library
import time             ## Import 'time' library. Allows us to use 'sleep'

########################################################################
# Main Program
print("LCD program : Importing PIN Input")

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

# Outputs Pin Config
LCD_RS = 7              # GPIO7 = Pi pin 26
LCD_E = 8               # GPIO8 = Pi pin 24

GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_E, GPIO.OUT)