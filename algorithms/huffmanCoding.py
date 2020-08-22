from collections import Counter
from queue import PriorityQueue
import datastructures.trees.src.bst as bst


def optimalTransportCost(msg):
    pq = PriorityQueue()
    counterDict = Counter(msg)
    for k, v in counterDict.items():
        pq.put((v, k))
    tree = bst.Tree()
    for i in range(0, len(counterDict)):
        newNode = bst.Node(None)
        newNode.leftChild = pq.get()
        newNode.rightChild = pq.get()
        newNode.data = newNode.leftChild[0] + newNode.rightChild[0]
        pq.put((newNode.data, '*'))
        tree.insertNode(newNode, newNode.data)


message = "BCCABBDDAECCBBAEDDCC"
optimalTransportCost(message)