

class heap(object):
    # nodeArray index start from 1
    def __init__(self, nodeArray):
        self.nodeArray = nodeArray
        self.nodeArray.insert(0, 0)
        self.buildMyHeap(len(self.nodeArray)-1)

    # t: root index
    # n: upper bound of index
    def adjust(self, t, n):
        x = self.nodeArray[t]  # root data
        j = 2 * t  # left child index
        while j <= n:
            if j < n:
                # there is also a right child
                # need to find MAX
                if self.nodeArray[j] < self.nodeArray[j+1]:
                    j = j+1
            if self.nodeArray[j] > x:
                # child > present root
                self.nodeArray[j//2] = self.nodeArray[j]
                j = 2 * j
            else:
                break
        self.nodeArray[j//2] = x

    # n: the number of nodes
    def buildMyHeap(self, n):
        i = n//2
        while i > 0:
            self.adjust(i, n)
            i -= 1
        self.nodeArray.remove(0)

    def delMax(self) -> int:
        n = len(self.nodeArray)
        if n == 1:
            return self.nodeArray.pop()
        self.nodeArray.insert(0, 0)
        rootMax = self.nodeArray[1]  # root is the Max
        self.nodeArray[1] = self.nodeArray.pop() # the last node move to root
        self.adjust(1, n-1)
        self.nodeArray.remove(0)
        return rootMax


if __name__ == "__main__":
    myHeap = heap([7,3,2,5,8,1,6,9,10,100,250,148,132])
    print(myHeap.nodeArray)
    for i in range(len(myHeap.nodeArray)):
        print(myHeap.delMax() , end=" ,")


