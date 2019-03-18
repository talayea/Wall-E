from OpenGL.GL import*
from OpenGL.GLUT import*
import numpy as np
from math import *

def drawCircle(r=0, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + xc, y + yc)
    glEnd()




def draw():
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)




    for i in (1, -1):
        glColor3f(0.4, 0.5, 0.5)
        glBegin(GL_QUADS)
        glVertex(i * 0.8, -0.8)
        glVertex(i * 0.5, -0.8)
        glVertex(i * 0.5, -0.3)
        glVertex(i * 0.8, -0.3)
        glEnd()

        glColor3f(0.13, 0.27, 0.45)
        glLineWidth(0.1)
        glBegin(GL_LINE_LOOP)
        glVertex(i * 0.8, -0.8)
        glVertex(i * 0.8, -0.3)
        glVertex(i * 0.5, -0.3)
        glVertex(i * 0.5, -0.8)
        glEnd()

        glLineWidth(0.1)
        glBegin(GL_LINES)
        for j in range(0, 9):
            glVertex(i * 0.8, -0.765 + j * (0.8 - 0.3) / 9)
            glVertex(i * 0.5, -0.765 + j * (0.8 - 0.3) / 9)
        glEnd()



        glLineWidth(0.1)
        for ((R, G, B), type) in ( ((0.6, 0.2 , 0.9), GL_POLYGON), ((0.13, 0.27, 0.45), GL_LINE_LOOP)):
            glColor3f(R, G, B)

            glBegin(type)
            glVertex(i * 0.5, -0.65)
            glVertex(i * 0.45, -0.65)
            glVertex(i * 0.45, -0.6)
            glVertex(i * 0.5, -0.6)
            glEnd()

            glBegin(type)
            glVertex(i * 0.45, -0.7)
            glVertex(i * 0.34, -0.7)
            glVertex(i * 0.30, -0.63)
            glVertex(i * 0.30, -0.55)
            glVertex(i * 0.45, -0.55)
            glEnd()


            glBegin(type)
            glVertex(i * 0.30, -0.55)
            glVertex(i * 0.45, -0.55)
            glVertex(i * 0.5, -0.5)
            glVertex(i * 0.5, -0.35)
            glVertex(i * 0.30, -0.35)
            glEnd()




        glColor3f(0.13, 0.27, 0.45)
        drawCircle(0.08, i * 0.1, 0.55)
        glColor3f(1, 1, 1)
        drawCircle(0.065, i * 0.1, 0.55)



    for (R, G, B, type) in ((0.49, 0.56, 0.58, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(-0.45, 0)
        glVertex(-0.45, 0.2)
        glVertex(0.45, 0.2)
        glVertex(0.45, 0)
        glEnd()

    for (R, G, B, type) in ((0.7, 0.5, 0, GL_POLYGON),(0.13, 0.27, 0.45, GL_LINE_LOOP)):
        glColor3f(R, G, B)
        glBegin(type)
        glVertex(0.45, -0.5)
        glVertex(-0.45, -0.5)
        glVertex(-0.45, 0)
        glVertex(0.45, 0)
        glEnd()



        glBegin(type)
        glVertex(-0.1, 0.2)
        glVertex(0.1, 0.2)
        glVertex(0.1, 0.4)
        glVertex(-0.1, 0.4)
        glEnd()

        glBegin(type)
        glVertex(-0.05, 0.4)
        glVertex(0.05, 0.4)
        glVertex(0.05, 0.5)
        glVertex(-0.05, 0.5)
        glEnd()

        glBegin(type)
        glVertex(-0.05, 0.5)
        glVertex(-0.15, 0.6)
        glVertex(-0.15, 0.8)
        glVertex(0.15, 0.8)
        glVertex(0.15, 0.6)
        glVertex(0.05, 0.5)
        glEnd()





    glLineWidth(0.1)
    glColor3f(0.13, 0.27, 0.45)
    for i in (1, -1):
        glBegin(GL_LINES)
        glVertex(i * 0.3, 0)
        glVertex(i * 0.3, 0.2)
        glVertex(i * 0.45, 0.06)
        glVertex(i * 0.3, 0.06)
        glVertex(i * 0.45, 0.14)
        glVertex(i * 0.3, 0.14)
        glEnd()








    glColor3f(0.1, 0.2, 0.6)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = 0.1 * cos(theta)
        y = 0.1 * sin(theta)
        glVertex(x + 0.23, y + 0.75)
    glEnd()



    glColor3f(0.1, 0.2, 0.6)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = 0.1 * cos(theta)
        y = 0.1 * sin(theta)
        glVertex(x - 0.23, y + 0.75)
    glEnd()

    glColor3f(0.1, 0.5, 0.8)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = .05 * cos(theta)
        y = .05 * sin(theta)
        glVertex(x + 0.23, y + 0.75)
    glEnd()

    glColor3f(0.1, 0.5, 0.8)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .0001):  # arange for step not integer
        x = .05 * cos(theta)
        y = .05 * sin(theta)
        glVertex(x - 0.23, y + 0.75)
    glEnd()



    for i in (-1, 1):
        for (R, G, B, type) in ((0.7, 0.5, 0, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
            glColor3f(R, G, B)
            glBegin(type)
            glVertex(i * 0.45, 0.1)
            glVertex(i * 0.45, 0.2)
            glVertex(i * 0.51, 0.15)
            glVertex(i * 0.51, 0.1)
            glEnd()

        glColor3f(0.78, 0.9, 92)
        glBegin(GL_QUADS)
        glVertex(i * 0.25, 0.02)
        glVertex(i * 0.25, 0.1)
        glVertex(i * 0.55, 0.1)
        glVertex(i * 0.55, 0.02)
        glVertex(i * 0.55, 0.02)
        glVertex(i * 0.5, 0.02)
        glVertex(i * 0.5, -0.02)
        glVertex(i * 0.55, -0.02)
        glVertex(i * 0.25, -0.02)
        glVertex(i * 0.55, -0.02)
        glVertex(i * 0.55, -0.1)
        glVertex(i * 0.25, -0.1)
        glEnd()
        glColor3f(0.13, 0.27, 0.45)
        glBegin(GL_LINE_LOOP)
        glVertex(i * 0.25, 0.02)
        glVertex(i * 0.25, 0.1)
        glVertex(i * 0.55, 0.1)
        glVertex(i * 0.55, -0.1)
        glVertex(i * 0.25, -0.1)
        glVertex(i * 0.25, -0.02)
        glVertex(i * 0.5, -0.02)
        glVertex(i * 0.5, 0.02)
        glEnd()

        glBegin(GL_LINES)
        glVertex(i * 0.4, 0.1)
        glVertex(i * 0.4, 0.02)
        glVertex(i * 0.4, -0.1)
        glVertex(i * 0.4, -0.02)
        glEnd()

        for (R, G, B, type) in ((0.78, 0.9, 92, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
            glColor3f(R, G, B)
            glBegin(type)
            glVertex(i * 0.57, 0.06)
            glVertex(i * 0.5, 0.06)
            glVertex(i * 0.5, -0.06)
            glVertex(i * 0.57, -0.06)
            glEnd()

        for (R, G, B, type) in ((0.54, 0.63, 0.65, GL_POLYGON), (0.13, 0.27, 0.45, GL_LINE_LOOP)):
            glColor3f(R, G, B)
            glBegin(type)
            glVertex(i * 0.27, 0.02)
            glVertex(i * 0.5, 0.02)
            glVertex(i * 0.5, -0.02)
            glVertex(i * 0.27, -0.02)
            glEnd()



    glFlush()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(200, 200)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Wall-E")
glutDisplayFunc(draw)
glutMainLoop()