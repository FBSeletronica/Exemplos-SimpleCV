import SimpleCV
from SimpleCV import Camera, Display
from time import sleep


myCamera = Camera(prop_set={'width':320, 'height': 240})
myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
    frame = myCamera.getImage()
    faces = frame.findHaarFeatures('D:\processamentoImagem\haarcascade_frontalface_alt.xml')
    if faces:
        for face in faces:
            print "Face em: " + str(face.coordinates())
    else:
        print "Nenhuma face detectada!."
        frame.save(myDisplay)
        #sleep(.1)
#se ficar lento, retirar o sleep
