import datastructures.trees.src.bst as bst


def buildTree(postOrder):
    if len(postOrder) == 1:
        tree.insert(postOrder[-1])
    elif len(postOrder) > 1:
        inOrder = sorted(postOrder)
        tree.insert(postOrder[-1])
        lSubTree = inOrder[:inOrder.index(postOrder[-1])]
        lpostOrder = [x for x in postOrder if x in lSubTree]
        rSubTree = inOrder[inOrder.index(postOrder[-1]) + 1:]
        rpostOrder = [x for x in postOrder if x in rSubTree]
        buildTree(lpostOrder)
        buildTree(rpostOrder)


# postOrder -- left, right, root
# inOrder -- left, root, right
testData = [[20, 40, 30, 60, 80, 70, 50],
            [8, 4, 5, 2, 6, 7, 3, 1],
            [4, 12, 10, 18, 24, 22, 15, 31, 44, 35, 66, 90, 70, 50, 25]]
for _ in testData:
    postOrder = _
    tree = bst.Tree()
    buildTree(postOrder)
    print("InOrder traversal of the created tree:", tree.traverseInOrder())
