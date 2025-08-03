; hello_flat.asm - Minimal flat binary Hello World (x86-64 Linux, no ELF)
; Assembles to a raw binary (not ELF). Run in an emulator or with a custom loader.
; To assemble: nasm -f bin hello_flat.asm -o hello_flat.bin

BITS 64
ORG 0x400000 ; Typical Linux x86-64 base address for code

section .data
msg db "Hello, world!", 0xA
len equ $-msg

section .text
start:
    mov rax, 1          ; sys_write
    mov rdi, 1          ; file descriptor (stdout)
    mov rsi, msg        ; pointer to message
    mov rdx, len        ; message length
    syscall

    mov rax, 60         ; sys_exit
    xor rdi, rdi        ; exit code 0
    syscall
