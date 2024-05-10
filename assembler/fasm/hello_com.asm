format binary as "COM"
org 0x100

        mov     ah,9
        mov     dx,message
        int     21h

        xor     ax, ax
        retn

message db 'Hello world!$'
