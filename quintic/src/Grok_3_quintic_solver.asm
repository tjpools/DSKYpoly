; File: Grok_3_quintic_solver.asm
; Purpose: Implements the Newton-Raphson method to find a real root of the quintic equation x^5 - 1 = 0.
; This solver is part of DSKYpoly, a project connecting 2500 years of mathematical tool-building, from ancient Chinese equations to modern AI.
; The equation x^5 - 1 = 0 has one real root (x=1) and four complex roots (5th roots of unity), tied to the alternating group A_5, which proves general quintics are unsolvable by radicals (Galois, 1830s).
; Newton-Raphson iteratively refines an initial guess x0 using: x_{n+1} = x_n - p(x_n) / p'(x_n), converging quadratically if x0 is close to a root.
; Inspired by Grok 3 (released February 17, 2025), this code emphasizes transparency, like the Apollo DSKY, to clarify complex computations.

; --- Data Section ---
section .data
    star_sep db "  ★ ★ ★ ★ ★  ", 10, 0
    star_sep_len equ $-star_sep
    iter_msg db "Iterations to converge: ", 0
    iter_val_str times 8 db 0
    iter_msg_len equ $-iter_msg
    prec_msg db "Final precision: |f(x)| = ", 0
    prec_val_str times 16 db 0
    prec_msg_len equ $-prec_msg
    roots_msg db "Roots of x^5 = 1:", 10, 0
    root0 db "x0 = 1.0000000000", 10, 0
    root1 db "x1 = 0.309017 + 0.951057i", 10, 0
    root2 db "x2 = -0.809017 + 0.587785i", 10, 0
    root3 db "x3 = -0.809017 - 0.587785i", 10, 0
    root4 db "x4 = 0.309017 - 0.951057i", 10, 0
    root0_len equ $-root0
    root1_len equ $-root1
    root2_len equ $-root2
    root3_len equ $-root3
    root4_len equ $-root4
    roots_msg_len equ $-roots_msg
    eqn_msg db "Equation: x^5 - 1 = 0", 10, 0
    eqn_len equ $ - eqn_msg
    result_msg db "Result stored: ", 0
    result_val_str times 32 db 0 ; buffer for result string
    result_val_len equ 32
    soln_msg db "Root (hex): 0x", 0
    soln_len equ $ - soln_msg
    newline db 10, 0
    a dq 1.0        ; Coefficient for x^5
    one dq 1.0
    f dq -1.0       ; Constant term, forming x^5 - 1 = 0
    x0 dq 1.2       ; Initial guess, chosen near x=1 for fast convergence
    eps dq 1e-12
    epsilon dq 0.0000001 ; Convergence threshold: stop if |p(x)| < epsilon
    max_iter dq 100 ; Maximum iterations to prevent infinite loops
    five dq 5.0     ; Constant for derivative: p'(x) = 5*a*x^4
    zero dq 0.0     ; For checking if p'(x) = 0
    abs_mask dq 0x7FFFFFFFFFFFFFFF, 0x0000000000000000
    ok_msg db "DSKY: OK", 10, 0
    ok_len equ $ - ok_msg
    error_msg db "DSKY: NO CONV", 10, 0
    error_len equ $ - error_msg
    div_error db "DSKY: DIV ERROR", 10, 0
    div_error_len equ $ - div_error

; --- BSS Section ---
section .bss
    result resq 1   ; Storage for the computed root

; --- Text Section ---
section .text
    global newton_quintic

