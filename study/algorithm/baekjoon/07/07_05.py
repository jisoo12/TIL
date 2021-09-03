import string

# print(string.ascii_lowercase)

q = "aaabbbccc"
set_q = ''.join(set(q))


for i in set_q:
    print(f'count of {i}:', q.count(i))