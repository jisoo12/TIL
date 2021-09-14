# 1차원 배열: 2단계 (최댓값)

import sys

n = {}
for i in range(9):
    n[(int(sys.stdin.readline().rstrip()))] = i+1

print(sorted(list(n.keys()), reverse=True)[0], n[sorted(list(n.keys()), reverse=True)[0]], sep='\n')
