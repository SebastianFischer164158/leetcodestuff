jewels = "aA"
stones = "aAAbbbb"


def numJewelsInStones(jewels: str, stones: str) -> int:
    def find_all(a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: return
            yield start
            start += len(sub)  # use start += 1 to find overlapping matches

    res = 0
    for charr in jewels:
        res += len(list(find_all(stones, charr)))

    return res

print(numJewelsInStones(jewels,stones))