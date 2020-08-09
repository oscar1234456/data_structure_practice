class treeNode(object):
    data = 0
    leftNode = None
    rightNode = None

    def __init__(self, val):
        self.data = val
        self.leftNode = None
        self.rightNode = None

    # let this node has Left child
    def addLeftNode(self, data):
        node = treeNode(data)
        self.leftNode = node
        return node
    # let this node has Right child
    def addRightNode(self, data):
        node = treeNode(data)
        self.rightNode = node
        return node
    buffer = ""
    def inorder(self, root):
        global buffer
        if root is not None:
            self.inorder(root.leftNode)
            buffer += str(root.data)
            self.inorder(root.rightNode)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.leftNode)
            self.postorder(root.rightNode)
            print(root.data,end=" ")

    def preorder(self, root):
        if root is not None:
            print(root.data,end=" ")
            self.preorder(root.leftNode)
            self.preorder(root.rightNode)

    #Copy binary tree
    def copy(self, origroot):
        if origroot is None:
            t = None
        else:
            #origroot is a true node
            t = treeNode(origroot.data) #make new node
            t.leftNode = self.copy(origroot.leftNode) #copy original bt's left child
            t.rightNode = self.copy(origroot.rightNode)#copy original bt's right child
        return t
    #test two BT are equal or not equal
    def equal(self, s, t):
        res = False
        if s is None and t is None:
            # Both BT are empty
            return True
        elif s is not None and t is not None:
            # Both BT may be equal
            if s.data == t.data:
                # s,t node have same data
                if self.equal(s.leftNode, t.leftNode):
                    # the left child of s,t are same
                    res = self.equal(s.rightNode, t.rightNode)

        return res

    #get total count of node of BT
    def countNode(self, node):
        if node is None:
            return 0
        else:
            nL = self.countNode(node.leftNode)
            nR = self.countNode(node.rightNode)
            return nL + nR + 1

    #get the height of BT
    def height(self, node):
        if node is None:
            return 0
        else:
            hL = self.height(node.leftNode)
            hR = self.height(node.rightNode)
            return max(hL, hR) + 1
    #let all nodes of BT resorted by left to right, right to left
    def swap(self, node):
        if node is not None:
            #let children of leftnode all be sorted well
            self.swap(node.leftNode)
            # let children of rightnode all be sorted well
            self.swap(node.rightNode)
            #make children of itself all be sorted well
            temp = node.leftNode
            node.leftNode = node.rightNode
            node.rightNode = temp

    #get the number of leaves in BT
    def countLeaf(self, node):
        if node is None:
            return 0
        else:
            nL = self.countLeaf(node.leftNode)
            nR = self.countLeaf(node.rightNode)
            if (nL + nR) == 0:
                return 1
            else:
                return nL+nR


    def __repr__(self):
        global buffer
        buffer = ""
        self.inorder(self)
        return buffer
