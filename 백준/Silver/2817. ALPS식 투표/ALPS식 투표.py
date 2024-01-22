# 수고비를 받을 가치가 있는 스태프 한 명 투표(안 할 수도 있음)
# 1. 전체 대회 참가자의 5% 미만은 제외
# 2. 득표수를 1로 나눈 값, 2로 나눈 값, ... 14로 나눈 값 => 점수집합
# 3. 전체 집합에서 점수가 큰 1~14번째 스태프에게 칩 1개씩 배분 
# x : 참가자수, n : 참여한 스태프 수, ~ : 스태프의 이름 - 득표수 
# 스태프의 이름 사전순 출력 
participants = int(input())
n = int(input())
percent = participants * 0.05
scores = {}
staff = {}

for i in range(n) :
    name, votes = input().split()
    votes = int(votes)
    if votes >= percent :
        staff[name] = 0 # 칩을 나눠받을 스태프 목록 
        for j in range(1, 15) : # 점수와 이름을 함께 입력 
            scores[votes/j] = name

# 점수들을 내림차순으로 
scores = sorted(scores.items(), reverse=True)

# 칩 배분
for i in range(14) :
    name = scores[i][1]
    staff[name] += 1

# 스태프명 정렬
staff = sorted(staff.items())

# 결과 출력 
for j in range(len(staff)) :
    print(staff[j][0], staff[j][1])
