# 백준 1157 단어 공부

# 알파벳 대소문자의 단어 속에서 가장 많이 사용되는 알파벳이 무엇인지 알아내기
# 이 단어서 가장 많이 사용된 알파벳을 대문자로 출력
# 가장 많이 사용된 알파벳이 여러 개 일때는 ? 

alphas = [0] * 26
s = input().lower()

for c in s :
    idx = ord(c) - 97
    alphas[idx] += 1

max_cnt = max(alphas)
if alphas.count(max_cnt) > 1 :
    print("?")
else :
    print(chr(alphas.index(max_cnt)+97).upper())
