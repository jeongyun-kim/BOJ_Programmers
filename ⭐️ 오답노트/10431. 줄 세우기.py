# 백준 10431 줄 세우기

# 아무나 한 명 뽑아 줄의 맨 앞에 세움
# 그 다으부터 학생이 한 명씩 줄의 맨 뒤에 서면서 다음 과정을 거침
# 1. 자기 앞에 자기보다 키 큰 사람이 없으면 거기에 섬
# 2. 자기 앞에 자기보다 키 큰 학생이 한 명이상이라면 그 중 가장 앞에 있는 학생의 바로 앞에 선다 -> 학생들 한 칸씩 물러남
# 학생들이 물러난 횟수
import sys
input = sys.stdin.readline

# 테스트케이스 개수
p = int(input())
answer = []  # 1 - 2 - 5 - 4 => height : 5, idx : 2
# idx=1에 4가 들어감 => 0:1, 1:2, 2:5, 3:4 이 상태에서 4가 들어오면 한 걸음 물러나야 함 

for i in range(p) :
    cnt = 0
    line = list(map(int, input().split()))[1:]
    for i in range(0, len(line)-1) :
        for j in range(i+1, len(line)) :
            if line[i] > line[j] :
                line[i], line[j] = line[j], line[i]
                cnt += 1
    answer.append(cnt)

for i in range(len(answer)) :
    print(i+1, answer[i])
