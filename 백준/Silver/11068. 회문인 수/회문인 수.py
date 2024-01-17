# 회문인 수 : 왼쪽부터 읽어도 오른쪽부터 읽어도 같은 수
# 어떤 진법(2~64)로 표현했을 때, 회문이 된다면 1출력 아니면 0
import sys
input = sys.stdin.readline

n = int(input())

def calc(num, b) :
    arr = []
    n = num
    while(n > 0) :
        n, r = divmod(n, j)
        if r >= 10 :
            arr.append(chr(r + 65 - 10))
        else :
            arr.append(str(r))
    for k in range(len(arr)//2+1) :
        if arr[k] != arr[-1-k] :
            return 0
    return 1

for i in range(n) :
    num = int(input())
    answer = 0
    for j in range(2, 65) :
        if calc(num, j) == 1 :
            answer = 1
            break
    print(answer)