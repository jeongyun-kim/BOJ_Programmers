# n : 배열 A의 크기, m : 배열 B의 크기
# 둘째줄 : 배열 A의 내용
# 셋째줄 : 배열 B의 내용 
# 두 배열을 합친 후 정렬한 결과 출력 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sorted_arr = sorted(A+B)

for num in sorted_arr :
    print(num, end=" ")