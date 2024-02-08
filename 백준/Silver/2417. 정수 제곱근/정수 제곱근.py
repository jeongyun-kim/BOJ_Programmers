# 정수가 주어지면 그 수의 정수 제곱근 구하기 
import sys
input = sys.stdin.readline

num = int(input())
left = 0
right = num

def calc(left, right) :
    while left <= right : 
        mid = (left + right) // 2 
        if mid * mid == num : # 딱 제곱으로 된다면 바로 제곱근 return 
            return mid 
        elif mid * mid < num : # 중간값을 제곱했을 때, 목표수보다 작다면 범위를 1 크게
            left = mid + 1
        else :
            right = mid - 1  # 중간값을 제곱했을 때, 목표수보다 크다면 범위를 1 작게
    return right + 1
    # left가 right보다 커졌는데, 딱 떨어지는 제곱근을 찾지못했다면 right의 수가 주어진 수의 제곱근에 가장 가까움
    # 모든 소수점을 무시하고 반올림해주므로 +1 처리 

print(calc(left, right))
