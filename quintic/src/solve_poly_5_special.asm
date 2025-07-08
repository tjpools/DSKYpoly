; DSKYpoly-5: Special Cases Solver (Solvable Quintics)
; Mathematical Foundation: Cases that ARE solvable by radicals
; Implementation: 5th roots of unity, factorization detection

section .data
    ; Mathematical constants for solvable cases
    two_pi          dq 6.283185307179586    ; 2π for root calculations
    fifth_pi        dq 1.256637061435917    ; 2π/5 for 5th roots of unity
    tolerance       dq 1.0e-12             ; Zero detection tolerance
    
    ; Debug strings
    debug_special   db "=== Special Cases Solver ===", 10, 0
    debug_monomial  db "Detected: Monomial form x^5 = %.6f", 10, 0
    debug_roots     db "Root %d: %.6f + %.6fi", 10, 0
    debug_binomial  db "Detected: Binomial form x^5 + px + q = 0", 10, 0
    debug_factor    db "Detected: Factorizable form", 10, 0
    debug_general   db "General case: requires numerical methods", 10, 0
    debug_complete  db "=== Special Cases Analysis Complete ===", 10, 0

section .bss
    ; Storage for computed roots (5 complex roots)
    align 16
    roots_real      resq 5    ; Real parts of 5 roots
    roots_imag      resq 5    ; Imaginary parts of 5 roots
    root_count      resq 1    ; Number of roots found
    
    ; Storage for current polynomial coefficients
    coeff_a         resq 1    ; x^5 coefficient
    coeff_b         resq 1    ; x^4 coefficient
    coeff_c         resq 1    ; x^3 coefficient
    coeff_d         resq 1    ; x^2 coefficient
    coeff_e         resq 1    ; x^1 coefficient
    coeff_f         resq 1    ; constant coefficient

section .text
    global solve_poly_5_special
    extern printf
    extern sin, cos, pow, fabs

; Special cases solver for solvable quintics
; Input: Six coefficients in XMM0-XMM5 (a,b,c,d,e,f)
; Returns: Number of roots found and stores them in roots arrays
solve_poly_5_special:
    ; === Function Prologue ===
    push rbp
    mov rbp, rsp
    sub rsp, 48                     ; Stack space aligned to 16 bytes
    
    ; Store coefficients in global variables for easy access
    movsd [coeff_a], xmm0          ; a (x^5)
    movsd [coeff_b], xmm1          ; b (x^4)  
    movsd [coeff_c], xmm2          ; c (x^3)
    movsd [coeff_d], xmm3          ; d (x^2)
    movsd [coeff_e], xmm4          ; e (x^1)
    movsd [coeff_f], xmm5          ; f (constant)
    
    ; Initialize root count
    mov qword [root_count], 0
    
    ; Debug output
    mov rdi, debug_special
    xor eax, eax
    call printf
    
    ; === Case 1: Check for Monomial Form ===
    ; x^5 + f = 0 (b,c,d,e all zero)
    call check_monomial_quintic
    cmp rax, 1
    je monomial_case_detected
    
    ; === Case 2: Check for Binomial Form ===
    ; x^5 + ex + f = 0 (b,c,d zero)
    call check_binomial_quintic
    cmp rax, 1
    je binomial_case_detected
    
    ; === Case 3: Check for Factorizable Form ===
    call check_factorizable_quintic
    cmp rax, 1
    je factorizable_case_detected
    
    ; === General Case ===
    mov rdi, debug_general
    xor eax, eax
    call printf
    jmp special_cases_exit

monomial_case_detected:
    ; Solve x^5 = -f/a using 5th roots of unity
    call solve_monomial_quintic
    jmp special_cases_exit

binomial_case_detected:
    ; Handle binomial case (more complex)
    mov rdi, debug_binomial
    xor eax, eax
    call printf
    jmp special_cases_exit

factorizable_case_detected:
    ; Handle factorizable case
    mov rdi, debug_factor
    xor eax, eax
    call printf
    jmp special_cases_exit

special_cases_exit:
    mov rdi, debug_complete
    xor eax, eax
    call printf
    
    ; Return number of roots found
    mov rax, [root_count]
    
    add rsp, 48
    pop rbp
    ret

; === Helper Functions ===

; Check if quintic is monomial: ax^5 + f = 0
check_monomial_quintic:
    push rbp
    mov rbp, rsp
    
    ; Load tolerance for zero checking
    movsd xmm7, [tolerance]
    
    ; Check if b,c,d,e coefficients are essentially zero
    movsd xmm0, [coeff_b]          ; b coefficient
    call fabs
    ucomisd xmm0, xmm7
    ja not_monomial
    
    movsd xmm0, [coeff_c]          ; c coefficient
    call fabs
    ucomisd xmm0, xmm7
    ja not_monomial
    
    movsd xmm0, [coeff_d]          ; d coefficient
    call fabs
    ucomisd xmm0, xmm7
    ja not_monomial
    
    movsd xmm0, [coeff_e]          ; e coefficient
    call fabs
    ucomisd xmm0, xmm7
    ja not_monomial
    
    ; Monomial form detected
    mov rax, 1
    pop rbp
    ret

not_monomial:
    mov rax, 0
    pop rbp
    ret

