#!/usr/bin/env python3
import sys
import math
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

R = 0.5
r = 0.05
N = 10
d = 20

tablica_wierzcholkow = [[[0,0,0] for _ in range(N)] for _ in range(N)]
tablica_kolorow = [[[0,0,0] for _ in range(N)] for _ in range(N)]

def x(u,v):
    return (R + r * math.cos(2 * math.pi * v)) * math.cos(2 * math.pi * u)
    
def y(u,v):
    return (R + r * math.cos(2 * math.pi * v)) * math.sin(2 * math.pi * u)
    
def z(u,v):
    return r * math.sin(2 * math.pi * v)
    
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


def torus():
    for u in range(N):
        glBegin(GL_TRIANGLE_STRIP)
        for v in range(N):
            glColor3f(tablica_kolorow[u][v][0], tablica_kolorow[u][v][1], tablica_kolorow[u][v][2])
            glVertex3f(tablica_wierzcholkow[u][v][0], tablica_wierzcholkow[u][v][1], tablica_wierzcholkow[u][v][2])
            glColor3f(tablica_kolorow[(u+1) % N][v][0], tablica_kolorow[(u+1)%N][v][1], tablica_kolorow[(u+1)%N][v][2])
            glVertex3f(tablica_wierzcholkow[(u+1)%N][v][0], tablica_wierzcholkow[(u+1) % N][v][1], tablica_wierzcholkow[(u+1) %N][v][2])
        glColor3f(tablica_kolorow[u][0][0], tablica_kolorow[u][0][1], tablica_kolorow[u][0][2])
        glVertex3f(tablica_wierzcholkow[u][0][0], tablica_wierzcholkow[u][0][1], tablica_wierzcholkow[u][0][2]) 
        glColor3f(tablica_kolorow[(u+1) % N][0][0], tablica_kolorow[(u+1) % N][0][1], tablica_kolorow[(u+1)%N][0][2])
        glVertex3f(tablica_wierzcholkow[(u+1)%N][0][0], tablica_wierzcholkow[(u+1)%N][0][1], tablica_wierzcholkow[(u+1)%N][0][2])            
        glEnd()


def lancuch():
    glTranslatef(-5,-5,0)
    for u in range(d):
        glRotatef(90, 0.5, 0.5, 0)
        glTranslatef(0.5,0.5,0)
        torus()



def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


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

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    
def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180 / 3.1415)
    axes()
    lancuch()
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
    glfwSwapInterval(1)
    
    kolorki()
    wypelnij_tablice()
    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
