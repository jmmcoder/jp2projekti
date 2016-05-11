# -*- encoding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
               print "Liikettä tunnistettu!"

print "Liiketunnistimen testaus, JP2-projekti (CTRL+C to exit)"
time.sleep(2)
print "Valmis"

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                              time.sleep(100)
except KeyboardInterrupt:
               print " Heippa"
               GPIO.cleanup()
