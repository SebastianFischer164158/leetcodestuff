#!/usr/bin/python3
from itertools import product
from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    res = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i < j:
                # print(f"found pair {(i,j)}")
                res += 1
    # l = range(len(nums))
    # for i, j in product(l, l):
    #     if nums[i] == nums[j] and i < j:
    #         res += 1

    return res


print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(numIdenticalPairs([1, 1, 1, 1]))
print(numIdenticalPairs([1, 2, 3]))
