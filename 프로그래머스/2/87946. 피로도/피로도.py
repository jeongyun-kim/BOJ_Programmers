from itertools import permutations
def solution(k, dungeons):
    # 최소 필요 피로도 : 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도
    # 소모 피로도 : 던전 탐험 후 소모되는 피로도
    # dungeon:[최소, 소모] => 유저가 탐험할 수 있는 최대 던전 수 return 
    # pertmutation : 서로 다른 n개의 원소에서 r개를 순서를 고려해 중복없이 나열
    answer = 0
    # => [[80, 20], [50, 40], [30, 10]] , [[50, 40], [80, 20], [30, 10]] 등 생성
    for dungeon in permutations(dungeons, len(dungeons)) :
        cnt = 0
        hp = k
        
        for d in dungeon :
            minimum, spend = d
            if minimum <= hp :
                hp -= spend
                cnt += 1
                
        if cnt > answer : 
            answer = cnt
            
    return answer