#!/usr/bin/env python3
import sys
import random
import math

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass
    
def trojkat(x, y, a):
         
    glColor3f(1.0, 0.2, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(a + x, y)
    glVertex2f((1/2 * a) + x, (math.sqrt(3) * a * 1/2) + y)
    glEnd()
 

def dywan(x, y, a, poziom = 0):
    dlugosc = 1/2 * a
    
    if poziom == 0:
        trojkat(x, y, a)
    
    elif poziom > 1:
        dywan(x, y, dlugosc, poziom -1)
        dywan(x + dlugosc, y, dlugosc, poziom-1)
        dywan(x + 1/2*dlugosc, y + (dlugosc * math.sqrt(3) * 1/2), dlugosc, poziom -1)
    
    elif poziom == 1:
        trojkat(x, y, dlugosc)
        trojkat(x + dlugosc, y, dlugosc)
        trojkat((1/2 * dlugosc) + x , (math.sqrt(3) * dlugosc * 1/2) + y, dlugosc)


    
def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    dywan(-100.0, -80.0, 200.0, 7.0)
    glFlush()


def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0,
                1.0, -1.0)

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

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main() 
