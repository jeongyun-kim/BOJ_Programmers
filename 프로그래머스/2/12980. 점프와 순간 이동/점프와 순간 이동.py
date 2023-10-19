def solution(n):
    # 한 번에 K칸 앞으로 전진 or 현재까지 온 거리x2 위치로 순간이동 가능
    # 앞으로 K칸 점프 시 K만큼의 건전지 사용 -> 순간이동이 더 효율적
    # 이동하려는 거리 N이 주어지면 사용해야 하는 건전지 사용량의 최솟값
    ans = 1
    
    while(n >= 2) :
        n2 = n % 2
        n = n // 2
        if n2 == 1 :
            ans += 1

    return ans