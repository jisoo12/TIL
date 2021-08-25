# 1차원 배열: 7단계 (평균은 넘겠지)

import sys
from functools import reduce

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    cnt = 0
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    avg = reduce(lambda x, y: x+y, data[1:]) / data[0]
    for i in data[1:]:
        if i > avg: cnt += 1
    
    print('{:.3f}%'.format(round(cnt/data[0]*100, 3)))