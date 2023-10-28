from collections import Counter
def solution(str1, str2):
    # 자카드 유사도 : 두 (다중)집합의 교집합 크기 / 합집합 크기
    # 집합 A와 집합 B가 모두 공집합일 경우에는 J(A, B) = 1
    # 두 글자씩 끊어서 다중집합 원소로, 그 외는 그 쌍 버림
    # 대소문자 구분 X
    # 유사도 값은 0에서 1사이의 실수 => 65536 곱한 후 return 
    answer = 0
    str1 = Counter([str1[i:i+2].lower() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()])
    str2 = Counter([str2[i:i+2].lower() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()])
    intersection, union = 0, 0
    if len(str1) == 0 and len(str2) == 0 :
        answer = 65536
    else :
        for key in str1.keys() :
            if key in str2 : # 겹치는 요소들은 따로 처리하고 0처리
                intersection += min(str1[key], str2[key])
                union += max(str1[key], str2[key])
                str1[key] = 0 
                str2[key] = 0
        # 교집합 이후 남은 문자들 합집합에 카운트
        union = union + sum(str1.values()) + sum(str2.values())
        answer = intersection / union * 65536
        
    return int(answer)