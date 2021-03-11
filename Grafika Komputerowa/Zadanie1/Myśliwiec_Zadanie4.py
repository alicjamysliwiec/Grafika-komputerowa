#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def prostokat(x, y, a, b):
    
    glColor3f(1.0,0.0,0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(a + x, y)
    glVertex2f(x, b + y)
    glEnd()
    
    glColor3f(1.0,0.0,0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(a + x, b + y)
    glVertex2f(a + x, y)
    glVertex2f(x, b + y)
    glEnd()
    
def dywan(x, y, a, b, poziom = 0):
    wysokosc = 1/3 * b
    szerokosc = 1/3 * a
    
    if poziom == 0:
        prostokat(x, y, a, b)
    
    elif poziom > 1:
        dywan(x, y, szerokosc, wysokosc, poziom -1)
        dywan(x + szerokosc, y, szerokosc, wysokosc, poziom -1)
        dywan(x + 2*szerokosc, y, szerokosc, wysokosc, poziom -1)
        dywan(x, y + wysokosc, szerokosc, wysokosc, poziom-1)
        dywan(x, y + 2*wysokosc, szerokosc, wysokosc, poziom -1)
        dywan(x + 2*szerokosc, y + wysokosc, szerokosc, wysokosc, poziom -1)
        dywan(x + 2*szerokosc, y + 2*wysokosc, szerokosc, wysokosc, poziom -1)
        dywan(x + szerokosc, y + 2* wysokosc, szerokosc, wysokosc, poziom -1)
    
    elif poziom == 1:
        prostokat(x, y, szerokosc, wysokosc)
        prostokat(x + szerokosc, y, szerokosc, wysokosc)
        prostokat(x + 2*szerokosc, y, szerokosc, wysokosc)
        prostokat(x, y + wysokosc, szerokosc, wysokosc)
        prostokat(x, y + 2*wysokosc, szerokosc, wysokosc)
        prostokat(x + 2*szerokosc, y + wysokosc, szerokosc, wysokosc)
        prostokat(x + 2*szerokosc, y + 2*wysokosc, szerokosc, wysokosc)
        prostokat(x + szerokosc, y + 2*wysokosc, szerokosc, wysokosc)

    
def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    dywan(-100.0, -80.0, 200.0, 150.0, 4.0)
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
