; hello_minimal.asm - Minimal x86-64 Linux Hello World (no libc)
; Assembles to <100 bytes

section .data
    msg db "Hello, world!", 10
    len equ $-msg

section .text
    global _start

_start:
    mov rax, 1          ; syscall: write
    mov rdi, 1          ; file descriptor: stdout
    mov rsi, msg        ; pointer to message
    mov rdx, len        ; message length
    syscall

    mov rax, 60         ; syscall: exit
    xor rdi, rdi        ; status 0
    syscall
