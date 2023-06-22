from vpython import *
from time import *

#this is the temporary fix
c = canvas()

#this is just a scene
def triShaft(length, size, xpos, ypos, zpos, orientation, opacity):
    if orientation == 'up':
        vertexes = [
            vec(xpos,ypos,zpos),
            vec(xpos+size,ypos,zpos),
            vec(xpos+size/2,ypos+(size/2)*1.73205081,zpos),
            vec(xpos,ypos,zpos-length),
            vec(xpos+size,ypos,zpos-length),
            vec(xpos+size/2,ypos+(size/2)*1.73205081,zpos-length)
        ]
    elif orientation == 'down':
        vertexes = [
            vec(xpos,ypos+(size/2)*1.73205081,zpos),
            vec(xpos+size,ypos+(size/2)*1.73205081,zpos),
            vec(xpos+size/2,ypos,zpos),
            vec(xpos,ypos+(size/2)*1.73205081,zpos-length),
            vec(xpos+size,ypos+(size/2)*1.73205081,zpos-length),
            vec(xpos+size/2,ypos,zpos-length)
        ]
    a0 = vertex( pos=vertexes[0] )   
    b0 = vertex( pos=vertexes[1] )
    c0 = vertex( pos=vertexes[2] )

    a1 = vertex( pos=vertexes[3] )   
    b1 = vertex( pos=vertexes[4] )
    c1 = vertex( pos=vertexes[5] )
    
    a0.opacity = opacity
    b0.opacity = opacity
    c0.opacity = opacity

    a1.opacity = opacity
    b1.opacity = opacity
    c1.opacity = opacity

    triangle(v0=a0,v1=b0,v2=c0)
    curve(pos=[vertexes[0],vertexes[1],vertexes[2],vertexes[0]])
    triangle(v0=a1,v1=b1,v2=c1)
    curve(pos=[vertexes[3],vertexes[4],vertexes[5],vertexes[3]])
    quad( vs=[a0,b0,b1,a1] )
    curve(pos=[vertexes[0],vertexes[3]])
    quad( vs=[a0,c0,c1,a1] )
    curve(pos=[vertexes[1],vertexes[4]])
    quad( vs=[c0,b0,b1,c1] )
    curve(pos=[vertexes[2],vertexes[5]])

for k in range(3):

    for i in range(16):
        triShaft(10,1,i,k*-6,0,'up',0.1)
    for i in range(15):
        triShaft(10,1,0.5+i,k*-6,0,'down',0.1)

while True:
    rate(100)