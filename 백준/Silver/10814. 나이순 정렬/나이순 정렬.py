# 회원의 나이, 이름 (입력은 가입한 순)
# 나이순 정렬 > 나이가 같으면 가입순 
n = int(input())
answer = []

for i in range(n) :
    age, name = input().split()
    age = int(age)
    answer.append((i, age, name)) # i : 가입 순서 

# 나이순 정렬 + 나이가 같으면 가입순
answer = sorted(answer, key=lambda x:(x[1], x[0]))

# 결과 출력
for j in range(n) :
    print(answer[j][1], answer[j][2])