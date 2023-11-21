from collections import Counter
def solution(toppings):
    answer = 0
    bro2 = set() # 동생
    bro1 = Counter(toppings) # 형
    
    for t in toppings :
        bro2.add(t) # 동생한테 토핑 나누어주기 
        bro1[t] -= 1 # 동생한테 준 토핑빼기
        if bro1[t] == 0 : # 이제 형한테 해당 토핑이 없다면 딕셔너리에서 제거 
            del bro1[t]
        if len(bro1) == len(bro2) : # 둘이 가진 토핑의 가짓수가 같다면 +1
            answer += 1
            
    return answer