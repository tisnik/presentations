call   r14       ; call HashSHA1.update()         
mov    ebx, eax  ; return value into register EBX        
test   ebx, ebx  ; test EBX - error or not?
jnz    fail      ; if error: goto fail
jmp    fail      ; and goto fail again, without any test
