#include <SDL2/SDL.h>
#include <unistd.h>
#include <iostream>

#define WINDOW_WIDTH 640
#define WINDOW_HEIGHT 320

#define PIXEL_SCALE_FACTOR 10
#define SCALE_PX(px) (PIXEL_SCALE_FACTOR * px)

#define WINDOW_UP_HACK SDL_Event e; bool quit = false; while (!quit) { while (SDL_PollEvent(&e)) { if (e.type == SDL_QUIT) quit = true; } }

uint8_t FONT_DATA[] = {
    0xF0, 0x90, 0x90, 0x90, 0xF0,   // 0
    0x20, 0x60, 0x20, 0x20, 0x70,   // 1
    0xF0, 0x10, 0xF0, 0x80, 0xF0,   // 2
    0xF0, 0x10, 0xF0, 0x10, 0xF0,   // 3
    0x90, 0x90, 0xF0, 0x10, 0x10,   // 4
    0xF0, 0x80, 0xF0, 0x10, 0xF0,   // 5
    0xF0, 0x80, 0xF0, 0x90, 0xF0,   // 6
    0xF0, 0x10, 0x20, 0x40, 0x40,   // 7
    0xF0, 0x90, 0xF0, 0x90, 0xF0,   // 8
    0xF0, 0x90, 0xF0, 0x10, 0xF0,   // 9
    0xF0, 0x90, 0xF0, 0x90, 0x90,   // A
    0xE0, 0x90, 0xE0, 0x90, 0xE0,   // B
    0xF0, 0x80, 0x80, 0x80, 0xF0,   // C
    0xE0, 0x90, 0x90, 0x90, 0xE0,   // D
    0xF0, 0x80, 0xF0, 0x80, 0xF0,   // E
    0xF0, 0x80, 0xF0, 0x80, 0x80    // F
};

inline int font_base_index(u_int8_t font) {
    return (5 * font);
}

inline void draw_font(SDL_Renderer *renderer, u_int8_t font) {
    SDL_SetRenderDrawColor(renderer, 0xFF, 0xFF, 0xFF, 0xFF);
    SDL_RenderClear(renderer);
    for (int y = 0; y < 5; y++) {
        for (int x = 0; x < 4; x++) {
            bool to_color = ((FONT_DATA[font_base_index(font) + y] >> (7 - x)) & 1);
            if (to_color) {
                SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0xFF);
                SDL_RenderDrawPoint(renderer, x, y);
            }
        }
    }
    SDL_RenderPresent(renderer);
}

int main(void) { 
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window = SDL_CreateWindow("FONTS", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_SHOWN);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    SDL_RenderSetLogicalSize(renderer, 64, 32);
    // for (int i = 0; i <= 0xf; i++) {
    //     draw_font(renderer, i);
    //     sleep(2);
    // }
    SDL_SetRenderDrawColor(renderer, 0xFF, 0xFF, 0xFF, 0xFF);
    SDL_RenderClear(renderer);
    bool black = false;
    for (int i = 0; i < WINDOW_HEIGHT; ++i) {
        for (int j = 0; j < WINDOW_WIDTH; ++j) {
            if (black) {
                SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0xFF);
                SDL_RenderDrawPoint(renderer, i, j);
            }
            black = !black;
        }
        black = !black;
    }
    SDL_RenderPresent(renderer);
    WINDOW_UP_HACK;
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
