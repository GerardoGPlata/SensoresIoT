import RPi.GPIO as GPIO
import time
import board


#Codigo de Prueba no funcional
# Configurar VEX 2 Wire Servo
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.LOW)
pwm = GPIO.PWM(4, 100)
pwm.start(0)
