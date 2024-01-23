# S1 : 2~20, S2 : 2~20, S3 : 2~40
# 세 주사위를 동시에 던져 가장 높은 빈도로 나오는 세 주사위의 합을 구하기 
arr = [0]*81 # 최대 합이 80이기 때문에 배열 길이는 81
s1, s2, s3 = map(int, input().split())

for i in range(1, s1+1) :
    for j in range(1, s2+1) :
        for k in range(1, s3+1) :
            arr[i+j+k] += 1

# 정답이 여러개라면 가장 합이 작은 것
# index의 경우 일치하는 항목 중 가장 앞의 것을 가져오기 때문에 조건에 부합
print(arr.index(max(arr)))
