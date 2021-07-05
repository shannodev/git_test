#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import commands
import math

FLASH_SIZE = 1024
MEM_SIZE = 196
TARGET= sys.argv[1]

def convertBytes(bytes, lst=['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']):
    i = int(math.floor( # 舍弃小数点，取小
             math.log(bytes, 1024) # 求对数(对数：若 a**b = N 则 b 叫做以 a 为底 N 的对数)
            ))

    if i >= len(lst):
        i = len(lst) - 1
    return ('%.2f' + " " + lst) % (bytes/math.pow(1024, i))

PREFIX = 'arm-none-eabi-size'
# The gcc compiler bin path can be either defined in make command via GCC_PATH variable (> make GCC_PATH=xxx)
# either it can be added to the PATH environment variable.

result = os.popen('arm-none-eabi-size ' +TARGET)
r = result.read()
# print r
arr=r.splitlines()[1].split("\t")
# print arr
flash = int(arr[0]) + int(arr[1])
mem = int(arr[1]) + int(arr[2])

flash_size=FLASH_SIZE*1024
mem_size=MEM_SIZE*1024
flash_usage = float(flash*100/flash_size)
mem_usage = float(mem*100/mem_size)
# print ("")
print ("-------------------------------------------------------------")
print ('Flash:  %s / %s , %4.2f%% (.text + .data)'%(convertBytes(flash),convertBytes(flash_size),flash_usage))
print ('SRAM:   %s / %s, %4.2f%% (.data + .bss )'%(convertBytes(mem),convertBytes(mem_size),mem_usage))