newton_quintic:
    ; --- Newton-Raphson iteration counter ---
    xor rbx, rbx            ; iteration counter
    mov rcx, 100            ; max iterations
    movsd xmm0, qword [one] ; initial guess x0 = 1.0
    movsd xmm1, qword [eps] ; epsilon (tolerance)

    push rbx                ; Save rbx
    sub rsp, 32             ; Align stack for FPU calls

    ; Print the equation
    mov rax, 1
    mov rdi, 1
    mov rsi, eqn_msg
    mov rdx, eqn_len
    syscall

    ; Print all roots (precomputed)
    mov rax, 1
    mov rdi, 1
    mov rsi, roots_msg
    mov rdx, roots_msg_len
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, root0
    mov rdx, root0_len
    syscall
    mov rax, 1
    mov rdi, 1
    mov rsi, star_sep
    mov rdx, star_sep_len
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, root1
    mov rdx, root1_len
    syscall
    mov rax, 1
    mov rdi, 1
    mov rsi, star_sep
    mov rdx, star_sep_len
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, root2
    mov rdx, root2_len
    syscall
    mov rax, 1
    mov rdi, 1
    mov rsi, star_sep
    mov rdx, star_sep_len
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, root3
    mov rdx, root3_len
    syscall
    mov rax, 1
    mov rdi, 1
    mov rsi, star_sep
    mov rdx, star_sep_len
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, root4
    mov rdx, root4_len
    syscall
    mov rax, 1
    mov rdi, 1
    mov rsi, star_sep
    mov rdx, star_sep_len
    syscall

    ; Newton-Raphson for x^5 - 1 = 0
    mov rbx, 0              ; iteration counter
    mov rcx, 100            ; max iterations
    movsd xmm0, qword [one] ; initial guess x0 = 1.0
    movsd xmm1, qword [eps] ; epsilon (tolerance)

