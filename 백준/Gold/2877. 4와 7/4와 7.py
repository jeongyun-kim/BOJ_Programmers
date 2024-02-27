# 창영이는 4와 7로 이루어진 수를 좋아함
# 창영이가 좋아하는 수 중 K번째 작은 수 구하기
# k+1을 이진수로 변환한 후 맨앞의 수를 뗀 상태에서 0을 4로, 1을 7로 바꿔주면 k번째 수
k = int(input())
answer = format(k+1, 'b')[1:].replace('0', '4').replace('1', '7')
print(answer)