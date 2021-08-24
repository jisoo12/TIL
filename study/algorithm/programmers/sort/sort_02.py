# numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]

numbers = list(map(str, numbers))
print(numbers)

# print(list(map(lambda x: x*2, numbers)))

numbers.sort(key=lambda x: x*2, reverse=True)
print(numbers)
print(str(int(''.join(numbers))))

