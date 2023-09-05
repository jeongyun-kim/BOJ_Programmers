def solution(lottos, win_nums):
    ranks = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    cnt = 0
    cnt_zero = lottos.count(0)
    
    for l in lottos :
        if l in win_nums :
            cnt += 1
    
    max_rank = cnt + cnt_zero
    min_rank = cnt

    return [ranks[max_rank], ranks[min_rank]]