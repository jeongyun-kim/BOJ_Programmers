# 수 N개가 주어짐 -> 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수 구하기 
# => Ai + ... Aj의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수 구하기 
# 모든 경우의 수를 확인해야 하므로 누적합으로 풀면 빠르고 쉽게 풀 수 있음!
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] * (n+1) # 누적합 배열
prefix_m = [0] * m # 각 구간의 % m 했을 때의 나머지 배열

for i in range(1, n+1) :
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]  
    # 각 구간의 합을 % m 했을 때 나머지의 개수 구하기 
    prefix_m[prefix_sum[i] % m] += 1

answer = prefix_m[0] # 각 누적합이 m의 배수인 경우 
# 각 누적합의 조합으로 만들 수 있는 경우 구하기 
# ex) %m == 0인 누적합[i]가 3개인 경우, 3개 중 2개 고르기 => i~j
# ex) %m == 1인 누적합[i]가 2개인 경우, 1인것끼리 빼면 0이므로 1인 것들 중에 2개 고르기
# 3C2 / 2C2 => 3*2 // 2, 2*1 // 2
for num in prefix_m :
    answer += (num * (num-1) // 2) 

print(answer)
