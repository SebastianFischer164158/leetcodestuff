from functools import reduce
from operator import mul


def subtractProductAndSum(n: int) -> int:
    res = list(map(int, str(n)))
    return reduce(mul, res, 1) - sum(res)

print(subtractProductAndSum(234))
print(subtractProductAndSum(4421))