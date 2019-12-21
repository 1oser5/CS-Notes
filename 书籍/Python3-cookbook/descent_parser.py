#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-
'''
@File    :   descent_parser.py
@Time    :   2019/12/21 16:31:21
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   递归下降解析器
'''

# here put the import lib
import re
import collections

NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))
Token = collections.namedtuple('Token',['type','value'])
def generate_token(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok

#Parse
class ExpressionEvaluator(object):
    def parse(self,text):
        """ 解析函数 """
        self.tokens = generate_token(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self.expr()
    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)
    def _accept(self, tok):
        if self.nexttok and self.nexttok.type == tok:
            self._advance()
            return True
        else: return False
    def _except(self, tok):
        if not self._accept(tok):
            raise SyntaxError('Expected ' + tok)
    def expr(self):
        termval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                termval += right
            elif op == 'MINUS':
                termval -= right
        return termval
    def term(self):
        t = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                t *= right
            elif op == 'DIVIDE':
                t /= right
        return t
    def factor(self):
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._except('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')

if __name__ == '__main__':
    e = ExpressionEvaluator()
    print(e.parse('2'))
    print(e.parse('2+3*4'))