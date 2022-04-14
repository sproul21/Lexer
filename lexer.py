#COMP 340 HW5
#Josh Sproul

seq = list()

class lex:

    def __init__(self, type, value):
        self.type = type
        self.value = value
        seq.append(self)

class lexer(lex):

    def tokenize(srcCode):
        for source in srcCode:
            if source == '(':
                type = "LPAREN"
                value = "("

            elif source == ')':
                type = "RPAREN"
                value = ")"

            elif source == '/':
                type = "DIVISION"
                value = "/"

            elif source == '*':
                type = "MULTIPLICATION"
                value = "*"

            elif source == '+':
                type = "PLUS"
                value = "+"

            elif source == '-':
                type = "MINUS"
                value = "-"

            elif source.isnumeric():
                type = "NUMBER"
                value = str(source)

            lex(type, value)
        return seq