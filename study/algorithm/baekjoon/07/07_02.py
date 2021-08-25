# 문자열: 2단계 (숫자의 합)

import sys

_ = int(sys.stdin.readline().rstrip())
print(sum(list(map(int, list(str(sys.stdin.readline().rstrip()))))))
