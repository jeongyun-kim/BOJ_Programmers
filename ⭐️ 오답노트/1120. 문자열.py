# A의 길이 <= B의 길이
# A의 길이와 B의 길이가 같아질 때 까지
# 1. A의 앞에 아무 알파벳이나 추가
# 2. A의 뒤에 아무 알파벳이나 추가 
# => A와 B의 길이가 같으면서, A와 B의 차이를 최소로 
A, B = input().split()
min_value = 50

# a의 시작점을 변경해 b를 탐색할 수 있는 기회
for i in range(len(B) - len(A) + 1):
    cnt = 0
		# a 길이만큼 전체
    for j in range(len(A)):
				# b의 시작점을 변경해가며 a 전체 문장 탐색 
        if A[j] != B[i + j]:
            cnt += 1
		# 가장 차이가 적은 경우 선택 
    min_value = min(min_value, cnt)

print(min_value)
