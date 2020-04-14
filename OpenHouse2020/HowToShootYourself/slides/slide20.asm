call   r14             ; zavolej HashSHA1.update()
mov    ebx, eax        ; získej návratovou hodnotu - ovšem již bez kontroly
lea    rdi, [rbp-0xf8] ; v každém případě končíme, žádný test podmínky atd.
call   _SSLFreeBuffer

// vůbec se nevolá HashSHA1.final() - volání bylo překladačem optimalizováno
