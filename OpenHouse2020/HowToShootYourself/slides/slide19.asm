call   r14       ; zavolej HashSHA1.update()         
mov    ebx, eax  ; návratová hodnota do registru EBX        
test   ebx, ebx  ; test EBX na nenulovou hodnotu (došlo k chybě?)
jnz    fail      ; pokud došlo k chybě: goto fail
jmp    fail      ; a znovu skok, tentokrát bez podmínky
