from itertools import product
# 중복X 순열 : permutation / 중복O 순열 : product
def solution(word):
    answer = 0
    w = ["A", "E", "I", "O", "U"]
    words = []
    
    # 모든 경우의 수 들어있는 사전 생성
    for j in range(1,6):
        for i in product(w,repeat=j):
            s = ''.join(i)
            words.append(s) 
    # 알파벳순 정렬
    words = sorted(words)
                
    return words.index(word)+1