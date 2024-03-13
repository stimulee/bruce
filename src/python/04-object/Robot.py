#!/bin/python3
#
# emulate raspberry pi on linux :
#   https://farabimahmud.github.io/emulate-raspberry-pi3-in-qemu/
#
####################################################################

import time
from config import *
import logging
# from DRV8825 import DRV8825
# from RpiMotorLib import RpiMotorLib
# from gpiozero import Servo

# pour moteur 28BYJ
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

class MoteurPaP():
    
    def __init__(self, name, dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20)) -> None:
        self.name = name
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        self.enable_pin = enable_pin
        self.mode_pins = mode_pins
        # self.motor_card = DRV8825(step_pin, enable_pin, mode_pins)
        # self.motor_cd = RpiMotorLib.A4988Nema(step_pin, enable_pin, mode_pins,motor_type="DRV8825")
        self.motor_cd = "{'name': '"+name+"', 'parameters': ('"+str(dir_pin)+"', '"+str(step_pin)+"', '"+str(enable_pin)+"', '"+str(mode_pins)+"',motor_type=\"DRV8825\")'}"
        # logging.debug,(self.motor_cd)
        
    def __enter__(self):
        # self.motor_card.SetMicroStep('softward','halfstep')
        pass
        
    def rotation(self, sens: str, angle: int):
        """_summary_

        Args:
            sens (str): CW pour Clockwise / CC pour Counter Cloclwise
            angle (int): ange de rotation souhaité
        """
        logging.info("{'name': '"+self.name+"','action': 'rotation', 'sens': '"+sens+"', 'angle': '"+str(angle)+"'}")
        
        if sens == "CC":
            self.TurnStep(Dir='forward', steps=400, stepdelay = 0.005)
        elif sens == "CW":
            self.TurnStep(Dir='backward', steps=400, stepdelay = 0.005)
        else:
            self.Stop()
        
        time.sleep(3)

    def TurnStep(self, Dir='forward', steps=400, stepdelay = 0.005):
        print("Tourne : "+str(Dir)+" "+str(steps)+" "+str(stepdelay))
        pass
    
    def Stop(self):
        print("Stop")
        
class Moteur_28BYJ(RpiMotorLib.BYJMotor):
    def __init__(self, name, bob1_pin1=18, bob1_pin2=23, bob2_pin1=24, bob2_pin2=25) -> None:
        self.GpioPins = [bob1_pin1, bob1_pin2, bob2_pin1, bob2_pin2]
        self.name = name

        # Declare an named instance of class pass a name and motor type
        mymotortest = RpiMotorLib.BYJMotor(self.name, "28BYJ")

    def TurnStep(self, Dir='forward', steps=400, stepdelay = 0.005):
        if Dir == 'forward':
            cc = False
        else:
            cc = True
        print(self.GpioPins)
        print("Tourne : "+str(Dir)+" "+str(steps)+" "+str(stepdelay))
        self.motor_run(self.GpioPins , stepdelay, steps, cc, False, "half", .05)
        pass


# class ServoMoteur(Servo):
class ServoMoteur():
    
    def __init__(self, name, cmd_pin=18) -> None:
        # super().__init__(cmd_pin)
        self.name = name
        self.cmd_pin = cmd_pin
        
    def rotation(self, sens: str, angle: int):
        """_summary_

        Args:
            sens (str): CW pour Clockwise / CC pour Counter Cloclwise
            angle (int): ange de rotation souhaité
        """
        logging.info("{'name': '"+self.name+"', 'action': 'rotation', 'sens': '"+sens+"', 'angle': '"+str(angle)+"'}")
        
        if sens == "CC":
            self.min()
        elif sens == "CW":
            self.max()
        else:
            self.mid()
            
        time.sleep(3)  # import time

    def min(self):
        print("Tourne CC anti horaire")
        pass

    def max(self):
        print("Tourne CW horaire")
        pass

    def mid(self):
        print("Stop")
        pass

class Base(MoteurPaP):
    
    def __init__(self, name) -> None:
        super().__init__(name, base_dir_pin, base_step_pin, base_enable_pin, base_mode_pins)
    
    def droite(self):
        logging.info("{'name': '"+self.name+"', 'action': 'droite'}")   
        self.rotation('CW', 90)
        self.Stop()
    
    def gauche(self):
        logging.info("{'name': '"+self.name+"', 'action': 'gauche'}")   
        self.rotation('CC', 90)
        self.Stop()

    def stop(self):
        logging.info("{'name': '"+self.name+"', 'action': 'stop'}")   
        self.rotation('STOP', 0)
                 
