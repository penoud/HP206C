#!/usr/bin/env python
# -*- coding: utf-8 -*-
import HPC206
import PyBCM2835

def main():
        myHPC206 = HPC206.HPC206()
        while(1):
                myHPC206.startPTConversion()
                pressure = myHPC206.readPressure()
                temp = myHPC206.readTemp()
                PyBCM2835.delay(1000)
                print "Temp = " + str(temp) + " C, pression = " + str(pressure)


if __name__ == '__main__':
    main()
