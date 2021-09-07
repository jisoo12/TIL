# 기본 수학 1: 1단계 (손익분기점)

import sys

a, b, c = sys.stdin.readline().rstrip().split()
if int(c) - int(b) < 1: print(-1)
else: print(int(int(a) / (int(c) - int(b)) + 1))