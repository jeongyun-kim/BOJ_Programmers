# 백준 1233 주사위

# 주사위 S1, S2(2이상 20이하) / S3(2이상 40이하)의 주사위들을 동시에 던져
# 가장 높은 빈도로 나오는 세 주사위의 합 구하기 
# S1, S2, S3이 입력으로 주어짐
s1, s2, s3 = map(int, input().split())
nums = [0] * (s1+s2+s3+1) # 세 주사위의 면을 합쳐서 나오는 수의 횟수 

# 세 주사위 면의 수 합쳐서 세기 
for i in range(1, s1+1) : 
    for j in range(1, s2+1) :
        for k in range(1, s3+1) :
            nums[i+j+k] += 1

# 가장 많이 나오는 수 출력하기 
max_num = max(nums)
print(nums.index(max_num))
