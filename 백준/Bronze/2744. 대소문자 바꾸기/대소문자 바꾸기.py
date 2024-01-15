# 대문자는 소문자로, 소문자는 대문자로
answer = ""

for c in input() :
    if c.islower() :
        answer += c.upper()
    else :
        answer += c.lower()

print(answer)