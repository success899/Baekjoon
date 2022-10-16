from collections import deque

n = int(input())
card_list = deque([])


for i in range(n):
    card_list.append(i+1)

while True:
    
    if len(card_list) == 1:
        break

    else:
        card_list.popleft()
        card_list.rotate(-1)

print(card_list[0])