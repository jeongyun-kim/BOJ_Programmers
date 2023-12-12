from itertools import permutations
def solution(numbers):
    answer = 0
    combis = set()
    
    for i in range(1, len(numbers)+1) :
        c = list(permutations(numbers,i))  # 순서를 고려하여 뽑기 => AB != BA
        for j in range(0, len(c)) : # 순열 리스트 돌면서
            num = int(''.join(c[j])) # 각 데이터를 숫자로 변환
            if num != 0 and num != 1 : # 0과 1을 제외하고 추가
                combis.add(num)
    
    for combi in combis : # 중복된 숫자가 없는 set돌며
        cnt = 0
        for k in range(2, int(combi**0.5)+1) : # 소수인지 아닌지 판단
            if cnt > 0 : break # cnt가 0보다 크면 소수X
            else :
                if combi % k == 0 : cnt += 1
        if cnt == 0 : # cnt가 0이면 소수이므로 answer += 1
            answer += 1
            
    return answer