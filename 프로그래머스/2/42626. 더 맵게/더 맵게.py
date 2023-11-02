import heapq as hp
def solution(scoville, K):
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    # 모든 음식의 스코빌지수가 K이상이 될 때까지 반복 => 최소 횟수 return
    # 힙에서 최소값 읽어오기 h[0] / 빼내기 hp.heappop()
    answer = 0
    scoville.sort()
    hp.heapify(scoville) # scoville을 heap으로 변경
    length = len(scoville)
    
    
    if scoville[0] > K :
        answer = -1
    else :
        while(scoville[0] < K) :
            if len(scoville) == 1: # 모든 음식을 섞어서 하나 남았는데 이게 K보다 작을 때 
                answer = -1
                break
            else :
                n1 = scoville[0] # 가장 맵지 않은 음식의 스코빌 지수
                hp.heappop(scoville)
                n2 = scoville[0] # 두 번째로 맵지 않은 음식의 스코빌 지수
                k = n1 + (n2 * 2)
                hp.heappushpop(scoville, k)
            answer += 1

    return answer