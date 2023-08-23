def solution(price, money, count):
    cnt = 0
    
    for i in range(1, count+1): # 탈 때마다 N배
        cnt += (price*i)
    
    if cnt-money > 0 :
        return cnt-money
    else :
        return 0
    
