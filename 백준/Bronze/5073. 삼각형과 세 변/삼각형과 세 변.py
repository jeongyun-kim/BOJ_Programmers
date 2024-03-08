# 삼각형 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의
# 1. Equilateral : 세 변의 길이가 모두 같은 경우
# 2. Isosceles : 두 변의 길이만 같은 경우
# 3. Scalene : 세 변의 길이가 모두 다른 경우
# 4. Invalid : 모든 조건이 포함되지 않을 때
# ! 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건 충족 못함
import sys
input = sys.stdin.readline
answer = ""

while 1 :
    n1, n2, n3 = map(int, input().split())
    cnt, flag = 0, 0
    arr = sorted([n1, n2, n3], reverse=True)
    if sum(arr) == 0 :
        break
    else :
        if arr[0] < arr[1] + arr[2] :
            flag = 1
            for i in range(0, 2) :
                for j in range(i+1, 3) :
                    if arr[i] == arr[j] :
                        cnt += 1
    if flag == 0 :
        answer = "Invalid" 
    else :
        if cnt == 3 :
            answer = "Equilateral"
        elif cnt == 1 :
            answer = "Isosceles"
        elif cnt == 0  :
            answer = "Scalene"
    print(answer)