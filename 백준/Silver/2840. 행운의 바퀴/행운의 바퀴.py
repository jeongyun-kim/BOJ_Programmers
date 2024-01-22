# 바퀴를 k번 돌림 -> 화살표가 가리키는 글자가 변하는 횟수, 어떤 글자에서 멈췄는지 적음 
# 해당 내용을 통해 바퀴에 적은 알파벳 알아내기 
# n : 바퀴의 칸 수, k : 바퀴를 돌리는 횟수
# s : 화살표가 가리키는 글자가 몇 번 바뀌었는지, 회전을 멈추었을 때 가리키던 글자 
# 어떤 글자인지 결정못하는 칸은 ?, 해당하는 바퀴가 없다면 ! 
# 바퀴에 같은 글자 X
n, k = map(int, input().split())
wheels = ['?' for _ in range(n)]
rotate = 0
answer = ""

for i in range(k) :
    num, alpha = input().split()
    rotate = (rotate + int(num)) % n 
    if wheels[rotate] != '?' and wheels[rotate] != alpha :
        answer = "!"
        break
    elif wheels[rotate] == '?' and alpha in wheels :
        answer = "!"
        break 
    else :
        wheels[rotate] = alpha

if answer != "!" :
    answer = ''.join(wheels[rotate::-1]+wheels[-1:-(n-rotate):-1])

print(answer)