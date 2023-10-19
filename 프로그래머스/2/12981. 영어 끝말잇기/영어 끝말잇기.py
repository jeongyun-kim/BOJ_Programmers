def solution(n, words):
    answer = []
    # 1번부터 번호 순으로 한 사람씩 단어를 말함
    # 마지막 사람이 말한 다음 다시 1번부터 ~
    # !앞 사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 하며
    #  이전에 등장한 단어는 사용할 수 없음
    # ! 한 글자인 단어도 불가
    w = []
    cnt_dic = {i+1:0 for i in range(n)}
    
    for idx, word in enumerate(words) :
        person = idx % n + 1
        cnt_dic[person] += 1
        if (word in w) or len(w)>=1 and (w[-1][-1] != word[0]) :
            answer = [person, cnt_dic[person]]
            break
        else :
            w.append(word)
    
    if len(answer) == 0 :
        answer = [0, 0]
            
    return answer