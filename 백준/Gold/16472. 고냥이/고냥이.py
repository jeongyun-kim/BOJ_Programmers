# n : 인식할 수 있는 알파벳의 종류의 최대 개수 
# 최대 n개의 종류의 알파벳을 가진 연속된 문자열만 인식 가능
# 번역기가 인식할 수 있는 문자열의 최대길이 출력 
# ord('a') = 97, ord('z') = 122 
cnts = [0]*26 # 알파벳의 개수 
n = int(input())
s = input()
j = 0 
answer = 0
arr = []

# 들어있는 알파벳이 몇 개 인지 확인하고 n과 같은 지 
def countAlpha(cnt, n) :
    cnt = 0
    for i in range(26) :
        if cnts[i] > 0 :
            cnt += 1
    if cnt == n :
        return True
    else :
        return False 

for i in range(len(s)) :
    alpha_i = ord(s[i]) - 97 # i번째의 알파벳 
    while j < len(s) : 
        alpha_j = ord(s[j]) - 97 # j번째의 알파벳 
        # 이미 알파벳의 개수가 최대에 달했는데, 다음 알파벳이 새로운 알파벳일 경우 
        if countAlpha(cnts, n) and cnts[alpha_j] == 0 : 
            break 
        # 알파벳의 개수가 최대에 달했는데, 다음 알파벳이 새로운 알파벳이 아닐 경우
        # 또는 알파벳의 개수가 최대에 달하지 않은 경우 
        else :
            cnts[alpha_j] += 1 # 해당 알파벳이 나온 횟수 카운트 
            j += 1 # j 범위 확장
    answer = max(answer, sum(cnts)) # answer과 현재 알파벳들의 개수 비교해서 대입 
    # i + 1 을 위해 
    cnts[alpha_i] -= 1 

print(answer)
