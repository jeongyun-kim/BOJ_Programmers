def solution(s):
    arrP = ['p','P']
    arrY =  ['y','Y']
    cntP, cntY = 0, 0
    
    for c in s :
        if c in arrP :
            cntP += 1
        elif c in arrY :
            cntY += 1
    
    if cntP == cntY :
        return True
    else :
        return False