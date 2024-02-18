# n : 수열의 길이, s : 합 
# "s 이상" 조건을 만족하면서 길이가 가장 짧은 것 구하기
# 만들어지지 않으면 0 출력 
n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = n + 1 # 최대길이는 n이지만 s 이상의 수를 만족하는지 확인하기 위해
j, total = 0, 0

for i in range(n) :
    while total < s and j < n : # 합이 s를 넘지않으면서 우측 포인터가 n을 넘지않을때
        total += arr[j]
        j += 1
    if total >= s : # 합이 s 이상이면 현재의 길이와 이전의 길이 비교해 대입
        answer = min(j-i, answer)
    total -= arr[i] # i 증가하면서 1~2를 2~로 변경 

if answer == n + 1 :
    print(0)
else :
    print(answer)