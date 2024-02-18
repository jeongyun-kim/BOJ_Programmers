# 수열의 i번째부터 j번째까지의 합이 M이 되는 경우의 수
# n : 수열의 길이, m : 만들어야 하는 수
# sum > m : i + 1
# sum < m : j + 1
# sum == m : i + 1, answer + 1
n, m = map(int, input().split())
arr = list(map(int, input().split()))
i = 0
j = 1
current_sum = arr[0]
answer = 0

while (1) :
    if current_sum < m :
        if j < n :
            current_sum += arr[j]
            j += 1
        else :
            break 
    elif current_sum == m :
        answer += 1
        current_sum -= arr[i]
        i += 1
    else :
        current_sum -= arr[i]
        i += 1

print(answer)
