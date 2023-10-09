def solution(ingredient):
    answer = 0
    # 빵 - 야채 - 고기 - 빵 
    ingredients = []
    
    for i in ingredient :
        ingredients.append(i) # 재료를 하나씩 쌓음
        # 쌓인 재료가 4개 이상에 연달아 1, 2, 3, 1 이면
        #  answer+1하고 쌓인 재료에서 1, 2, 3, 1 재료 제거 
        if len(ingredients) >= 4 and ingredients[-4:] == [1, 2, 3, 1] :
            answer += 1
            for j in range(0, 4) :
                ingredients.pop()
                
    return answer