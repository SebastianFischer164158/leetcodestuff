from typing import List


def restoreString(s: str, indices: List[int]) -> str:
    resp = [""]*len(s)
    for idx, indice in enumerate(indices):
        resp[indice] = s[idx]
    return ''.join(resp)


s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
print(restoreString(s,indices))