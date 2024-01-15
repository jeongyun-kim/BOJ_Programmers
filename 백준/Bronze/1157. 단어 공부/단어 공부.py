from collections import Counter
# 대소문자 구분하지 않고 해당 단어에서 가장 많이 사용된 알파벳이 무엇인지
# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우 ? 출력
# most_common() : 빈도수가 많은 것부터 출력
cnt = Counter(input().upper()).most_common()

# 만약 단어에 알파벳이 두 개 이상있고 빈도순으로 했을 때 같은게 있는 경우
if len(cnt) >= 2 and cnt[0][1] == cnt[1][1] :
    answer = "?"
else :
    answer = cnt[0][0]

print(answer)
