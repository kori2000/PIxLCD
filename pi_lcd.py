import RPi.GPIO as GPIO ## Import GPIO library
import time             ## Import 'time' library. Allows us to use 'sleep'

########################################################################
# Main Program
print("LCD program : Importing PIN Input")

GPIO.setwarnings(False)  ## Ignore warnings

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

# Outputs Pin Config
LCD_RS = 7   # GPIO7  = Pi pin 26
LCD_E = 8    # GPIO8  = Pi pin 24
LCD_D4 = 17  # GPIO17 = Pi pin 11
LCD_D5 = 18  # GPIO18 = Pi pin 12
LCD_D6 = 27  # GPIO21 = Pi pin 13
LCD_D7 = 22  # GPIO22 = Pi pin 15

OUTPUTS = [LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7]

for lcdLine in OUTPUTS:
    GPIO.setup(lcdLine, GPIO.OUT)

print("LCD program : Done")