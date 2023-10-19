from collections import deque
def solution(people, limit):
    # 구명보트는 한 번에 최대 2명, 무게제한O
    # 구출하기 위해 사용할 구명보트 개수의 최솟값 return
    # 가장 가벼운 사람 + 가장 무거운 사람이 limit보다 큰 지 비교하기
    # => dequeue 이용 맨왼쪽/맨오른쪽에서 값 빼내오기 
    answer = 0
    people = deque(sorted(people)) # 오름차순으로 정렬한 dequeue
    
    while(len(people)>1) :
        weight = people[0] + people[-1]
        if weight <= limit : # 두 명의 무게가 limit에 걸리지 않으면 두 명 빼내기
            people.pop()
            people.popleft()
            answer += 1
        else : # 두 명의 무게가 limit보다 크면 몸무게가 큰 쪽만 빼내기
            people.pop()
            answer += 1
            
    if len(people) == 1 : # 마지막 한 명 남아있다면
        answer += 1
        
    return answer