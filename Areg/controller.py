from object_recognition import face_detection
import RPi.GPIO as GPIO                    #Import GPIO library

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class controller(metaclass=Singleton):

    def __init__(self):
        self.__in_process = False
        self.__face_detection = face_detection()
    
    def in_process(self):
        return self.__in_process

    def show(self):
        self.__body_detection.show()

    def hide(self):
        self.__body_detection.hide()


    def run(self):  
        self.__in_process = True
        try:
        	self.__face_detection.detect_runtime_and_move()
        except:
            GPIO.cleanup()

c = controller()
c.run()
