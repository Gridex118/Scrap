    SECTION .text
                                                                                                ; executable
                        global                  _start                                          ; this, apparently, defines which label your code starts
                                                                                                ; syscall numbers go to ax register
_start:                 mov                     eax,                    4                       ; syscall for write
                        mov                     ebx,                    1                       ; write to stdout(1)
                        mov                     ecx,                    message                 ; string to output
                        mov                     edx,                    msglen                  ; number of bytes -- size of the string
                        int                     0x80                                            ; call the kernel
                        mov                     eax,                    1                       ; syscall for exit
                        mov                     ebx,                    0                       ; exit code 0
                        int                     0x80

    SECTION .rdata
                                                                                                ; readable writable, not executable
message: db "Hello, World!", 0x0a
msglen: equ $ - message

