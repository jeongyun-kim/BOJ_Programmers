# 키의 합이 100이 되는 일곱난쟁이를 찾고 오름차순으로 정렬
from itertools import combinations
import sys
input = sys.stdin.readline

# 난쟁이들 배열
arr = [int(input()) for i in range(9)]

combis = list(combinations(arr, 7))
for combi in combis :
    if sum(combi) == 100 :
        for num in sorted(combi) :
            print(num)
        break
