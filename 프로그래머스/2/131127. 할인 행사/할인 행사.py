from collections import Counter
def solution(want, number, discount):
    # XYZ 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여
    # 할인하는 제품은 하루에 하나씩만 구매 가능
    # 원하는 제품과 수량이 할인하는 날짜와 10일 연속 일치할 경우에 맞춰 회원가입
    # answer : 할인받을 수 있는 회원등록 날짜들 / 없으면 0 return 
    want_dic = {}
    answer = 0

    for i in range(0, len(want)) :
        key, value = want[i], number[i]
        want_dic[key] = value
    want_dic2 = want_dic

    for j in range(0, len(discount)) :
        discounts = Counter(discount[j:j+10])
        if discounts == want_dic :
            answer += 1
        
    return answer