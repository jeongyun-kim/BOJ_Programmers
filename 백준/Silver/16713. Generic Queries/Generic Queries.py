# 첫째줄 : 수열의 길이 N, Q개의 쿼리
# 둘째줄 : 수열 a1 ... an
# ~ : 하나의 쿼리 Si, ei
# 누적합을 XOR(^)로 푸는 것 뿐
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
dq = [0] * (n+1)
for i in range(1, n+1) :
    dq[i] = dq[i-1] ^ arr[i-1]

for j in range(q) :
    s, e = map(int, input().split())
    answer = answer ^ (dq[e] ^ dq[s-1])

print(answer)