call   r14             ; call HashSHA1.update()
mov    ebx, eax        ; return value - without any check!
lea    rdi, [rbp-0xf8] ; no tests again, just leave the function
call   _SSLFreeBuffer

// either HashSHA1.final() is not called (optimized by compiler)
