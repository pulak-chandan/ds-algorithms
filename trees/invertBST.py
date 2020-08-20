import datastructures.bst as bst


def invertRec(node):
    if node.leftChild:
        invertRec(node.leftChild)
    if node.rightChild:
        invertRec(node.rightChild)
    temp = node.leftChild
    node.leftChild = node.rightChild
    node.rightChild = temp


def invertTree():
    if tree.root:
        invertRec(tree.root)


tree = bst.Tree()
num_list = [50, 30, 20, 40, 70, 60, 80]
for _ in num_list:
    tree.insert(_)
print(tree.traverseInOrder())
invertTree()
print(tree.traverseInOrder())

