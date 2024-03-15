# 백준 1157 단어 공부

# 알파벳 대소문자의 단어 속에서 가장 많이 사용되는 알파벳이 무엇인지 알아내기
# 이 단어서 가장 많이 사용된 알파벳을 대문자로 출력
# 가장 많이 사용된 알파벳이 여러 개 일때는 ? 
from collections import Counter

s = input().upper()
# 카운트 많이 된 순으로 정렬해서 보여줌
alphas = Counter(s).most_common()

if len(alphas) >= 2 and alphas[0][1] == alphas[1][1] :
    print("?")
else :
    print(alphas[0][0])
