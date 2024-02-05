# N : 상근이가 가진 숫자 카드의 개수 
# 상근이가 가진 카드에 적힌 수
# M 
# 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수 
from collections import Counter

n = int(input())
arr = Counter(list(map(int, input().split())))
m = int(input())
nums = list(map(int, input().split()))

for i in range(m) :
    key = nums[i]
    if key in arr :
        print(arr[key], end=" ")
    else :
        print(0, end=" ")
