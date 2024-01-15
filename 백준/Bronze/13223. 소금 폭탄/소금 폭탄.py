# 첫째줄 : 현재 시각 = hh:mm:ss
# 둘째줄 : 소금 투하 시간 = hh:mm:ss
# 소금을 투하하기까지 필요한 시간 (초 단위로 계산하기)
h1, m1, s1 = map(int,input().split(":"))
h2, m2, s2 = map(int,input().split(":"))

if h2 <= h1 :
    h2 += 24

time1 = h1*3600 + m1*60 + s1
time2 = h2*3600 + m2*60 + s2
diff_time = time2 - time1

h = diff_time // 3600
m = (diff_time % 3600) // 60
s = diff_time % 60 

print("{:02d}:{:02d}:{:02d}".format(h, m, s))