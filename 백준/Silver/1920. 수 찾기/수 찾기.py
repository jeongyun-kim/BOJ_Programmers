# 첫째줄 : N 
# 둘째줄 : N개의 정수(A[1], A[2]...A[N])
# 셋째줄 : M
# 넷째줄 : M개의 수 -> 이 수들이 A안에 존재하는지 알아내기 
n = int(input())
arr = set(map(int,input().split()))
m = int(input())
nums = list(map(int,input().split()))
for i in range(m) :
    if nums[i] in arr :
        print(1)
    else :
        print(0)