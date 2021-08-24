participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


temp = 0
dic = {}

for part in participant:
  dic[hash(part)] = part
  temp += int(hash(part))

for com in completion:
  temp -= hash(com)

print(dic[temp])