#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright : 2022 - Benoit Debaenst

# Ce programme permet de tester la commande de 3 moteurs pas à pas.
# Tant que les touches de direction sont appuyées, les moteurs tournent.
# Touches associées :
# - moteur 1 : haut / bas
# - moteur 2 : droite / gauche
# - moteur 3 : page haut / page bas

import tk as tkinter
from pynput import keyboard    # Bibliothèque de gestion clavier
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

M3_ID = "moteur-03"
M3_PIN_STEP = 18                      # La commande de pas du moteur 3 est reliée au GPIO 18
M3_PIN_DIR = 19                       # La commande de direction du moteur 3 est reliée au GPIO 19
M3_STEP_PER_TOUR = 3200               # nombre pas par tour, défini selon le mode de transmission (nombre de dents engrenage)
M3_SPEED = 1                          # Vitesse de rotation en tour/s

def rotate(ID, PIN_STEP, PIN_DIR, DIRECTION, STEP_NUMBER, STEP_PER_TOUR, SPEED):
    # ID : identifiant du device/moteur
    # PIN_STEP : pinoche de commande de pas du moteur
    # PIN_DIR : pinoche de commande de direction
    # DIRECTION : CW pour sens horaire, CCW pour sens antihoraire
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
    print('"device": "{ID}", "movement": "{MOVEMENT}", "direction": "{DIRECTION}", "distance": "{DISTANCE}", "speed": "{SPEED}"'.format(ID = ID, DIRECTION = DIRECTION, MOVEMENT = MOVEMENT, DISTANCE = STEP_NUMBER, SPEED = SPEED)) 
    for x in range(STEP_NUMBER):
        GPIO.output(PIN_STEP, GPIO.HIGH)
        sleep(TIME_TO_SLEEP)
        GPIO.output(PIN_STEP, GPIO.LOW)
        sleep(TIME_TO_SLEEP)


# Fonction appelée quand une touche est appuyée
def push(key):
    try:
        print('Touche alphanumérique : {0} '.format(
            key.char))
    except AttributeError:
        print('Touche spéciale : {0}'.format(
            key))
        # Touche flèche gauche - Sens inverse des aiguilles d'une montre - 10 pas
        if (key == keyboard.Key.left):
            rotate(M1_ID, M1_PIN_STEP, M1_PIN_DIR, "CCW", STEP_NUMBER, M1_STEP_PER_TOUR, M1_SPEED)
        # Touche flèche droite - Sens des aiguilles d'une montre - 10 pas
        elif (key == keyboard.Key.right):
            rotate(M1_ID, M1_PIN_STEP, M1_PIN_DIR, "CW", STEP_NUMBER, M1_STEP_PER_TOUR, M1_SPEED)
        # Touche flèche haute - Sens inverse des aiguilles d'une montre - 100 pas
        elif (key == keyboard.Key.up):
            rotate(M2_ID, M2_PIN_STEP, M2_PIN_DIR, "CCW", STEP_NUMBER, M2_STEP_PER_TOUR, M2_SPEED)
        # Touche flèche basse - Sens des aiguilles d'une montre - 100 pas
        elif (key == keyboard.Key.down):
            rotate(M2_ID, M2_PIN_STEP, M2_PIN_DIR, "CW", STEP_NUMBER, M2_STEP_PER_TOUR, M2_SPEED)
        # Touche page haute - Sens inverse des aiguilles d'une montre - 800 pas = 1/4 de tour
        elif (key == keyboard.Key.page_up):
            rotate(M3_ID, M3_PIN_STEP, M3_PIN_DIR, "CCW", STEP_NUMBER, M3_STEP_PER_TOUR, M3_SPEED)
        # Touche page basse - Sens des aiguilles d'une montre - 800 pas = 1/4 de tour
        elif (key == keyboard.Key.page_down):
            rotate(M3_ID, M3_PIN_STEP, M3_PIN_DIR, "CW", STEP_NUMBER, M3_STEP_PER_TOUR, M3_SPEED)

# Fonction exécutée quand une touche est relachée
def release(key):
    print('Key released: {0}'.format(
        key))
    # Si c'est la touche ESC on sort du programme
    if key == keyboard.Key.esc:
        # Stop listener
        print("Sortie du programme")
        GPIO.cleanup()
        return False


# Nombre de pas de rotation 
STEP_NUMBER = 1                     # Nombre de pas à parcourir 3200 = 1 tour, 1600 = 1/2 tour

# Le listener collecte les événements et appelle les fonctions en callback
with keyboard.Listener(
        on_press = push,
        on_release = release) as listener:
    listener.join()