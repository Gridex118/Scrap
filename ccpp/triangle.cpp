#include <GL/glut.h>
#include <GL/gl.h>

void draw_triangle() {
    glClearColor(0.4, 0, 0.4, 0.1);
    glClear(GL_COLOR_BUFFER_BIT);

    glColor3f(0.5, 0.0, 1.0);
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);

    glBegin(GL_TRIANGLES);
        glVertex3f(-0.7, 0.7, 0);
        glVertex3f(0.7, 0.7, 0);
        glVertex3f(0, -1, 0);
    glEnd();

    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Triangle");
    glutDisplayFunc(draw_triangle);
    glutMainLoop();
    return 0;
}

