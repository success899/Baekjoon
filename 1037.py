from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int,input().split()))

print(max(N_list)*min(N_list))