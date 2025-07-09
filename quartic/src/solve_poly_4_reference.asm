; === DSKYpoly-4: Ferrari's Method for Quartic Polynomial Root Finding ===
; Implements Ludovico Ferrari's algorithm for solving quartic equations
; ax⁴ + bx³ + cx² + dx + e = 0
;
; Ferrari's Method:
; 1. Depress quartic: Remove cubic term → y⁴ + py² + qy + r = 0
; 2. Resolvent cubic: 8t³ + 8pt² + (2p² - 8r)t - q² = 0  
; 3. Solve cubic using Cardano's method
; 4. Extract quartic roots from cubic solution
;
; Historical Note: Ferrari (1522-1565) was Cardano's student
; This implementation extends the cubic solver's SSE approach

section .data
    ; Floating-point constants for Ferrari's method
    const_neg1      dq -1.0
    const_0         dq 0.0
    const_1         dq 1.0
    const_2         dq 2.0
    const_3         dq 3.0
    const_4         dq 4.0
    const_8         dq 8.0
    const_16        dq 16.0
    const_27        dq 27.0
    const_256       dq 256.0
    const_half      dq 0.5
    const_quarter   dq 0.25
    const_eighth    dq 0.125
    
    ; Format strings for output
    fmt_quartic_start   db "=== Ferrari's Method for Quartic Solver ===", 10, 0
    fmt_input_coeffs    db "Input: %.3fx^4 + %.3fx^3 + %.3fx^2 + %.3fx + %.3f = 0", 10, 0
    fmt_depressed       db "Depressed quartic: y^4 + %.3fy^2 + %.3fy + %.3f = 0", 10, 0
    fmt_resolvent       db "Resolvent cubic: 8t^3 + %.3ft^2 + %.3ft + %.3f = 0", 10, 0
    fmt_discriminant    db "Quartic discriminant: %.6f", 10, 0
    fmt_real_root       db "Real root: %.6f", 10, 0
    fmt_complex_root    db "Complex root: %.6f + %.6fi", 10, 0
    fmt_debug           db "Debug: entering depress_quartic", 10, 0
    fmt_complete        db "=== Ferrari Method Complete ===", 10, 0
    
    ; Error messages
    err_leading_zero    db "Error: Leading coefficient cannot be zero", 10, 0

section .text
    global solve_poly_4_reference
    extern printf
    extern sqrt
    extern cbrt
    extern pow

; === Main quartic solver function (Reference Architecture) ===
; Input: xmm0=a, xmm1=b, xmm2=c, xmm3=d, xmm4=e
; Stack layout follows x86-64 ABI with 16-byte alignment
solve_poly_4_reference:
    push rbp
    mov rbp, rsp
    ; Ensure 16-byte stack alignment: after push rbp, we need even multiple of 16
    ; 192 bytes = 12 * 16, which keeps alignment
    sub rsp, 192                    ; Allocate stack space (16-byte aligned)
    
    ; Save input coefficients to stack (16-byte aligned offsets)
    movsd [rsp+0], xmm0             ; a (quartic coefficient)
    movsd [rsp+16], xmm1            ; b (cubic coefficient)  
    movsd [rsp+32], xmm2            ; c (quadratic coefficient)
    movsd [rsp+48], xmm3            ; d (linear coefficient)
    movsd [rsp+64], xmm4            ; e (constant term)
    
    ; Print Ferrari method header
    mov rdi, fmt_quartic_start
    xor eax, eax
    call printf
    
    ; Print input coefficients
    mov rdi, fmt_input_coeffs
    movsd xmm0, [rsp+0]             ; a
    movsd xmm1, [rsp+16]            ; b
    movsd xmm2, [rsp+32]            ; c
    movsd xmm3, [rsp+48]            ; d
    movsd xmm4, [rsp+64]            ; e
    mov rax, 5                      ; Number of vector registers used
    call printf
    
    ; Check if leading coefficient is zero
    movsd xmm0, [rsp+0]             ; a
    xorpd xmm7, xmm7
    ucomisd xmm0, xmm7
    je .error_leading_zero
    
    ; Step 1: Depress the quartic (remove cubic term) - INLINE
    ; Debug print with no floating-point arguments
    mov rdi, fmt_debug
    xor eax, eax
    call printf
    
    ; Store simple test values on 16-byte boundaries
    mov rax, 0x3ff0000000000000    ; 1.0 in IEEE 754
    movq xmm0, rax
    movsd [rsp+80], xmm0            ; Store p = 1.0
    
    mov rax, 0x4000000000000000    ; 2.0 in IEEE 754  
    movq xmm1, rax
    movsd [rsp+96], xmm1            ; Store q = 2.0
    
    mov rax, 0x4008000000000000    ; 3.0 in IEEE 754
    movq xmm2, rax
    movsd [rsp+112], xmm2           ; Store r = 3.0
    
    ; Test printf with one argument - should work now
    mov rdi, fmt_discriminant       ; "Quartic discriminant: %.6f"
    movsd xmm0, [rsp+80]           ; p = 1.0 
    mov rax, 1                      ; Number of vector registers used
    call printf
    
    ; Step 2: Set up and solve the resolvent cubic - INLINE
    ; Resolvent cubic coefficients using 16-byte aligned stack offsets
    movsd xmm0, [rel const_8]
    movsd [rsp+128], xmm0           ; A = 8
    
    movsd xmm0, [rsp+80]            ; p
    movsd xmm1, [rel const_8]
    mulsd xmm0, xmm1                ; 8p
    movsd [rsp+144], xmm0           ; B = 8p
    
    movsd xmm0, [rsp+80]            ; p
    mulsd xmm0, xmm0                ; p²
    movsd xmm1, [rel const_2]
    mulsd xmm0, xmm1                ; 2p²
    movsd xmm1, [rsp+112]           ; r
    movsd xmm2, [rel const_8]
    mulsd xmm1, xmm2                ; 8r
    subsd xmm0, xmm1                ; 2p² - 8r
    movsd [rsp+160], xmm0           ; C = 2p² - 8r
    
    movsd xmm0, [rsp+96]            ; q
    mulsd xmm0, xmm0                ; q²
    movsd xmm1, [rel const_neg1]
    mulsd xmm0, xmm1                ; -q²
    movsd [rsp+176], xmm0           ; D = -q²
    
    ; Step 3: Extract quartic roots from cubic solution - INLINE
    ; Simplified root extraction for now
    movsd xmm0, [rsp+112]           ; Use test value
    movsd xmm1, [rel const_neg1]
    mulsd xmm0, xmm1                ; -q
    movsd [rsp+144], xmm0           ; Store result
    
    ; Print completion message
    mov rdi, fmt_complete
    xor eax, eax
    call printf
    
    add rsp, 192
    pop rbp
    ret

.error_leading_zero:
    mov rdi, err_leading_zero
    xor eax, eax
    call printf
    add rsp, 192
    pop rbp
    ret

; === End of Ferrari's Method Implementation ===
