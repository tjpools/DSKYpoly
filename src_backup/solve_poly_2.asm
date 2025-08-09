;**************************************************************************
; solve_poly_2.asm
; Robust quadratic solver for ax^2 + bx + c = 0
; Accepts inputs from C, returns real and imaginary parts of both roots
;**************************************************************************

section .text
    global solve_poly_2

solve_poly_2:
    ; Arguments (System V AMD64):
    ; xmm0 = a, xmm1 = b, xmm2 = c
    ; rdi = &r1_real, rsi = &r1_imag
    ; rdx = &r2_real, rcx = &r2_imag

    ; Save inputs to stack for FPU access
    sub rsp, 32
    movsd qword [rsp], xmm0    ; a
    movsd qword [rsp+8], xmm1  ; b
    movsd qword [rsp+16], xmm2 ; c

    ; === Compute Discriminant: D = b^2 - 4ac ===
    ; Load and compute b^2
    fld qword [rsp+8]          ; ST0 = b
    fmul st0, st0              ; ST0 = b^2
    
    ; Load a and c, compute 4ac
    fld qword [rsp]            ; ST0 = a, ST1 = b^2
    fld qword [rsp+16]         ; ST0 = c, ST1 = a, ST2 = b^2
    fmul st0, st1              ; ST0 = ac, ST1 = a, ST2 = b^2
    
    ; Multiply ac by 4
    fld1                       ; ST0 = 1, ST1 = ac, ST2 = a, ST3 = b^2
    fadd st0, st0              ; ST0 = 2, ST1 = ac, ST2 = a, ST3 = b^2
    fadd st0, st0              ; ST0 = 4, ST1 = ac, ST2 = a, ST3 = b^2
    fmul st0, st1              ; ST0 = 4ac, ST1 = ac, ST2 = a, ST3 = b^2
    
    ; Compute discriminant: b^2 - 4ac
    fld st3                    ; ST0 = b^2, ST1 = 4ac, ST2 = ac, ST3 = a, ST4 = b^2
    fsub st0, st1              ; ST0 = b^2 - 4ac = D, ST1 = 4ac, ST2 = ac, ST3 = a, ST4 = b^2
    
    ; Store discriminant temporarily
    fst qword [rsp+24]         ; Store D at [rsp+24]
    
    ; Clean up stack completely
    fstp st0                   ; Pop D
    fstp st0                   ; Pop 4ac  
    fstp st0                   ; Pop ac
    fstp st0                   ; Pop a
    fstp st0                   ; Pop b^2
    
    ; Reload discriminant
    fld qword [rsp+24]         ; ST0 = D

    ; Duplicate D for comparison
    fld st0                    ; ST0 = D, ST1 = D

    ; === Check if D < 0 ===
    ftst                       ; Compare ST0 (which is D) with 0
    fstsw ax                   ; Store FPU status word in AX
    sahf                       ; Load status flags from AH
    jb .complex_roots          ; If D < 0, jump to complex roots
    ; D >= 0, continue to real roots

.real_roots:
    ; === Compute sqrt(D) ===
    fsqrt                          ; ST0 = sqrt(D)

    ; === Compute -b / 2a (common term) ===
    fld qword [rsp+8]              ; ST0 = b, ST1 = sqrt(D)
    fchs                           ; ST0 = -b, ST1 = sqrt(D)
    fld qword [rsp]                ; ST0 = a, ST1 = -b, ST2 = sqrt(D)
    fadd st0, st0                  ; ST0 = 2a, ST1 = -b, ST2 = sqrt(D)

    ; === Compute root1 = (-b + sqrt(D)) / 2a ===
    fld st2                        ; ST0 = sqrt(D), ST1 = 2a, ST2 = -b, ST3 = sqrt(D)
    fadd st0, st2                  ; ST0 = sqrt(D) + (-b), ST1 = 2a, ST2 = -b, ST3 = sqrt(D)
    fdiv st0, st1                  ; ST0 = root1, ST1 = 2a, ST2 = -b, ST3 = sqrt(D)
    mov rax, rdi
    fstp qword [rax]              ; *r1_real = root1

    ; Set root1 imaginary part = 0
    fldz
    mov rax, rsi
    fstp qword [rax]

    ; === Compute root2 = (-b - sqrt(D)) / 2a ===
    fld st2                        ; ST0 = sqrt(D), ST1 = 2a, ST2 = -b, ST3 = sqrt(D)
    fsub st2, st0                  ; ST2 = -b - sqrt(D), ST1 = 2a, ST0 = sqrt(D), ST3 = sqrt(D)
    fstp st0                       ; Pop sqrt(D), ST0 = 2a, ST1 = -b - sqrt(D), ST2 = sqrt(D)
    fxch st1                       ; ST0 = -b - sqrt(D), ST1 = 2a, ST2 = sqrt(D)
    fdiv st0, st1                  ; ST0 = root2, ST1 = 2a, ST2 = sqrt(D)
    mov rax, rdx
    fstp qword [rax]              ; *r2_real = root2

    ; Set root2 imaginary part = 0
    fldz
    mov rax, rcx
    fstp qword [rax]

    ; Clean up FPU stack
    fstp st0                       ; Pop 2a
    fstp st0                       ; Pop sqrt(D)
    add rsp, 32
    ret

.complex_roots:
    ; ST0 = D (negative), ST1 = D
    fstp st1                   ; ST0 = D, pop duplicate

    ; Compute sqrt(-D)
    fchs                       ; ST0 = -D
    fsqrt                      ; ST0 = sqrt(-D)

    ; Save sqrt(-D) for later use
    fst qword [rsp+24]         ; Store sqrt(-D) at [rsp+24]

    ; Compute real part: -b / 2a
    fld qword [rsp+8]          ; ST0 = b, ST1 = sqrt(-D)
    fchs                       ; ST0 = -b, ST1 = sqrt(-D)
    fld qword [rsp]            ; ST0 = a, ST1 = -b, ST2 = sqrt(-D)
    fadd st0, st0              ; ST0 = 2a, ST1 = -b, ST2 = sqrt(-D)
    
    ; Compute -b / 2a
    fxch st1                   ; ST0 = -b, ST1 = 2a, ST2 = sqrt(-D)
    fdiv st0, st1              ; ST0 = -b/2a = real part, ST1 = 2a, ST2 = sqrt(-D)

    ; Store real part to both roots
    mov rax, rdi
    fst qword [rax]            ; *r1_real = real part
    mov rax, rdx
    fst qword [rax]            ; *r2_real = real part

    ; Compute imag part: sqrt(-D) / 2a
    fxch st2                   ; ST0 = sqrt(-D), ST1 = 2a, ST2 = real part
    fdiv st0, st1              ; ST0 = sqrt(-D) / 2a = imag part, ST1 = 2a, ST2 = real part

    ; Store positive imaginary part to r1_imag
    mov rax, rsi
    fst qword [rax]            ; *r1_imag = +imag part

    ; Store negative imaginary part to r2_imag
    fchs                       ; ST0 = -imag part
    mov rax, rcx
    fstp qword [rax]           ; *r2_imag = -imag part

    ; Clean up FPU stack
    fstp st0                   ; Pop 2a
    fstp st0                   ; Pop real part

    add rsp, 32
    ret
    