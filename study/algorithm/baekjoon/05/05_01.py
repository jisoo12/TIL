# 1차원 배열: 1단계 (최소, 최대)

import sys

n = int(sys.stdin.readline().rstrip())
# n_list = [0] * n

n_list = list(map(int, sys.stdin.readline().rstrip().split()))
n_list.sort()
print(n_list[0], n_list[-1])
