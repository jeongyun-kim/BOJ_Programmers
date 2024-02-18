# 수열의 i번째부터 j번째까지의 합이 M이 되는 경우의 수
# n : 수열의 길이, m : 만들어야 하는 수
# sum >= m : i + 1
# sum < m : j + 1
n, m = map(int, input().split())
arr = list(map(int, input().split()))
j = 0
current_sum = 0 # i부터 j까지의 합 
answer = 0

for num in arr :
    while current_sum < m and j < n : 
        current_sum += arr[j]
        j += 1
    if current_sum == m :
        answer += 1
    current_sum -= num # A[0] + A[1]의 상태에서 A[0]값빼주면 i가 +1 된 것과 같음 
    
print(answer)