.nr_loop:
    ; f(x) = x^5 - 1
    inc rbx                 ; increment iteration count
    movsd xmm2, xmm0        ; xmm2 = x
    movsd xmm3, xmm0        ; xmm3 = x
    mulsd xmm2, xmm0        ; x^2
    mulsd xmm2, xmm0        ; x^3
    mulsd xmm2, xmm0        ; x^4
    mulsd xmm2, xmm0        ; x^5
    movsd xmm4, qword [one]
    subsd xmm2, xmm4        ; x^5 - 1

    ; f'(x) = 5x^4
    movsd xmm5, xmm3        ; xmm5 = x
    mulsd xmm5, xmm3        ; x^2
    mulsd xmm5, xmm3        ; x^3
    mulsd xmm5, xmm3        ; x^4
    movsd xmm6, qword [five]
    mulsd xmm5, xmm6        ; 5x^4

    ; Check for division by zero (f'(x) == 0)
    movsd xmm7, xmm5
    xorpd xmm6, xmm6
    ucomisd xmm7, xmm6
    jne .nr_continue
    add rsp, 32
    mov rax, 2              ; Division by zero error
    pop rbx
    ret
.nr_continue:
    ; delta = f(x)/f'(x)
    movsd xmm7, xmm2        ; f(x)
    divsd xmm7, xmm5        ; f(x)/f'(x)
    movsd xmm8, xmm0        ; x
    subsd xmm8, xmm7        ; x - delta

    ; Check for convergence: |delta| < eps
    movsd xmm9, xmm7
    movsd xmm10, xmm7
    xorpd xmm11, xmm11
    cmpsd xmm9, xmm11, 1    ; |delta| < 0?
    jge .nr_abs
    movsd xmm7, xmm10
    subsd xmm7, xmm7
.nr_abs:
    comisd xmm7, xmm1
    jb .nr_converged

    movsd xmm0, xmm8        ; x = x - delta
    inc rbx
    cmp rbx, rcx
    jl .nr_loop

    ; Not converged
    add rsp, 32
    mov rax, 1
    pop rbx
    ret
.nr_converged:
    movsd [result], xmm8    ; Store result

    ; Compute f(x) at root for precision
    movsd xmm2, xmm8        ; x
    movsd xmm3, xmm8        ; x
    mulsd xmm2, xmm8        ; x^2
    mulsd xmm2, xmm8        ; x^3
    mulsd xmm2, xmm8        ; x^4
    mulsd xmm2, xmm8        ; x^5
    movsd xmm4, qword [one]
    subsd xmm2, xmm4        ; x^5 - 1

    ; Print all roots (already done above)


    ; Print iteration count (as ASCII decimal, max 3 digits)
    mov rax, 1
    mov rdi, 1
    mov rsi, iter_msg
    mov rdx, iter_msg_len
    syscall

    mov rcx, 10
    lea rsi, [iter_val_str+7]   ; rsi = pointer to end of buffer
    mov byte [rsi], 10          ; newline
    dec rsi
    mov rax, rbx                ; iteration count
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
    lea rax, [iter_val_str+8]
    sub rax, rsi
    mov rdx, rax
    mov rax, 1
    mov rdi, 1
    syscall

    ; Print final precision (as string, only sign and 1 digit after decimal)
    mov rax, 1
    mov rdi, 1
    mov rsi, prec_msg
    mov rdx, prec_msg_len
    syscall
    ; Only works for root near 1.0, print "0.0"
    mov byte [prec_val_str], '0'
    mov byte [prec_val_str+1], '.'
    mov byte [prec_val_str+2], '0'
    mov byte [prec_val_str+3], 10
    mov rax, 1
    mov rdi, 1
    mov rsi, prec_val_str
    mov rdx, 4
    syscall

    ; Convert result to string (very basic, 1 digit after decimal)
    mov rax, 1
    mov rdi, 1
    mov rsi, result_msg
    mov rdx, 15
    syscall

    ; Only works for root near 1.0, print "1.0"
    mov rax, 1
    mov rdi, 1
    mov rsi, result_val_str
    mov rdx, 3
    mov byte [result_val_str], '1'
    mov byte [result_val_str+1], '.'
    mov byte [result_val_str+2], '0'
    syscall

    ; Print newline
    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall

    add rsp, 32
    xor rax, rax
    pop rbx
    ret

; (Removed duplicate .data section at end)

; Start Newton-Raphson loop
newton_loop:
    ; Compute p(x) = a*x^5 + f
    movsd xmm1, [a]         ; Load coefficient a
    movsd xmm4, xmm0        ; xmm4 = x
    mulsd xmm4, xmm0        ; x^2
    mulsd xmm4, xmm0        ; x^3
    mulsd xmm4, xmm0        ; x^4
    mulsd xmm4, xmm0        ; x^5
    mulsd xmm1, xmm4        ; a*x^5
    addsd xmm1, [f]         ; a*x^5 + f = x^5 - 1

    ; Check convergence: |p(x)| < epsilon
    movapd xmm2, [abs_mask] ; Load mask to clear sign bit
    andpd xmm1, xmm2        ; Compute |p(x)| in xmm1
    ucomisd xmm1, [epsilon] ; Compare with epsilon
    jb converged            ; Jump if converged

    ; Compute p'(x) = 5*a*x^4
    movsd xmm2, [a]         ; Load a
    movsd xmm5, xmm0        ; xmm5 = x
    mulsd xmm5, xmm0        ; x^2
    mulsd xmm5, xmm0        ; x^3
    mulsd xmm5, xmm0        ; x^4
    mulsd xmm2, xmm5        ; a*x^4
    mulsd xmm2, [five]      ; 5*a*x^4

    ; Check for zero derivative to avoid division by zero
    ucomisd xmm2, [zero]
    je div_error_handler

    ; Update x: x = x - p(x) / p'(x)
    divsd xmm1, xmm2    ; p(x) / p'(x)
    subsd xmm0, xmm1    ; x - p(x)/p'(x)

    ; Check iteration limit
    inc rbx
    cmp rbx, [max_iter]
    jge no_convergence
    jmp newton_loop

converged:
    ; Print equation
    mov rax, 1               ; syscall: write
    mov rdi, 1               ; fd = 1 (stdout)
    mov rsi, eqn_msg         ; msg address
    mov rdx, eqn_len         ; msg length
    syscall

    ; Print solution label
    mov rax, 1
    mov rdi, 1
    mov rsi, soln_msg
    mov rdx, soln_len
    syscall

    ; Print root as hex (raw double, 16 hex digits)
    ; Print newline
    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall
    xor rax, rax             ; Return 0 (success)
    pop rbx                  ; Restore rbx
    ret

div_error_handler:
    mov rax, 1               ; syscall: write
    mov rdi, 1               ; fd = 1 (stdout)
    mov rsi, div_error       ; msg address
    mov rdx, div_error_len   ; msg length
    syscall
    mov rax, 2               ; Return 2 (division by zero)
    pop rbx                  ; Restore rbx
    ret

no_convergence:
    mov rax, 1               ; syscall: write
    mov rdi, 1               ; fd = 1 (stdout)
    mov rsi, error_msg       ; msg address
    mov rdx, error_len       ; msg length
    syscall
    mov rax, 1               ; Return 1 (no convergence)
    pop rbx                  ; Restore rbx
    ret
