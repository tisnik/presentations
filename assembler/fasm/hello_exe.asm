format MZ

        push    cs
        pop     ds
        mov     ah,9
        mov     dx,message
        int     21h

        mov     ax,4C00h
        int     21h

message db 'Hello world!$'
