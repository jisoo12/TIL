# 함수: 1단계 (정수 N개의 합)

def solve(a: list):
    sum = 0
    for i in range(len(a)):
        sum += a[i]

    return sum

print(solve([1, 2, 3]))