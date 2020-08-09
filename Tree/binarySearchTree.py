from Tree import treeNode

class binarySearchTree(object):
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root is None:
            # if BST is empty
            self.root = treeNode.treeNode(data)
            # create a new root
        else:
            # there was a tree already
            self.insertNonEmpty(self.root, data)

    def insertNonEmpty(self, node:treeNode, data):
        if data >= node.data:
            if node.rightNode is None:
                node.rightNode = treeNode.treeNode(data)
            else:
                self.insertNonEmpty(node.rightNode, data)
        else:
            if node.leftNode is None:
                node.leftNode = treeNode.treeNode(data)
            else:
                self.insertNonEmpty(node.leftNode, data)

    def search(self, node, data):
        if node is not None:
            if data > node.data:
                return self.search(node.rightNode, data)
            elif data == node.data:
                print(str(data),":","Find")
                return (True, node)
            else:
                #data < node.data
                return self.search(node.leftNode, data)
        else:
            print(str(data),":","Not Found")
            return (False, None)

    def delete(self, data):
        res = self.search(self.root, data)
        if res[0]:
            # find data, can do delete
            if res[1].leftNode is None and res[1].rightNode is None:
                res[1] = None
            elif res[1].leftNode is not None and res[1].rightNode is not None:
                pass
            else:
                pass
        else:
            print("Can't delete.(Not Found this data)")

if __name__ == "__main__":
    bst = binarySearchTree()
    for i in [5,3,8,7,9,6,4,1,2]:
        bst.insert(i)
    # bst.root.preorder(bst.root)
    # #the inorder of BST is the number serial in ascending order
    # print("inorder",end="")
    # print(bst.root)

    bst.delete(100)
