#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Dec 2021 **********************************
#*******************************************************************************
from vpython import *
import numpy as np

#---------------------- Scene Information ----------------------
scene = canvas()
scene.range = 400
scene.height = 1080
scene.width = 1920
scene.fov = pi/6

#---------------------- Changeable Info -------------------------
W = 1200    #Circuit Width
H = 500     #Circuit Height
Nx = 60      #Width in Field Arrows
Ny = 30      #Height in Field Arrows

#---------------------- Draws Objects -------------------------
Wire = curve( color = color.gray(0.7) , radius = 25 ,
              pos = [ vector(W/2,H/2,0), vector(-W/2,H/2,0),
                      vector(-W/2,-H/2,0), vector(W/2,-H/2,0) ,
                      vector(W/2,H/2,0) ] )

LightBulb = sphere( pos = vector(0,H/2,0) , radius = 75 ,
                    color = color.yellow )


Battery = cylinder( pos = vector(0,-H/2,0) , axis = vector(W/2,0,0) ,
                    radius = LightBulb.radius , color = color.blue )
Battery.pos -= Battery.axis/2
BatteryTip = cylinder( pos = vector(0,-H/2,0) , axis = vector(50,0,0) ,
                       radius = LightBulb.radius/2 , color = Battery.color )
BatteryTip.pos -= Battery.axis/2 + BatteryTip.axis/2

#---------------------- Draws Fields -------------------------
def EField_Rod(x,y,a,sideways):
    Ex = 1 / np.sqrt( (x-a)**2 + y**2 ) -  1 / np.sqrt( (x+a)**2 + y**2 )
    Ey = (1/y) * ( (x+a) / np.sqrt( (x+a)**2 + y**2 ) - (x-a) / np.sqrt( (x-a)**2 + y**2 ) )
    if sideways == True:
        E = vector(Ey,Ex,0)
    else:
        E = vector(Ex,Ey,0)
    return E

def BField_Rod(x,y,a):
    B = (1/y) * ( (x+a) / np.sqrt( (x+a)**2 + y**2 ) - (x-a) / np.sqrt( (x-a)**2 + y**2 ) )
    return vector(0,0,B)

for x in np.linspace(-1400,1400,Nx):
    for y in np.linspace(-700,700,Ny):
        
        #Electric Field Arrows
        E = vector(0,0,0)
        if abs( abs(y) - H/2 ) <= Wire.radius and abs(x) <= W/2:
            E = E
        elif abs( abs(x) - W/2 ) <= Wire.radius and abs(y) <= H/2:
            E = E
        else:
            E += EField_Rod( x+W/4  , y+H/2   , W/4     , False )
            E += EField_Rod( y      , x+W/2   , H/2     , True )
            E += EField_Rod( x+W/4  , y-H/2   , W/4     , False )
            E -= EField_Rod( x-W/4  , y-H/2   , W/4     , False )
            E -= EField_Rod( y      , x-W/2   , H/2     , True )
            E -= EField_Rod( x-W/4  , y+H/2   , W/4     , False )
        arrow( pos = vector(x,y,0) , axis = 1000*E , color=color.cyan ,
               headwidth = 400*mag(E) , headlength = 400*mag(E) )
        
        #Magnetic Field Arrows
        B = vector(0,0,0)
        if abs( abs(y) - H/2 ) <= Wire.radius and abs(x) <= W/2:
            B = B
        elif abs( abs(x) - W/2 ) <= Wire.radius and abs(y) <= W/2:
            B = B
        else:
            B += BField_Rod( x , y-H/2 , W/2 )
            B -= BField_Rod( x , y+H/2 , W/2 )
            B += BField_Rod( y , x-W/2 , H/2 )
            B -= BField_Rod( y , x+W/2 , H/2 )
        arrow( pos = vector(x,y,0) , axis = 500*B , color=color.orange ,
               headwidth = 200*mag(B) , headlength = 200*mag(B) )
        
        #Poynting Arrows
        S = cross(E,B)
        arrow( pos = vector(x,y,0) , axis = 2e4*S , color=color.white ,
               headwidth = 4*2e3*mag(S) , headlength = 4*2e3*mag(S) )

#scene.capture("Poynting")
