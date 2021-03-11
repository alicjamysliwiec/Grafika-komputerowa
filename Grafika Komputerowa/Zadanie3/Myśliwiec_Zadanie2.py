#!/usr/bin/env python3
import sys
import math

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

N = 100
tablica_wierzcholkow = [[[0,0,0] for _ in range(N)] for _ in range(N)]

def x(u,v):
    return (-90 * u**5  + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * (math.cos(math.pi * v))
    
def y(u,v):
    return 160 * u**4 - 320 * u**3 + 160 * u**2
    
def z(u,v):
    return (-90 * u**5 + 225 * u**4 - 270 * u**3 + 180 * u**2 - 45 * u) * (math.sin(math.pi * v))

def wypelnij_tablice():
    for u in range(N):
        for v in range(N):
            tablica_wierzcholkow[u][v][0] = x(u/N, v/N)
            tablica_wierzcholkow[u][v][1] = y(u/N, v/N)
            tablica_wierzcholkow[u][v][2] = z(u/N, v/N)

def jajko():
    glBegin(GL_LINES)
    
    for u in range(N):
        for v in range(N):
            glVertex3f(tablica_wierzcholkow[u][v][0], tablica_wierzcholkow[u][v][1] - 5, tablica_wierzcholkow[u][v][2])
            glVertex3f(tablica_wierzcholkow[(u+1) % N][v][0], tablica_wierzcholkow[(u+1) % N][v][1] - 5, tablica_wierzcholkow[(u+1) % N][v][2])
            
    for u in range(N):
        glVertex3f(tablica_wierzcholkow[(N-u) % N][N-1][0], tablica_wierzcholkow[(N-u) % N][N-1][1] - 5, tablica_wierzcholkow[(N-u) % N][N-1][2])
        glVertex3f(tablica_wierzcholkow[u][0][0], tablica_wierzcholkow[u][0][1] - 5, tablica_wierzcholkow[u][0][2])
            
    for u in range(N):
        for v in range(N - 1): 
            glVertex3f(tablica_wierzcholkow[u][v][0], tablica_wierzcholkow[u][v][1] - 5, tablica_wierzcholkow[u][v][2])
            glVertex3f(tablica_wierzcholkow[u][v+1][0], tablica_wierzcholkow[u][v+1][1] - 5, tablica_wierzcholkow[u][v+1][2])
    
    glEnd()
    
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
    spin(time * 180 / math.pi)
    axes()
    jajko()

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
