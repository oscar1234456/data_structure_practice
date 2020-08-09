from Tree import treeNode





if __name__ == "__main__":
    root = treeNode.treeNode(3)
    node1 = root.addLeftNode("5")
    node1.addRightNode("4")
    node2 = root.addRightNode("2")
    node3 = node2.addRightNode("1")
    node3.addRightNode("6")
    print(root)

    # root2 = root.copy(root)
    # print(root2)
    root2 = treeNode.treeNode("1")
    node2 = root2.addRightNode("3")
    print(root.equal(root, root2))

    print(root.countNode(root2))
    print(root.height(root2))

    print(root.swap(root))
    print(root)

    print(root.countLeaf(root))
