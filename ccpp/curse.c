#include <ncurses.h>
#include <stdlib.h>

int main() {
    initscr();
    start_color();
    init_pair(1, COLOR_CYAN, COLOR_RED);
    init_pair(2, COLOR_CYAN, COLOR_CYAN);
    WINDOW *screen = newwin(20, 36, 10, 15);
    WINDOW *screen2 = newwin(5, 25, 3, 10);
    wbkgd(screen, COLOR_PAIR(1));
    wbkgd(screen2, COLOR_PAIR(1));
    bkgd(COLOR_PAIR(2));
    wattron(screen, COLOR_PAIR(1));
    wattron(screen2, COLOR_PAIR(1));
    wmove(screen, 4, 3);
    wmove(screen2, 2, 3);
    wprintw(screen2, "Nuff Said");
    wprintw(screen, "Hello world!");
    refresh();
    wrefresh(screen2);
    wrefresh(screen);
    wattroff(screen, COLOR_PAIR(1));
    wgetch(screen);
    endwin();
    return 0;
}
