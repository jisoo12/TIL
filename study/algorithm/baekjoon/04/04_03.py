# while문: 3단계 (더하기 사이클)

import sys

data = sys.stdin.readline().rstrip()
cnt = 0

new_data = data
while True:
    if int(new_data) < 10:
        sum_data = 0 + int(new_data)
    else:    
        sum_data = int(new_data[0]) + int(new_data[-1])
    
    if sum_data >= 10:
        sum_data = sum_data - 10
    
    new_data = new_data[-1] + str(sum_data)

    cnt = cnt + 1

    if int(data) == int(new_data): break

print(cnt)
