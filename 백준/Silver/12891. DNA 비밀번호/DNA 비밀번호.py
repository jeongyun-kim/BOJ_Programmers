# 임의의 DNA문자열에서 부분문자열의
# 1. 주어진 길이를 충족하면서 
# 2. 포함되어야 할 문자의 최소 개수 조건을 충족
# 길이가 p인 부분문자열의 개수 = s - p + 1
# 세어져있는 알파벳에서 왼쪽빼고 오른쪽만 더해주면 됨
s, p = map(int, input().split())
dnaString = input()
min_dna = list(map(int, input().split()))
dnas = {'A':0, 'C':1, 'G':2, 'T':3} # 각 dna의 인덱스값 
cnt_dnas = [0] * 4 # 각 dna 카운트 

# 주어진 길이만큼의 문자열 내 카운트  
for dna in dnaString[:p] :
    cnt_dnas[dnas[dna]] += 1

# 문자열 내 dna가 최소 개수 이상인지 체크 
# 하나라도 충족하지않으면 0 반환 
def check() :
    for i in range(4) :
        if cnt_dnas[i] < min_dna[i] :
            return 0
    return 1

# 첫 슬라이드 체크 
answer = check() 

# 다음 슬라이드부터 왼쪽은 빼고 오른쪽 값은 더해서 체크
for i in range(1, s-p+1) :
    cnt_dnas[dnas[dnaString[i-1]]] -= 1 # 왼쪽 dna의 cnt 빼기 
    cnt_dnas[dnas[dnaString[i+p-1]]] += 1 # 오른쪽 dna의 cnt 더하기 
    answer += check() # 바뀐 dna 개수로 확인 

# 결과 출력 
print(answer)