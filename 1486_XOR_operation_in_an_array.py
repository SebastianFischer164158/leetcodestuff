import numpy as np


def xorOperation(n: int, start: int) -> int:
    res = 0
    for num in np.arange(start=start, stop=start+2*n, step=2):
        res ^= num
    return res


n1 = 5
start1 = 0
n2 = 4
start2 = 3
n3 = 1
start3 = 7
n4 = 10
start4 = 5
print(xorOperation(n1,start1))
print(xorOperation(n2,start2))
print(xorOperation(n3,start3))
print(xorOperation(n4,start4))

