# 이분탐색 방식

# t : 더해서 되는 수
# n : 배열 A의 정수의 개수 
# m : 배열 B의 정수의 개수 
# ex) arr = [1, 2, 2, 2, 3] 
# start = bisect.bisect_left(arr, 2) = 1
# end = bisect.bisect_right(arr, 2) = 4
# 2의 개수(경우의 수) = end - start = 3 
import sys
input = sys.stdin.readline
import bisect

t = int(input())
n = int(input())
arr1= list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
answer = 0 
Asum, Bsum = arr1, arr2

for i in range(n) : # A의 누적합
    for j in range(i+1, n) :
        Asum.append(sum(arr1[i:j+1]))

for i in range(m) : # B의 누적합 
    for j in range(i+1, m) :
        Bsum.append(sum(arr2[i:j+1])) 

# bisect를 위한 정렬 
Asum = sorted(Asum)
Bsum = sorted(Bsum)

for i in range(len(Asum)) :
    start = bisect.bisect_left(Bsum, t-Asum[i]) 
    end = bisect.bisect_right(Bsum, t-Asum[i]) 
    answer += (end - start) # t - a = b를 만족하는 경우의 수 

print(answer)
