from typing import Literal, get_args
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path

Command = Literal['C_ARITHMETIC', 'C_PUSH', 'C_POP', 'C_LABEL', 'C_GOTO', 'C_IF', 'C_FUNCTION', 'C_RETURN', 'C_CALL']
Arithmetic = Literal["add", "sub", 'eq', 'lt', 'gt', 'neg', 'and', 'or', 'not']

Segment = Literal['local', 'argument', 'this', 'that', 'constant', 'temp', 'pointer', 'static']

def to_command(command: str) -> Command | None:
        match command:
            case 'push':
                return 'C_PUSH'
            case 'pop':
                return 'C_POP'
            case 'label':
                return 'C_LABEL'
            case 'goto':
                return 'C_GOTO'
            case 'if-goto':
                return 'C_IF'
            case 'function':
                return 'C_FUNCTION'
            case 'return':
                return 'C_RETURN'
            case 'call':
                return 'C_CALL'
            case _:
                if command in set(get_args(Arithmetic)):
                    return 'C_ARITHMETIC'
                else:
                    return None

@dataclass              
class ParsedLine:
    command: Command
    arg1: str
    arg2: int | None


class Parser:
    def __init__(self, input_file_path: str):
        self.file = open(input_file_path, 'r')
        self.lines = self.file.readlines()
        self.cursor = 0

    def has_more_commands(self) -> bool:
        return self.cursor < len(self.lines)

    def advance(self) -> ParsedLine | None:
        line = self.lines[self.cursor]
        self.cursor += 1;

        if line.startswith('//'):
            return None
        line_splitted: list[str] = line.split()
        if len(line_splitted) == 0:
            return None

        command = to_command(line_splitted[0])
        if command is None:
            return None
        
        if command == 'C_ARITHMETIC':
            arg1 = line_splitted[0]
            arg2 = None

        elif command in {'C_LABEL', 'C_GOTO', 'C_IF'}:
            arg1 = line_splitted[1]
            arg2 = None

        elif command == 'C_RETURN':
            arg1 = None
            arg2 = None

        else:
            arg1 = line_splitted[1]
            arg2 = int(line_splitted[2])

        return ParsedLine(command=command, arg1=arg1, arg2=arg2)
            

WriteMode = Literal['w', 'a']

