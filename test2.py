from pyModbusTCP.client import ModbusClient
import time
import cv2
import  numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from pyqt5.pyqt5first import Ui_MainWindow
import sys


#SERVER_HOST = "127.0.1.1"
SERVER_HOST = "192.168.1.1"
SERVER_U_ID = 2
c = ModbusClient(auto_open=True)


c.host(SERVER_HOST)
c.unit_id(SERVER_U_ID)
c.open()

a=np.array(65536)
x1 = c.read_holding_registers(0xf0,1)
x2 = c.read_holding_registers(0xf1,1)

y1 = c.read_holding_registers(0xf2,1)
y2 = c.read_holding_registers(0xf3,1)

z1 = c.read_holding_registers(0xf4,1)
z2 = c.read_holding_registers(0xf5,1)

rx1 = c.read_holding_registers(0xf6,1)
rx2 = c.read_holding_registers(0xf7,1)

ry1 = c.read_holding_registers(0xf8,1)
ry2 = c.read_holding_registers(0xf9,1)

rz1 = c.read_holding_registers(0xfA,1)
rz2 = c.read_holding_registers(0xfB,1)

x=((a*x2)+x1)/1000
y=((a*y2)+y1)/1000
z=((a*z2)+z1)/1000
rx=((a*rx2)+rx1)/1000
ry=((a*ry2)+ry1)/1000
rz=((a*rz2)+rz1)/1000

data = c.write_single_register(0x1100,12)
data = c.read_holding_registers(0x1100,1)
print(data)