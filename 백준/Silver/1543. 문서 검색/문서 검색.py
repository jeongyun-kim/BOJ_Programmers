# find(찾을 문자, 시작 인덱스)
s1 = input()
s2 = input()
i = 0
answer = 0

while i < len(s1) :
    if s1[i:i+len(s2)] == s2 :
        answer += 1
        i += len(s2)
    else :
        i += 1
    
print(answer)
