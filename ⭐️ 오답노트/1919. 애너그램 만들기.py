# 백준 1919 애너그램 만들기

# 두 영어 단어가 철자의 순서를 뒤바꾸어 같아질 때, 둘은 애너그램 관계에 있음
# 두 영단어가 주어졌을 때, 두 단어가 애너그램 관계에 있게 하기 위해 제거해야 하는 
# 최소 개수의 문자 수 구하기 
alphas = [0] * 26
s1 = input() # 첫번째 영단어
s2 = input() # 두번째 영단어
answer = 0

# 첫번째 영단어 돌면서
for c in s1 :
    # 첫번째 영단어 내에 있는 알파벳 개수 + 1
    idx = ord(c) - 97
    alphas[idx] += 1

# 두번째 영단어 돌면서
for c in s2 :
    # 첫번째 영단어에서 겹치거나 첫번째 영단어에는 없는 알파벳 빼기
    idx = ord(c) - 97
    alphas[idx] -= 1

# 두 영단어에서 겹치지 않는 알파벳들의 개수만 남은 alphas 돌면서
# 음수가 있을수도 있으므로 abs로 감싸서 answer에 더하기
for alpha in alphas :
    answer += abs(alpha)

# 결과 출력
print(answer)
