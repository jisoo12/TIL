# 1차원 배열: 4단계 (나머지)

import sys

n = list(map(lambda _: int(sys.stdin.readline().rstrip()) % 42, range(10)))
print(len(set(n)))