from jack_tokenizer import Token, JackTokenizer, TokenType, xml_to_tokens
from typing import List, Literal, Any
from dataclasses import dataclass
import sys
import textwrap
import xml.dom.minidom as XML


class CompilationEngine():
    tokens: List[Token]
    current: int

    indent: int

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.indent = -2
        

    def get_compiled_xml(self) -> str:
        xml =  self.compile_class()
        print(xml, sep='\n')
        pretty_xml = XML.parseString(xml.replace('\n', '')).toprettyxml(indent="  ")
        return pretty_xml;


    def compile_class(self) -> str:
        xml = '<class>\n'
       
        xml += self.__consume(Token('keyword', 'class'), "incorrect class")
        xml += self.compile_class_name()
        xml += self.__consume(Token('symbol', '{'), "incorrect class")

        # classVarDec
        xml += self.compile_class_var_dec()

        # subroutineDec
        xml += self.compile_subroutine()

        xml += self.__consume(Token('symbol', '}'), "incorrect class")

       
        xml += '</class>\n'
        return xml
    

    def compile_class_var_dec(self) -> str:
        xml = '<varDec>\n'
        while True:
            if self.__check_token(Token('keyword', 'static')):
                xml += self.__consume(Token('keyword', 'static'), "incorrect class var dec")
                    
            elif self.__check_token(Token('keyword', 'field')):
                xml += self.__consume(Token('keyword', 'field'), "incorrect class var dec")
            
            else:
                break;

            xml += self.compile_type()
            xml += self.compile_var_name()

            while self.__check_token(Token('symbol', ',')):
                xml += self.__consume(Token('symbol', ','), "incorrect class var dec")
                xml += self.compile_var_name()
            
            xml += self.__consume(Token('symbol', ';'), "incorrect class var dec")
       
        xml += '</varDec>\n'
        return xml
    

    def compile_subroutine(self) -> str:
        xml = '<subroutineDec>\n'
        while True:
            if self.__check_token(Token('keyword', 'constructor')):
                xml += self.__consume(Token('keyword', 'constructor'), "incorrect subroutine")

            elif self.__check_token(Token('keyword', 'function')):
                xml += self.__consume(Token('keyword', 'function'), "incorrect subroutine")

            elif self.__check_token(Token('keyword', 'method')):
                xml += self.__consume(Token('keyword', 'method'), "incorrect subroutine")

            else:
                break
            
            if self.__check_token(Token('keyword', 'void')):
                xml += self.__consume(Token('keyword', 'void'), "incorrect subroutine")

            elif self.__is_type():
                self.compile_type()

            xml += self.compile_subroutine_name()

            xml += self.__consume(Token('symbol', '('), "incorrect subroutine")
            xml += self.compile_parameter_list()
            xml += self.__consume(Token('symbol', ')'), "incorrect subroutine")

            # subroutineBody
            xml += self.__consume(Token('symbol', '{'), "incorrect subroutine body")
            while self.__check_token(Token('keyword', 'var')):
                xml += self.compile_var_dec()
            self.compile_statements()
            xml += self.__consume(Token('symbol', '}'), "incorrect subroutine body")
        
        xml += '</subroutineDec>\n'
        return xml
    

    def compile_parameter_list(self) -> str:
        xml = '<parameterList>\n'
        if self.__is_type():
            xml += self.compile_type()
            xml += self.compile_var_name()

        while True:
            if self.__check_token(Token('symbol', ',')):
                xml += self.__consume(Token('symbol', ','), 'incorrect parameter list')
                xml += self.compile_type()
                xml += self.compile_var_name()
            else:
                break               

        xml += '</parameterList>\n'
        return xml


    def compile_var_dec(self) -> str:
        xml = ''

        xml += '<varDec>\n'
        xml += self.__consume(Token('keyword', 'var'), 'incorrect var dec')
        xml += self.compile_type()
        xml += self.compile_var_name()

        while self.__check_token(Token('symbol', ',')):
            xml += self.__consume(Token('symbol', ','), 'incorrect var dec')
            xml += self.compile_var_name()

        xml += self.__consume(Token('symbol', ';'), 'incorrect var dec')
        xml += '</varDec>\n'
            
        return xml


    def compile_statements(self) -> str:
        xml = '<statements>\n'
        while self.__has_next() and not self.__check_token(Token('symbol', '}')):
            # let
            if self.__check_token(Token('keyword', 'let')):
                xml += self.compile_let()
                continue
            # if
            if self.__check_token(Token('keyword', 'if')):
                xml +=  self.compile_if()
                continue
            # while
            if self.__check_token(Token('keyword', 'while')):
                xml += self.compile_while()
                continue
            # do
            if self.__check_token(Token('keyword', 'do')):
                xml += self.compile_do()
                continue
            # return
            if self.__check_token(Token('keyword', 'return')):
                xml += self.comile_return()
                continue

        xml += '</statements>\n'
        return xml


    def compile_do(self) -> str:
        return '- TODO\n'


    def compile_let(self) -> str:   
        xml = '<letStatement>\n'

        xml += self.__consume(Token('keyword', 'let'), "incorrect let statement")

        xml += self.compile_var_name()

        if self.__check_token(Token('symbol', '[')):
            xml += self.__consume(Token('symbol', '['), "incorrect let statement")
            xml += self.compile_expression()
            xml += self.__consume(Token('symbol', ']'), "incorrect let statement")

        xml += self.__consume(Token('symbol', '='), "incorrect let statement")
        xml += self.compile_expression()
        xml += self.__consume(Token('symbol', ';'), "incorrect let statement")

        xml += '</letStatement>\n'
        return xml


    def compile_while(self) -> str:
        xml = '<whileStatement>\n'

        xml += self.__consume(Token('keyword', 'while'), "incorrect while statement")

        xml += self.__consume(Token('symbol', '('), "incorrect while statement")
        xml += self.compile_expression()
        xml += self.__consume(Token('symbol', ')'), "incorrect while statement")

        xml += self.__consume(Token('symbol', '{'), "incorrect while statement")
        xml += self.compile_statements()
        xml += self.__consume(Token('symbol', '}'), "incorrect while statement")

        xml += '</whileStatement>\n'
        return xml


    def comile_return(self) -> str:
        xml = '<returnStatement>\n'

        xml += self.__consume(Token('keyword', 'return'), "incorrect return statement")

        if not self.__check_token(Token('symbol', ';')):
             xml += self.compile_expression()

        xml += self.__consume(Token('symbol', ';'), "incorrect return statement")
       

        xml += '</returnStatement>\n'
        return xml


    def compile_if(self) -> str:
        xml = '<ifStatement>\n'

        xml += self.__consume(Token('keyword', 'if'), "incorrect if statement")
        xml += self.__consume(Token('symbol', '('), "incorrect if statement")
        xml += self.compile_expression()
        xml += self.__consume(Token('symbol', ')'), "incorrect if statement")

        xml += self.__consume(Token('symbol', '{'), "incorrect if statement")
        xml += self.compile_statements()
        xml += self.__consume(Token('symbol', '}'), "incorrect if statement")

        if (self.__check_token(Token('keyword', 'else'))):
            xml += self.__consume(Token('keyword', 'else'), "incorrect if statement")
            xml += self.__consume(Token('symbol', '{'), "incorrect if statement")
            xml += self.compile_statements()
            xml += self.__consume(Token('symbol', '}'), "incorrect if statement")

        xml += '</ifStatement>\n'
        return xml


    def compile_expression(self) -> str:
        xml = '<expression>\n'
        
        xml += self.compile_term()

        while self.__peek().value in ['+', '-', '*', '/', '&', '|', '<', '>', '=']:
            if self.__check_token(Token('symbol', '+')):
                xml += self.__consume(Token('symbol', '+'), 'incorrect expression')

            elif self.__check_token(Token('symbol', '-')):
                xml += self.__consume(Token('symbol', '-'), 'incorrect expression')

            elif self.__check_token(Token('symbol', '*')):
                xml += self.__consume(Token('symbol', '*'), 'incorrect expression')

            elif self.__check_token(Token('symbol', '/')):
                xml += self.__consume(Token('symbol', '*'), 'incorrect expression')

            elif self.__check_token(Token('symbol', '&')):
                xml += self.__consume(Token('symbol', '&'), 'incorrect expression')

            elif self.__check_token(Token('symbol', '|')):
                xml += self.__consume(Token('symbol', '|'), 'incorrect expression')

            elif self.__check_token(Token('symbol', '<')):
                xml += self.__consume(Token('symbol', '<'), 'incorrect expression')

            elif self.__check_token(Token('symbol', '>')):
                xml += self.__consume(Token('symbol', '>'), 'incorrect expression')

            elif self.__check_token(Token('symbol', '=')):
                xml += self.__consume(Token('symbol', '='), 'incorrect expression')

            else:
                self.__print_error('incorrect expression')

            xml += self.compile_term()

        xml += '<expression>\n'
        return xml


    def compile_term(self) -> str:
        return '- TODO\n'


    def compile_expression_list(self) -> str:
        return '- TODO\n'
    

    def compile_class_name(self) -> str:
        return self.__compile_identifier('className')
    

    def compile_var_name(self) -> str:
        return self.__compile_identifier('varName')
    

    def compile_subroutine_name(self) -> str:
        return self.__compile_identifier('subroutineName')
    

    def compile_type(self) -> str:
        xml = ''
        if self.__check_token(Token('keyword', 'int')):
            xml += self.__consume(Token('keyword', 'int'), "incorrect type")
        
        elif self.__check_token(Token('keyword', 'char')):
            xml += self.__consume(Token('keyword', 'char'), "incorrect type")

        elif self.__check_token(Token('keyword', 'boolean')):
            xml += self.__consume(Token('keyword', 'boolean'), "incorrect type")

        else:
            xml += self.compile_class_name()

        return xml
    

    def __compile_identifier(self, key: str) -> str:
        xml = ''
        if self.__check_token_type('identifier'):
            token = self.__advance()
            xml += f'<{key}>{token.value}</{key}>\n'
        else:
            self.__print_error(f"! incorrect {key} name")
        return xml


    def __consume(self, token: Token, error: str) -> str:
        if not self.__check_token(token):
            self.__print_error(f"! Error: expected: {token}, actual: {self.__peek()} - {error}")
        self.current += 1
        return f'<{token.type}>{token.value}</{token.type}>\n'
            

    def __has_next(self) -> bool:
        return self.current + 1 < len(self.tokens)
    

    def __peek(self) -> Token:
        return self.tokens[self.current]
    
    
    def __check_token(self, token: Token) -> bool:
        return self.__peek() == token
    

    def __check_token_type(self, type: TokenType) -> bool:
        return self.__peek().type == type

    
    def __advance(self) -> Token:
        token = self.__peek()
        self.current += 1
        return token
    
    def __is_type(self) -> bool:
        return self.__check_token(Token('keyword', 'int')) \
            or self.__check_token(Token('keyword', 'char')) \
            or self.__check_token(Token('keyword', 'boolean')) \
            or self.__check_token_type('identifier');
    

    def __print_error(self, error: str):
        print(error)


    def __with_indent(self, xml: str) -> str:
        return textwrap.indent(xml, prefix=' ' * self.indent)



