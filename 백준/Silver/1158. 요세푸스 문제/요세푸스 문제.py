# 1번부터 n번까지 n명의 사람이 원을 이루면서 앉고
# 순서대로 k번째 사람을 제거
# 남은 사람들로 이루어진 원을 따라 n명의 사람이 제거될 때 까지
# 인덱스 = (인덱스+k-1)%len(arr)
n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
j = 0 
answer = []

for _ in range(n) :
    j = (j + k - 1) % len(arr)
    answer.append(str(arr[j]))
    arr.pop(j)

# 정답 출력 
print("<", end="")
print(', '.join(answer), end="")
print(">")