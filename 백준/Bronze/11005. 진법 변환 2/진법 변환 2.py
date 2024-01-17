# 10진법 수 N이 주어지면 이 수를 B진법으로 바꾸어 출력하기
# 10진법 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있음 => 10:A ~ 35:Z
import sys
input = sys.stdin.readline
alphas = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
answer = ""
n, b = map(int, input().split())

while n > 0 :
    n, r = divmod(n, b) 
    if r >= 10 : # 나머지가 10 이상이라면 
        answer += alphas[r]
    else :
        answer += str(r)

print(answer[-1::-1]) # 반대로 출력해주어야 맞음 
