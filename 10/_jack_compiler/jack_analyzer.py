from typing import List, Literal, Any
from dataclasses import dataclass
import sys
from jack_tokenizer import Token, JackTokenizer

class CompilationEngine():
    tokens: List[Token]
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def compile_class(self):
        pass

    def compile_class_var_dec(self):
        pass

    def compile_subroutine(self):
        pass

    def compile_parameter_list(self):
        pass

    def compile_var_dec(self):
        pass

    def compile_statements(self):
        pass

    def compile_do(self):
        pass

    def compile_let(self):
        pass

    def compile_while(self):
        pass

    def comile_return(self):
        pass

    def compile_if(self):
        pass

    def compile_expression(self):
        pass

    def compile_term(self):
        pass

    def compile_expression_list(self):
        pass

    


class JackAnalyzer():
    tokenizer: JackTokenizer

    def __init__(self, code: str):
        self.tokenizer = JackTokenizer(code)

    def get_tokens(self) -> List[Token]:
        tokens = []
        while self.tokenizer.has_next():
            token = self.tokenizer.scan_token()
            if token is not None:
                tokens.append(token)
        self.tokenizer.reset()
        return tokens
    
    def get_tokens_xml(self) -> str:
        tokens_xml = '<tokens>\n'

        for token in self.get_tokens():
            tokens_xml += f'   <{token.type}>{token.value if token.value is not None else ""}</{token.type}>\n'
        tokens_xml += '</tokens>'

        return tokens_xml


if __name__ == '__main__':
    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        code = f.read()
        ce = JackAnalyzer(code)
        tokens_xml = ce.get_tokens_xml()
        print(tokens_xml)

        # tokens = ce.get_tokens()
        # print(*tokens, sep='\n')
