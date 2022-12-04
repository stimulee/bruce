#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright : 2022 - Benoit Debaenst

# Ce programme permet de tester la commande de 2 moteurs pas à pas.
# Les moteurs tournent alternativement en faisant un demi tour dans un sens puis dans l'autre.

from time import sleep         # Importer la bibliothèque de gestion du temps 
import RPi.GPIO as GPIO        # Importer la bibliothèque de gestion des GPIO

M1_ID = "moteur-01"
M1_PIN_STEP = 14                      # La commande de pas du moteur 1 est reliée au GPIO 14
M1_PIN_DIR = 15                       # La commande de direction du moteur 1 est reliée au GPIO 15
M1_STEP_PER_TOUR = 14800              # nombre pas par tour, défini selon le mode de transmission (nombre de dents engrenage)
M1_SPEED = 1                          # Vitesse de rotation en tour/s

M2_ID = "moteur-02"
M2_PIN_STEP = 16                      # La commande de pas du moteur 2 est reliée au GPIO 16
M2_PIN_DIR = 17                       # La commande de direction du moteur 2 est reliée au GPIO 17
M2_STEP_PER_TOUR = 3200               # nombre pas par tour, défini selon le mode de transmission (nombre de dents engrenage)
M2_SPEED = 1                          # Vitesse de rotation en tour/s

GPIO.setmode(GPIO.BCM)                # Paramétrage de la numérotation des GPIO en mode BCM
GPIO.setwarnings(False)               # Ne pas tenir comte des alertes
GPIO.setup(M1_PIN_STEP, GPIO.OUT)     # GPIO M1_PIN_STEP configuré en sortie
GPIO.setup(M1_PIN_DIR, GPIO.OUT)      # GPIO M1_PIN_DIR configuré en sortie
GPIO.setup(M2_PIN_STEP, GPIO.OUT)     # GPIO M2_PIN_STEP configuré en sortie
GPIO.setup(M2_PIN_DIR, GPIO.OUT)      # GPIO M2_PIN_DIR configuré en sortie

def rotate(ID, PIN_STEP, PIN_DIR, DIRECTION, STEP_NUMBER, STEP_PER_TOUR, SPEED):
    # ID : identifiant du device/moteur
    # PIN_STEP : pinoche de commande de pas du moteur
    # PIN_DIR : pinoche de commande de direction
    # DIRECTION : CW pour sens horaire, ACW pour sens antihoraire
    # STEP_NUMBER : nombre de pas a effectuer
    # STEP_PER_TOUR : nombre de pas par tour
    # SPEED : vitesse de rotation tour/s

    MOVEMENT = "rotation"
    TIME_TO_SLEEP = SPEED/STEP_PER_TOUR

    # Sens de rotation
    if (DIRECTION == "CW"):
        GPIO.output(PIN_DIR, GPIO.HIGH)
    else:
        GPIO.output(PIN_DIR, GPIO.LOW)

    # Avancer du nombre de pas
    print('{"device": "{ID}", "movement": "{MOVEMENT}", "direction": "{DIRECTION}", "distance": "{DISTANCE}", "speed": "{SPEED}"}'.format(ID = ID, DIRECTION = DIRECTION, MOVEMENT = MOVEMENT, DISTANCE = STEP_NUMBER, SPEED = SPEED)) 
    for x in range(STEP_NUMBER):
        GPIO.output(PIN_STEP, GPIO.HIGH)
        sleep(TIME_TO_SLEEP)
        GPIO.output(PIN_STEP, GPIO.LOW)
        sleep(TIME_TO_SLEEP)

    sleep(1)

# Nombre de pas de rotation pour le test
STEP_NUMBER = 1600                     # Nombre de pas à parcourir 3200 = 1 tour, 1600 = 1/2 tour

while True:
    rotate(M1_ID, M1_PIN_STEP, M1_PIN_DIR, "CW", STEP_NUMBER, M1_STEP_PER_TOUR, M1_SPEED)
    rotate(M1_ID, M1_PIN_STEP, M1_PIN_DIR, "ACW", STEP_NUMBER, M1_STEP_PER_TOUR, M1_SPEED)
    rotate(M2_ID, M2_PIN_STEP, M2_PIN_DIR, "CW", STEP_NUMBER, M2_STEP_PER_TOUR, M2_SPEED)
    rotate(M2_ID, M2_PIN_STEP, M2_PIN_DIR, "ACW", STEP_NUMBER, M2_STEP_PER_TOUR, M2_SPEED)
