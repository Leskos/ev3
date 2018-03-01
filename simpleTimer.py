#!/usr/bin/env python3
from ev3dev.ev3 import *
from time   import sleep



# A simple timer for the EV3 brick using 3 touch sensors.
#
# - Start Button
# - Stop Button
# - Rest Button
#
# This is for recreating Galileo's leaning tower of Pisa experiment
# at Brighton's Self Managed Learning College



# Initialise input and output objects
lcd         = Screen()
startButton = TouchSensor('in1') 
stopButton  = TouchSensor('in2')
resetButton = TouchSensor('in3')

# Check we have all sensors connected
assert startButton.connected, "Connect a touch sensor to sensor port 1"
assert stopButton.connected,  "Connect a touch sensor to sensor port 2"
assert resetButton.connected, "Connect a touch sensor to sensor port 3"

# Initialise our python timer variables
timerRunning = False
timeElapsed  = 0.0
timeStarted  = 0.0
displayText  = "Time Elapsed : "



while True:                                         # Loop forever
  
  if startButton.value() > 0:                           # If the start button is pressed down...
    if not timerRunning:                                # ...and we are not already running the timer
      timerRunning = True                                   # Set timerRunning to true
      timeStarted  = time.clock()                           # Set timeStarted to the current system time
      
  if stopButton.value() > 0:                            # If the stop button is pressed down...
    if timerRunning:                                    # ...and we are already running the timer
      timerRunning = False                                  # Set timerRunning to false
    
  if resetButton.value() > 0:                           # If the reset button is pressed down
    timeElapsed = 0                                         # Set timeElapsed to 0
  
  if timerRunning:                                      # If we are running the timer
    timeElapsed = time.clock() - timeStarted           		# Update the timeElapsed
    
  displayText = "Time Elapsed : %.3f" % timeElapsed     # Format a string to show only 3 decimal points
   
  lcd.clear()                                           # Clear the lcd screen
  lcd.draw.rectangle((0,0,177,40),   fill='black' )     # Draw a black rectangle as a background
  lcd.draw.text((28,13),displayText, fill='white' )     # Draw our displayText in white on top
  lcd.update()                                          # Draw this all to the screen
    
    
    
