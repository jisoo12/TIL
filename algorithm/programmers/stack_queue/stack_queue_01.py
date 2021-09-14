from collections import deque


# progresses = deque([93, 30, 55])
# speeds = deque([1, 30, 5])

progresses = deque([95, 90, 99, 99, 80, 99])
speeds = deque([1, 1, 1, 1, 1, 1])

cnt_list = []
while progresses:
    cnt = 0

    for i in range(len(progresses)):
        if progresses[i] >= 100: continue
        progresses[i] = progresses[i] + speeds[i]

    try:
        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt = cnt + 1
    except IndexError: pass

    if cnt != 0: cnt_list.append(cnt)
        
print(cnt_list)