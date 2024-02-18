n = int(input())
values = sorted(list(map(int, input().split())))
i = 0
j = n - 1
ans_left = i
ans_right = j
total = 2e+9+1

while i < j :
    mixed_values = values[i] + values[j]
    if abs(mixed_values) < total : 
        total = abs(mixed_values)
        answer = [values[i], values[j]]
    if mixed_values < 0 :
        i += 1
    else :
        j -= 1

print(answer[0], answer[1])
