from vpython import *
from DataReading import *

#this is the temporary fix
c = canvas(width=1000,height=800)

class triShaft():
    def __init__(self):
        self.type = 'x'
        self.length = 16
        self.size = 1
        self.xpos = 0
        self.ypos = 0
        self.zpos = 0
        self.orientation = 'up'
        self.opacity = 0.05
        self.color = vec(255,255,255)
        self.outline = vec(255,255,255)
        self.lineradius = 0.01
        self.lines = []
        self.surfaces = []
    #this is just a scene
    def render(self):

        shortleg=self.size/2
        longleg=self.size/2
        if self.type == 'x':
            if self.orientation == 'up':
                vertexes = [
                    vec(self.xpos,self.ypos,self.zpos),
                    vec(self.xpos+self.size,self.ypos,self.zpos),
                    vec(self.xpos+shortleg,self.ypos+longleg,self.zpos),
                    vec(self.xpos,self.ypos,self.zpos-self.length),
                    vec(self.xpos+self.size,self.ypos,self.zpos-self.length),
                    vec(self.xpos+shortleg,self.ypos+longleg,self.zpos-self.length)
                ]
            elif self.orientation == 'down':
                vertexes = [
                    vec(self.xpos,self.ypos+longleg,self.zpos),
                    vec(self.xpos+self.size,self.ypos+longleg,self.zpos),
                    vec(self.xpos+shortleg,self.ypos,self.zpos),
                    vec(self.xpos,self.ypos+longleg,self.zpos-self.length),
                    vec(self.xpos+self.size,self.ypos+longleg,self.zpos-self.length),
                    vec(self.xpos+shortleg,self.ypos,self.zpos-self.length)
                ]
        elif self.type == 'y':
            if self.orientation == 'up':
                vertexes = [
                    vec(self.xpos,self.ypos,self.zpos),
                    vec(self.xpos,self.ypos,self.zpos-self.size),
                    vec(self.xpos,self.ypos+longleg,self.zpos-shortleg),
                    vec(self.xpos+self.length,self.ypos,self.zpos),
                    vec(self.xpos+self.length,self.ypos,self.zpos-self.size),
                    vec(self.xpos+self.length,self.ypos+longleg,self.zpos-shortleg),
                ]
            elif self.orientation == 'down':
                vertexes = [
                    vec(self.xpos,self.ypos+longleg,self.zpos),
                    vec(self.xpos,self.ypos+longleg,self.zpos-self.size),
                    vec(self.xpos,self.ypos,self.zpos-shortleg),
                    vec(self.xpos+self.length,self.ypos+longleg,self.zpos),
                    vec(self.xpos+self.length,self.ypos+longleg,self.zpos-self.size),
                    vec(self.xpos+self.length,self.ypos,self.zpos-shortleg),
                ]

        a0 = vertex( pos=vertexes[0] , color=self.color)   
        b0 = vertex( pos=vertexes[1] , color=self.color)
        c0 = vertex( pos=vertexes[2] , color=self.color)

        a1 = vertex( pos=vertexes[3] , color=self.color)   
        b1 = vertex( pos=vertexes[4] , color=self.color)
        c1 = vertex( pos=vertexes[5] , color=self.color)
        
        a0.opacity = self.opacity
        b0.opacity = self.opacity
        c0.opacity = self.opacity

        a1.opacity = self.opacity
        b1.opacity = self.opacity
        c1.opacity = self.opacity
        
        
        t1 = triangle(v0=a0,v1=b0,v2=c0)
        l1 = curve(pos=[vertexes[0],vertexes[1],vertexes[2],vertexes[0]],color=self.outline, radius=self.lineradius)
        t2 = triangle(v0=a1,v1=b1,v2=c1)
        l2 = curve(pos=[vertexes[3],vertexes[4],vertexes[5],vertexes[3]],color=self.outline, radius=self.lineradius)
        q1 = quad( vs=[a0,b0,b1,a1])
        l3 = curve(pos=[vertexes[0],vertexes[3]], color=self.outline, radius=self.lineradius)
        q2 = quad( vs=[a0,c0,c1,a1])
        l4 = curve(pos=[vertexes[1],vertexes[4]],color=self.outline, radius=self.lineradius)
        q3 = quad( vs=[c0,b0,b1,c1])
        l5 = curve(pos=[vertexes[2],vertexes[5]],color=self.outline, radius=self.lineradius)

        self.lines+=[l1,l2,l3,l4,l5]
        self.surfaces+=[t1,t2,q1,q2,q3]
    
