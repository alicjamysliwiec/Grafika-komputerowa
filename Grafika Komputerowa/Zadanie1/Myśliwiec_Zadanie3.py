#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

w = random.random()
k = random.random()
e = random.random()

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass
    
def prostokat(x, y, a,  b, d=0):
    glClear(GL_COLOR_BUFFER_BIT)
    
    if d!= 0:
        a = a*d
        b = b*d
        
    glColor3f(w,k,e)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(a + x, y)
    glVertex2f(x, b + y)
    glEnd()
    
    glColor3f(e,w,k)
    glBegin(GL_TRIANGLES)
    glVertex2f(a + x, b + y)
    glVertex2f(a + x, y)
    glVertex2f(x, b + y)
    glEnd()

    glFlush()

    
def render(time):
    prostokat(-40.0, -10.0, 5.0, 10.0, 3.0)



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
