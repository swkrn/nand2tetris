from typing import Literal, get_args
import sys
import textwrap

Command = Literal['C_ARITHMETIC', 'C_PUSH', 'C_POP', 'C_LABEL', 'C_GOTO', 'C_IF', 'C_FUNCTION', 'C_RETURN', 'C_CALL']
Arithmetic = Literal["add", "sub", 'eq', 'lt', 'gt', 'neg', 'and', 'or', 'not']

Segment = Literal['local', 'argument', 'this', 'that', 'constant']


def to_command(command: str) -> Command | None:
    match command:
        case 'push':
            return 'C_PUSH'
        case 'pop':
            return 'C_POP'
        case _:
            if command in set(get_args(Arithmetic)):
                return 'C_ARITHMETIC'
            else:
                return None
                

class Parser:
    def __init__(self, input_file: str):
        file = open(input_file, 'r')
        lines = file.readlines()

        writer = None;
        if input_file.endswith('.vm'):
            writer = CodeWriter(f'{input_file[:-3]}.asm')
        else:
            exit(1)

        for line in lines:
            if line.startswith('//'):
                continue
            line_splitted: list[str] = line.split()
            if len(line_splitted) == 0:
                continue


            command = to_command(line_splitted[0])
            arg1 = None
            arg2 = None
            if command == 'C_ARITHMETIC':
                arg1 = line_splitted[0]
                writer.write_arithmetic(arg1)
            else:
                arg1 = line_splitted[1]
                arg2 = int(line_splitted[2])
                writer.write_push_pop(command=command, segment=arg1, index=arg2)


class CodeWriter:
    def __init__(self, output_file):
         self.file = open(output_file, 'w')
         self.label = 0

    def write_arithmetic(self, arithmetic: Arithmetic):
        match arithmetic:
            case 'add':
                self.file.write(textwrap.dedent(f"""\
                @SP
                AM=M-1
                D=M
                A=A-1
                M=D+M
                """));
            
            case 'sub':
                self.file.write(textwrap.dedent(f"""\
                @SP
                AM=M-1
                D=M
                A=A-1
                M=M-D
                """));
            
            case 'gt':
                self.file.write(textwrap.dedent(f"""\
                @SP
                AM=M-1
                D=M
                A=A-1
                D=M-D
                @label.true.{self.label}
                D;JGT
                @SP
                A=M-1
                M=0
                @label.end.{self.label}
                0;JMP
                (label.true.{self.label})
                @SP
                A=M-1
                M=-1
                (label.end.{self.label})
                """));
                self.label += 1

            case 'lt':
                self.file.write(textwrap.dedent(f"""\
                @SP
                AM=M-1
                D=M
                A=A-1
                D=M-D
                @label.true.{self.label}
                D;JLT
                @SP
                A=M-1
                M=0
                @label.end.{self.label}
                0;JMP
                (label.true.{self.label})
                @SP
                A=M-1
                M=-1
                (label.end.{self.label})
                """));
                self.label += 1

            case 'eq':
                self.file.write(textwrap.dedent(f"""\
                @SP
                AM=M-1
                D=M
                A=A-1
                D=M-D
                @label.true.{self.label}
                D;JEQ
                @SP
                A=M-1
                M=0
                @label.end.{self.label}
                0;JMP
                (label.true.{self.label})
                @SP
                A=M-1
                M=-1
                (label.end.{self.label})
                """));
                self.label += 1

            case 'neg':
                self.file.write(textwrap.dedent(f"""\
                @SP
                A=M-1
                M=-M
                """));
    
            case 'and':
                self.file.write(textwrap.dedent(f"""\
                @SP
                AM=M-1
                D=M
                A=A-1
                M=D&M
                """));
    
            case 'or':
                self.file.write(textwrap.dedent(f"""\
                @SP
                AM=M-1
                D=M
                A=A-1
                M=D|M
                """));
    
            case 'not':
                self.file.write(textwrap.dedent(f"""\
                @SP
                A=M-1
                M=!M
                """));

    def write_push_pop(self, command: Command, segment: Segment, index: int):
        if segment == 'constant':
            if command == 'C_PUSH':
                self.file.write(textwrap.dedent(f"""\
                @{index}
                D=A
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """));

    def close(self):
        self.file.close()
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python vm_translator.py <filename>")
    else:
        parser = Parser(sys.argv[1])