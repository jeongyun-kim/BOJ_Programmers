# t : 더해서 되는 수
# n : 배열 A의 정수의 개수 
# m : 배열 B의 정수의 개수 
# 배열 내 수들을 더해 t가 되는 경우의 수 출력, 없을 경우 0
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
arr1= list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
dicA = {} # 배열 A의 누적합 dictionary 
answer = 0 

for i in range(n) : # 배열 A의 누적합을 배열로 
    numA = 0
    for j in range(i, n) :
        numA = sum(arr1[i:j+1])
        if numA not in dicA :
            dicA[numA] = 1
        else :
            dicA[numA] += 1

for i in range(m) : 
    numB = 0
    for j in range(i, m) :
        numB = sum(arr2[i:j+1]) # 배열 B의 누적합 계산 
        numB = t - numB # t - b 
        if numB in dicA.keys() : # t - b == a 라면
            answer += dicA[numB] # answer + 충족되는 경우의 수

print(answer)
