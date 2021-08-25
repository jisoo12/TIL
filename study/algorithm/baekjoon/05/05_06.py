# 1차원 배열: 6단계 (OX귀즈)

import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    cnt = 0
    plus_cnt = 0

    ox = sys.stdin.readline().rstrip()
    for i in ox:
        if i == 'O':
            plus_cnt += 1
            cnt += plus_cnt
        else: plus_cnt = 0

    print(cnt)
    