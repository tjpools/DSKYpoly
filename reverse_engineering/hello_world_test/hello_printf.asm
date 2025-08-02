; hello_printf.asm - Hello World using printf (nasm, x86-64, Linux)

; hello_printf.asm - Hello World using printf (nasm, x86-64, Linux)
;
; Build:
;   nasm -f elf64 hello_printf.asm -o hello_printf.o
;   gcc hello_printf.o -o hello_printf
;
; Run:
;   ./hello_printf
; This program demonstrates calling the C library printf function from NASM assembly.
; It prints "Hello, world!" followed by a newline to standard output.
; The program uses the System V AMD64 ABI calling convention (Linux x86-64).

section .data
    ; The message to print, null-terminated (required by printf)
    msg db "Hello, world!", 0xA, 0

section .text
    global main        ; Make 'main' visible to linker (entry point for C runtime)
    extern printf      ; Declare the external printf function from libc

main:
    ; Arguments for printf are passed in registers according to the calling convention:
    ;   RDI = pointer to format string (our message)
    mov rdi, msg       ; First argument: pointer to our message
    xor rax, rax       ; Clear RAX (no floating point arguments used)
    call printf        ; Call printf(msg)
    mov eax, 0         ; Return 0 from main (conventional success)
    ret                ; Return to caller (exit program)
