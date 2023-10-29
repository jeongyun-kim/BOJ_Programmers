def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    
    for i in range(0, len(phone_book)-1) :
        s = phone_book[i]
        s2 = phone_book[i+1]
        if s == s2[:len(s)] :
            answer = False
            break

    return answer