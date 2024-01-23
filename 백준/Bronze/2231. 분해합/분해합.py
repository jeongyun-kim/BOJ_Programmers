# N의 분해합은 N과 N을 이루는 각 자리수의 합 
# 어떤 자연수 M의 분해합이 N일 때, M을 N의 생성자라고 함 
# ex) 245의 분해합은 245+2+4+5 = 256 => 245는 256의 생성자
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자 구하기 
n = int(input())
answer = 0

for i in range(1, n+1) :
    num = str(i) # n까지의 수 
    nums = list(map(int, num)) # 자릿수
    total = i + sum(nums) 
    if total == n :
        answer = i 
        break

print(answer)

