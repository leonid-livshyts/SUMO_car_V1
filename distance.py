from time import sleep_us, sleep  
from machine import Pin, time_pulse_us


class Distance:  
    def __init__(self,
                 trigger_pin: int,
                 echo_pin_forward: int,
                 echo_pin_backward: int,
                 max_distance=50,
                 echo_timeout_us=10000):
                     
        self.max_distance_ = max_distance  
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)  
        self.echo_forward = Pin(echo_pin_forward, mode=Pin.IN, pull=None)  
        self.echo_backward = Pin(echo_pin_backward, mode=Pin.IN, pull=None)  

    def pulse(echo, trigger, echo_timeout_us=10000):  
        trigger.value(0)  
        sleep_us(5)  
        trigger.value(1)  
        sleep_us(10)  
        trigger.value(0)  

        pulse_time = time_pulse_us(echo, 1, echo_timeout_us)
        cms = (pulse_time / 2) / 29.1  
        
        return cms if cms >= 0 else None  
