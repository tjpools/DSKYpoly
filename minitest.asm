section .text
global test_fstp

test_fstp:
    fld1
    mov rax, rdi
    fstp qword [rax]
    ret

