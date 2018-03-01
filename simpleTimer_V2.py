#!/usr/bin/env python3
from ev3dev.ev3 import *
from time   import sleep



# Improved version of simpleTimer.py that is more suitable for 
# performing the experiment. The timer is primed when a weight
# is placed on the start sensor, and only started upon release
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
timerReady   = False
timerRunning = False
timeElapsed  = 0.0
timeStarted  = 0.0
displayText  = "Time Elapsed : "


while True:                                      # Loop forever
  
  if resetButton.value() > 0:                        # If the reset button is pressed down
      timeElapsed  = 0                                   # Set timeElapsed to 0
      timerReady   = False                               # Set timerReady to False
      timerRunning = False                               # Set timerRunning to False

  if timerReady:                                    # If the timer is ready
    
    if startButton.value() == 0:                          # If the start button is released...
      if not timerRunning:                                # ...and we are not already running the timer
        timerRunning = True                                   # Set timerRunning to true
        timeStarted  = time.clock()                           # Set timeStarted to the current system time
        
    if stopButton.value() > 0:                            # If the stop button is pressed down...
      if timerRunning:                                    # ...and we are already running the timer
        timerRunning = False                                  # Set timerRunning to False
        timerReady   = False                                  # Set timerReady to False
      
    if timerRunning:                                      # If we are running the timer
      timeElapsed = time.clock() - timeStarted                # Update the timeElapsed
    
    if timeElapsed > 0:                                   # If we have a recorded time
      displayText = "Time Elapsed : %.3f" % timeElapsed       # Display it to 3 decimal places
    else:                                                 # Otherwise we are in a primed state
      displayText = "Release to Start"                        # So display the "Release to Start" message

  else:                                             # Otherwise the timer is not ready

    if timeElapsed == 0:                                 # If we have no recorded time
      displayText = "Press to Prime"                         # Display "Press to Prime"

    if startButton.value() > 0:                          # If the start button is pressed down...
      if not timerReady:                                 # ...and we are not already ready
        timerReady = True;                                   # Set us to be ready
   

  lcd.clear()                                            # Clear the lcd screen
  lcd.draw.rectangle((0,0,177,40),   fill='black' )      # Draw a black rectangle as a background
  lcd.draw.text((28,13),displayText, fill='white' )      # Draw our displayText in white on top
  lcd.update()                                           # Draw this all to the screen
    
    
    
