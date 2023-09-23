def solution(numbers, hand):
    answer = ''
    # 키패드 위치를 좌표로
    keypad = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 0:(3,1), '#':(3,2)}
    left = keypad['*'] # 왼손 엄지 시작점
    right = keypad['#'] # 오른손 엄지 시작점
    ld, rd = 0, 0 # 왼손 거리, 오른손 거리
    
    for num in numbers :
        p = keypad[num] # 입력할 숫자의 위치 = position
        if num in [1, 4, 7] : # 왼쪽 열 숫자 3개 입력 시
            answer += 'L'
            left = p
        elif num in [3, 6, 9] : # 오른쪽 열 숫자 3개 입력 시
            answer += 'R'
            right = p
        else : # 가운데 열 숫자 4개 입력 시 왼손/오른손 거리 비교(ld>rd / ld<rd / ld==rd)
            ld = abs(left[0]-p[0])+abs(left[1]-p[1])
            rd = abs(right[0]-p[0])+abs(right[1]-p[1])
            if ld > rd :
                answer += 'R'
                right = p
            elif ld < rd :
                answer += 'L'
                left = p
            elif ld == rd :
                if hand == 'right' :
                    answer += 'R'
                    right = p
                else :
                    answer += 'L'
                    left = p
            
    return answer