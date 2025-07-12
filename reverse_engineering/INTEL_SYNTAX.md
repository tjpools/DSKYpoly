# Assembly Syntax Comparison

## Intel vs AT&T Syntax

The DSKYpoly reverse engineering toolkit now uses Intel syntax by default for better readability.

### Key Differences

| Feature | AT&T Syntax | Intel Syntax |
|---------|-------------|--------------|
| **Source/Destination** | `mov %rax, %rbx` (src, dst) | `mov rbx, rax` (dst, src) |
| **Register Prefix** | `%rax` | `rax` |
| **Immediate Values** | `$0x10` | `0x10` |
| **Memory Reference** | `8(%rsp)` | `[rsp+8]` or `QWORD PTR [rsp+8]` |
| **Size Specification** | `movl` (32-bit) | `mov DWORD PTR` |

### Examples from DSKYpoly

#### AT&T Syntax (old):
```assembly
sub    $0x8,%rsp
mov    0x2c95(%rip),%rax
test   %rax,%rax
add    $0x8,%rsp
```

#### Intel Syntax (new):
```assembly
sub    rsp,0x8
mov    rax,QWORD PTR [rip+0x2c95]
test   rax,rax
add    rsp,0x8
```

### Benefits for Mathematical Software Analysis

1. **Readability**: Intel syntax reads left-to-right (destination ← source)
2. **Intuitive**: Matches most programming languages (variable = value)
3. **Tool Compatibility**: Works better with Windows tools like IDA Pro
4. **Educational Value**: Easier for students learning assembly

### Usage in Toolkit

All tools now use `-M intel` flag:
```bash
objdump -d -M intel binary_name
```

This makes mathematical algorithm analysis much clearer when examining polynomial evaluation routines and floating-point operations.
