# + : 현재 보고있는 채널 +1된 채널로 이동
# - : 현재 보고있는 채널 -1된 채널로 이동(채널 0에서는 - X)
# n : 이동하려고 하는 채널
# 현재 보고있는 채널은 100번 => n번으로 가기 위한 버튼을 누르는 최소 횟수
# 버튼은 고장난 버튼 제외 0부터 9까지 있음
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
# 고장난 버튼이 있다면 
if m > 0 :
    broken = list(map(int, input().split()))
else : # 없다면
    broken = []
btns = [i for i in range(10) if i not in broken] # 고장나지 않은 버튼의 모음
answer = abs(n-100) # 현재 채널 100번에서 n으로 이동할 때 +, -로만 이동할 수 있는 횟수 

for channel in range(999900) : # 최대이동횟수 : 999999 - 100회 
    flag = 0 # 고장난 버튼이 포함된 채널인지 
    s = str(channel)
    for c in s :
        if int(c) not in btns :
            flag = 1
            break
    if flag == 0 : # 리모콘으로 이동할 수 있는 채널이면 
        # [해당 채널과 이동하고자 하는 채널의 차이 + 해당 채널 누르는 횟수] 와 [원래의 answer] 비교해서 더 작은 값 대입하기 
        answer = min(answer, abs(channel-n)+len(str(channel)))
    
print(answer)