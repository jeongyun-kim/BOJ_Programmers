# n : 수열의 크기
# 수열에 포함되는 수
# x 
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
answer = 0
cnt = [0] * 1000001 # 들어있는 숫자 확인하는 배열

# 1이 들어있다면 cnt[1] = 1
for i in range(n) :
    idx = arr[i]
    cnt[idx] += 1

# 1+12 / 2+11 / 3+10 / 10+3 / 11+2 / 12+1
# 같은 경우를 두 번 세고 있기때문에 [만들어야되는 수//2+1]로 범위 줄이기
for i in range(1, (x-1) // 2 + 1):
    if x-i <= 100000 :
        answer += (cnt[i]*cnt[x-i])

print(answer)