if __name__ == '__main__':
    # ce = CompilationEngine([
    #     Token('keyword', 'class'),
    #     Token('identifier', 'Ping'),
    #     Token('symbol', '{'),
    #     Token('keyword', 'field'),
    #     Token('keyword', 'int'),
    #     Token('identifier', 'x'),
    #     Token('symbol', ','),
    #     Token('identifier', 'y'),
    #     Token('symbol', ';'),
    #     Token('symbol', '}'),
    # ])
    ce = CompilationEngine(xml_to_tokens("""

<tokens>
<keyword> class </keyword>
<identifier> Main </identifier>
<symbol> { </symbol>
<keyword> function </keyword>
<keyword> void </keyword>
<identifier> main </identifier>
<symbol> ( </symbol>
<symbol> ) </symbol>
<symbol> { </symbol>
<keyword> var </keyword>
<identifier> Array </identifier>
<identifier> a </identifier>
<symbol> ; </symbol>
<keyword> var </keyword>
<keyword> int </keyword>
<identifier> length </identifier>
<symbol> ; </symbol>
<keyword> var </keyword>
<keyword> int </keyword>
<identifier> i </identifier>
<symbol> , </symbol>
<identifier> sum </identifier>
<symbol> ; </symbol>
<keyword> let </keyword>
<identifier> length </identifier>
<symbol> = </symbol>
<identifier> Keyboard </identifier>
<symbol> . </symbol>
<identifier> readInt </identifier>
<symbol> ( </symbol>
<stringConstant> HOW MANY NUMBERS?  </stringConstant>
<symbol> ) </symbol>
<symbol> ; </symbol>
<keyword> let </keyword>
<identifier> a </identifier>
<symbol> = </symbol>
<identifier> Array </identifier>
<symbol> . </symbol>
<identifier> new </identifier>
<symbol> ( </symbol>
<identifier> length </identifier>
<symbol> ) </symbol>
<symbol> ; </symbol>
<keyword> let </keyword>
<identifier> i </identifier>
<symbol> = </symbol>
<integerConstant> 0 </integerConstant>
<symbol> ; </symbol>
<keyword> while </keyword>
<symbol> ( </symbol>
<identifier> i </identifier>
<symbol> &lt; </symbol>
<identifier> length </identifier>
<symbol> ) </symbol>
<symbol> { </symbol>
<keyword> let </keyword>
<identifier> a </identifier>
<symbol> [ </symbol>
<identifier> i </identifier>
<symbol> ] </symbol>
<symbol> = </symbol>
<identifier> Keyboard </identifier>
<symbol> . </symbol>
<identifier> readInt </identifier>
<symbol> ( </symbol>
<stringConstant> ENTER THE NEXT NUMBER:  </stringConstant>
<symbol> ) </symbol>
<symbol> ; </symbol>
<keyword> let </keyword>
<identifier> i </identifier>
<symbol> = </symbol>
<identifier> i </identifier>
<symbol> + </symbol>
<integerConstant> 1 </integerConstant>
<symbol> ; </symbol>
<symbol> } </symbol>
<keyword> let </keyword>
<identifier> i </identifier>
<symbol> = </symbol>
<integerConstant> 0 </integerConstant>
<symbol> ; </symbol>
<keyword> let </keyword>
<identifier> sum </identifier>
<symbol> = </symbol>
<integerConstant> 0 </integerConstant>
<symbol> ; </symbol>
<keyword> while </keyword>
<symbol> ( </symbol>
<identifier> i </identifier>
<symbol> &lt; </symbol>
<identifier> length </identifier>
<symbol> ) </symbol>
<symbol> { </symbol>
<keyword> let </keyword>
<identifier> sum </identifier>
<symbol> = </symbol>
<identifier> sum </identifier>
<symbol> + </symbol>
<identifier> a </identifier>
<symbol> [ </symbol>
<identifier> i </identifier>
<symbol> ] </symbol>
<symbol> ; </symbol>
<keyword> let </keyword>
<identifier> i </identifier>
<symbol> = </symbol>
<identifier> i </identifier>
<symbol> + </symbol>
<integerConstant> 1 </integerConstant>
<symbol> ; </symbol>
<symbol> } </symbol>
<keyword> do </keyword>
<identifier> Output </identifier>
<symbol> . </symbol>
<identifier> printString </identifier>
<symbol> ( </symbol>
<stringConstant> THE AVERAGE IS:  </stringConstant>
<symbol> ) </symbol>
<symbol> ; </symbol>
<keyword> do </keyword>
<identifier> Output </identifier>
<symbol> . </symbol>
<identifier> printInt </identifier>
<symbol> ( </symbol>
<identifier> sum </identifier>
<symbol> / </symbol>
<identifier> length </identifier>
<symbol> ) </symbol>
<symbol> ; </symbol>
<keyword> do </keyword>
<identifier> Output </identifier>
<symbol> . </symbol>
<identifier> println </identifier>
<symbol> ( </symbol>
<symbol> ) </symbol>
<symbol> ; </symbol>
<keyword> return </keyword>
<symbol> ; </symbol>
<symbol> } </symbol>
<symbol> } </symbol>
</tokens>


    """))
    print(ce.get_compiled_xml())