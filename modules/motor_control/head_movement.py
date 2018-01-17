import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library

class head_movement:
    def __init__(self, servo, duty_min, duty_max):
        #servo initialization
        self.SERVO = servo
        self.DUTY_MIN = duty_min
        self.DUTY_MAX= duty_max
        self.DUTY_MID = (self.DUTY_MAX - self.DUTY_MIN)/2+self.DUTY_MIN
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.SERVO, GPIO.OUT)
        self.p = GPIO.PWM(self.SERVO, 50)
        self.curr_pos=90.0
        self.p.start(self.DUTY_MID)
        time.sleep(1)

    def SetAngle(self):
        duty = (self.curr_pos /180)*(self.DUTY_MAX-self.DUTY_MIN) + self.DUTY_MIN
        self.p.ChangeDutyCycle(duty)
    
    def MoveHead(self, dir, speed):
        if dir:
            self.curr_pos += speed
            if self.curr_pos > 180:
                self.curr_pos = 180
                return True
        else:
            self.curr_pos -= speed
            if self.curr_pos < 0:
                self.curr_pos = 0
                return True

        self.SetAngle()
        time.sleep(speed/100)
        return False
