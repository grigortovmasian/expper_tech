import os
import time
import RPi.GPIO as gpio


class movement_controller:
    def __init__(self):
        #Port Initialization
        gpio.setmode(gpio.BOARD)
        gpio.setup(21,gpio.OUT)
        gpio.setup(23,gpio.OUT)
        gpio.setup(29,gpio.OUT)
        gpio.setup(31,gpio.OUT)
        gpio.setup(33,gpio.OUT)
        gpio.setup(35,gpio.OUT)
        self.Motor_RearA = gpio.PWM(21,100)        #GPgpio21 as PWM output, with 100Hz frequency
        self.Motor_RearB = gpio.PWM(23,100)        #GPgpio23 as PWM output, with 100Hz frequency
        self.Motor_RightA = gpio.PWM(29,100)        #GPgpio29 as PWM output, with 100Hz frequency
        self.Motor_RightB = gpio.PWM(31,100)        #GPgpio31 as PWM output, with 100Hz frequency
        self.Motor_LeftA = gpio.PWM(33,100)        #GPgpio33 as PWM output, with 100Hz frequency
        self.Motor_LeftB = gpio.PWM(35,100)        #GPgpio35 as PWM output, with 100Hz frequency
        gpio.setwarnings(False)
    def __del__(self):
        gpio.cleanup()

    def move_backward(self,delay):
        self.Motor_RearA.start(0)
        self.Motor_RearB.start(0)
        self.Motor_RightA.start(100)
        self.Motor_RightB.start(0)
        self.Motor_LeftA.start(0)
        self.Motor_LeftB.start(100)
        time.sleep(delay)
        self.stop()


    def move_forward(self,delay):
        self.Motor_RearA.start(0)
        self.Motor_RearB.start(0)
        self.Motor_RightA.start(0)
        self.Motor_RightB.start(100)
        self.Motor_LeftA.start(100)
        self.Motor_LeftB.start(0)
        time.sleep(delay)
        self.stop()

    def rotate_right(self,delay):
        self.Motor_RearA.start(100)
        self.Motor_RearB.start(0)
        self.Motor_RightA.start(100)
        self.Motor_RightB.start(0)
        self.Motor_LeftA.start(100)
        self.Motor_LeftB.start(0)
        time.sleep(delay)
        self.stop()

    def rotate_left(self, delay):
        self.Motor_RearA.start(0)
        self.Motor_RearB.start(100)
        self.Motor_RightA.start(0)
        self.Motor_RightB.start(100)
        self.Motor_LeftA.start(0)
        self.Motor_LeftB.start(100)
        time.sleep(delay)
        self.stop()

    def stop(self):
        self.Motor_RearA.start(0)
        self.Motor_RearB.start(0)
        self.Motor_RightA.start(0)
        self.Motor_RightB.start(0)
        self.Motor_LeftA.start(0)
        self.Motor_LeftB.start(0)

