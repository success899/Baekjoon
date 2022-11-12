room_number = int(input())
start_room = 1
room = 1
index = 6
tmp = 1
if room_number == start_room:
    print(start_room)
else:    
    while True:
        tmp = tmp + index
        room+=1
        if room_number <= tmp:
            print(room)
            break
        index += 6