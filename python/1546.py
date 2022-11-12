n = int(input())
test_score_list = input().split()
test_score_list = list(map(int, test_score_list))
test_score_list.sort()
fake_score_sum = 0
fake_score_avg = 0

for i in range(0,n):
    fake_score_sum = fake_score_sum + test_score_list[i]/test_score_list[-1]*100
fake_score_avg = fake_score_sum / n

print(fake_score_avg)