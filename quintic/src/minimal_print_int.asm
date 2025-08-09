; minimal_print_int.asm
; Prints the integer 42 to stdout using pointer-based decimal conversion

section .data
    buffer times 8 db 0
    msg db "Iteration count: ", 0
    msg_len equ $-msg

section .text
    global _start

_start:
    ; Print label
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, msg_len
    syscall

    mov rbx, 42         ; integer to print
    mov rcx, 10
    lea rsi, [buffer+7] ; pointer to end of buffer
    mov byte [rsi], 10  ; newline
    dec rsi
    mov rax, rbx
    cmp rax, 0
    jne .digits
    mov byte [rsi], '0'
    jmp .done
.digits:
    xor rdx, rdx
    div rcx
    add dl, '0'
    mov byte [rsi], dl
    dec rsi
    cmp rax, 0
    jne .digits
.done:
    inc rsi
    lea rax, [buffer+8]
    sub rax, rsi
    mov rdx, rax
    mov rax, 1
    mov rdi, 1
    syscall

    ; Exit
    mov rax, 60
    xor rdi, rdi
    syscall
