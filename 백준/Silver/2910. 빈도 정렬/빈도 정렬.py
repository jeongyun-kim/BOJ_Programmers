# X와 Y를 비교했을 때, X의 빈도수가 높다면 X -> Y
# 빈도수가 같다면 먼저 나온 것이 앞으로 
# => 빈도 정렬
# N개로 이루어진 수열에 숫자는 모두 C보다 작거나 같다
import sys
input = sys.stdin.readline
from collections import Counter

n, c = map(int, input().split()) 
nums = list(map(int, input().split())) # 수열 -> 배열 
cnts = Counter(nums) # 빈도수 카운트 

# 빈도수 순으로 내림차순 -> 빈도수가 같다면 인덱스순으로 오름차순 
answer = sorted(nums, key=lambda x:(-cnts[x], nums.index(x)))

# 결과 출력 
print(*answer)

