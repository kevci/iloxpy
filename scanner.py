from tokentype import TokenType as t
from token import Token
from lox import Lox

class Scanner:
    def __init__(self, source: str):
        self.source = source 
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current;
            self.scanToken()
        
        self.tokens.append(Token(...))
        return self.tokens

    def scanToken(self):
        c = self.advance()
        match c:
            case '(': 
                self.addToken(t.LEFT_PAREN)
            case ')':
                self.addToken(t.RIGHT_PAREN)
            case '{':
                self.addToken(t.LEFT_BRACE)
            case '}':
                self.addToken(t.RIGHT_BRACE)
            case ',': 
                self.addToken(t.COMMA)
            case '.':
                self.addToken(t.DOT)
            case '-':
                self.addToken(t.MINUS)
            case '+':
                self.addToken(t.PLUS)
            case ';':
                self.addToken(t.SEMICOLON)
            case '*':
                self.addToken(t.STAR)
            case _:
                Lox.error(self.line, 'Unexpected character.')

    def advance(self):
        index = self.current
        self.current += 1
        return self.source[index]

    def addToken(self, type: t):
        text = self.source[self.start : self.current] #idk if this is right
        self.tokens.append(Token(type, text, self.line))


    def isAtEnd(self) -> bool:
        return self.current >= len(self.source)