class Sensor():
    def __init__(self, data):
        self.centerx=0
        self.centery=0
        self.centerz=0
        self.planeSpacing=6
        self.gridx=28
        self.gridy=48
        self.xcolor = vec(255,0,0) #red
        self.ycolor = vec(0,0,255) #blue
        self.xtransparency = 0.05
        self.ytransparency = 0.05
        self.xstart = 'down'
        self.ystart = 'down'
        self.data = data

        #lists of triangle shaft objects according to layer and type
        self.shafts = {
            0:{
                'x':[],
                'y':[]
            },
            1:{
                'x':[],
                'y':[]
            },
            2:{
                'x':[],
                'y':[]
            }
        }
    
    def render(self):
        for k in range(3):
            xpattern = 1
            if self.xstart == 'down': xpattern = 0
            ypattern = 1
            if self.ystart == 'down': ypattern = 0

            #upward triangles in the x direction
            for i in range(self.gridx//2):
                new = triShaft()
                new.length = self.gridy//2
                new.xpos = self.centerx-self.gridx/4 + i + new.size/2 * (1-xpattern)
                new.ypos = (1-k)*self.planeSpacing + self.centery
                new.zpos = self.centerz+self.gridy/4
                new.color = self.xcolor
                new.opacity = self.xtransparency
                new.render()
                self.shafts[k][new.type]+=[new]
            #downward triangles in the x direction
            for i in range(self.gridx//2):
                new = triShaft()
                new.length = self.gridy//2
                new.orientation = "down"
                new.xpos = self.centerx-self.gridx/4 + i + new.size/2 * xpattern
                new.ypos = (1-k)*self.planeSpacing + self.centery
                new.zpos = self.centerz+self.gridy/4
                new.color = self.xcolor
                new.opacity = self.xtransparency
                new.render()
                self.shafts[k][new.type]+=[new]

            #upward triangles in the y direction
            for i in range(self.gridy//2):
                new = triShaft()
                new.type = 'y'
                new.length = self.gridx//2 + new.size/2
                new.xpos = self.centerz-self.gridx/4
                new.ypos = (1-k)*self.planeSpacing + self.centery + new.size/2
                new.zpos = self.centery-self.gridy/4 + i + new.size * ypattern + new.size
                new.color = self.ycolor
                new.opacity = self.ytransparency
                new.render()
                self.shafts[k][new.type]+=[new]
            #downward triangles in the y direction
            for i in range(self.gridy//2):
                new = triShaft()
                new.type = 'y'
                new.orientation = 'down'
                new.length = self.gridx//2 + new.size/2
                new.xpos = self.centerz-self.gridx/4
                new.ypos = (1-k)*self.planeSpacing + self.centery + new.size/2
                new.zpos = self.centery-self.gridy/4 + i + new.size*1.5
                new.color = self.ycolor
                new.opacity = self.ytransparency
                new.render()
                self.shafts[k][new.type]+=[new]
                

c.lights = []
test = Data()
dtest = test.data
s = Sensor(dtest)
s.xtransparency=0
s.ytransparency=0
s.xstart = 'down'
s.ystart = 'down'

s.render()

s.shafts[0]["x"][0].surfaces[0].opacity = 1
#for surface in s.shafts[0]['x'][0].surfaces:
    #surface.color = vec(255,255,255)
        
#60 and 100 cm long
#x is long and y is short
#triangles have width 4cm and 2cm high
while True:
    rate(100)