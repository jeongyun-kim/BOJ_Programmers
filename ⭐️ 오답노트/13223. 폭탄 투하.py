# 백준 13223 소금 폭탄

# 현재 시각 : hh:mm:ss
# 소금 투하의 시간 : hh:mm:ss
# 1분 = 60초, 60분 = 3600초 
now_h, now_m, now_s = map(int, input().split(":"))
bomb_h, bomb_m, bomb_s = map(int, input().split(":"))

# 현재 시간이 10이고 투하 시간이 4라면 두 시간의 차이는 18시간
# 이는 '투하 시간 + 24 - 현재 시간'과 같음
# + 현재 시간이 20시, 다음 투하 시간이 20시라면 24시간의 차이가 발생하므로 + 24 
if now_h >= bomb_h :
    bomb_h += 24

# 현재 시간을 초로
now_t_to_s = now_h * 3600 + now_m * 60 + now_s
# 소금 투하 시간을 초로 
bomb_t_to_s = bomb_h * 3600 + bomb_m * 60 + bomb_s
# 두 시간의 차이를 초로 표현 
diff_s = abs(bomb_t_to_s - now_t_to_s)

# 시간은 3600으로 나눈 몫
h = diff_s // 3600
# 분은 3600으로 나눈 나머지를 60으로 나눈 몫
m = (diff_s % 3600) // 60
# 초는 3600으로 나눈 나머지를 60으로 나눈 나머지
s = (diff_s % 3600) % 60

# 결과 출력 
# 시간, 분, 초가 10 미만일 때에는 앞에 0이 붙도록 :02d 처리 
answer = "{:02d}:{:02d}:{:02d}".format(h, m, s)
print(answer)
