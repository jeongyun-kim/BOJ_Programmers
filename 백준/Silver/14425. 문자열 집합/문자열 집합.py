# 첫째줄 : N, M - 문자열의 개수 
# 다음 N개의 줄에 집합S에 포함되어 있는 문자열들이 주어짐
# 다음 M개의 줄에 검사해야 하는 문자여들이 주어짐 
n, m = map(int, input().split())
s = set()
answer = 0 

for i in range(n) :
    s.add(input().rstrip())

for j in range(m) :
    string = input().rstrip()
    if string in s :
        answer += 1

print(answer)