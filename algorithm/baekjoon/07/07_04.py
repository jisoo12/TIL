# 문자열: 4단계 (문자열 반복)

import sys

l = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    m = sys.stdin.readline().rstrip().split()
    l.append(''.join(list(map(lambda x: x*int(m[0]), m[-1]))))
list(map(lambda x: print(x), l))
        