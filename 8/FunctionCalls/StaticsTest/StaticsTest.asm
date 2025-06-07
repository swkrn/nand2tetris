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
// ParsedLine(command='C_FUNCTION', arg1='Class1.set', arg2=0)
(Class1.set)             

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

// ParsedLine(command='C_POP', arg1='static', arg2=0)
@SP
AM=M-1
D=M
@Class1.static.0
M=D

// ParsedLine(command='C_PUSH', arg1='argument', arg2=1)
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_POP', arg1='static', arg2=1)
@SP
AM=M-1
D=M
@Class1.static.1
M=D

// ParsedLine(command='C_PUSH', arg1='constant', arg2=0)
@0
D=A
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

// ParsedLine(command='C_FUNCTION', arg1='Class1.get', arg2=0)
(Class1.get)             

// ParsedLine(command='C_PUSH', arg1='static', arg2=0)
@Class1.static.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_PUSH', arg1='static', arg2=1)
@Class1.static.1
D=M
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

// ParsedLine(command='C_FUNCTION', arg1='Class2.set', arg2=0)
(Class2.set)             

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

// ParsedLine(command='C_POP', arg1='static', arg2=0)
@SP
AM=M-1
D=M
@Class2.static.0
M=D

// ParsedLine(command='C_PUSH', arg1='argument', arg2=1)
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_POP', arg1='static', arg2=1)
@SP
AM=M-1
D=M
@Class2.static.1
M=D

// ParsedLine(command='C_PUSH', arg1='constant', arg2=0)
@0
D=A
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

// ParsedLine(command='C_FUNCTION', arg1='Class2.get', arg2=0)
(Class2.get)             

// ParsedLine(command='C_PUSH', arg1='static', arg2=0)
@Class2.static.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_PUSH', arg1='static', arg2=1)
@Class2.static.1
D=M
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

// ParsedLine(command='C_PUSH', arg1='constant', arg2=6)
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_PUSH', arg1='constant', arg2=8)
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_CALL', arg1='Class1.set', arg2=2)
@Class1.set.ret.0
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
@7
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Class1.set
0;JMP

(Class1.set.ret.0)

// ParsedLine(command='C_POP', arg1='temp', arg2=0)
@SP
AM=M-1
D=M
@5
M=D

// ParsedLine(command='C_PUSH', arg1='constant', arg2=23)
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_PUSH', arg1='constant', arg2=15)
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// ParsedLine(command='C_CALL', arg1='Class2.set', arg2=2)
@Class2.set.ret.1
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
@7
D=D-A
@ARG
M=D

@SP
D=M
@LCL
M=D

@Class2.set
0;JMP

(Class2.set.ret.1)

// ParsedLine(command='C_POP', arg1='temp', arg2=0)
@SP
AM=M-1
D=M
@5
M=D

// ParsedLine(command='C_CALL', arg1='Class1.get', arg2=0)
@Class1.get.ret.2
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

@Class1.get
0;JMP

(Class1.get.ret.2)

// ParsedLine(command='C_CALL', arg1='Class2.get', arg2=0)
@Class2.get.ret.3
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

@Class2.get
0;JMP

(Class2.get.ret.3)

// ParsedLine(command='C_LABEL', arg1='END', arg2=None)
(END)             

// ParsedLine(command='C_GOTO', arg1='END', arg2=None)
@END
0;JMP