; Check if quintic is binomial: ax^5 + ex + f = 0
check_binomial_quintic:
    push rbp
    mov rbp, rsp
    
    ; Load tolerance
    movsd xmm7, [tolerance]
    
    ; Check if b,c,d coefficients are zero
    movsd xmm0, [coeff_b]          ; b coefficient
    call fabs
    ucomisd xmm0, xmm7
    ja not_binomial
    
    movsd xmm0, [coeff_c]          ; c coefficient
    call fabs
    ucomisd xmm0, xmm7
    ja not_binomial
    
    movsd xmm0, [coeff_d]          ; d coefficient
    call fabs
    ucomisd xmm0, xmm7
    ja not_binomial
    
    ; Binomial form detected (e and f can be non-zero)
    mov rax, 1
    pop rbp
    ret

not_binomial:
    mov rax, 0
    pop rbp
    ret

; Check for factorizable forms
check_factorizable_quintic:
    push rbp
    mov rbp, rsp
    
    ; Check if f = 0 (x is a factor)
    movsd xmm0, [coeff_f]          ; f coefficient
    call fabs
    movsd xmm7, [tolerance]
    ucomisd xmm0, xmm7
    jbe factorizable_detected
    
    ; Other factorization checks could go here
    ; (rational root theorem, etc.)
    
    mov rax, 0
    pop rbp
    ret

factorizable_detected:
    mov rax, 1
    pop rbp
    ret

; Solve monomial quintic: x^5 = -f/a
solve_monomial_quintic:
    push rbp
    mov rbp, rsp
    sub rsp, 64
    
    ; Calculate -f/a
    movsd xmm0, [coeff_f]          ; f coefficient
    movsd xmm1, [coeff_a]          ; a coefficient
    
    ; Check for zero divisor
    xorpd xmm2, xmm2
    ucomisd xmm1, xmm2
    je division_by_zero
    
    divsd xmm0, xmm1               ; f/a
    xorpd xmm1, xmm1
    subsd xmm1, xmm0               ; -f/a
    movsd [rsp+0], xmm1            ; Store target value
    
    ; Display the equation being solved
    mov rdi, debug_monomial
    movsd xmm0, [rsp+0]
    mov eax, 1
    call printf
    
    ; Calculate 5th root of absolute value
    movsd xmm0, [rsp+0]
    call fabs                      ; |target|
    
    ; Check if target is zero
    movsd xmm1, [tolerance]
    ucomisd xmm0, xmm1
    jbe zero_target
    
    ; Calculate fifth root: |target|^(1/5)
    movsd xmm1, [five_const]       ; 1/5 = 0.2
    call pow                       ; |target|^(1/5)
    movsd [rsp+8], xmm0            ; Store magnitude
    
    ; Generate 5 roots using 5th roots of unity
    mov r8, 0                      ; Root index
    
root_loop:
    cmp r8, 5
    jge roots_complete
    
    ; Calculate angle: 2π * k / 5
    mov rax, r8
    cvtsi2sd xmm0, rax             ; Convert k to double
    mulsd xmm0, [fifth_pi]         ; k * (2π/5)
    
    ; Calculate cos(angle) and sin(angle)
    movsd [rsp+16], xmm0           ; Save angle
    call cos
    movsd [rsp+24], xmm0           ; Save cos(angle)
    
    movsd xmm0, [rsp+16]           ; Restore angle
    call sin
    movsd [rsp+32], xmm0           ; Save sin(angle)
    
    ; Calculate root: magnitude * (cos + i*sin)
    movsd xmm0, [rsp+8]            ; Load magnitude
    mulsd xmm0, [rsp+24]           ; magnitude * cos
    
    ; Store real part
    lea rax, [roots_real]
    mov rdx, r8
    shl rdx, 3                     ; k * 8 (size of double)
    movsd [rax + rdx], xmm0
    
    ; Calculate imaginary part
    movsd xmm0, [rsp+8]            ; Load magnitude
    mulsd xmm0, [rsp+32]           ; magnitude * sin
    
    ; Store imaginary part
    lea rax, [roots_imag]
    movsd [rax + rdx], xmm0
    
    ; Display root
    mov rdi, debug_roots
    mov rsi, r8
    movsd xmm0, [roots_real + rdx]
    movsd xmm1, [roots_imag + rdx]
    mov eax, 2
    call printf
    
    inc r8
    jmp root_loop

zero_target:
    ; Target is zero, so all roots are zero
    mov r8, 0
zero_loop:
    cmp r8, 5
    jge roots_complete
    
    xorpd xmm0, xmm0
    lea rax, [roots_real]
    mov rdx, r8
    shl rdx, 3
    movsd [rax + rdx], xmm0
    
    lea rax, [roots_imag]
    movsd [rax + rdx], xmm0
    
    inc r8
    jmp zero_loop

division_by_zero:
    ; Handle a=0 case (not actually a quintic)
    mov qword [root_count], 0
    add rsp, 64
    pop rbp
    ret

roots_complete:
    ; Set root count
    mov qword [root_count], 5
    
    add rsp, 64
    pop rbp
    ret

section .rodata
    align 16
    five_const      dq 0.2         ; 1/5 for 5th root calculation
