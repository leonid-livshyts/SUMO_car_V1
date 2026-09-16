from machine import Pin, PWM, UART, ADC
from uasyncio import sleep, run
import os

class MotorDriver:
    def __init__(self,
                 left_pin: int,
                 right_pin: int,
                 left_speed_pin: int,
                 right_speed_pin: int,
                 driver_freq=20000):

        self.left = Pin(left_pin, Pin.OUT)
        self.right = Pin(right_pin, Pin.OUT)

        self.left_speed = PWM(Pin(left_speed_pin), freq=driver_freq)
        self.right_speed = PWM(Pin(right_speed_pin), freq=driver_freq)

    def rotate_left_side(self, direction: bool, speed: int):
        if direction:
            self.left.value(1)
        else:
            self.left.value(0)

        self.left_speed.duty(speed)

    def rotate_right_side(self, direction: bool, speed: int):
        if direction:
            self.right.value(1)

        else:
            self.right.value(0)

        self.right_speed.duty(speed)

    def motor_controll(self, direction_left: bool,
                             direction_right: bool,
                             speed_left: int,
                             speed_right: int):
        self.rotate_left_side(direction=direction_left, speed=speed_left)
        self.rotate_right_side(direction=direction_right, speed=speed_right)
