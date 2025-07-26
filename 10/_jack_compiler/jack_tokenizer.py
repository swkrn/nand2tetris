from typing import List, Literal, Any, cast
from dataclasses import dataclass
import sys
import xml.etree.ElementTree as ET





TokenType = Literal['keyword', 'symbol', 'identifier', 'intConstant', 'stringConstant']

KEYWORDS = {'class', 'method', 'function', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return'}
SYMBOLS = {'{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~'}



@dataclass
class Token:
    type: TokenType
    value: str | int | None



class JackTokenizer():
    code: str
    start: int 
    current: int

    tokens: List[Token]

    def __init__(self, code: str):
        self.code = code
        self.start = 0
        self.current = 0
        self.tokens = []


    def scan_token(self) -> Token | None:
        c = self.__advance()

        # single line comment
        if c == '/' and self.__peek() == '/':
            self.__advance()
            while self.has_next() and self.__peek() != '\n':
                self.__advance()
            return None
        
        # multiline comment
        if c == '/' and self.__peek() == '*':
            self.__advance()
            while self.has_next():
                if self.__peek() == '*' and self.__peek_next() == '/':
                    break;
                self.__advance()
            self.__advance()
            self.__advance()
            return None

        if c in SYMBOLS:
            return self.__add_token('symbol', c)

        if c.isdigit():
            return self.__exec_int()

        if c == '"':
            return self.__exec_string()

        if c in {' ', '\n', '\t', '\r'}:
            return None
        
        return self.__exec_identifier()

            
    def __advance(self) -> str:
        c = self.__peek()
        self.current += 1
        return c


    def __peek(self) -> str:
        return self.code[self.current]


    def __peek_next(self) -> str | None:
        if self.has_next():
            return self.code[self.current + 1]
        else:
            return None


    def has_next(self) -> bool:
        return self.current + 1 < len(self.code)
    

    def __add_token(self, type: TokenType, value: str | int | None) -> Token:
        self.tokens.append(Token(type, value))
        return self.tokens[-1]

    
    def __exec_int(self) -> Token:
        self.start = self.current - 1

        while (self.__peek().isdigit()):
            self.__advance()

        return self.__add_token('intConstant', int(self.code[self.start: self.current]))


    def __exec_string(self) -> Token:
        self.start = self.current

        while (self.__peek() != '"'):
            self.__advance()

        token = self.__add_token('stringConstant', self.code[self.start: self.current])
        # consume '"'
        self.__advance()
        return token
    

    def __exec_identifier(self) -> Token:
        self.start = self.current - 1

        while (self.__peek().isalpha() or self.__peek().isdigit()):
            self.__advance()

        text = self.code[self.start: self.current]
        if text in KEYWORDS:
            return self.__add_token('keyword', text)
        else:
            return self.__add_token('identifier', text)
        
    def reset(self):
        self.start = 0
        self.current = 0
        self.tokens = []


def xml_to_tokens(xml: str) -> List[Token]:
    tokens: List[Token] = []
    root = ET.fromstring(xml)
    for token in root:
        t = cast(TokenType, token.tag)

        assert token.text is not None
        value = token.text[1: -1]
        
        tokens.append(Token(t, value))
    return tokens
