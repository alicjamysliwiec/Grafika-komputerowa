#!/usr/bin/env python3
import sys
import math

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

translacja = [0.0, 0.0, 0.0]
viewer = [0.0, 0.0, 10.0]

theta = 0.0
phi = 0.0
theta1 = 0.0
phi1 = 0.0
pix2angle = 1.0

key_A = 0
key_D = 0
key_S = 0
key_UP = 0
key_DOWN = 0
key_1 = 0
key_2 = 0
key_3 = 0

R = 10.0
R_start = 1.0
roznica = 0.0

reset_button_pressed = 0
right_mouse_button_pressed = 0
left_mouse_button_pressed = 0
mouse_x_pos_old = 0
delta_x = 0
mouse_y_pos_old = 0
delta_y = 0


mat_ambient = [1.0, 1.0, 1.0, 1.0]
mat_diffuse = [1.0, 1.0, 1.0, 1.0]
mat_specular = [1.0, 1.0, 1.0, 1.0]
mat_shininess = 20.0

light_ambient = [0.1, 0.1, 0.0, 1.0]
light_diffuse = [0.8, 0.8, 0.0, 1.0]
light_specular = [1.0, 1.0, 1.0, 1.0]
light_position = [0.0, 0.0, 10.0, 1.0]

light_ambient1 = [1.0, 0.3, 0.0, 1.0]
light_diffuse1 = [0.0, 0.2, 0.7, 1.0]
light_specular1 = [0.4, 0.0, 0.8, 1.0]

light_position1 = [10.0, 0.0, 0.0, 1.0]

att_constant = 1.0
att_linear = 0.05
att_quadratic = 0.001

def xeye(R, theta, phi):
    return R * math.cos(theta) * math.cos(phi)

def yeye(R, theta, phi):
    return R * math.sin(phi)
    
def zeye(R, theta, phi):
    return R * math.sin(theta) * math.cos(phi)

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)
    
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular1)
    
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    
def shutdown():
    pass


def render(time):
    global theta
    global phi
    global theta1
    global phi1
    global R
    global R_start
    global roznica

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    gluLookAt(viewer[0], viewer[1], viewer[2],
              0.0, 0.0, 0.0, 0.0, R_start, 0.0)

    if key_1:
        if key_UP:      
            if key_A:
                if(light_ambient1[0] < 1):
                    light_ambient1[0] += 0.1

            if key_D:
                if(light_diffuse1[0] < 1):
                    light_diffuse1[0] += 0.1
           
            if key_S:
                if(light_specular1[0] < 1):
                    light_specular1[0] += 0.1
    
        if key_DOWN:
            if key_A:
                if(light_ambient1[0] > 0):
                    light_ambient1[0] -= 0.1

            if key_D:
                if(light_diffuse1[0] > 0):
                    light_diffuse1[0] -= 0.1
           
            if key_S:
                if(light_specular1[0] > 0):
                    light_specular1 [0] -= 0.1
    if key_2:
        if key_UP:      
            if key_A:
                if(light_ambient1[1] < 1):
                    light_ambient1[1] += 0.1

            if key_D:
                if(light_diffuse1[1] < 1):
                    light_diffuse1[1] += 0.1
           
            if key_S:
                if(light_specular1[1] < 1):
                    light_specular1[1] += 0.1
    
        if key_DOWN:
            if key_A:
                if(light_ambient1[1] > 0):
                    light_ambient1[1] -= 0.1

            if key_D:
                if(light_diffuse1[1] > 0):
                    light_diffuse1[1] -= 0.1
           
            if key_S:
                if(light_specular1[1] > 0):
                    light_specular1[1] -= 0.1                 
    if key_3:
        if key_UP:      
            if key_A:
                if(light_ambient1[2] < 1):
                    light_ambient1[2] += 0.1

            if key_D:
                if(light_diffuse1[2] < 1):
                    light_diffuse1[2] += 0.1
           
            if key_S:
                if(light_specular1[2] < 1):
                    light_specular1[2] += 0.1
    
        if key_DOWN:
            if key_A:
                if(light_ambient1[2] > 0):
                    light_ambient1[2] -= 0.1

            if key_D:
                if(light_diffuse1[2] > 0):
                    light_diffuse1[2] -= 0.1
           
            if key_S:
                if(light_specular1[2] > 0):
                    light_specular1[2] -= 0.1  

    if left_mouse_button_pressed:
        theta += delta_x * pix2angle
        phi += delta_y * pix2angle
    
    if right_mouse_button_pressed:
        theta1 += delta_x * pix2angle
        phi1 += delta_y * pix2angle

    if phi < 0 :
        phi += 2*math.pi
    elif phi >2*math.pi:
        phi +=2*math.pi
   
    if (phi+math.pi/2) %(2*math.pi)> math.pi:
        R_start = -1.0
    else:
        R_start = 1.0
      

    light_position1[0] = xeye(R, theta, phi)
    light_position1[1] = yeye(R, theta, phi)
    light_position1[2] = zeye(R, theta, phi)
    
    light_position[0] = xeye(R, theta1, phi1)
    light_position[1] = yeye(R, theta1, phi1)
    light_position[2] = zeye(R, theta1, phi1)
    
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_FILL)
    gluSphere(quadric, 3.0, 10, 10)
    gluDeleteQuadric(quadric)
    
    quadric = gluNewQuadric()
    gluQuadricDrawStyle(quadric, GLU_LINE)
    gluSphere(quadric, 0.6, 6, 5)
    gluDeleteQuadric(quadric)
                    
    glTranslate(light_position1[0], light_position1[1], light_position1[2])   
    glTranslate(light_position[0], light_position[1], light_position[2])
    
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse1)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient1)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular1)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position1)
    
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    
    
    glFlush()


