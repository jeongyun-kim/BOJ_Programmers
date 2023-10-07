def solution(board, moves):
    answer = 0
    stack = []
    # 0 0 0 0 0 : board - 0 
    # 0 0 1 0 3 : board - 1
    # 0 2 5 0 1 : board - 2
    # 4 2 4 4 2 : board - 3
    # 3 5 1 3 1 : board - 4
    
    for move in moves :
        for i in range(len(board)) :
            if board[i][move-1] != 0 :
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                if len(stack) >= 2 and stack[-1] == stack[-2] :
                    answer += 2
                    stack.pop()
                    stack.pop()
                break
        
    return answer