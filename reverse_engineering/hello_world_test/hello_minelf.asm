; hello_minelf.asm - Minimal ELF64 Hello World (x86-64 Linux)
; This file includes a minimal ELF header and can be run directly on Linux or with QEMU.
; To assemble: nasm -f bin hello_minelf.asm -o hello_minelf

BITS 64
ORG 0x400000

; --- ELF64 Header (64 bytes) ---
; See: https://wiki.osdev.org/ELF

db 0x7F, "ELF"         ; Magic number
 db 2                  ; EI_CLASS: 64-bit
 db 1                  ; EI_DATA: little endian
 db 1                  ; EI_VERSION: original
 db 0                  ; EI_OSABI: System V
 db 0                  ; EI_ABIVERSION
 times 7 db 0          ; EI_PAD
 dw 2                  ; e_type: EXEC (2)
 dw 0x3E               ; e_machine: x86-64 (62)
 dd 1                  ; e_version
 dq _start             ; e_entry
 dq phdr - $$          ; e_phoff
 dq 0                  ; e_shoff
 dd 0                  ; e_flags
 dw ehdrsize           ; e_ehsize
 dw phdrsize           ; e_phentsize
 dw 1                  ; e_phnum
 dw 0                  ; e_shentsize
 dw 0                  ; e_shnum
 dw 0                  ; e_shstrndx

ehdrsize equ $-$$

; --- Program Header (56 bytes) ---
phdr:
 dd 1                  ; p_type: LOAD
 dd 5                  ; p_flags: RX
 dq 0                  ; p_offset
 dq 0x400000           ; p_vaddr
 dq 0x400000           ; p_paddr
 dq filesize           ; p_filesz
 dq filesize           ; p_memsz
 dq 0x200000           ; p_align (2MB)
phdrsize equ $-phdr

; --- Code and Data ---
section .text
_start:
    mov rax, 1          ; sys_write
    mov rdi, 1          ; file descriptor (stdout)
    mov rsi, msg        ; pointer to message
    mov rdx, len        ; message length
    syscall

    mov rax, 60         ; sys_exit
    xor rdi, rdi        ; exit code 0
    syscall

section .data
msg db "Hello, world!", 0xA
len equ $-msg

filesize equ $-$$
