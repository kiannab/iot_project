#!/usr/bin/env python
import smbus
import RPi.GPIO as GPIO
import time         

#Sensor set up code
i2c_bus = smbus.SMBus(1)

#LED set up code
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)         #Led at pin 18

#Buzzer set up code
#GPIO.setmode(GPIO.BCM)         #These two lines commented out since they appear above
#GPIO.setwarnings(False)        #Don't forget to include them if just using buzzer
GPIO.setup(17,GPIO.OUT)         #Buzzer at pin 17
    
#function to collect current temperature
def get_patient_temp(bus):
    temp = bus.read_byte_data(0x48, 0x00)
    return(temp)

#function to turn on LED
def turn_on_LED():
    print "LED on"              #print statement for testing
    GPIO.output(18,GPIO.HIGH)    

#functionn to turn off LED
def turn_off_LED():
    print "LED off"             #print statement for testing
    GPIO.output(18,GPIO.LOW)
    
#function to buzz buzzer for 2 seconds
def buzz():
    print "buzz"
    GPIO.output(17,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(17,GPIO.LOW)

#test code
print(get_patient_temp(i2c_bus))        #read temp and print it
turn_on_LED()                           #turn on led for 5 sec then turn off
time.sleep(5)
turn_off_LED()
#buzz()
