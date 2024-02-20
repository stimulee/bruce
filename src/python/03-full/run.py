#!/usr/bin/env python2
import RPi.GPIO as GPIO
import time
from DRV8825 import DRV8825
from gpiozero import Servo
from time import sleep


try:
	# Init des moteurs
	Card1Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
	Card1Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
	
	Card2Motor1 = DRV8825(dir_pin=2, step_pin=3, enable_pin=17, mode_pins=(16, 17, 20))
	Card2Motor2 = DRV8825(dir_pin=27, step_pin=22, enable_pin=10, mode_pins=(21, 22, 27))

	Card1Motor1.SetMicroStep('softward','halfstep')
	#Card1Motor1.SetMicroStep('softward','fullstep')
	Card1Motor2.SetMicroStep('softward','halfstep')
	#Card1Motor2.SetMicroStep('softward','fullstep')

	Card2Motor1.SetMicroStep('softward','halfstep')
	#Card2Motor1.SetMicroStep('softward','fullstep')
	Card2Motor2.SetMicroStep('softward','halfstep')
	#Card2Motor2.SetMicroStep('softward','fullstep')
	
	# ROTATION DE LA PINCE
	print("Carte 1 - moteur 2 : rotation pince")
	Card1Motor2.TurnStep(Dir='forward', steps=400, stepdelay = 0.005)
	time.sleep(0.5)
	Card1Motor2.TurnStep(Dir='backward', steps=400, stepdelay = 0.005)
	time.sleep(0.5)	
	
		
	"""
	# 1.8 degree: nema23, nema14
	# softward Control :
	# 'fullstep': A cycle = 200 steps
	# 'halfstep': A cycle = 200 * 2 steps
	# '1/4step': A cycle = 200 * 4 steps
	# '1/8step': A cycle = 200 * 8 steps
	# '1/16step': A cycle = 200 * 16 steps
	# '1/32step': A cycle = 200 * 32 steps
	"""
	# ROTATION DU BRAS
	print ("Carte 1 - moteur 1 : bras")
	Card1Motor1.TurnStep(Dir='forward', steps=400, stepdelay = 0.005)
	time.sleep(0.5)
	Card1Motor1.TurnStep(Dir='backward', steps=400, stepdelay = 0.005)
	time.sleep(0.5)

	###
	print ("Carte 2 - moteur 1 : rotation")
	Card2Motor1.TurnStep(Dir='forward', steps=400, stepdelay = 0.005)
	time.sleep(0.5)
	Card2Motor1.TurnStep(Dir='backward', steps=400, stepdelay = 0.005)
	time.sleep(0.5)

	"""
	# 28BJY-48:
	# softward Control :
	# 'fullstep': A cycle = 2048 steps
	# 'halfstep': A cycle = 2048 * 2 steps
	# '1/4step': A cycle = 2048 * 4 steps
	# '1/8step': A cycle = 2048 * 8 steps
	# '1/16step': A cycle = 2048 * 16 steps
	# '1/32step': A cycle = 2048 * 32 steps
	"""
	print ("Carte 2 - moteur 2 : avant-bras")
	Card2Motor2.TurnStep(Dir='forward', steps=400, stepdelay = 0.005)
	time.sleep(0.5)
	Card2Motor2.TurnStep(Dir='backward', steps=400, stepdelay = 0.005)
	time.sleep(0.5)

	print ("Servo : action pince")
	servo = Servo(18)
	servo.min()
	sleep(1)
	servo.mid()
	sleep(1)
	servo.max()
	sleep(1)

	
	# Liberer les moteurs
	Card1Motor1.Start()
	Card2Motor1.Start()
	Card2Motor2.Start()
	Card1Motor2.Start()

    
except:
	# GPIO.cleanup()
	print ("\nMotor stop")
	Card1Motor1.Stop()
	Card2Motor1.Stop()
	Card2Motor2.Stop()
	Card1Motor2.Stop()
	exit()
