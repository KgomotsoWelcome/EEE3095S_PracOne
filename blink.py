#!/usr/bin/python3
"""
Names: Kgomotso Welcome
Student Number: WLCKGO001
Prac: 1
Date: 3 August 2019
"""

#import Librares
import RPi.GPIO as GPIO
import time

#Setting up variables
LED1 = 12
LED2 = 16
LED3 = 18
ButtonOne = 11
ButtonTwo = 13
counter = 0
LED_list = [LED1, LED2, LED3]

#Disable warnings
GPIO.setwarnings(False)

#Setting up the mode
GPIO.setmode(GPIO.BOARD)

#Setting up button and LED channels
GPIO.setup(ButtonOne, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ButtonTwo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_list, GPIO.OUT)

#Callback method for the up button
def my_callback(channel):
	global counter
	input_stateOne = GPIO.input(ButtonOne)
	if input_stateOne == False:
                      	counter = counter+1
                        if counter == 8:
                                counter = 0
                        elif counter == -1:
                                counter = 7
                        print("Up is pressed!")
			print(counter)
			LED(counter)
			time.sleep(0.2)

#Callback method for the down button
def my_callback2(channel):
	global counter
	input_stateTwo = GPIO.input(ButtonTwo)
	if input_stateTwo == False:
                        counter = counter-1
                        if counter == 8:
                                counter = 0
                        elif counter == -1:
                                counter = 7
                        print("Down is pressed!")
                        print(counter)
                        LED(counter)
                        time.sleep(0.2)

#Outputing to the LED
def LED(count):
        if (count==0):
		GPIO.output(LED_list, GPIO.LOW)
        elif (count==1):
                GPIO.output(LED_list, (GPIO.LOW, GPIO.LOW, GPIO.HIGH))
	elif(count==2):
		GPIO.output(LED_list, (GPIO.LOW, GPIO.HIGH, GPIO.LOW))
	elif(count==3):
		GPIO.output(LED_list, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
	elif(count==4):
		GPIO.output(LED_list, (GPIO.HIGH, GPIO.LOW, GPIO.LOW))
	elif(count==5):
		GPIO.output(LED_list, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
	elif(count==6):
		GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
	elif(count==7):
		GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))

#Using Interrupts
GPIO.add_event_detect(ButtonOne, GPIO.FALLING, callback=my_callback, bouncetime=300)
GPIO.add_event_detect(ButtonTwo, GPIO.FALLING, callback=my_callback2, bouncetime=300)

#Main method
def main():
	while True:
		my_callback(ButtonOne)
		my_callback2(ButtonTwo)

if __name__ == "__main__":
# Make sure the GPIO is stopped correctly
	try:
			main()
		except KeyboardInterrupt:
			print("Exiting gracefully")
			# Turn off your GPIOs here
		GPIO.output(LED_list, GPIO.LOW)
			GPIO.cleanup() #cleanup previous channel
		except e:
			GPIO.cleanup() #cleanup previous channel
			print("Some other error occurred")
			print(e.message)	
