# 문자열: 6단계 (단어의 개수)

import sys

input_sentence = sys.stdin.readline().rstrip()
print(len(input_sentence.strip().split()))
