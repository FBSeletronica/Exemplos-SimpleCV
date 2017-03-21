'''
Exercício

Calcula distância entre as laterias de uma estrada

Aluno: Fábio B Souza 

'''


#importa bibliotecas necessárias
from SimpleCV import Image, Color
import math


#função para calcular o X para o ponto Y dado
def calculaX(m, Y, pt1):
    x =  (Y - pt1[1])/m + pt1[0]
    return x
 
img = Image("d:/estrada.jpg")  #carrega imagem a ser analisada
imgBy = img.binarize(90)       #binariza imagem
lines = imgBy.findLines()      #encontra linhas
size = imgBy.size()            #verifica tamanho da imagem

while True:
    question = "Digite o ponto Y (de 130 a 210): "  #imprime mensagem para entrada do Y

    Y = int(raw_input(question))        #le valor informado
    print Y                             #imprime na tela
     
    if Y < 130 or Y > 210:
        print "Erro: Valor fora do limite especificado. Tente novamente"
    else:
        break

    

x1 = x1_temp = 0                    #variáveis auxiliares para varredura do ponto x na linha 1 à esquerda
x2 = x2_temp = size[0]              #variáveis auxiliares para varredura do ponto x na linha 2 à direita


for line1 in lines:                 #varre as linhas
    
    (pt1,pt2) = line1.end_points    #pega os pontos finais da linha

    if line1.angle()> 18 and line1.angle()<28:          #varre linhas entre com angulo de 18 a 28(angulos para linhas da estrada à esquerda)
        imgBy.dl().line(pt1, pt2, Color.BLUE, width = 3) #desenha linha 
        m = math.tan(math.radians(line1.angle()))         #calcula coeficinte angular da reta, através do angulo da mesma
        x2_temp = calculaX(m, Y, pt1)                     #calcula x na reta
        if x2 > x2_temp:                                  #verifica se é o maior x à esquerda
            x2 = x2_temp                                #salva o maior x
        
        

    if line1.angle() >-28 and line1.angle()< -18:           #varre linhas entre com angulo de 18 a 28(angulos para linhas da estrada à direita)
        imgBy.dl().line(pt1, pt2, Color.BLUE, width = 3)    #desenha linha 
        m = math.tan(math.radians(line1.angle()))           #calcula coeficinte angular da reta, através do angulo da mesma
        x1_temp = calculaX(m, Y, pt1)                       #calcula x na reta
        if x1 < x1_temp:                                    #verifica se é o maior x à direita
            x1 = x1_temp                                    #salva o maior x
        



#desenha linha entre os pontos da estrada
img.dl().line((x1, Y), (x2, Y), Color.RED, width = 3)
distancia = x2 - x1     #calcula distância
print "DISTANCIA: ", distancia  #imprime no console
text = "DISTANCIA: " + str(math.ceil(distancia)) #formata string par imprimir na imagem
img.drawText(text,120,220, color=(0,0,255),fontsize = 32);  #imprime valor na imagem
img.show() #Exibe imagem

