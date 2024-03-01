# 단어 수학 문제는 n개의 단어(알파벳 대문자)
# 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔 n개의 수를 합하는 문제 
# 각 문자열을 뒤부터 그 수의 자리를 계산해 자릿수 내림차순으로 정렬한 후 숫자 배정해주기 
# 이전의 문자열에서 이미 나온 알파벳이라면 이미 있던 자릿수에 현재 자릿수 더해주기 
import sys
input = sys.stdin.readline

n = int(input())
alpha_cnt = [0] * 26

for i in range(n) :
    s = input().rstrip()
    num = 1 # 자릿수 
    for j in range(len(s)-1, -1, -1) : # 받아온 문자열 맨뒤부터 자릿수 계산
        c_idx = ord(s[j]) - ord('A') # 해당 알파벳의 인덱스 값
        alpha_cnt[c_idx] += num 
        num *= 10 # 자릿수 올리기 1의 자리 -> 10의 자리 -> 100의 자리 ...

alpha_cnt = sorted(alpha_cnt, reverse=True)
answer = 0

for i in range(9, -1, -1) :
    answer += (alpha_cnt[9-i]*i)

print(answer)
