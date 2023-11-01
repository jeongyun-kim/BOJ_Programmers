def solution(n, t, m, p):
    # 숫자를 0부터 시작해서 말함 => 10 이상의 수는 한 자리씩 끊어 말함(모든 진법)
    # 진법 2 / 미리 구할 숫자의 개수 t / 게임 참가인원 m / 튜브의 순서 p
    # 0 - 2(10) => 1 -> 3(11) => 1 -> 4(100) -> 1
    # p가 짝수면 인덱스가 홀수인 수, p가 홀수면 인덱스가 짝수인 수 
    answer = ''
    nums = "0"
 
    for i in range(0, t*m) : # 1부터 2칸씩 16개 
        nums += (calc(i, n))

    for j in range(p-1, len(nums), m) :
        answer += nums[j]
    
    return answer[:t]


def calc(num, n) : #진수 변환 함수
    s = ""
    alpha = ["A", "B", "C", "D", "E", "F"]
    
    while(num > 0) :
        num, mod = divmod(num, n)
        if n > 10 and mod >= 10 and mod <= 15 : 
            # 진수가 11진수 이상이고 나머지가 10에서 15사이라면 알파벳 처리
            s += alpha[mod%10]
        else :
            s += str(mod)
    s = s[::-1]
    return s 