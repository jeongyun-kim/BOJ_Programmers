def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = truck_weights[-1::-1]
    bw = 0 # 다리 위 무게
    bridge = [0] * bridge_length # 다리위에 있는 트럭들의 무게
    
    while(truck_weights) :
        answer += 1
        bw = bw - bridge.pop(0) # 맨 앞의 트럭이 다리를 빠져나가며 무게 = 무게 - 맨 앞 트럭의 무게
        if bw + truck_weights[-1] <= weight : # 만약 (현무게 + 들어올 트럭의 무게)가 한계치보다 적다면
            truck = truck_weights.pop() # 다음 들어올 트럭 준비
        else : # (현 무게 + 들어올 트럭의 무게)가 한계치보다 크다면
            truck = 0 # 다음에 들어올 트럭없음
        bw += truck # 다음 트럭(또는 없음) 더하기
        bridge.append(truck) # 새로 들어온 트럭을 다리위에 최종 배치
        
    return answer + bridge_length