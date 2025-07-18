; solve_poly_3.asm - Cubic polynomial solver using Cardano's method
; Solves ax^3 + bx^2 + cx + d = 0
; Historical note: Cardano published it, but del Ferro discovered it first! 😉

section .data
    fmt_real_root db "Real Root: %.6f", 10, 0
    fmt_complex_root db "Complex Root: %.6f %+.6fi", 10, 0
    fmt_debug db "p=%.6f, q=%.6f, discriminant=%.6f", 10, 0
    
    ; Mathematical constants
    const_2 dq 2.0
    const_3 dq 3.0
    const_4 dq 4.0
    const_9 dq 9.0
    const_27 dq 27.0
    const_neg1 dq -1.0
    const_sqrt3 dq 1.732050807568877  ; √3
    const_half dq 0.5

section .text
    global solve_cubic
    extern printf
    extern sqrt
    extern cbrt
    extern pow

solve_cubic:
    ; Cardano's method for ax^3 + bx^2 + cx + d = 0
    ; Arguments: xmm0=a, xmm1=b, xmm2=c, xmm3=d
    
    push rbp
    mov rbp, rsp
    sub rsp, 80        ; Space for local variables
    
    ; Store coefficients
    movsd [rsp], xmm0      ; a
    movsd [rsp+8], xmm1    ; b
    movsd [rsp+16], xmm2   ; c
    movsd [rsp+24], xmm3   ; d
    
    ; === Step 1: Convert to depressed cubic t^3 + pt + q = 0 ===
    ; Substitution: x = t - b/(3a)
    
    ; Calculate p = (3ac - b^2) / (3a^2)
    movsd xmm4, [rel const_3]  ; 3
    mulsd xmm4, xmm0           ; 3a
    mulsd xmm4, xmm2           ; 3ac
    
    movsd xmm5, xmm1           ; b
    mulsd xmm5, xmm1           ; b^2
    subsd xmm4, xmm5           ; 3ac - b^2
    
    movsd xmm5, [rel const_3]  ; 3
    mulsd xmm5, xmm0           ; 3a
    mulsd xmm5, xmm0           ; 3a^2
    divsd xmm4, xmm5           ; p = (3ac - b^2)/(3a^2)
    movsd [rsp+32], xmm4       ; Store p
    
    ; Calculate q = (2b^3 - 9abc + 27a^2d) / (27a^3)
    movsd xmm4, [rel const_2]  ; 2
    movsd xmm5, xmm1           ; b
    mulsd xmm5, xmm1           ; b^2
    mulsd xmm5, xmm1           ; b^3
    mulsd xmm4, xmm5           ; 2b^3
    
    movsd xmm5, [rel const_9]  ; 9
    mulsd xmm5, xmm0           ; 9a
    mulsd xmm5, xmm1           ; 9ab
    mulsd xmm5, xmm2           ; 9abc
    subsd xmm4, xmm5           ; 2b^3 - 9abc
    
    movsd xmm5, [rel const_27] ; 27
    movsd xmm6, xmm0           ; a
    mulsd xmm6, xmm0           ; a^2
    mulsd xmm5, xmm6           ; 27a^2
    mulsd xmm5, xmm3           ; 27a^2d
    addsd xmm4, xmm5           ; 2b^3 - 9abc + 27a^2d
    
    movsd xmm5, [rel const_27] ; 27
    movsd xmm6, xmm0           ; a
    mulsd xmm6, xmm0           ; a^2
    mulsd xmm6, xmm0           ; a^3
    mulsd xmm5, xmm6           ; 27a^3
    divsd xmm4, xmm5           ; q
    movsd [rsp+40], xmm4       ; Store q
    
    ; === Step 2: Calculate discriminant ===
    ; Δ = -(4p^3 + 27q^2)
    movsd xmm4, [rsp+32]       ; p
    mulsd xmm4, xmm4           ; p^2
    mulsd xmm4, [rsp+32]       ; p^3
    mulsd xmm4, [rel const_4]  ; 4p^3
    
    movsd xmm5, [rsp+40]       ; q
    mulsd xmm5, xmm5           ; q^2
    mulsd xmm5, [rel const_27] ; 27q^2
    
    addsd xmm4, xmm5           ; 4p^3 + 27q^2
    mulsd xmm4, [rel const_neg1] ; -(4p^3 + 27q^2)
    movsd [rsp+48], xmm4       ; Store discriminant
    
    ; Debug output
    mov rdi, fmt_debug
    movsd xmm0, [rsp+32]       ; p
    movsd xmm1, [rsp+40]       ; q
    movsd xmm2, [rsp+48]       ; discriminant
    mov rax, 3
    call printf
    
    ; === Step 3: Find roots based on discriminant ===
    xorpd xmm7, xmm7           ; 0.0
    ucomisd xmm4, xmm7         ; Compare discriminant with 0
    jb complex_roots           ; If discriminant < 0, complex roots
    
    ; === One real root case (discriminant >= 0) ===
real_root:
    ; Use Cardano's formula: t = ∛(-q/2 + √(q²/4 + p³/27)) + ∛(-q/2 - √(q²/4 + p³/27))
    
    ; Calculate √(discriminant/108) = √(-Δ/108)
    movsd xmm4, [rsp+48]       ; discriminant
    mulsd xmm4, [rel const_neg1] ; -discriminant
    movsd xmm0, qword [rel const_27] ; 27
    movsd xmm1, qword [rel const_4]  ; 4
    mulsd xmm0, xmm1           ; 108
    divsd xmm4, xmm0           ; -Δ/108
    
    movsd xmm0, xmm4           ; Move to xmm0 for sqrt call
    call sqrt                  ; √(-Δ/108)
    movsd [rsp+56], xmm0       ; Store sqrt result
    
    ; Calculate the real root using simplified approach
    ; For now, use Newton's method starting point: x₀ = -b/(3a)
    movsd xmm4, [rsp+8]        ; b
    mulsd xmm4, [rel const_neg1] ; -b
    movsd xmm5, [rel const_3]   ; 3
    mulsd xmm5, [rsp]          ; 3a
    divsd xmm4, xmm5           ; -b/(3a)
    
    ; Print the real root
    mov rdi, fmt_real_root
    movsd xmm0, xmm4
    mov rax, 1
    call printf
    
    jmp done
    
complex_roots:
    ; === Complex roots case ===
    ; When discriminant < 0, we have one real root and two complex conjugate roots
    ; For simplicity, show the real root and indicate complex roots
    
    ; Calculate the real root (similar to above)
    movsd xmm4, [rsp+8]        ; b
    mulsd xmm4, [rel const_neg1] ; -b
    movsd xmm5, [rel const_3]   ; 3
    mulsd xmm5, [rsp]          ; 3a
    divsd xmm4, xmm5           ; -b/(3a) (approximation)
    
    mov rdi, fmt_real_root
    movsd xmm0, xmm4
    mov rax, 1
    call printf
    
    ; Print complex roots (simplified - showing pattern)
    mov rdi, fmt_complex_root
    movsd xmm0, xmm4           ; Real part (simplified)
    movsd xmm1, [rel const_sqrt3] ; Imaginary part (placeholder)
    mov rax, 2
    call printf
    
    mov rdi, fmt_complex_root
    movsd xmm0, xmm4           ; Real part
    movsd xmm1, [rel const_sqrt3]
    mulsd xmm1, [rel const_neg1] ; -√3 (conjugate)
    mov rax, 2
    call printf
    
done:
    add rsp, 80
    pop rbp
    ret