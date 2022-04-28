#COMP 340 HW6
#Josh Sproul

import lexer
import parserr

srcCode = "1 + 310 * 5"
tokSeq = lexer.tokenize(srcCode)
rootNode = parserr.parse(tokSeq)
parserr.printTree((rootNode))
print()

