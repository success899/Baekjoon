import sys
input=sys.stdin.readline

N, mood = map(int, input().split())
mood_list = list(map(float, input().split()))
bad, good = 0.0, 0.0

if mood == 0:
    good = 1.0
else:
    bad = 1.0
    
good_good = mood_list[0]
good_bad = mood_list[1]
bad_good = mood_list[2]
bad_bad = mood_list[3]

for i in range(N):
    prev_good = good
    good = good * good_good + bad * bad_good
    bad = prev_good * good_bad + bad * bad_bad

print(int(good * 1000))
print(int(bad * 1000))