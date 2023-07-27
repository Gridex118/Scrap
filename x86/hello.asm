                                                                                                ; Prints Hello World

[org 0x7c00]

                        mov                     AH,                     0x0E                    ; Teletype mode
                        mov                     BX,                     hello                   ; Move starting adress of hello string to bx
START:                  mov                     AL,                     [BX]                    ; Move value stored at adress specified in bx to al
                        cmp                     AL,                     0                     
                        je                      DONE                                            ; End of string reached
                        int                     0x10                                            ; Video services interrupt
                        add                     BX,                     1                       ; Move to next character in the hello string
                        jmp                     START                                           ; Continue the loop

DONE:                   jmp                     $

hello:                  dw                      "Hello World",          0

                        times                   510 - ($-$$)            db 0                    ; Pad the remaining space with 0
                        dw                      0xaa55                                          ; End of boot loader code
