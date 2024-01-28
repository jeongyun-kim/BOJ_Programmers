# 오늘 하루동안 팔린 책의 제목이 입력으로 들어올 때
# 가장 많이 팔린 책의 제목 출력
# 가장 많이 팔린 책이 여러 개일 경우 사전순 정렬해서 맨 앞의 책
n = int(input())
sells = {}
answer = []

for i in range(n) :
    title = input()
    if title not in sells :
        sells[title] = 1
    else :
        sells[title] += 1

# 가장 많이 팔린 책의 횟수 
bestSelling = max(sells.values())

for k, v in sells.items() : # 많이 팔린 책이 여러 권이라면 
    if v == bestSelling : # 가장 많이 팔린 책의 횟수와 같을 때 answer에 append
        answer.append(k)

# answer 정렬 
answer = sorted(answer)

# 사전순으로 정렬한 answer의 맨 앞 책제목 출력 
print(answer[0])

