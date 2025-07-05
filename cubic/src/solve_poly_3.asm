; solve_poly_3.asm - Cubic polynomial solver

section .data
    fmt_result db "Cubic root: %.6f", 10, 0

section .text
    global solve_cubic
    extern printf

solve_cubic:
    push rbp
    mov rbp, rsp
    
    mov rdi, fmt_result
    movsd xmm0, xmm1
    mov rax, 1
    call printf
    
    pop rbp
    ret
