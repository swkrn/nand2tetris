                @10
D=A

                @SP
                A=M
                M=D
                @SP
                M=M+1
                @LCL
D=M
@0
A=D+A
D=M

                // keep target memory in temp (R5)
                @5
                M=D
                @SP
                M=M-1
                A=M
                D=M
                @5
                A=M
                M=D
                @21
D=A

                @SP
                A=M
                M=D
                @SP
                M=M+1
                @22
D=A

                @SP
                A=M
                M=D
                @SP
                M=M+1
                @ARG
D=M
@2
A=D+A
D=M

                // keep target memory in temp (R5)
                @5
                M=D
                @SP
                M=M-1
                A=M
                D=M
                @5
                A=M
                M=D
                @ARG
D=M
@1
A=D+A
D=M

                // keep target memory in temp (R5)
                @5
                M=D
                @SP
                M=M-1
                A=M
                D=M
                @5
                A=M
                M=D
                @36
D=A

                @SP
                A=M
                M=D
                @SP
                M=M+1
                @THIS
D=M
@6
A=D+A
D=M

                // keep target memory in temp (R5)
                @5
                M=D
                @SP
                M=M-1
                A=M
                D=M
                @5
                A=M
                M=D
                @42
D=A

                @SP
                A=M
                M=D
                @SP
                M=M+1
                @45
D=A

                @SP
                A=M
                M=D
                @SP
                M=M+1
                @THAT
D=M
@5
A=D+A
D=M

                // keep target memory in temp (R5)
                @5
                M=D
                @SP
                M=M-1
                A=M
                D=M
                @5
                A=M
                M=D
                @THAT
D=M
@2
A=D+A
D=M

                // keep target memory in temp (R5)
                @5
                M=D
                @SP
                M=M-1
                A=M
                D=M
                @5
                A=M
                M=D
                @510
D=A

                @SP
                A=M
                M=D
                @SP
                M=M+1
                @5
D=M
@6
A=D+A
D=M

                // keep target memory in temp (R5)
                @5
                M=D
                @SP
                M=M-1
                A=M
                D=M
                @5
                A=M
                M=D
                @LCL
D=M
@0
A=D+A
D=M

                @SP
                A=M
                M=D
                @SP
                M=M+1
                @THAT
D=M
@5
A=D+A
D=M

                @SP
                A=M
                M=D
                @SP
                M=M+1
@SP
A=M
A=A-1
D=M
A=A-1
M=M+D
@SP
M=M-1
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
@SP
A=M
A=A-1
D=M
A=A-1
M=M-D
@SP
M=M-1
                @THIS
D=M
@6
A=D+A
D=M

                @SP
                A=M
                M=D
                @SP
                M=M+1
                @THIS
D=M
@6
A=D+A
D=M

                @SP
                A=M
                M=D
                @SP
                M=M+1
@SP
A=M
A=A-1
D=M
A=A-1
M=M+D
@SP
M=M-1
@SP
A=M
A=A-1
D=M
A=A-1
M=M-D
@SP
M=M-1
                @5
D=M
@6
A=D+A
D=M

                @SP
                A=M
                M=D
                @SP
                M=M+1
@SP
A=M
A=A-1
D=M
A=A-1
M=M+D
@SP
M=M-1
