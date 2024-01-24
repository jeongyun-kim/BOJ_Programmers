arr = [0] * 10001

for i in range(1, 10001) :
    num = str(i)
    total = int(num)
    for n in num :
        total += int(n)
    if total <= 10000 :
        arr[total] += 1

for j in range(1, 10001) :
    if arr[j] == 0 :
        print(j)