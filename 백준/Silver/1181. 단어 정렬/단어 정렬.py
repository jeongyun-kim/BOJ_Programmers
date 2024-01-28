# 중복제거 
# 1. 길이가 짧은 순
# 2. 길이가 같으면 사전 순 
n = int(input())
answer = set()

for i in range(n) :
    answer.add(input())

# 길이 짧은 순 + 길이가 같으면 사전순
answer = sorted(answer, key=lambda x:(len(x), x))

for j in range(len(answer)) :
    print(answer[j])