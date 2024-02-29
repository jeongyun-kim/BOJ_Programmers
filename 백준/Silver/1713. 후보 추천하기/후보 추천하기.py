# 1. 학생들이 추천을 시작하 전 사진틀은 비어있음
# 2. 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 사진틀에 게시
# 3. 비어있는 사진틀이 없는 경우 추천 횟수가 가장 적은 학생의 사진 -> 새로운 학생의 사진
# 3-1. 추천받은 횟수가 가장 적은 학생이 두 명 이상일 경우 게시된 지 가장 오래된 사진 삭제(인덱스비교, 작으면 오래된 것)
# 4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우 추천받은 횟수만 증가
# 5. 사진틀에 게시된 사진이 삭제되는 경우 해당 학생이 추천받은 횟수는 0으로 바뀜
# 최종 후보가 누구인지 결정하기
n = int(input())
votes_cnt = int(input())
votes_dic = {}
votes = list(map(int, input().split()))

for vote in votes :
    if len(votes_dic) == n :
        if vote not in votes_dic.keys() :
            minimum = min(votes_dic.values())
            for k, v in votes_dic.items() :
                if v == minimum :
                    break
            votes_dic.pop(k, None)
            votes_dic[vote] = 1
        else :
            votes_dic[vote] += 1
    else :
        if vote not in votes_dic.keys() :
            votes_dic[vote] = 1
        else :
            votes_dic[vote] += 1

keys = sorted(list(votes_dic.keys()))
for key in keys :
    print(key, end=" ")
