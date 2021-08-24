import heapq

scoville = [1, 2, 3, 9, 10, 12]
# scoville = [5, 2, 20, 15, 10, 12]

k = 7

cnt = 0
heap = []
result = []

for value in scoville:
  heapq.heappush(heap, value)

while True:
  if heap == []:
    cnt = -1
    break

  for i in range(len(heap)):
    result.append(heapq.heappop(heap))
  
  if result[0] >= k: break
  cnt = cnt + 1
  result.append(result.pop(0) + result.pop(0) *2)
  heap = result

  # for value in result:
  #   heapq.heappush(heap, value)
  

print(cnt)

# aaa = sorted(scoville)

# while True:
  
#   # print(aaa)
#   pop1 = aaa.pop(0)
#   pop2 = aaa.pop(0)
#   if pop1 >= k:
#     break
#   aaa.append(pop1 + (pop2 * 2))
#   aaa = sorted(aaa)
#   count = count + 1
#   # print(aaa)

# print(count)

