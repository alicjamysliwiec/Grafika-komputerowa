#!/usr/bin/env python3
import sys
import math
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

key_1 = 0
key_2 = 0

N = 50
tablica_kolorow = [[[0,0,0] for _ in range(N)] for _ in range(N)]
tablica_wierzcholkow = [[[0,0,0] for _ in range(N)] for _ in range(N)]
tablica_wektorow = [[[0,0,0] for _ in range(N)] for _ in range(N)]

mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient1 = [0.5, 0.8, 1.0, 0.0]
light_diffuse1 = [0.0, 0.0, 1.0, 0.8]
light_specular1 = [0.0, 1.0, 0.0, 1.0]
light_position1 = [1.0, 10.0, 0.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001

yv = 0;

def keyboard_key_callback(window, key, scancode, action, mods):
    global key_1
    global key_2
         
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)
        
    if key == GLFW_KEY_1 and action == GLFW_PRESS:
        key_1 = 1
        
    if key == GLFW_KEY_2 and action == GLFW_PRESS:
        key_1 = 0
        
def x(u,v):
    return (-90 * u**5  + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * (math.cos(math.pi * v))
    
def y(u,v):
    return 160 * u**4 - 320 * u**3 + 160 * u**2
    
def z(u,v):
    return (-90 * u**5 + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * (math.sin(math.pi * v))

def xu(u,v):
    return (-450 * u**4 + 900 * u**3 - 810 * u**2 + 360 * u - 45) * math.cos(math.pi * v)
    
def xv(u,v):
    return math.pi * (90 * u**5 - 225 * u**4 + 270 * u**3 - 180 * u**2 + 45 * u) * math.sin(math.pi * v)

def yu(u,v):
    return 640 * u**3 - 960 * u**2 + 320 * u

def zu(u,v):
    return (-450 * u**4 + 900 * u**3 - 810 * u**2 + 360 * u - 45) * math.sin(math.pi * v)

def zv(u,v):
    return -math.pi * (90 * u**5 - 225 * u**4 + 270 * u**3 - 180 * u**2 + 45 * u) * math.cos(math.pi * v)

def kolorki():
    for u in range(N):
        for v in range(N):
            tablica_kolorow[u][v][0] = random.random()
            tablica_kolorow[u][v][1] = random.random()
            tablica_kolorow[u][v][2] = random.random()
            
def wypelnij_tablice():
    for u in range(N):
        for v in range(N):
            tablica_wierzcholkow[u][v][0] = x(u/N, v/N)
            tablica_wierzcholkow[u][v][1] = y(u/N, v/N)
            tablica_wierzcholkow[u][v][2] = z(u/N, v/N)

def wypelnij_tablice_wektorow():
    for u in range(N):
        for v in range(N):
            tablica_wektorow[u][v][0] = yu(u/N,v/N) * zv(u/N,v/N)
            tablica_wektorow[u][v][1] = zu(u/N,v/N) * xv(u/N,v/N)- xu(u/N,v/N) * zv(u/N,v/N)
            tablica_wektorow[u][v][2] = -yu(u/N,v/N) * xv(u/N,v/N)
            
            dlugosc_kw = tablica_wektorow[u][v][0]**2 + tablica_wektorow[u][v][1]**2 + tablica_wektorow[u][v][2]**2
            dlugosc = dlugosc_kw**(1/2)
            if dlugosc !=0 :
                tablica_wektorow[u][v][0] = tablica_wektorow[u][v][0]/dlugosc
                tablica_wektorow[u][v][1] = tablica_wektorow[u][v][1]/dlugosc
                tablica_wektorow[u][v][2] = tablica_wektorow[u][v][2]/dlugosc
                if u < N/2:
                    tablica_wektorow[u][v][0] *= -1
                    tablica_wektorow[u][v][1] *= -1
                    tablica_wektorow[u][v][2] *= -1  
            else:
                tablica_wektorow[u][v][0] = 0
                tablica_wektorow[u][v][1] = 1
                tablica_wektorow[u][v][2] = 0    

            if u == N/2:
                tablica_wektorow[u][v][0] = 0
                tablica_wektorow[u][v][1] = -1
                tablica_wektorow[u][v][2] = 0                
def jajko():
    
    for u in range(N):
        glBegin(GL_TRIANGLE_STRIP)
        for v in range(N):
            glColor3f(tablica_kolorow[u][v][0], tablica_kolorow[u][v][1], tablica_kolorow[u][v][2])
            glNormal(tablica_wektorow[u][v][0], tablica_wektorow[u][v][1], tablica_wektorow[u][v][2])
            glVertex3f(tablica_wierzcholkow[u][v][0], tablica_wierzcholkow[u][v][1] - 5, tablica_wierzcholkow[u][v][2])
            glColor3f(tablica_kolorow[(u+1) % N][v][0], tablica_kolorow[(u+1)%N][v][1], tablica_kolorow[(u+1)%N][v][2])
            glNormal(tablica_wektorow[(u+1)%N][v][0], tablica_wektorow[(u+1) % N][v][1], tablica_wektorow[(u+1) %N][v][2])
            glVertex3f(tablica_wierzcholkow[(u+1)%N][v][0], tablica_wierzcholkow[(u+1) % N][v][1] - 5, tablica_wierzcholkow[(u+1) %N][v][2])
            
        glColor3f(tablica_kolorow[(N-u) % N][0][0], tablica_kolorow[(N-u) % N][0][1], tablica_kolorow[(N-u) % N][0][2])
        glNormal(tablica_wektorow[(N-u) % N][0][0], tablica_wektorow[(N-u) % N][0][1], tablica_wektorow[(N-u) % N][0][2])    
        glVertex3f(tablica_wierzcholkow[(N-u) % N][0][0], tablica_wierzcholkow[(N-u) % N][0][1] - 5, tablica_wierzcholkow[(N-u) % N][0][2])    
        glColor3f(tablica_kolorow[(N-u - 1) % N][0][0], tablica_kolorow[(N-u - 1) % N][0][1], tablica_kolorow[(N-u - 1) % N][0][2])
        glNormal(tablica_wektorow[(N-u - 1) % N][0][0], tablica_wektorow[(N-u - 1) % N][0][1], tablica_wektorow[(N-u - 1) % N][0][2])
        glVertex3f(tablica_wierzcholkow[(N-u - 1) % N][0][0], tablica_wierzcholkow[(N-u - 1) % N][0][1] - 5, tablica_wierzcholkow[(N-u - 1) % N][0][2])
        glEnd()     
   
def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)
    
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular1)
    
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT1)

def shutdown():
    pass

def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def wektory():
    glBegin(GL_LINES)

    for u in range(N):
        for v in range(N):
            glColor3f(1.0, 1.0, 1.0)
            glVertex3f(tablica_wierzcholkow[u][v][0], tablica_wierzcholkow[u][v][1] - 5, tablica_wierzcholkow[u][v][2])
            glVertex3f(tablica_wektorow[u][v][0] + tablica_wierzcholkow[u][v][0], tablica_wektorow[u][v][1] + tablica_wierzcholkow[u][v][1] - 5, tablica_wektorow[u][v][2] + tablica_wierzcholkow[u][v][2])
    glEnd()

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    
def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180 / math.pi)
    axes()
    
    if key_1:
        jajko()
    else:
        wektory()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSwapInterval(1)
    
    wypelnij_tablice()
    wypelnij_tablice_wektorow()
    kolorki()
    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
