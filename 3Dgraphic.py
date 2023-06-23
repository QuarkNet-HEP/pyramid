from vpython import *

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
    #this is just a scene
    def render(self):

        shortleg=self.size/2
        longleg=shortleg*1.73205081
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
        
        
        triangle(v0=a0,v1=b0,v2=c0)
        curve(pos=[vertexes[0],vertexes[1],vertexes[2],vertexes[0]],color=self.outline)
        triangle(v0=a1,v1=b1,v2=c1)
        curve(pos=[vertexes[3],vertexes[4],vertexes[5],vertexes[3]],color=self.outline)
        quad( vs=[a0,b0,b1,a1])
        curve(pos=[vertexes[0],vertexes[3]], color=self.outline)
        quad( vs=[a0,c0,c1,a1])
        curve(pos=[vertexes[1],vertexes[4]],color=self.outline)
        quad( vs=[c0,b0,b1,c1])
        curve(pos=[vertexes[2],vertexes[5]],color=self.outline)
    
class Sensor():
    def __init__(self):
        self.centerx=0
        self.centery=0
        self.centerz=0
        self.planeSpacing=6
        self.gridx=7
        self.gridy=12
        self.xcolor = vec(255,0,0) #red
        self.ycolor = vec(0,0,255) #blue
        self.xtransparency = 0.05
        self.ytransparency = 0.05

        #lists of triangle shaft objects according to orientation and type
        #ux = upward triangles for the x-configuration
        #dx = downward triangles for the x-configuration
        #uy = upward triangles for the y-configuration
        #dy = downward triangles for the y-configuration
        self.ux = []
        self.dx = []
        self.uy = []
        self.dy = []
    
    def render(self):
        for k in range(3):
            #upward triangles in the x direction
            for i in range(self.gridx):
                new = triShaft()
                new.length = self.gridy
                new.xpos = self.centerx-self.gridx/2 + i
                new.ypos = (1-k)*self.planeSpacing + self.centery
                new.zpos = self.centerz+self.gridy/2
                new.color = self.xcolor
                new.opacity = self.xtransparency
                new.render()
                self.ux.append(new)
            #downward triangles in the x direction
            for i in range(self.gridx):
                new = triShaft()
                new.length = self.gridy
                new.orientation = "down"
                new.xpos = self.centerx-self.gridx/2 + i + new.size/2
                new.ypos = (1-k)*self.planeSpacing + self.centery
                new.zpos = self.centerz+self.gridy/2
                new.color = self.xcolor
                new.opacity = self.xtransparency
                new.render()
                self.dx.append(new)

            #upward triangles in the y direction
            for i in range(self.gridy):
                new = triShaft()
                new.type = 'y'
                new.length = self.gridx + new.size/2
                new.xpos = self.centerz-self.gridx/2
                new.ypos = (1-k)*self.planeSpacing + self.centery + new.size
                new.zpos = self.centery-self.gridy/2 + i + new.size
                new.color = self.ycolor
                new.opacity = self.ytransparency
                new.render()
                self.uy.append(new)
            #downward triangles in the x direction
            for i in range(self.gridy):
                new = triShaft()
                new.type = 'y'
                new.orientation = 'down'
                new.length = self.gridx + new.size/2
                new.xpos = self.centerz-self.gridx/2
                new.ypos = (1-k)*self.planeSpacing + self.centery + new.size
                new.zpos = self.centery-self.gridy/2 + i + new.size/2
                new.color = self.ycolor
                new.opacity = self.ytransparency
                new.render()
                self.dy.append(new)

c.lights = []

s = Sensor()
s.xtransparency=1
s.ytransparency=1
s.render()


while True:
    rate(100)