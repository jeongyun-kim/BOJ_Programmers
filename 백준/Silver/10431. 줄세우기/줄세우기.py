# 아무나 한 명을 뽑아 줄의 맨 앞에 세움
# 그 다음부터는 자기 앞에 자기보다 키 큰 학생이 없다면 그 자리에 선다
# 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그 중 가장 앞에 있는 학생의 앞에 선다
# 그럼 그 학생은 뒤로 물러난다
# 학생들이 뒤로 물러난 횟수는?

# n : 테스트케이스 수
# 테스트케이스~
n = int(input())

for i in range(n) :
    line = list(map(int,input().split()))[1:]
    cnt = 0 
    for j in range(0, len(line)-1) :
        for k in range(j, len(line)) :
            if line[j] > line[k] : # 앞에 친구가 지금 친구보다 키가 크면 자리 바꾸기 
                line[j], line[k] = line[k], line[j]
                cnt += 1
    print(i+1, cnt)
        
