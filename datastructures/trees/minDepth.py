import datastructures.trees.src.bst as bst


def getLeafNodes(tree):
    if tree.root:
        findLeaf(tree.root)


def findLeaf(node):
    if node.leftChild:
        findLeaf(node.leftChild)
    if node.rightChild:
        findLeaf(node.rightChild)
    if not node.leftChild and not node.rightChild:
        leafs.append(node.data)


def getLeafDistance(data):
    dist = 0
    if tree.root:
        return searchLeafRec(tree.root, data, dist)
    return dist


def searchLeafRec(node, data, dist):
    dist += 1
    if node.data == data:
        return dist
    if node.leftChild and data < node.data:
        dist = searchLeafRec(node.leftChild, data, dist)
        return dist
    if node.rightChild and data > node.data:
        dist = searchLeafRec(node.rightChild, data, dist)
        return dist
    return dist


tree = bst.Tree()
leafs = []
num_list = [30, 14, 36, 18, 12, 70, 45, 6, 38, 20, 1]
for _ in num_list:
    tree.insert(_)
getLeafNodes(tree)
print(leafs)
minimum = None
for _ in leafs:
    distance = getLeafDistance(_)
    print(_, "\t", distance)
    if not minimum:
        minimum = distance
    elif distance < minimum:
        minimum = distance
print("Min depth is:", minimum)
print(tree.traverseLevelOrder())