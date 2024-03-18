# 백준 10448 유레카 이론

# 삼각수 : Tn = n(n+1) / 2
# 자연수가 주어졌을 때, 그 수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지
k = int(input())

triangleNumbers = [0] * 45
for i in range(1, 45) :
    tNum = i * (i+1) // 2
    triangleNumbers[i] = tNum

def calc(num) :
    for j in range(1, len(triangleNumbers)) :
        for k in range(1, len(triangleNumbers)) :
            for h in range(1, len(triangleNumbers)) :
                total = triangleNumbers[j] + triangleNumbers[k] + triangleNumbers[h]
                if total == num :
                    return 1
    return 0

for i in range(k) :
    num = int(input())
    print(calc(num))
