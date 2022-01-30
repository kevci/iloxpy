import sys
from lox import Lox

lox = Lox()

if len(sys.argv > 1):
    print('Usage: iloxpy [script]')
    sys.exit(64)
elif len(sys.argv) == 1:
    lox.runFile(sys.argv[0])
else:
    lox.runPrompt()
