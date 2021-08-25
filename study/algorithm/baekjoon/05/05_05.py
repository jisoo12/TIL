# 1차원 배열: 5단계 (평균)

import sys
from functools import reduce

n = int(sys.stdin.readline().rstrip())
scores = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    scores[i] = scores[i]/scores[-1]*100
    
print(reduce(lambda x, y: x+y, scores) / n)
