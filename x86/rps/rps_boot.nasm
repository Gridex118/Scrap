[org 0x7c00]

mov BP, 0x8c00
mov SP, BP 

mov dx, welcome_msg
call print_string

%include "rps_utils.nasm"

jmp $
times 510-($$-$) db 0x0000
dw 0xaa55

welcome_msg: 
db "Rock Paper Scissors; 'coz there ain't no need to load any OSs", 0

