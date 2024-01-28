# A가 B의 앞에 오는 경우
# 1. A와 B의 길이가 다르면 짧은 것 우선
# 2. 길이가 같다면 A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합이 먼저(숫자만 더함)
# 3. 1, 2번으로도 안된다면 사전순
n = int(input())
alphas = [input() for _ in range(n)]

# 자리수 합
def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

alphas = sorted(alphas, key=lambda x:(len(x), sum_num(x), x))

for a in alphas :
    print(a)

