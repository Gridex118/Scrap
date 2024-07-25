#include <SDL2/SDL.h>
#include <iostream>

#define SCREEN_WIDTH  640
#define SCREEN_HEIGHT 480

void close_window(SDL_Window *window) {
    SDL_DestroyWindow(window);
    SDL_Quit();
}

int main (int argc, char *argv[]) {
    SDL_Window *window = NULL;
    SDL_Surface *screen_surface = NULL;
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cout << "SDL could not initialize! SDL ERROR: " << SDL_GetError() << '\n';
    } else {
        window = SDL_CreateWindow("SDL", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
        if (window == NULL) {
            std::cout << "Window could not be created! SDL ERROR: " << SDL_GetError() << '\n';
        } else {
            screen_surface = SDL_GetWindowSurface(window);
            SDL_FillRect(screen_surface, NULL, SDL_MapRGB(screen_surface->format, 0x50, 0xFE, 0xF8));
            SDL_UpdateWindowSurface(window);
            // Hack to keep the window up
            SDL_Event e; bool quit = false; while (!quit) { while (SDL_PollEvent(&e)) { if (e.type == SDL_QUIT) quit = true; } }
        }
    }
    close_window(window);
    return 0;
}
