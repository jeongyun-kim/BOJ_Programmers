# 아스키코드로 정리하기
# a : 97
arr = [0 for _ in range(26)]

# 첫번째 단어에 있는 알파벳
for c in input() :
    idx = ord(c) - 97
    arr[idx] += 1

# 두 단어에서 겹치는 건 빠지고 없는건 -로 내려감
for c in input() :
    idx = ord(c) - 97
    arr[idx] -= 1

# 절댓값으로 변환(- 없애기)해서 sum 구하기 
print(sum(map(abs, arr)))