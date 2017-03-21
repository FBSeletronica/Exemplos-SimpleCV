'''
DETEC��O DA POSI��O DA FACE NA CAPTURA DA CAMERA

F�BIO B. DE SOUZA

'''


import SimpleCV                 #importa biblioteca do Simple CV
display = SimpleCV.Display()    #tela
cam = SimpleCV.Camera()         #habilita a camera

haarcascade = SimpleCV.HaarCascade('d:/haarcascade_frontalface_alt.xml') #script para detec��o de face

while display.isNotDone():
    image = cam.getImage().flipHorizontal().scale(1)    #captura imagem
    faces = image.findHaarFeatures(haarcascade)         #detecta face
    if faces:                                           #se tiver face
        face = faces.sortArea()                         #pega �rea da face                 
        face.draw(SimpleCV.Color.RED, 2)                #desenha retangulo
        image.show()                                    #exibe imagem
