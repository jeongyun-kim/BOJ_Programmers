# A의 길이 <= B의 길이
# A의 길이와 B의 길이가 같아질 때 까지
# 1. A의 앞에 아무 알파벳이나 추가
# 2. A의 뒤에 아무 알파벳이나 추가 
# => A와 B의 길이가 같으면서, A와 B의 차이를 최소로 
A, B = input().split()
min_value = 50

for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            cnt += 1
    min_value = min(min_value, cnt)

print(min_value)