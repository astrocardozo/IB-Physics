from vpython import *

scene = canvas(width=500, height=500,background=color.white)

run = False
def runbutton(b):
    global run
    if run:b.text = 'Run'
    else: b.text = 'Pause'
    run = not run
    
button(text='Run', bind=runbutton)

def Fb(a):
    Fb_mag = rho_w*g*volume
    Fb_dir = norm(vec(0,1,0))
    if (a.x>= -water.size.x/2. and a.x <= water.size.x/2. and a.y>= -water.size.y/2. 
        and a.y <= water.size.y/2. and a.z>= -water.size.z/2. and a.z <= water.size.z/2.):
        Fb_val = Fb_mag*Fb_dir
    else:
        Fb_val = 0*Fb_dir
    return Fb_val

# Define gravitational force

def Fg(r):
    Fg_mag = particle.mass*g
    Fg_dir = norm(vec(0,-1,0))
    Fg_val = Fg_mag*Fg_dir
    return Fg_val

# Defining function to calculate acceleration due to electric force

def acc(a):
    Net_force = Fb(a.pos) + Fg(a.pos)
    return Net_force/a.mass


vy = 0
g=9.8
m_st = 10
rho_st = 1.8E3
rho_w = 1.0E3
t  = 0
dt=0.01
Sim_max = 300

volume = m_st/rho_st


water = box(pos= vector(0,0,0),color=color.blue,size=vector(100,300,100),opacity = 0.5)
particle = sphere(pos=vector(0,200,0),radius=10, mass = m_st, color=color.red, length=10,width=10,height=10,velocity=vector(0,vy,0)
           ,Fg=vector(0,0,0),Fb=vector(0,0,0))
scene.camera.follow(particle)
attach_arrow(particle, "Fg", color=color.orange)
attach_arrow(particle, "Fb", color=color.green)

#Define our live graphs
graph = graph(width=400,height=300,align="left", title='Velocity Vs. Time', xtitle='Time(s)',ytitle='Velocity(m/s)', foreground=color.black, background=color.white)


#Define the curves to which our graphs will draw 
Graph_yvel = gcurve(graph = graph,color=color.blue)

while (particle.pos.y > -water.size.y):
    rate(100)
    if run:
        particle.velocity = particle.velocity + acc(particle)*dt
        particle.pos = particle.pos + particle.velocity*dt
        particle.Fg = Fg(particle.pos)
        particle.Fb = Fb(particle.pos)
        Graph_yvel.plot(pos=(t,particle.velocity.y))
        if (particle.pos.y > Sim_max or particle.pos.y < -Sim_max):  
        # Stop updating position of particle if goes outside region of interest
            break
        t = t+dt