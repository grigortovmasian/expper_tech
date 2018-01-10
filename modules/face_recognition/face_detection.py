import io
import picamera
import cv2
import numpy

class face_detection(object):
    def __init__(self):
        #Create a me2mory stream so photos doesn't need to be saved in a file
        self.stream = io.BytesIO()
        self.camera = picamera.PiCamera()
        self.camera.resolution = (320, 240)
    def __delete__(self):
        pass
    
    def detect_lower_body(self):
        self.get_pic()
        self.get_opencv()

        #Load a cascade file for detecting faces
        self.face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_lowerbody.xml')

        self.detect_object()
        self.save_pic("lower_body.jpg")

    def detect_eye(self):
        self.get_pic()
        self.get_opencv()

        #Load a cascade file for detecting faces
        self.face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_eye.xml')

        self.detect_object()
        self.save_pic("eye.jpg")

    def detect_upper_body(self):
        self.get_pic()
        self.get_opencv()

        #Load a cascade file for detecting faces
        self.face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_upperbody.xml')

        self.detect_object()
        self.save_pic("upper_body.jpg")

    def detect_full_body(self):
        self.get_pic()
        self.get_opencv()

        #Load a cascade file for detecting faces
        self.face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_fullbody.xml')

        self.detect_object()
        self.save_pic("full_body.jpg")

    def detect_smile(self):
        self.get_pic()
        self.get_opencv()

        #Load a cascade file for detecting faces
        self.face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_smile.xml')

        self.detect_object()
        self.save_pic("smile.jpg")

    def detect_face(self):
        self.get_pic()
        self.get_opencv()

        #Load a cascade file for detecting faces
        self.face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

        self.detect_object()
        self.save_pic("face.jpg")


    #using functions
    def get_pic(self):
        #Get the picture (low resolution, so it should be quite fast)
        #Here you can also specify other parameters (e.g.:rotate the image)
        self.camera.capture(self.stream, format='jpeg')
    
    def get_opencv(self):
        #Convert the picture into a numpy array
        buff = numpy.fromstring(self.stream.getvalue(), dtype=numpy.uint8)
	
        #Now creates an OpenCV image
        self.image = cv2.imdecode(buff, 1)

    def detect_object(self):
        #Convert to grayscale
        gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
	
        #Look for faces in the image using the loaded cascade file
        self.faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
	
        print ("Found "+str(len(self.faces))+" object(s)")
	
        #Draw a rectangle around every found face
        for (x,y,w,h) in self.faces:
            cv2.rectangle(self.image,(x,y),(x+w,y+h),(255,255,0),2)
   

    def save_pic(self, fileName):
        #Save the result image
        cv2.imwrite(fileName,self.image)




