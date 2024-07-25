#include <SDL2/SDL.h>
#include <iostream>

#define SCREEN_WIDTH 640
#define SCREEN_HEIGHT 420

#define WINDOW_UP_HACK SDL_Event e; bool quit = false; while (!quit) { while (SDL_PollEvent(&e)) { if (e.type == SDL_QUIT) quit = true; } }

int init(SDL_Window **window, SDL_Surface **screen_surface) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        return -1;
    } else {
        *window = SDL_CreateWindow("SDL", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
                SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN
                );
        if (*window == NULL) {
            return -1;
        } else {
            *screen_surface = SDL_GetWindowSurface(*window);
        }
    }
    return 0;
}

int load_media(SDL_Surface **image_surface) {
    *image_surface = SDL_LoadBMP("../herrschers.bmp");
    if (*image_surface == NULL) {
        return -1;
    }
    return 0;
}

void close_window(SDL_Window **window, SDL_Surface **image_surface) {
    SDL_FreeSurface(*image_surface);
    *image_surface = NULL;
    SDL_DestroyWindow(*window);
    *window = NULL;
    SDL_Quit();
}

int main(int argc, char *argv[]) {
    SDL_Window *window = NULL;
    SDL_Surface *screen_surface = NULL;
    SDL_Surface *image_surface = NULL;
    if (init(&window, &screen_surface) == 0) {
        if (load_media(&image_surface) == 0) {
            SDL_BlitSurface(image_surface, NULL, screen_surface, NULL);
            SDL_UpdateWindowSurface(window);
            WINDOW_UP_HACK;
        }
    }
    close_window(&window, &image_surface);
    return 0;
}
