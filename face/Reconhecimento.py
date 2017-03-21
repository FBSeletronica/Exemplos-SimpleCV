from SimpleCV import Camera, Color, Display
from time import sleep

myCamera = Camera(prop_set = {'width': 320, 'height':240})
myDisplay = Display(resolution=(320,240))
size  = myCamera.getImage().size()
while not myDisplay.isDone():
    frame = myCamera.getImage()
    faces = frame.findHaarFeatures('D:\processamentoImagem\haarcascade_frontalface_alt.xml')
    if faces:
        for face in faces:
            xy = face.coordinates()
            frame.dl().rectangle((xy[0] - 40, xy[1] - 50), (100,100), Color.GREEN, width = 3)
    else:
        print "Nenhuma face detectada!."
    frame.save(myDisplay)
    sleep(.1)
