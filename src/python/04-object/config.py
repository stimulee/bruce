
# rotation - base
# Card2Motor1 = DRV8825(dir_pin=2, step_pin=3, enable_pin=17, mode_pins=(16, 17, 20))
base_dir_pin=2
base_step_pin=3
base_enable_pin=17
base_mode_pins=(16, 17, 20)

# bras - epaule
# Card1Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
epaule_dir_pin=13
epaule_step_pin=19
epaule_enable_pin=12
epaule_mode_pins=(16, 17, 20)

# avant-bras - coude
# Card2Motor2 = DRV8825(dir_pin=27, step_pin=22, enable_pin=10, mode_pins=(21, 22, 27))
coude_dir_pin=27
coude_step_pin=22
coude_enable_pin=10
coude_mode_pins=(21, 22, 27)

# rotation pince - poignet
# Card1Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
poignet_dir_pin=24
poignet_step_pin=18
poignet_enable_pin=4
poignet_mode_pins=(21, 22, 27)

# pince
pince_cmd_pin=18

log_file="/tmp/robot.log"
logging_conf="logging.conf"