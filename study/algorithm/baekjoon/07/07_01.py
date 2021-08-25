# 문자열: 1단계 (아스키 코드)

import sys

print((lambda x: ord(x))(sys.stdin.readline().rstrip()))