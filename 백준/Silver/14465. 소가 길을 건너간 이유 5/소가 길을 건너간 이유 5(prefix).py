# prefix
n, k, b = map(int, input().split())
answer = n 

states = [0] * (n+1)
for i in range(b) :
    states[int(input())] = 1

prefix_states = states
for j in range(1, n+1) :
    prefix_states[j] += prefix_states[j-1]

for h in range(k, n+1) :
    answer = min(answer, prefix_states[h]-prefix_states[h-k])

print(answer)
