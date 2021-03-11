#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)


    glBegin(GL_TRIANGLES)
    glColor(1.0, 1.0, 0.0)
    glVertex2f(0.0, 0.0)
    glColor(0.0, 1.0, 0.0)
    glVertex2f(0.0, 50.0)
    glColor(0.0, 0.0, 1.0)
    glVertex2f(50.0, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1.0, 1.0, 0.0)
    glVertex2f(0.0, 0.0)
    glColor(0.0, 1.0, 0.0)
    glVertex2f(0.0, 50.0)
    glColor(1.0, 0.0, 0.0)
    glVertex2f(-50.0, 0.0)
    glEnd()
    
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
