#COMP 340 HW5
#Josh Sproul

import lexer

srcCode = "((12+3*5)+5/4)"
tokSeq = lexer.lexer.tokenize(srcCode)

for i in tokSeq:
    print(i.type, i.value)