def update_viewport(window, width, height):
    global pix2angle
    pix2angle = 2*math.pi/ width

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(70, 1.0, 0.1, 300.0)

    if width <= height:
        glViewport(0, int((height - width) / 2), width, width)
    else:
        glViewport(int((width - height) / 2), 0, height, height)
        
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard_key_callback(window, key, scancode, action, mods):
    global key_A
    global key_D
    global key_S
    global key_UP
    global key_DOWN
    global key_1
    global key_2
    global key_3
    global reset_button_pressed
        
    if key == GLFW_KEY_ESCAPE and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)
        
    if key == GLFW_KEY_A and action == GLFW_PRESS:
        key_A = 1
        key_D = 0
        key_S = 0
        
    if key == GLFW_KEY_D and action == GLFW_PRESS:
        key_D = 1
        key_S = 0
        key_A = 0        

    if key == GLFW_KEY_S and action == GLFW_PRESS:
        key_S = 1
        key_D = 0
        key_A = 0

    if key == GLFW_KEY_UP and action == GLFW_PRESS:
        key_UP = 1
    else:
        key_UP = 0
        
    if key == GLFW_KEY_DOWN and action == GLFW_PRESS:
        key_DOWN = 1
    else:
        key_DOWN = 0
        
    if key == GLFW_KEY_Q and action == GLFW_PRESS:
        reset_button_pressed = 1
    else: 
        reset_button_pressed = 0

    if key == GLFW_KEY_1 and action == GLFW_PRESS:
        key_1 = 1
        key_2 = 0
        key_3 = 0
        
    if key == GLFW_KEY_2 and action == GLFW_PRESS:
        key_2 = 1
        key_1 = 0
        key_3 = 0        

    if key == GLFW_KEY_3 and action == GLFW_PRESS:
        key_3 = 1
        key_1 = 0
        key_2 = 0

def mouse_motion_callback(window, x_pos, y_pos):
    global delta_x
    global mouse_x_pos_old
    global delta_y
    global mouse_y_pos_old

    delta_x = x_pos - mouse_x_pos_old
    mouse_x_pos_old = x_pos
    delta_y = y_pos - mouse_y_pos_old
    mouse_y_pos_old = y_pos


def mouse_button_callback(window, button, action, mods):
    global left_mouse_button_pressed
    global right_mouse_button_pressed

    if button == GLFW_MOUSE_BUTTON_LEFT and action == GLFW_PRESS:
        left_mouse_button_pressed = 1
    else:
        left_mouse_button_pressed = 0
        
    if button == GLFW_MOUSE_BUTTON_RIGHT and action == GLFW_PRESS:
        right_mouse_button_pressed = 1
    else:
        right_mouse_button_pressed = 0


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
    glfwSetCursorPosCallback(window, mouse_motion_callback)
    glfwSetMouseButtonCallback(window, mouse_button_callback)
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
