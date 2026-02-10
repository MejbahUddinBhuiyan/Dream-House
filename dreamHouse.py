from OpenGL.GL import *    
from OpenGL.GLUT import *   
from OpenGL.GLU import * 
import random
#global variables 
# line_x0 = 20
# line_y0 = 490
# line_x1 = 20
# line_y1 = 450
R,G,B = 0.05, 0.07, 0.15
width = 0.9
wind_effect = 0.0
line_length = 40  
num_drops = 150
cordinates_rains = []
for i in range(num_drops):
    x = random.randint(0, 1000)
    y = random.randint(0, 500)
    sp_list = [0.5,2.0,1.0,1.5]
    speed = random.choice(sp_list) 
    color = random.choice([(0.0, 0.3, 1.0), (0.5, 0.7, 1.0)])  
    cordinates_rains.append([x, y, x, y - line_length, speed, color])


  
def draw_village() :
    #field part start  
    glBegin(GL_TRIANGLES)
    glColor3f(0.55, 0.27, 0.07)
    glVertex2f(0,360) 
    glVertex2f(0,0) 
    glVertex2f(1000,0) 
    glEnd() 
     
    glBegin(GL_TRIANGLES)
    glColor3f(0.55, 0.27, 0.07)
    glVertex2f(1000,360) 
    glVertex2f(0,360) 
    glVertex2f(1000,0) 
    glEnd()  
   #Grass Part Start 

    x0 = 0
    X1 = 66  
    y0 = 280
    y1 = 360

    for i in range(16):
        mid = (x0+X1)/2  
        glBegin(GL_TRIANGLES)
        glColor3f(0.13, 0.55, 0.13)
        glVertex2f(x0,y0)   
        glVertex2f(X1,y0)   
        glVertex2f(mid,y1)      
        glEnd()
        x0 += 66
        X1 += 66
    #House Start  
    glBegin(GL_TRIANGLES)
    glColor3f(0.65, 0.4, 0.65)
    glVertex2f(500,370) 
    glVertex2f(300,280) 
    glVertex2f(700,280) 
    glEnd() 
    
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.96, 0.86)
    glVertex2f(330,280) 
    glVertex2f(330,125) 
    glVertex2f(670,125) 
    glEnd() 
    
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.96, 0.86)
    glVertex2f(670,280) 
    glVertex2f(330,280)  
    glVertex2f(670,125) 
    glEnd()     
    
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(545,230) 
    glVertex2f(455,230)  
    glVertex2f(455,125) 
    glEnd() 
  
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(545,230) 
    glVertex2f(545,125)  
    glVertex2f(455,125) 
    glEnd()   
    
    glLineWidth(3)                
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)              
    glVertex2f(500,230)
    glVertex2f(500,125)
    glEnd()
  
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(420,175) 
    glVertex2f(420,230)  
    glVertex2f(364,230) 
    glEnd()     
    
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(364,230) 
    glVertex2f(364,175)  
    glVertex2f(420,175) 
    glEnd()   
  
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(636,175) 
    glVertex2f(636,230)  
    glVertex2f(580,230)
    glEnd()     
    
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.5)
    glVertex2f(580,230) 
    glVertex2f(580,175)  
    glVertex2f(636,175) 
    glEnd()     

    glLineWidth(3)                
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)              
    glVertex2f(392,175)
    glVertex2f(392,230)
    glEnd()

    glLineWidth(3)                
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)              
    glVertex2f(608,175)
    glVertex2f(608,230)
    glEnd()

    glLineWidth(3)                
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)              
    glVertex2f(420,202.5)
    glVertex2f(364,202.5)
    glEnd()

    glLineWidth(3)                
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)              
    glVertex2f(580,202.5)
    glVertex2f(636,202.5)
    glEnd()
    #House End 


def skycolor(R,G,B):
    glBegin(GL_TRIANGLES)
    glColor3f(R, G, B)

    glVertex2f(0,360) 
    glVertex2f(0,500) 
    glVertex2f(1000,500) 
    glEnd() 
     
    glBegin(GL_TRIANGLES)
    glColor3f(R, G, B)
    glVertex2f(1000,500) 
    glVertex2f(1000,360) 
    glVertex2f(0,360) 
    glEnd()           
  
def raindrops(x0,x1,y0,y1,w,color):
    r,g,b = color     
    glLineWidth(w)                
    glColor3f(r, g, b)
    glBegin(GL_LINES)              
    glVertex2f(x0,y0)
    glVertex2f(x1,y1)
    glEnd()         


def animate():
    global cordinates_rains, line_length ,sp_list,wind_effect
    for i in cordinates_rains:
        speed = i[4]
        i[1] -= speed
        i[3] -= speed
        i[2] = i[0] + wind_effect
        if i[3] < 0:
            i[1] = 500
            i[3] = 500 - line_length
            i[0] = random.randint(0, 1000)
            i[2] = i[0] + wind_effect
            i[4] = random.choice(sp_list)   
            i[5] = random.choice([(0.0, 0.3, 1.0), (0.5, 0.7, 1.0)])  
    glutPostRedisplay()
def keyboard_listener(key, x, y):
    global R,G,B 
    min_R, min_G, min_B = 0.05, 0.07, 0.15 
    max_R, max_G, max_B = 0.35, 0.55, 0.75  
    step = 0.02  
    if key == b'm':
       R = min(R + step, max_R)
       G = min(G + step, max_G)
       B = min(B + step, max_B)
       print("Color Changing to White")
       print(R,G,B)
    elif key == b'n':  
       R = max(R - step, min_R)
       G = max(G - step, min_G)
       B = max(B - step, min_B)
       print("Color Changing to DARK") 
    glutPostRedisplay()          

def special_key_listener(key, x, y):    
    global wind_effect
    maxWind = 30
    if key == GLUT_KEY_RIGHT:
        wind_effect = min(wind_effect + 0.7, maxWind)  
        print("Wind blowing right", wind_effect)
    elif key == GLUT_KEY_LEFT:
        wind_effect = max(wind_effect - 0.7, -maxWind)
        print("Wind blowing left", wind_effect)
    glutPostRedisplay()
          
def setup_projection():
    glViewport(0, 0, 1000, 500)
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    glOrtho(0.0, 1000, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
     

def display():      
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glLoadIdentity()
     setup_projection() 
     skycolor(R,G,B)
     draw_village()
     for i in cordinates_rains:
             raindrops(i[0], i[2], i[1], i[3], width, i[5])                  
     glutSwapBuffers()  
     

def main():
     glutInit()
     glutInitDisplayMode(GLUT_RGBA)
     glutInitWindowSize(1000,500)
     glutInitWindowPosition(450, 250) 
     glutCreateWindow(b"Dream House")
     glutDisplayFunc(display)
     glutIdleFunc(animate)
     glutKeyboardFunc(keyboard_listener)
     glutSpecialFunc(special_key_listener)  
     glutMainLoop() 
     

if __name__ == '__main__':
     main()
     