class Epaule(MoteurPaP):
    
    def __init__(self, name) -> None:
        super().__init__(name, epaule_dir_pin, epaule_step_pin, epaule_enable_pin, epaule_mode_pins)
        
    def monter(self):
        logging.info("{'name': '"+self.name+"', 'action': 'monter'}")   
        self.rotation('CW', 90)
        self.Stop()
    
    def descendre(self):
        logging.info("{'name': '"+self.name+"', 'action': 'descendre'}")   
        self.rotation('CC', 90)
        self.Stop()

    def stop(self):
        logging.info("{'name': '"+self.name+"', 'action': 'stop'}")   
        self.rotation('STOP', 0)

class Coude(MoteurPaP):
    
    def __init__(self, name) -> None:
        super().__init__(name, coude_dir_pin, coude_step_pin, coude_enable_pin, coude_mode_pins)

    def plier(self):
        logging.info("{'name': '"+self.name+"', 'action': 'plier'}")   
        self.rotation('CW', 90)
        self.Stop()
    
    def deplier(self):
        logging.info("{'name': '"+self.name+"', 'action': 'deplier'}")   
        self.rotation('CC', 90)
        self.Stop()

    def stop(self):
        logging.info("{'name': '"+self.name+"', 'action': 'stop'}")   
        self.rotation('STOP', 0)

class Poignet(MoteurPaP):
    
    def __init__(self, name) -> None:
        super().__init__(name, poignet_dir_pin, poignet_step_pin, poignet_enable_pin, poignet_mode_pins)

    def plier(self):
        logging.info("{'name': '"+self.name+"', 'action': 'plier'}")   
        self.rotation('CW', 90)
        self.Stop()
    
    def deplier(self):
        logging.info("{'name': '"+self.name+"', 'action': 'deplier'}")   
        self.rotation('CC', 90)
        self.Stop()

    def stop(self):
        logging.info("{'name': '"+self.name+"', 'action': 'stop'}")   
        self.rotation('STOP', 0)

class Poignet2(Moteur_28BYJ):
    def __init__(self, name) -> None:
        super().__init__(name, poignet2_bob1_pin1, poignet2_bob1_pin2, poignet2_bob2_pin1, poignet2_bob2_pin2)
        # mymotortest = Moteur_28BYJ.BYJMotor("MyMotorOne", "28BYJ")

    def plier(self):
        logging.info("{'name': '"+self.name+"', 'action': 'plier'}") 
        # 130 steps = 90°  
        self.TurnStep(Dir='forward', steps=130, stepdelay=0.001)
        # self.stop()
    
    def deplier(self):
        logging.info("{'name': '"+self.name+"', 'action': 'deplier'}")   
        self.TurnStep(Dir='backward', steps=130, stepdelay=0.001)
        # self.stop()

    def stop(self):
        logging.info("{'name': '"+self.name+"', 'action': 'stop'}")   
        self.rotation('STOP', 0)

class Pince(ServoMoteur):
    
    def __init__(self, name) -> None:
        super().__init__(name, pince_cmd_pin)
         
    def ouvrir(self):
        logging.info("{'name': '"+self.name+"', 'action': 'ouvrir'}")   
        # self.rotation('CC', 90)
        self.max()
        time.sleep(2)  # import time
        self.mid()
         
    def fermer(self):
        logging.info("{'name': '"+self.name+"', 'action': 'fermer'}")   
        # self.rotation('CW', 90)
        self.min()
        time.sleep(2)  # import time
        self.mid()
        
class Robot():
    
    def __init__(self, username, password, host, port, service_name):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._conn:
            self._conn.close()

class Bras():
    
    def __init__(self, name):
        self.name = name
        self.epaule = Epaule(name+'-epaule')
        self.coude = Coude(name+'-coude')
        self.poignet = Poignet(name+'-poignet')
        self.poignet2 = Poignet2(name+'-poignet2')
        self.pince = Pince(name+'-pince')
        self.base = Base(name+'-base')
