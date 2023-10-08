def solution(new_id):
    answer = ''
    
    # 1 . 대문자 -> 소문자
    new_id = new_id.lower()
    # 2 . 소문자 / 숫자 / - / _ / . 제외 모든 문자 제거 => 제거한 문자열이 new_id2
    new_id2 = ''
    for c in new_id :
        if c.isalpha() == True or c.isdigit() == True or c in ['-', '_', '.'] :
            new_id2 += c
    # 3 . 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표로 치환(while 사용)
    while '..' in new_id2 :
        new_id2 = new_id2.replace('..','.')
    # 4 . 마침표가 처음이나 끝에 위치한다면 제거(문자열 길이가 2이상인지 확인하기!)
    if len(new_id2) > 1 :
        if new_id2[0] == '.' :
            new_id2 = new_id2[1:]
        if new_id2[-1] == '.' :
            new_id2 = new_id2[:-1]
    else : # 문자열 길이가 1인데 . 하나면 빈 문자열로 바꾸기
        if new_id2[0] == '.' :
            new_id2 = ''
    # 5 . 빈 문자열이라면 a를 대입
    if new_id2 == '' :
        new_id2 = 'a'
    # 6 . 16자 이상이면 첫 15개 문자 제외 나머지 문자 제거, 끝의 . 제거
    if len(new_id2) >= 16 :
        new_id2 = new_id2[:15]
        while(new_id2[-1]=='.') :
            new_id2 = new_id2[:-1]
    # 7 . 2자 이하라면 마지막 문자를 new_id의 길이가 3이 될 때 까지 반복해서 붙임
    if len(new_id2) <= 2 :
        for i in range(0, 3-len(new_id2)) :
            new_id2 += new_id2[-1]

    return new_id2