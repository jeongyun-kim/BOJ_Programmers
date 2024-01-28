# 좌표 압축 결과 Xi의 값 = Xi보다 작은 Xj의 개수 
import sys
input = sys.stdin.readline 

n = int(input())
nums = list(map(int, input().split()))
set_nums = sorted((set(nums)))

dic = {num: i for i, num in enumerate(set_nums)}

for num in nums :
    print(dic[num], end = " ")