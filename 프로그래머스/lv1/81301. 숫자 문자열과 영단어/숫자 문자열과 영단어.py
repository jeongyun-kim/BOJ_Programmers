def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx,c in enumerate(arr):
        s = s.replace(c,str(idx))
        
    return int(s)