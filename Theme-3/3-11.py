# Solve 1
import sys
N,X = map(int,sys.stdin.readline().split())
inp = [x for x in map(int,sys.stdin.readline().split())]

for i in range(N):
	if X>inp[i]:
		print(inp[i], end=" ")

# Solve 2
# import sys
# N,X = map(int,sys.stdin.readline().split())
# inp = list(map(int,sys.stdin.readline().split()))

# for i in inp:
# 	if X>i:
# 		print(i, end=" ")