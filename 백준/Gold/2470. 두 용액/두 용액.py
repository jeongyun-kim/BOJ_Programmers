# N : 전체 용액의 수
# ~ : 용액의 특성 값 N개
# 두 용액의 특성값을 더했을 때 0에 가깝도록 하는 두 용액의 특성값 출력
n = int(input())
vs = list(map(int, input().split()))
vs = sorted(vs)

left = 0 
right = n-1
minValue = 2e+9+1

while left < right :
    diffValue = vs[left]+vs[right] # 두 용액의 특성합

    if abs(diffValue) < minValue :
        minValue = abs(diffValue) # 절댓값 씌웠을 때, 더 작은 값이 나온다면 대입 
        answer = [vs[left], vs[right]] # answer에 두 용액 넣기 

    if diffValue < 0 : # 특성합이 0보다 작다면 우측으로
        left += 1
    elif diffValue > 0 : # 특성값이 0보다 크다면 좌측으로
        right -= 1
    else :
        break

# 정답 출력
print(answer[0], answer[1])
    