import uasyncio as asyncio  
from machine import Pin


class BlackSensor:
    def __init__(self, fr_rh, fr_lf, bk_rh, bk_lf):
        self.fr_rh_pin = Pin(fr_rh, Pin.IN)
        self.fr_lf_pin = Pin(fr_lf, Pin.IN)
        self.bk_rh_pin = Pin(bk_rh, Pin.IN)
        self.bk_lf_pin = Pin(bk_lf, Pin.IN)

    def read_sensors(self):
        return self.fr_rh_pin.value(), self.fr_lf_pin.value(), self.bk_rh_pin.value(), self.bk_lf_pin.value()
