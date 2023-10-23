from collections import deque
def solution(cacheSize, cities):
    # LRU 사용 -> hit : 1 / miss : 5
    # => deque 이용하기
    answer = 0
    cache = deque()
    
    for city in cities :
        city = city.lower()
        # cacheSize가 0이면 아무것도 넣지 않음
        if cacheSize == 0 : 
            answer = len(cities) * 5
            break
        # cache에 이미 값이 있으면 뺐다 넣고 + 1
        elif city in cache : 
            cache.remove(city)
            cache.append(city)
            answer += 1
        elif len(cache) >= cacheSize  : # 사이즈를 초과하고 값이 안 들어있다면
            answer += 5
            cache.popleft()
            cache.append(city)
        else : # 사이즈 초과하지 않고 값이 안 들어있다면 
            answer += 5
            cache.append(city)

    return answer
