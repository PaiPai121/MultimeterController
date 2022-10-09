import pyvisa
from pyvisa.constants import *
import xlwt
import time
import os

class Multimeter:
    # 打开万A用表
    def __init__(self, count):
        rm = pyvisa.ResourceManager()
        tupl = rm.list_resources()
        if len(tupl) <= 0:
            print("can not find port !")
        else:
            self.res = rm.open_resource(tupl[count], AccessModes.no_lock, 3000, None)


if __name__ == "__main__":
    # multimeter = Multimeter(1)
    rm = pyvisa.ResourceManager()
    # pyvisa.resources.GPIBInstrument
    # pyvisa.highlevel.ResourceManager.open_resource("USB0::10893")
    print(rm.list_resources())
    inst = rm.open_resource(rm.list_resources()[0])
    # inst = rm.open_resource('GPIB0::12::INSTR')
    # print(inst.query("*IDN?"))
    print(inst.query("*IDN?"))