n, m = map(int, input().split())
arr = [input() for _ in range(n)]

def calc(i, j, pattern) :
    cnt = 0
    for k in range(i, i+8) :
        for h in range(j, j+8) :
            if arr[k][h] != pattern[(k+h) % 2] :
                cnt += 1
    return cnt 

answer = n * m 

for i in range(n-8 + 1) :
    for j in range(m-8 + 1) :
        bw, wb = 0, 0
        bw = calc(i, j, "BW")
        wb = calc(i, j, "WB")
        answer = min(answer, min(bw, wb))

print(answer)
                