@256
D=A
@SP
M=D                                
@Sys.init.ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@5
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Sys.init
0;JMP

(Sys.init.ret.0)
// ParsedLine(command='C_FUNCTION', arg1='Main.fibonacci', arg2=0)
(Main.fibonacci)             

// ParsedLine(command='C_PUSH', arg1='argument', arg2=0)
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_PUSH', arg1='constant', arg2=2)
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_ARITHMETIC', arg1='lt', arg2=None)
@SP
AM=M-1
D=M
A=A-1
D=M-D
@label.true.0
D;JLT
@SP
A=M-1
M=0
@label.end.0
0;JMP
(label.true.0)
@SP
A=M-1
M=-1
(label.end.0)

// ParsedLine(command='C_IF', arg1='N_LT_2', arg2=None)
@SP
AM=M-1
D=M
@N_LT_2
D;JNE

// ParsedLine(command='C_GOTO', arg1='N_GE_2', arg2=None)
@N_GE_2
0;JMP

// ParsedLine(command='C_LABEL', arg1='N_LT_2', arg2=None)
(N_LT_2)             

// ParsedLine(command='C_PUSH', arg1='argument', arg2=0)
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_RETURN', arg1=None, arg2=None)
@LCL
D=M
@label.temp.FRAME
M=D              
@label.temp.FRAME
D=M
@5
A=D-A
D=M
@label.temp.RET
M=D
@ARG
D=M
@0
D=D+A
@label.temp.addr
M=D
@SP
AM=M-1
D=M
@label.temp.addr
A=M
M=D
@ARG
D=M
@SP
M=D+1
@label.temp.FRAME
D=M
@1
A=D-A
D=M
@THAT
M=D
@label.temp.FRAME
D=M
@2
A=D-A
D=M
@THIS
M=D
@label.temp.FRAME
D=M
@3
A=D-A
D=M
@ARG
M=D
@label.temp.FRAME
D=M
@4
A=D-A
D=M
@LCL
M=D
@label.temp.RET
A=M
0;JMP

// ParsedLine(command='C_LABEL', arg1='N_GE_2', arg2=None)
(N_GE_2)             

// ParsedLine(command='C_PUSH', arg1='argument', arg2=0)
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_PUSH', arg1='constant', arg2=2)
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_ARITHMETIC', arg1='sub', arg2=None)
@SP
AM=M-1
D=M
A=A-1
M=M-D

// ParsedLine(command='C_CALL', arg1='Main.fibonacci', arg2=1)
@Main.fibonacci.ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@6
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP

(Main.fibonacci.ret.1)

// ParsedLine(command='C_PUSH', arg1='argument', arg2=0)
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_PUSH', arg1='constant', arg2=1)
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_ARITHMETIC', arg1='sub', arg2=None)
@SP
AM=M-1
D=M
A=A-1
M=M-D

// ParsedLine(command='C_CALL', arg1='Main.fibonacci', arg2=1)
@Main.fibonacci.ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@6
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP

(Main.fibonacci.ret.2)

// ParsedLine(command='C_ARITHMETIC', arg1='add', arg2=None)
@SP
AM=M-1
D=M
A=A-1
M=D+M

// ParsedLine(command='C_RETURN', arg1=None, arg2=None)
@LCL
D=M
@label.temp.FRAME
M=D              
@label.temp.FRAME
D=M
@5
A=D-A
D=M
@label.temp.RET
M=D
@ARG
D=M
@0
D=D+A
@label.temp.addr
M=D
@SP
AM=M-1
D=M
@label.temp.addr
A=M
M=D
@ARG
D=M
@SP
M=D+1
@label.temp.FRAME
D=M
@1
A=D-A
D=M
@THAT
M=D
@label.temp.FRAME
D=M
@2
A=D-A
D=M
@THIS
M=D
@label.temp.FRAME
D=M
@3
A=D-A
D=M
@ARG
M=D
@label.temp.FRAME
D=M
@4
A=D-A
D=M
@LCL
M=D
@label.temp.RET
A=M
0;JMP

// ParsedLine(command='C_FUNCTION', arg1='Sys.init', arg2=0)
(Sys.init)             

// ParsedLine(command='C_PUSH', arg1='constant', arg2=4)
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_CALL', arg1='Main.fibonacci', arg2=1)
@Main.fibonacci.ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

@SP
D=M
@6
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Main.fibonacci
0;JMP

(Main.fibonacci.ret.0)

// ParsedLine(command='C_LABEL', arg1='END', arg2=None)
(END)             

// ParsedLine(command='C_GOTO', arg1='END', arg2=None)
@END
0;JMP

