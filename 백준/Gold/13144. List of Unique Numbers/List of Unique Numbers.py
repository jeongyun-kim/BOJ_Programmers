# n : 수열의 길이 (1<=n<=100,000)
# 수열에서 연속한 1개 이상의 수를 뽑았을 때
# 같은 수가 여러 번 등장하지 않는 경우의 수 구하기 
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
nums_cnt = [0] * 100001 # 숫자 등장 횟수 카운트 
j = 0
answer = 0

for i in range(n) :
    while j < n : 
        num = arr[j] # 현재 수
        if nums_cnt[num] == 1 : # 현재 수가 등장한 적 있다면 반복문 탈출
            break
        else : # 현재 수가 등장한 적 없다면 
            nums_cnt[num] = 1 # 등장 표시
            j += 1 # j 범위 이동 
    answer += (j-i) # 수가 여러 번 등장하지 않는 경우 + 
    nums_cnt[arr[i]] = 0 # i 범위 이동하며 현재 i번째 방문하지 않음 표시 

print(answer)

