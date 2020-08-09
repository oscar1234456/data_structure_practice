class exptreeNode(object):
    def __init__(self, name):
        self.leftNode = None
        self.rightNode = None
        self.data = name
        self.res = 0

    def eval(self, node):
        if node is not None:
            self.eval(node.leftNode)
            self.eval(node.rightNode)
            data = node.data
            if data == "+":
                node.res = node.leftNode.res + node.rightNode.res
            elif data == "*":
                node.res = node.leftNode.res * node.rightNode.res
            elif data == "a":
                #let a to 5
                node.res = 5
            elif data == "b":
                #let a to 6
                node.res = 6
            elif data == "c":
                #let a to 7
                node.res = 7
            elif data == "d":
                #let a to 8
                node.res = 8
            elif data == "~":
                node.res = 0 - node.rightNode.res
    def postorder(self, node):
        if node is not None:
          self.postorder(node.leftNode)
          self.postorder(node.rightNode)
          print(node.res)

if __name__ == "__main__":
    root = exptreeNode("+")
    root.leftNode = exptreeNode("+")
    root.rightNode = exptreeNode("d")
    root.leftNode.leftNode = exptreeNode("a")
    root.leftNode.rightNode = exptreeNode("*")
    root.leftNode.rightNode.leftNode = exptreeNode("b")
    root.leftNode.rightNode.rightNode = exptreeNode("c")
    root.eval(root)

    print(root.postorder(root))
    print("final", root.res)