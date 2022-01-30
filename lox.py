from scanner import Scanner

class Lox:
    def __init__(self):
        self.hadError = False
        
    def runFile(self, path):
        pass

    def runPrompt(self):
        while True:
            print('> ')
            line = input()
            if line is None:
                break
            else:
                self.run(line)

    def run(self):
        scanner = Scanner()
        tokens = scanner.scanTokens()

        for token in tokens:
            print(token)

    @staticmethod
    def error(self, line: int, message: str):
        self.report(line, '', message)

    def report(self, line: int, where: str, message: str):
        print('[line ' + line + '] Error' + where + ': ' + message)
        self.hadError = True

