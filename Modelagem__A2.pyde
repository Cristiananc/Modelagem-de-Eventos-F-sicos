x1 = -450
y1 = -300
h = -300
x2 = -92
y2 = -75
x3 = 285
y3 = -75
y4 = -75
m1 = 1  
g = 98
teta = -PI/2
teta2 = 0
teta3 = 0
t0 = millis()/1000.0
R = 225
R2 = 100
R3 = 100
x = 0
y =0
ida = 1


def setup():
    size(900, 600)

def draw():
    global x1, x2, y1, y2, t0, m1, m2, h, teta, R, v1, teta2, aux, y, x, v2, y3, y4, x3, y5,v3, y4,  teta3, R3, ida, fundo
    translate(width/2, height/2)

    #variação do tempo 
    t2 =  millis()/1000.0
    dt = t2 - t0
    t0 = t2
    
    noStroke()
    fill(191, 255, 0)
    ellipse(x1, y1, 20, 20)
    line(-255,0,0,0)
    
    if ida == 1:
        if x1 < -225:
         #atualização da posição e velocidade
         x1 = R*sin(teta) - 225
         y1 = R*cos(teta) - 300
         v1 = sqrt(abs(2*g*(h-y1)))
         teta = teta + v1*dt/R

        elif x1 < -112:
         x1 = x1 + v1*dt
         y1 = -75
        
        elif x1 >= -112 and x2 < 0 and y2 == -75 and x < 1:
         x2 = x2 + v1*dt
         y2 = -75
         v2 = v1

        elif x2 >= 0 and y2 <= 0 and y <= 0:
         x = x + 1
         y3 = y2
         x2 = R2*sin(teta2) 
         y2 = R2*cos(teta2) - 175
         v2 = sqrt(abs(2*((v2**2)/2 + g*y3 - g*y2)))
         teta2 = teta2 + v2*dt/R2

        elif x2 <= 0 and y2 <= 0:
         x = x + 1
         y = y + 1
         y3 = y2
         x2 = R2*sin(teta2) 
         y2 = R2*cos(teta2) - 175
         v2 = sqrt(abs(2*((v2**2)/2 + g*y3 - g*y2)))
         teta2 = teta2 + v2*dt/R2
        
        elif x2 >= 0 and y2 <= 0 and y > 0 and x2<225:
         x2 = x2 + v2*dt
         if x2 > 225:
             x2 = 225
         y2 = -75
    
    #movimento do pêndulo
        elif x2 >= 225 and teta3<=PI/3:
         y5 = y4
         x3 = R3*sin(teta3)+285 
         y4 = R3*cos(teta3)-175
         v2 = sqrt(abs(2*((v2**2)/2 + g*y5 - g*y4)))
         teta3 = teta3 + v2*dt/R2
         if teta3 >= PI/3:
             ida = 0
             
    ##########Volta:
    else:
        #volta: pêndulo
        if x2 >= 225 and teta3>=0:
            y5 = y4
            x3 = R3*sin(teta3)+285 
            y4 = R3*cos(teta3)-175
            v2 = sqrt(abs(2*((v2**2)/2 + g*y5 - g*y4)))
            teta3 = teta3 - v2*dt/R2
            if teta3 < 0:
                x3 = R3*sin(0)+285
                y4 = R3*cos(0)-175
                
        #volta: reta entre o loop e o pêndulo:
        elif x2 >= 0 and y2 < 0 and y > 0 and x2>0: 
          x2 = x2 - v2*dt
          y2 = -75
          
        #volta: loop (meia lua esquerda):
        elif x2 < 0 and y2 <= 0:
            y3 = y2
            x2 = R2*sin(teta2) 
            y2 = R2*cos(teta2) - 175
            v2 = sqrt(abs(2*((v2**2)/2 + g*y3 - g*y2)))
            teta2 = teta2 - v2*dt/R2
            if x2 > 0:
                y = 0
                
        #volta: loop (meia lua direita):
        elif x2 > 0 and y == 0 and teta2 >= 0: 
            y3 = y2
            x2 = R2*sin(teta2) 
            y2 = R2*cos(teta2) - 175
            v2 = sqrt(abs(2*((v2**2)/2 + g*y3 - g*y2)))
            teta2 = teta2 - v2*dt/R2
            
        #volta: reta entre queda e loop:
        # elif x2 < 0 and y == 0 and x2 <:
        #    elif x1 < -112:
        # x1 = x1 + v1*dt
        # y1 = -75
            
            
    #Imagem de fundo
    background(224,255,255)
    
    #imagens
    fundo = loadImage("1.jpg")
    image(fundo, -400, - 200)
    
    #Bolinhas colisão
    ellipse(x1, y1, 20, 20)
    fill(191, 0, 255)
    ellipse(x2, y2, 20, 20)
    
    #Bolinha estática
    fill(75,0,130)
    noStroke()
    ellipse(245, -75,20, 20)
    ellipse(265, -75,20, 20)
        
    #bolinha pêndulo
    ellipse(x3, y4,20,20)
    
    #Trajetória
    noFill()
    stroke(160,82,45)
    strokeWeight(4)
    arc(-230, -290, 450, 450, radians(90), radians(180))
    line(-230, -65, 5 , - 65)
    ellipse(0, -174, 216, 216)
    line(5, -65, 225 , - 65)
    
    #Pêndulo de Newton
    stroke(0)
    strokeWeight(1)
    line(245, -85 , 245, -190)
    line(265, -85 , 265, -190)
    line(x3-10*sin(teta3), y4-10*cos(teta3) ,285,-190)
    fill(165,42,42)
    rect(235, -205, 60 , 15)
    
    #obstáculo:
    rect(361, -147, 85, 15) 
    
