;**************************************************************************
; solve_poly_2.asm
; Clean, minimal version: ax^2+bx+c=0, Coefficients a,b,c defined in memory
; Solution computed using quadratic formula, Results stored in memory or 
; printed via C
;**************************************************************************

section .data
	; Coefficients (input)
	coeff_a		dq 1.0
	coeff_b		dq -5.0
	coeff_c		dq 6.0

	; Roots (output)
	root1_real	dq 0.0
	root2_real	dq 0.0

section .text
	global solve_poly_2

solve_poly_2:
	; Load coefficients into FPU stack
	fld qword [coeff_b]	; STO = b
	fld qword [coeff_b]	; STO = b, ST1 = b
	fmul st0, st1		; STO = b^2

	fld qword [coeff_a]	; STO = a, ST1 = b^2
	fld qword [coeff_c]	; STO = c, ST1 = a, ST2 = b^2
	fmul st0, st1		; STO = a*c, ST1 = b^2

	fld qword [coeff_a]	; STO = a, ST1 = a*c, ST2 = b^2
	fmul st0, st0		; STO = a^2, ST1 = a*c, ST2 = b^2

	fld1			; STO = 1.0, ST1 = a^2, ...
	fadd st0, st0		; ST0 = 2.0
	fmul st0, st1		; ST0 = 2a^2

	; Compute discriminant: b^2 - 4ac
	fld qword [coeff_a]	; STO a
	fld qword [coeff_c]	; STO c, ST1 = a
	fmul st0, st1		; STO ac
	fld1
	fadd st0, st0		; STO = 2.0
	fadd st0, st0		; STO = 4.0
	fmul st0, st1		; STO = 4ac
	fxch st1		; Swap STO and ST1 (b^2 is in ST1)
	fsub st0, st1		; STO = b^2 - 4ac

	; Compute sqrt (discriminant)
	fsqrt			; STO = sqrt (discriminant)

	; Compute -b +- sqrt (D)
	fld qword [coeff_b]	; STO = b
	fchs			; STO = -b
	fadd st0, st1		; STO = -b + sqrt(D)
	fld qword [coeff_a]
	fadd st0, st0		; STO = 2a
	fdiv st1, st0		; ST1 = root1
	fstp qword [root1_real]

	; Repeat for -b - sqrt (D)
	fld qword [coeff_b]
	fchs
	fsub st0, st1
	fld qword [coeff_a]
	fadd st0, st0
	fdiv st1, st0
	fstp qword [root2_real] 					

	ret 
