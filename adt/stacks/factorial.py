import adt.stacks.src.stack as stack


def findFactorial(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1
    return fact


def findFactRec(n):
    if n == 0:
        return 1
    else:
        return n * findFactRec(n-1)


def findFactStack(n):
    stk = stack.Stack()
    while n > 0:
        stk.push(n)
        n -= 1

    fact = 1
    while not stk.isEmpty():
        fact = fact * stk.pop()
    return fact


n = 6
print("The factorial of", n, "is:", findFactorial(n))
print("The factorial of", n, "is:", findFactRec(n))
print("The factorial of", n, "is:", findFactStack(n))
