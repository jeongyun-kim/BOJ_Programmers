# 집들의 위치가 주어졌을 때
# 모든 집까지의 거리가 최소가 되도록 안테나 설치할 위치구하기 
# 집의 위치들 중 중간 집에 설치하면 됨
n = int(input())
homes = sorted(list(map(int, input().split())))

print(homes[(n-1)//2])