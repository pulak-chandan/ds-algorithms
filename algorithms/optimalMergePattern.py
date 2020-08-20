from queue import PriorityQueue

def insert_to_maintain_sorting(x, list):
    count = 0
    for val in list:
        if val < x:
            count += 1
        else:
            list.insert(count, x)
            break
    if count == len(list):
        list.append(x)
    return list


def findOptimalMergingCost(filesSizeList):
    filesSizeList = sorted(filesSizeList)
    total_cost = 0
    while len(filesSizeList) > 2:
        x = (filesSizeList[0] + filesSizeList[1])
        total_cost += x
        filesSizeList = insert_to_maintain_sorting(x, filesSizeList[2:])
    print("Optimal cost of merging:", total_cost + sum(filesSizeList))


# MIN Priority Queue
def findOptimalMergingCostUsingPriorityQueue(filesSizeList):
    total_cost = 0
    pq = PriorityQueue()
    for filesize in filesSizeList:
        pq.put(filesize)
    for i in range(0, len(filesSizeList) - 1):
        combinedFileSize = pq.get() + pq.get()
        total_cost += combinedFileSize
        pq.put(combinedFileSize)
    print("Optimal cost of merging using Priority Queue:", total_cost)


# n = number of lists
n = 5
fileSizes = [20, 30, 10, 5, 30]
findOptimalMergingCost(fileSizes)
findOptimalMergingCostUsingPriorityQueue(fileSizes)
