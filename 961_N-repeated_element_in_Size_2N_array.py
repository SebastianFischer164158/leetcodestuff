from typing import List


# two solutions

def repeatedNTimes(A: List[int]) -> int:
    setx = set()
    for n in A:
        if n in setx:
            return n
        else:
            setx.add(n)


def repeatedNTimes2(A: List[int]) -> int:
    hashtable = {}
    for number in A:
        if number not in hashtable:
            hashtable[number] = 1
        else:
            hashtable[number] += 1
    print(hashtable)
    max_n = max(hashtable.values())
    for key, value in hashtable.items():
        if value == max_n:
            return key
        else:
            continue
print(repeatedNTimes([1, 2, 3, 3]))
print(repeatedNTimes([2, 1, 2, 5, 3, 2]))
print(repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))
