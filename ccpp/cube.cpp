#define GL_GLEXT_PROTOTYPES
#include <GL/glut.h>
#include <GL/gl.h>
#include <math.h>


// Rotations
double rX = 0;
double rY = 0;

// Vertices
double x = 0.4;
double y = 0.4;
double z = 0.4;


void draw_cube() {
    glClearColor(0.4, 0.4, 0.4, 1.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glLoadIdentity();

    glRotatef(rX, 1.0, 0.0, 0.0);
    glRotatef(rY, 0.0, 1.0, 0.0);

    // Back
    glBegin(GL_TRIANGLES);
        glColor3f(0.4, 0.3, 0.5);
            glVertex3f(x, y, z);
            glVertex3f(x, -y, z);
            glVertex3f(-x, y, z);
    glEnd();
    glBegin(GL_TRIANGLES);
        glColor3f(0.5, 0.3, 0.2);
            glVertex3f(-x, -y, z);
            glVertex3f(x, -y, z);
            glVertex3f(-x, y, z);
    glEnd();

    // Front
    glBegin(GL_TRIANGLES);
        glColor3f(0.1, 0.5, 0.3);
            glVertex3f(-x, y, -z);
            glVertex3f(0, 0, -z);
            glVertex3f(-x, -y, -z);
    glEnd();
    glBegin(GL_TRIANGLES);
        glColor3f(0.0, 0.5, 0.0);
            glVertex3f(-x, -y, -z);
            glVertex3f(0, 0, -z);
            glVertex3f(x, -y, -z);
    glEnd();
    glBegin(GL_TRIANGLES);
        glColor3f(0.1, 0.3, 0.3);
            glVertex3f(-x, y, -z);
            glVertex3f(x, y, -z);
            glVertex3f(0, 0, -z);
    glEnd();
    glBegin(GL_TRIANGLES);
        glColor3f(0.2, 0.2, 0.2);
            glVertex3f(0, 0, -z);
            glVertex3f(x, y, -z);
            glVertex3f(x, -y, -z);
    glEnd();

    // Left
    glBegin(GL_TRIANGLES);
        glColor3f(0.3, 0.5, 0.6);
            glVertex3f(-x, -y, -z);
            glVertex3f(-x, -y, z);
            glVertex3f(-x, y, -z);
    glEnd();
    glBegin(GL_TRIANGLES);
        glColor3f(0.5, 0.5, 0.5);
            glVertex3f(-x, y, z);
            glVertex3f(-x, -y, z);
            glVertex3f(-x, y, -z);
    glEnd();

    // Right
    glBegin(GL_TRIANGLES);
        glColor3f(0.2, 0.2, 0.2);
            glVertex3f(x, y, z);
            glVertex3f(x, y, -z);
            glVertex3f(x, -y, z);
    glEnd();
    glBegin(GL_TRIANGLES);
        glColor3f(0.0, 0.0, 0.0);
            glVertex3f(x, -y, -z);
            glVertex3f(x, y, -z);
            glVertex3f(x, -y, z);
    glEnd();

    // Top
    glBegin(GL_TRIANGLES);
        glColor3f(0.6, 0.0, 0.0);
            glVertex3f(x, y, z);
            glVertex3f(x, y, -z);
            glVertex3f(-x, y, -z);
    glEnd();
    glBegin(GL_TRIANGLES);
        glColor3f(0.6, 0.1, 0.2);
            glVertex3f(-x, y, z);
            glVertex3f(x, y, z);
            glVertex3f(-x, y, -z);
    glEnd();

    // Bottom
    glBegin(GL_TRIANGLES);
        glColor3f(0.4, 0.0, 0.4);
            glVertex3f(-x, -y, -z);
            glVertex3f(-x, -y, z);
            glVertex3f(x, -y, z);
    glEnd();
    glBegin(GL_TRIANGLES);
        glColor3f(0.3, 0.0, 0.3);
            glVertex3f(x, -y, -z);
            glVertex3f(-x, -y, -z);
            glVertex3f(x, -y, z);
    glEnd();

    glFlush();
    glutSwapBuffers();
}

void keyboard(unsigned char key, int x, int y) {
    if (key == 'h') rY += 15;
    else if (key == 'l') rY -= 15;
    else if (key == 'k') rX -= 15;
    else if (key == 'j') rX += 15;
    glutPostRedisplay();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Cube");
    glEnable(GL_DEPTH_TEST);
    glutDisplayFunc(draw_cube);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
    return 0;
}
