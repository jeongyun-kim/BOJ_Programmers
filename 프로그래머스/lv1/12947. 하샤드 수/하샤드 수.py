def solution(x):
    total = 0
    
    for c in str(x) :
        total += int(c)

    if x % total == 0 :
        return True
    else :
        return False
    