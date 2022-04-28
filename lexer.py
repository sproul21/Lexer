#COMP 340 HW5
#Josh Sproul

class token:
    def __int__(self, type, value):
        self.type = type
        self.value = value

def tokenize(srcCode):
    tokSeq = []
    while srcCode != "":
        char = srcCode[0]
        if char == "+":
            newToken = token("PLUS", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == "*":
            newToken = token("MULTIPLICATION", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == " ":
            srcCode = srcCode[1:]
        elif char.isdigit():
            numbStr = ""
            while char.isdigit():
                numbStr += char
                srcCode = srcCode[1:]
                if srcCode == "":
                    char = srcCode
                else:
                    char = srcCode[0]
            newToken = token("NUMBER", numbStr)
            tokSeq.append(newToken)

    return tokSeq
