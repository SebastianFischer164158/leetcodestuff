import itertools
from typing import List


def shift(l, n):
    return itertools.islice(itertools.cycle(l), n, n + len(l))


def decrypt(code: List[int], k: int) -> List[int]:
    resp = []
    if k > 0:

        for i in range(1,len(code)):
            # print(" ---> ", code[i + 1:k + 1])
            resp.append(sum(code[i:k]))

    return resp


code = [5, 7, 1, 4]

k = 3
print(decrypt(code, k))
