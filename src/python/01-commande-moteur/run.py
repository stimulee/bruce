#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright : 2022 - Benoit Debaenst

# Ce programme permet de tester la commande d'un moteur pas à pas.
# Le moteur tourne alternativement en faisant un demi tour dans un sens puis dans l'autre.
# Cela permet de controler qu'aucun décalage n'apparait au fil du temps.

from time import sleep         # Importer la bibliothèque de gestion du temps 
import RPi.GPIO as GPIO        # Importer la bibliothèque de gestion des GPIO

STEP = 14                      # La commande de pas est reliée au GPIO 14
DIR = 15                       # La commande de direction est reliée au GPIO 15
vitesse = 0.0005

GPIO.setmode(GPIO.BCM)         # Paramétrage de la numérotation des GPIO en mode BCM
GPIO.setwarnings(False)        # Ne pas tenir comte des alertes
GPIO.setup(STEP, GPIO.OUT)     # GPIO STEP configuré en sortie
GPIO.setup(DIR, GPIO.OUT)      # GPIO DIR configuré en sortie

GPIO.output(DIR, GPIO.HIGH)   # Sens de rotation initial
NB_PAS = 1600                 # Nombre de pas à parcourir 3200 = 1 tour, 1600 = 1/2 tour

while True:
    # On travaille en 1/16 de pas soit 3200 micropas par tour
    for x in range(NB_PAS):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(vitesse)
        GPIO.output(STEP, GPIO.LOW)
        sleep(vitesse)

    sleep(1)

    # Changement de sens
    GPIO.output(DIR, GPIO.LOW)
    for x in range(NB_PAS):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(vitesse)
        GPIO.output(STEP, GPIO.LOW)
        sleep(vitesse)
        
    sleep(1)
    
    # Retour au sens initial
    GPIO.output(DIR, GPIO.HIGH)
