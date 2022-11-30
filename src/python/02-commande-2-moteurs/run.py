#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright : 2022 - Benoit Debaenst

# Ce programme permet de tester la commande de 2 moteurs pas à pas.
# Les moteurs tournent alternativement en faisant un demi tour dans un sens puis dans l'autre.

from time import sleep         # Importer la bibliothèque de gestion du temps 
import RPi.GPIO as GPIO        # Importer la bibliothèque de gestion des GPIO

M1_ID="moteur-01"
M1_PIN_STEP = 14                      # La commande de pas du moteur 1 est reliée au GPIO 14
M1_PIN_DIR = 15                       # La commande de direction du moteur 1 est reliée au GPIO 15
M2_ID="moteur-02"
M2_PIN_STEP = 16                      # La commande de pas du moteur 2 est reliée au GPIO 16
M2_PIN_DIR = 17                       # La commande de direction du moteur 2 est reliée au GPIO 17

GPIO.setmode(GPIO.BCM)            # Paramétrage de la numérotation des GPIO en mode BCM
GPIO.setwarnings(False)           # Ne pas tenir comte des alertes
GPIO.setup(M1_PIN_STEP, GPIO.OUT)     # GPIO M1_PIN_STEP configuré en sortie
GPIO.setup(M1_PIN_DIR, GPIO.OUT)      # GPIO M1_PIN_DIR configuré en sortie
GPIO.setup(M2_PIN_STEP, GPIO.OUT)     # GPIO M2_PIN_STEP configuré en sortie
GPIO.setup(M2_PIN_DIR, GPIO.OUT)      # GPIO M2_PIN_DIR configuré en sortie

# GPIO.output(M1_PIN_DIR, GPIO.HIGH)    # Sens de rotation initial du moteur 1
# GPIO.output(M2_PIN_DIR, GPIO.HIGH)    # Sens de rotation initial du moteur 2

SPEED = 0.0005
STEP_NUMBER = 1600                     # Nombre de pas à parcourir 3200 = 1 tour, 1600 = 1/2 tour

def rotate(ID, PIN_STEP, PIN_DIR, DIRECTION, STEP_NUMBER, SPEED):
    # Sens de rotation
    if (DIRECTION == "CW"):
        GPIO.output(PIN_DIR, GPIO.HIGH)
    else:
        GPIO.output(PIN_DIR, GPIO.LOW)
    # Avancer du nombre de pas
    for x in range(pas):
        print('MOTEUR: {ID} - direction: {DIRECTION}'.format(ID = ID, DIRECTION = DIRECTION)) 
        GPIO.output(PIN_STEP, GPIO.HIGH)
        sleep(SPEED)
        GPIO.output(PIN_STEP, GPIO.LOW)
        sleep(SPEED)

while True:

    rotate(M1_ID, M1_PIN_STEP, M1_PIN_DIR, "CW", STEP_NUMBER, SPEED)
    rotate(M1_ID, M1_PIN_STEP, M1_PIN_DIR, "ACW", STEP_NUMBER, SPEED)
    rotate(M2_ID, M2_PIN_STEP, M2_PIN_DIR, "CW", STEP_NUMBER, SPEED)
    rotate(M2_ID, M2_PIN_STEP, M2_PIN_DIR, "ACW", STEP_NUMBER, SPEED)
  