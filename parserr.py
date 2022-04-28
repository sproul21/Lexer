# COMP 340 HW6
# Josh Sproul

class treeNode:
    def __init__(self, type, value, precedence):
        self.type = type
        self.value = value
        self.precedence = precedence
    parent = None
    lChild = None
    rChild = None

def getPrecedence(type):
    precedence = 0
    if type == "PLUS" or type == "MINUS":
        precedence = 1
    elif type == "MULTIPLICATION" or type == "DIVISION":
        precedence = 2
    return precedence

def createTreeNodeList(tokSeq):
    treeNodeList = []
    for token in tokSeq:
        newNode = treeNode(token.type, token.value, getPrecedence(token.type))
        treeNodeList.append(newNode)
    return treeNodeList

def parse(tokSeq):
    rootNode = None
    treeNodeList = createTreeNodeList(tokSeq)
    parsing(treeNodeList)
    rootNode = findRoot(treeNodeList)
    return rootNode



def parsing(treeNodeList):
    dummyNode = treeNode("DUMMY", "", 0)
    treeNodeList.insert(0, dummyNode)
    treeNodeList.append(dummyNode)

    for index in range(len(treeNodeList)):
        node = treeNodeList[index]
        if node.type == "NUMBER":
            lOp = treeNodeList[index-1]
            rOp = treeNodeList[index+1]
            if rOp.precedence > lOp.precedence:
                #right
                rOp.lchild = node
                node.parent = rOp
                if lOp.type != "DUMMY":
                    lOp.rchild = rOp
                    rOp.parent = lOp
            else:
                #left
                lOp.rchild = node
                node.parent = lOp
                if rOp.type != "DUMMY":
                    while lOp.parent != None:
                        if lOp.parent.precedence < rOp.precedence:
                            break
                        lOp = lOp.parent

                    if lOp.parent != None:
                        lOp.parent.rchild = rOp
                        rOp.parent = lOp.parent
                    rOp.lchild = lOp
                    lOp.parent = rOp

def findRoot(treeNodeList):
    rootNode = None
    for node in treeNodeList:
        if node.parent == None and node.type != "DUMMY":
            rootNode = node
            break
    return rootNode

def printTree(rootNode):
    if rootNode.lchild == None and rootNode.rchild == None:
        print(rootNode.value, end="")
    else:
        print("(", end="")
        printTree(rootNode.lchild)
        print(rootNode.value, end="")
        printTree(rootNode.rchild)
        print("(", end="")