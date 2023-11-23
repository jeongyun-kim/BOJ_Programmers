def solution(files):
    # 1) head부분을 기준으로 사전 순 정렬(대소문자 구분X)
    # 2) number의 숫자 순으로 정렬
    # 3) head, number 모두 같을 경우 원래 주어진 순서 유지 
    answer = []
    
    for file in files :
        flag = False
        head, number, tail = "", "", ""
        for i in range(0, len(file)) :
            if file[i].isdigit() and len(number) < 5 : # 숫자이고 다섯 글자 사이라면 number에 추가
                number += file[i]
                flag = True # 숫자가 이미 나왔음을 알림
            elif flag == False : # 숫자가 나오기 전 => head
                head += file[i]
            elif flag == True : # 숫자가 나온 후 숫자가 아니라면 그 뒤는 모두 tail => break!
                tail += file[i:]
                break
        answer.append((head, number, tail))
        
    # head -> number 순으로 정렬
    answer = sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))

    return ["".join(s) for s in answer]