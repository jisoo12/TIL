# while문: 2단계 (A+B - 4)

import sys

# lines = sys.stdin.readlines()
# for line in lines:
#     a, b = map(int, line)
#     print(a+b)


while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError: break
