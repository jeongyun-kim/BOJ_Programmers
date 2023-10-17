def solution(s):
    # map : 리스트의 요소를 지정된 함수로 처리해주는 함수 => 새 리스트 생성
    # ex) list(map(함수, 리스트)) / tuple(map(함수, 튜플))
    s = list(map(int,s.split(' ')))
    
    return '{0} {1}'.format(min(s), max(s))