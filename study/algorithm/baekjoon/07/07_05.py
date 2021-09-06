# 문자열: 5단계 (단어 공부)

import string

# print(string.ascii_lowercase)

q = "aaabbbccccc"
set_q = ''.join(set(q))

list(map(lambda x: print(f'count of {x}:', q.count(x)), set_q))
# for i in set_q:
#     print(f'count of {i}:', q.count(i))