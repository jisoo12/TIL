# 문자열: 3단계 (알파벳 찾기)

import sys
import string

data = sys.stdin.readline().rstrip()
dict_aphabet = {i:-1 for i in string.ascii_lowercase}

for i in range(len(data)):
    if dict_aphabet[data[i]] == -1:
        dict_aphabet[data[i]] = i

list(map(lambda x: print(int(x), end=' '), list(dict_aphabet.values())))
