class Token:
    def __init__(self, type, lexeme, line):
        self.type = type
        self.lexeme = lexeme
        self.line = line

    def __str__(self) -> str:
        return self.type + ' ' + self.lexeme