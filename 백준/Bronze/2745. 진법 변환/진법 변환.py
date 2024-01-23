# n : b진법 수, b : 진법
# A : 10 ~ Z : 35
# 진법0*Z + 진법1*Z + 진법2*Z ... 
import sys
input = sys.stdin.readline
N, B = input().split()
B = int(B)
N = N[-1::-1] # 받아온 수 반대로
answer = 0 # 정답 
b = 1 # 커지는 진법

# 맨 뒤에 있던 수부터 돌기 
for n in N :
    if '0' <= n <= '9' : # 숫자가 0부터 9에 속한다면 
        answer += (int(n) * b)
    else : # 숫자의 형태가 아니라 알파벳이라면 
        answer += (ord(n) - ord('A') + 10) * b
    b = b * B
    
print(answer)