class CodeWriter:
    def __init__(self, output_file_path: str, vm_class_name: str | None, write_mode: WriteMode):
         self.file = open(output_file_path, write_mode)
         self.vm_class_name =  vm_class_name
         self.label = 0

    def write_init(self):
        self.file.write(textwrap.dedent(f"""\
        @256
        D=A
        @SP
        M=D                                
        """));
        self.write_call('Sys.init', 0)

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
    
        elif segment in {'temp', 'pointer'}:
            if segment == 'temp':
                base_address = 5
            if segment == 'pointer':
                base_address = 3

            if command == 'C_PUSH':
                self.file.write(textwrap.dedent(f"""\
                @{base_address + index}
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """));
            
            if command == 'C_POP':
                self.file.write(textwrap.dedent(f"""\
                @SP
                AM=M-1
                D=M
                @{base_address + index}
                M=D
                """));
        
        elif segment == 'static':
            if command == 'C_PUSH':
                self.file.write(textwrap.dedent(f"""\
                @{self.vm_class_name}.static.{index}
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """));
            
            if command == 'C_POP':
                self.file.write(textwrap.dedent(f"""\
                @SP
                AM=M-1
                D=M
                @{self.vm_class_name}.static.{index}
                M=D
                """));

        else:
            if command == 'C_PUSH':
                self.file.write(textwrap.dedent(f"""\
                @{self.__get_address_ref(segment)}
                D=M
                @{index}
                A=D+A
                D=M
                @SP
                A=M
                M=D
                @SP
                M=M+1
                """));
            
            if command == 'C_POP':
                self.file.write(textwrap.dedent(f"""\
                @{self.__get_address_ref(segment)}
                D=M
                @{index}
                D=D+A
                @label.temp.addr
                M=D
                @SP
                AM=M-1
                D=M
                @label.temp.addr
                A=M
                M=D
                """));

    def write_label(self, label: str):
        self.file.write(textwrap.dedent(f"""\
        ({label})             
        """));
    
    def write_goto(self, label: str):
        self.file.write(textwrap.dedent(f"""\
        @{label}
        0;JMP
        """));
    
    def write_if(self, label: str):
        self.file.write(textwrap.dedent(f"""\
        @SP
        AM=M-1
        D=M
        @{label}
        D;JNE
        """));
    
    def write_call(self, function_name: str, n_args: int):
        self.file.write(textwrap.dedent(f"""\
        @{function_name}.ret.{self.label}
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
        @{5 + n_args}
        D=D-A
        @ARG
        M=D

        @SP
        D=M
        @LCL
        M=D

        @{function_name}
        0;JMP

        ({function_name}.ret.{self.label})
        """));
        self.label += 1

    def write_return(self):
        self.file.write(textwrap.dedent(f"""\
        @LCL
        D=M
        @label.temp.FRAME
        M=D              
        """));
        self.file.write(textwrap.dedent(f"""\
        @label.temp.FRAME
        D=M
        @5
        A=D-A
        D=M
        @label.temp.RET
        M=D
        """));
        self.write_push_pop('C_POP', 'argument', 0)
        self.file.write(textwrap.dedent(f"""\
        @ARG
        D=M
        @SP
        M=D+1
        """));
        for i, addr_ref in enumerate(['THAT', 'THIS', 'ARG', 'LCL']):
            offset: int = i + 1
            self.file.write(textwrap.dedent(f"""\
            @label.temp.FRAME
            D=M
            @{offset}
            A=D-A
            D=M
            @{addr_ref}
            M=D
            """));
        self.file.write(textwrap.dedent(f"""\
        @label.temp.RET
        A=M
        0;JMP
        """));


    def write_function(self, function_name: str, num_locals: int):
        self.write_label(function_name)
        for _ in range(num_locals):
            self.write_push_pop('C_PUSH', 'constant', 0)


    def write_comment(self, comment: str):
        self.file.write(f'// {comment}\n')

    def write_empty_line(self):
        self.file.write('\n')
        

    def __get_address_ref(self, segment: Literal['local', 'argument', 'this', 'that']) -> Literal['LCL', 'ARG', 'THIS', 'THAT']:
        map_ref = {
            'local': 'LCL',
            'argument': 'ARG',
            'this': 'THIS',
            'that': 'THAT',
        }
        return map_ref[segment]

    def close(self):
        self.file.close()        

def write_init(output_file_path: str):
    writer = CodeWriter(output_file_path=output_file_path, vm_class_name=None, write_mode='w')
    writer.write_init()
    writer.close()
    

def write_asm(input_file_path: str, output_file_path: str, write_mode: WriteMode):
    parser = Parser(input_file_path)
    writer = CodeWriter(output_file_path, vm_class_name=input_file_path.split('/')[-1].split('.')[0], write_mode=write_mode)

    while parser.has_more_commands():
        line = parser.advance()
        if line is not None:
            writer.write_comment(line)
            match line.command:
                case 'C_ARITHMETIC':
                    writer.write_arithmetic(arithmetic=line.arg1)
                case 'C_PUSH' | 'C_POP':
                    writer.write_push_pop(command=line.command, segment=line.arg1, index=line.arg2)
                case 'C_LABEL':
                    writer.write_label(label=line.arg1)
                case 'C_GOTO':
                    writer.write_goto(label=line.arg1)
                case 'C_IF':
                    writer.write_if(label=line.arg1)
                case 'C_FUNCTION':
                    writer.write_function(function_name=line.arg1, num_locals=line.arg2)
                case 'C_RETURN':
                    writer.write_return()
                case 'C_CALL':
                    writer.write_call(function_name=line.arg1, n_args=line.arg2)
            writer.write_empty_line()
    writer.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python vm_translator.py <filename>")
    else:
        input_file_path = sys.argv[1]
        path = Path(input_file_path)

        if path.is_file():
            if input_file_path.endswith('.vm'):
                output_file_path = input_file_path[:-3] + '.asm'
                write_init(output_file_path=output_file_path)
                write_asm(input_file_path=input_file_path, output_file_path=output_file_path, write_mode='a')
            else:
                exit(1)

        elif path.is_dir():
            output_file_path = str(path) + '/' + path.name + '.asm'
            write_init(output_file_path=output_file_path)
            for p in path.rglob("*"):
                if p.is_file() and p.suffix == '.vm':
                    write_asm(input_file_path=p.as_posix(), output_file_path=output_file_path, write_mode='a')

        else:
            print('Path does not exist.');