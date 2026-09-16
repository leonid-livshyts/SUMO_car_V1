from distance import Distance
from motor_driver import MotorDriver
from black_sensor import BlackSensor
from machine import UART, ADC
import os


dist = Distance(trigger_pin=4, echo_pin_forward=5, echo_pin_backward=16)
driver = MotorDriver(left_pin=1, right_pin=3, left_speed_pin=0, right_speed_pin=2)
black_sensor = BlackSensor(fr_rh=13, fr_lf=15, bk_rh=12, bk_lf=14)
interupt = ADC(0)

left_reverse = True
right_reverse = False
left_speed = 1023
right_speed = 1023


def get_black_line():
    global left_reverse, right_reverse, left_speed, right_speed
    
    fr, fl, br, bl = await black_sensor.read_sensors()
    
    if fr:
        if fl:
            left_reverse = False
            right_reverse = False,
            left_speed = 1023
            right_speed = 1023
        elif br:
            left_reverse = False
            right_reverse = False,
            left_speed = 400
            right_speed = 1023
        else:
            left_reverse = True
            right_reverse = True
            left_speed = 400
            right_speed = 1023
    elif br:
        if bl:
            left_reverse = True
            right_reverse = True
            left_speed = 1023
            right_speed = 0
        else:
            left_reverse = False
            right_reverse = False,
            left_speed = 400
            right_speed = 1023
    elif bl:
        if fl:
            left_reverse = False
            right_reverse = False,
            left_speed = 1023
            right_speed = 400
        else:
            left_reverse = False
            right_reverse = False,
            left_speed = 1023
            right_speed = 400
    elif fl:
        left_reverse = True
        right_reverse = True,
        left_speed = 1023
        right_speed = 400
    else:
        return False
    
    return True


def attack():
    global left_reverse, right_reverse, left_speed, right_speed
    
    fd, bd = dist.check_distance()
    if fd is not None and bd is not None:
        min_d = min(fd, bd)
    
        if min_d >= dist.max_distance:
            left_reverse = True
            right_reverse = False
            left_speed = 1023
            right_speed = 1023
        elif fd == min_d:
            left_reverse = False
            right_reverse = False
            left_speed = 1023
            right_speed = 1023
        else:
            left_reverse = True
            right_reverse = True
            left_speed = 1023
            right_speed = 1023
        return True
    
    return False
  
            
def motion():
    driver.motor_controll(
        direction_left=left_reverse,
        direction_right=right_reverse,
        speed_left=left_speed,
        speed_right=right_speed
    )
 
    
def main():
    global left_reverse, right_reverse, left_speed, right_speed
    
    os.dupterm(None, 1)
    while interupt.read() >= 200:
        if not get_black_line():
            if not attack():  # якщо сенсор дистанції вернув None
                left_reverse = True
                right_reverse = False
                left_speed = 300
                right_speed = 300
        
        motion()
  
    uart = UART(0, baudrate=115200)
    os.dupterm(uart, 1)
