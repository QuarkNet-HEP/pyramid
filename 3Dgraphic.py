from vpython import *
from DataReadingv3 import *


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
        self.color = vector(1,1,1)
        self.outline = vector(1,1,1)
        self.lineradius = 0.02
        self.wireframe = []
        self.prism = None

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

        self.wireframe = [l1,l2,l3,l4,l5]
        self.prism = compound([t1,t2,q1,q2,q3])
    
class Sensor():
    def __init__(self, data):
        self.centerx=0
        self.centery=0
        self.centerz=0
        self.planeSpacing=6
        self.moduleSpacing=0.1
        self.gridx=28
        self.gridy=48
        self.xcolor = vector(1,1,1) 
        self.ycolor = vector(1,1,1) 
        self.xtransparency = 0.05
        self.ytransparency = 0.05
        self.xstart = 'down'
        self.ystart = 'down'
        self.data = data
        self.job = []

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

            spacing = 0
            #triangles in the x direction
            for i in range(self.gridx):
                new = triShaft()
                if i%2 != xpattern: new.orientation = "up"
                elif i%2 == xpattern: new.orientation = "down"

                new.length = self.gridy/2 + self.gridy/4 * self.moduleSpacing

                if i>0 and i%4==0: spacing += self.moduleSpacing

                offset = self.centerx-self.gridx/4 + spacing
                new.xpos = offset + i*new.size/2
                
                new.ypos = (1-k)*self.planeSpacing + self.centery
                new.zpos = self.centerz+self.gridy/4
                new.color = self.xcolor
                new.opacity = self.xtransparency
                self.job+=[new]
                self.shafts[k][new.type]+=[new]

            spacing = 0
            #upward triangles in the y direction
            for i in range(self.gridy):
                new = triShaft()
                new.type = 'y'

                if i%2 != ypattern: new.orientation = "up"
                elif i%2 == ypattern: new.orientation = "down"

                new.length = self.gridx/2 + new.size/2 + self.gridx/4 * self.moduleSpacing - self.moduleSpacing

                new.xpos = self.centerz-self.gridx/4
                new.ypos = (1-k)*self.planeSpacing + self.centery + new.size/2

                if i>0 and i%4==0: spacing += self.moduleSpacing
                offset = self.centery-self.gridy/4 + spacing

                new.zpos = offset + i*new.size/2 - new.size/2
                new.color = self.ycolor
                new.opacity = self.ytransparency
                self.job+=[new]
                self.shafts[k][new.type]+=[new]
        
        i = 0
        for obj in self.job:
            obj.render()
            loading.text = "loading (" + str(i) + "/" + str(len(self.job))+")"
            i+=1
        
                  

                

c.lights = []
test = Data()
dtest = test.data
s = Sensor(dtest)
s.xtransparency=1
s.ytransparency=1
s.xstart = 'down'
s.ystart = 'down'

data = Data().data
loading = label(pos = vector(0,0,0), text = "loading", height = 100)
s.render()
loading.visible = False
        


#60 and 100 cm long
#x is long and y is short
#triangles have width 4cm and 2cm high
def clear(highlighted):
    for obj in highlighted: 
        obj.prism.opacity = 0
        obj.prism.color = color.white

clear(s.job)


def load_event(event):
    for obj in s.job: 
        obj.prism.opacity = 0
        obj.prism.color = color.white

    k = 0
    for layer in event:
        i = 0
        for lg in layer:
            
            obj = s.shafts[k]["x"][i]
            obj.prism.opacity = lg/500
            obj.prism.color = color.red  
            i += 1
        k += 1


event_num=0
load_event(data[0])
counter = label(pos=vector(0,0,0), text = "Event 1", xoffset = 100, yoffset = 100)

choices = []
for choice in range(len(data)): choices.append( "Event " + str(choice+1))
def M(m):
    load_event(data[m.index])
    counter.text = "Event " + str(m.index+1)
menu( choices=choices, bind=M )
c.append_to_caption('\n\n')

while True:
    k = keysdown()
    if "right" in k:
        #print(event_num)
        if event_num < len(data)-1: 
            event_num += 1
            counter.text = "Event " + str(event_num+1)
            load_event(data[event_num])
    if "left" in k:
        #print(event_num)
        if event_num > 0: 
            event_num -= 1
            counter.text = "Event " + str(event_num+1)
            load_event(data[event_num])

    rate(100)
    