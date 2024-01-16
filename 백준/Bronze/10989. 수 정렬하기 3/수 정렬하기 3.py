import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*10001 

# 해당 숫자가 들어있는 개수
for i in range(n) :
    arr[int(input())] += 1

# 배열을 돌면서 해당 숫자가 있다면 그 개수만큼 print
for j in range(1, 10001) :
    if arr[j] > 0 :
        for k in range(arr[j]) :
            print(j)
