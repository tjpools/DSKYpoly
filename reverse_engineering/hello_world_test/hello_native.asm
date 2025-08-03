
;***************************************************************************************
; hello_native.asm - Hello World using native Linux syscalls (nasm, x86-64)
;
; Build:
;   nasm -f elf64 hello_native.asm -o hello_native.o
;   ld hello_native.o -o hello_native
;
; Run:
;   ./hello_native
; This program demonstrates a simple "Hello, world!" output using Linux system calls.
; It prints "Hello, world!" followed by a newline to standard output.
;***************************************************************************************
section .data
msg db "Hello, world!", 0xA
len equ $-msg

section .text
global _start

_start:
    mov rax, 1          ; sys_write
    mov rdi, 1          ; file descriptor (stdout)
    mov rsi, msg        ; pointer to message
    mov rdx, len        ; message length
    syscall

    mov rax, 60         ; sys_exit
    xor rdi, rdi        ; exit code 0
    syscall
