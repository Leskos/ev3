#!/usr/bin/env python3
from ev3dev.ev3 import *
from time   import sleep



# Improved version of simpleTimer.py that uses an IR distance sensor
# and also uses ev3dev.eve.Sound.speak() to read the result out loud
#
# This is for recreating Galileo's leaning tower of Pisa experiment
# at Brighton's Self Managed Learning College



# Initialise input and output objects
lcd         = Screen()
startButton = TouchSensor('in1') 
stopButton  = InfraredSensor('in2')
resetButton = TouchSensor('in3')

stopButton.mode = "IR-PROX"

# Check we have all sensors connected
assert startButton.connected, "Connect a touch sensor to sensor port 1"
assert stopButton.connected,  "Connect a touch sensor to sensor port 2"
assert resetButton.connected, "Connect a touch sensor to sensor port 3"

Sound.set_volume( 50 )

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
        Sound.tone(1500, 100)                                 # Play a beep
        
    if stopButton.value() < 50:                           # If the stop sensor is triggered...
      if timerRunning:                                    # ...and we are already running the timer
        timerRunning = False                                  # Set timerRunning to False
        timerReady   = False                                  # Set timerReady to False
        Sound.tone(2500, 100)                                 # Play a beep
        sleep(0.1)                                            # Wait for the beep to play
        Sound.speak( round( timeElapsed,3 ) )                 # Read the time out loud
        sleep(2)                                              # Wait for the time to be read out
        
      
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
    
    
    
