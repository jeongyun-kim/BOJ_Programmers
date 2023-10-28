def solution(n, k):
    # n -> k진수 내 소수에서
    # 소수 양 옆에 0이 있는 경우 / 소수 오른쪽에만 0 / 소수 왼쪽에만 0 / 소수 양쪽에 X
    nToK = ntok(n, k).split('0') # 진수변환한 문장을 0을 기준으로 자르기 
    answer = 0
    
    for i in range(0, len(nToK)) :
        val = nToK[i]
        if val == '' : 
            continue
        else :
            if int(val) in [2, 3, 5, 7] :
                answer += 1
            else :
                flag2 = calc(val)
                if flag2 == True :
                    answer +=1
    
    return answer

def ntok(n, k) :
    s = ""
    while(n > 0) :
        n, mod = divmod(n, k)
        s += str(mod)
    s = s[::-1]
    return s 

def calc(num) : # 소수라면 true return 
    num = int(num)
    flag = False
    for i in range(2, int(num**0.5)+1) :
        n2 = num % i
        if n2 == 0 :
            flag = False
            break
        else :
            flag = True
    return flag
            