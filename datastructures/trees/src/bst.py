# Recursive
import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# HAS A Relationship
# BinarySearchTree has a NODE
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)  # has a relationship
        else:
            self.insertNode(self.root, data)

    # O(logN), but if tree is unbalanced it can be reduced to O(N) - AVL, RBT needed
    def insertNode(self, node, data):
        if data < node.data:
            if not node.leftChild:
                node.leftChild = Node(data)
            else:
                self.insertNode(node.leftChild, data)
        else:
            if not node.rightChild:
                node.rightChild = Node(data)
            else:
                self.insertNode(node.rightChild, data)

    # Left most leaf node
    def minValue(self):
        if not self.root:
            return None
        else:
            return self.getMin(self.root)

    def getMin(self, node):
        if not node.leftChild:
            return node.data
        else:
            return self.getMin(node.leftChild)

    # in order traversal - left, root, right
    def traverseInOrder(self):
        tList = []
        if self.root:
            self.traverseInOrderRec(self.root, tList)
        return tList

    def traverseInOrderRec(self, node, tList):
        if node.leftChild:
            self.traverseInOrderRec(node.leftChild, tList)
        tList.append(node.data)
        if node.rightChild:
            self.traverseInOrderRec(node.rightChild, tList)

    # pre order traversal - root, left, right
    def traversePreOrder(self):
        tList = []
        if self.root:
            self.traversePreOrderRec(self.root, tList)
        return tList

    def traversePreOrderRec(self, node, tList):
        tList.append(node.data)
        if node.leftChild:
            self.traversePreOrderRec(node.leftChild, tList)
        if node.rightChild:
            self.traversePreOrderRec(node.rightChild, tList)

    # post order traversal - left, right, root
    def traversePostOrder(self):
        tList = []
        if self.root:
            self.traversePostOrderRec(self.root, tList)
        return tList

    def traversePostOrderRec(self, node, tList):
        if node.leftChild:
            self.traversePostOrderRec(node.leftChild, tList)
        if node.rightChild:
            self.traversePostOrderRec(node.rightChild, tList)
        tList.append(node.data)

    def traverseLevelOrder(self):
        tList = []
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            temp = q.get()
            tList.append(temp.data)
            if temp.leftChild:
                q.put(temp.leftChild)
            if temp.rightChild:
                q.put(temp.rightChild)
        return tList

    def search(self, data):
        if self.root:
            return self.searchRec(self.root, data)

    def searchRec(self, node, data):
        if node.data == data:
            return True
        if node.leftChild and data < node.data:
            return self.searchRec(node.leftChild, data)
        if node.rightChild and data > node.data:
            return self.searchRec(node.rightChild, data)

    def deleteDataRec(self, node, data):
        if data < node.data:
            node.leftChild = self.deleteDataRec(node.leftChild, data)
        elif data > node.data:
            node.rightChild = self.deleteDataRec(node.rightChild, data)

        # Base case
        elif data == node.data:
            # Case 1
            if not node.leftChild and not node.rightChild:
                print("Removing a leaf node!")
                del node
                return None

            # case 2
            elif node.rightChild and not node.leftChild:
                print("Removing a node with single right child!")
                temp = node.rightChild
                del node
                return temp

            # case 2
            elif node.leftChild and not node.rightChild:
                print("Removing a node with single left child!")
                temp = node.leftChild
                del node
                return temp

            # Case 3
            elif node.rightChild and node.leftChild:
                print("Removing a node with both left right children!")
                predecessor = self.getPredecessor(node.leftChild)
                node.data = predecessor.data
                node.leftChild = self.deleteDataRec(node.leftChild, predecessor.data)
        return node

    def getPredecessor(self, node):
        while node.rightChild:
            node = node.rightChild
        return node

    def deleteData(self, data):
        if self.root:
            self.root = self.deleteDataRec(self.root, data)


'''
bst = Tree()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(14)
print(bst.traverseInOrder())
bst.deleteData(10)
print(bst.traverseInOrder())
'''



