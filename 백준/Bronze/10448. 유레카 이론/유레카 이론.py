# 자연수가 주어졌을 때, 그 정수가 3개의 삼각수의 합으로 표현될 수 있는지 없는지
# 단, 3개의 삼각수가 모두 다를 필요는 없음 
# 삼각수 Tn = n(n+1)/2
import sys
input = sys.stdin.readline

# 테스트케이스의 개수
n = int(input()) 
arr = [] # 삼각수 넣을 배열 
answer = [0] * 1001 # 세 수가 합해서 나오는 수의 인덱스에 1 처리하기 위한 배열 

# n이 33인 경우까지(arr[-1] == 496)
for i in range(1, 1001) :
    tn = i * (i+1) // 2 
    if tn > 1000 :
        break
    else :
        arr.append(tn)

# 삼각수가 다를 필요 없으므로 i, j 포함해서 
for i in range(0, len(arr)) :
    for j in range(i, len(arr)) :
        for k in range(j, len(arr)) :
            num = arr[i]+arr[j]+arr[k] # 세 수를 더한 값 
            if num <= 1000 : # k의 최대가 1000이므로 세 수를 더한 값이 1000을 넘지 않는다면
                answer[num] = 1 # 해당 값의 인덱스에 1 표시, 삼각수로 만들어지지 않는 수는 0으로 유지
            else :
                break

# 테스트케이스 불러오면서 해당 인덱스 값 가져오기 
# 삼각수로 만들어졌으면 1, 아니면 0
for i in range(n) :
    print(answer[int(input())])


    