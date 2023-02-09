print_string:
    pusha
    mov ah, 0x0e
    PS_HEAD:
        mov al, [dx]
        int 0x10
        add dx, 1
        cmp [dx], 0
        jne PS_HEAD
    popa
    ret

%include "random.nasm"
