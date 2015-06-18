#!/usr/bin/env python
# -*- coding: utf-8 -*-
import HP206C 
import PyBCM2835

def main():
        myHP206C = HP206C.HP206C()

        while(1):
                myHP206C.startPTConversion()
                pressure = myHP206C.readPressure()
                temp = myHP206C.readTemp()
                PyBCM2835.delay(1000)
                print "Temp = " + str(temp) + " C, pression = " + str(pressure)


if __name__ == '__main__':
    main()
