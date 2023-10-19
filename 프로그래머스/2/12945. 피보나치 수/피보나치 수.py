def solution(n):
    # 피보나치 수 : F(n) = F(n-1) + F(n-2)
    F = [0, 1]
    
    for i in range(2, n+1) :
        F.append(F[i-1] + F[i-2])
            
    return F[-1] % 1234567