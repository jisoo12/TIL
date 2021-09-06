# 문자열: 7단계 (상수)

import sys

input_sentence = list(map(lambda x: x[::-1], sys.stdin.readline().rstrip().split()))
print(max(input_sentence))