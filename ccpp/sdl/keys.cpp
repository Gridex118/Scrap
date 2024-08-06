#include <SDL2/SDL.h>
#include <iostream>
#include <unordered_map>

std::unordered_map<u_int8_t, int> KEYS = {
    {SDLK_1, 0x1}, {SDLK_2, 0x2},
    {SDLK_3, 0x3}, {SDLK_4, 0xc},
    {SDLK_q, 0x4}, {SDLK_w, 0x5},
    {SDLK_e, 0x6}, {SDLK_r, 0xd},
    {SDLK_a, 0x7}, {SDLK_s, 0x8},
    {SDLK_d, 0x9}, {SDLK_f, 0xe},
    {SDLK_z, 0xa}, {SDLK_x, 0x0},
    {SDLK_c, 0xb}, {SDLK_v, 0xf}
};

int main(void) {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window;
    SDL_Renderer *renderer;
    SDL_CreateWindowAndRenderer(640, 320, SDL_WINDOW_SHOWN, &window, &renderer);
    SDL_SetRenderDrawColor(renderer, 0xA0, 0x0F, 0x55, 0xFF);
    SDL_RenderClear(renderer);
    SDL_RenderPresent(renderer);
    SDL_Event event;
    bool quit = false;
    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = true;
            } else if (event.type == SDL_KEYDOWN) {
                std::cout << "Pressed: " << KEYS[event.key.keysym.sym] << '\n';
            }
        }
    }
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
