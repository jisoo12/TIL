# scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
# scores = [[50,90],[50,87]]
scores = [[70,49,90],[68,50,38],[73,31,100]]
grades = ''

for i in range(len(scores)):
    compare_list = []

    for j in range(len(scores[i])):
        compare_list.append(scores[j][i])


    print(f'compare_list: {compare_list}')
    print(f'index({i}) value: {compare_list[i]}')
    print(f'count of index({i}) value: {compare_list.count(compare_list[i])}')
    print(f'max value of compare_list: {max(compare_list)}')
    

    if (max(compare_list) == compare_list[i] or min(compare_list) == compare_list[i]) and (compare_list.count(compare_list[i]) == 1):
        del compare_list[i]


    print(f'compare_list_result: {compare_list}')
    print(f'sum of compare_list_result: {sum(compare_list)}')
    print(f'average of compare_list_result: {sum(compare_list)/len(compare_list)}')
    print()


    average = sum(compare_list)/len(compare_list)
    if average >= 90:
        grades += "A"
    elif average >= 80:
        grades += "B"
    elif average >= 70:
        grades += "C"
    elif average >= 50:
        grades += "D"
    else:
        grades += "F"


print(f'result: {grades}')
    