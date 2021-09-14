# 1차원 배열: 3단계 (숫자의 개수)

import sys
from functools import reduce

n = list(map(lambda _: int(sys.stdin.readline().rstrip()), range(3)))
m = reduce(lambda x, y: x * y, n)

list(map(lambda x: print(str(m).count(str(x))), range(10)))
