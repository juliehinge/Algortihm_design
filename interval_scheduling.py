

n_intervals= input()


intervals = []
for interval in range(int(n_intervals)):
	line = input().split(' ')
	intervals.append(line)

sorted_intervals = sorted(intervals, key=lambda x: int(x[1]))

A = []

A.append(sorted_intervals[0])

for idx in range(1, len(sorted_intervals)):
	if int(sorted_intervals[idx][0]) >= int(A[-1][1]):
		A.append([sorted_intervals[idx][0], sorted_intervals[idx][1]])


print((A))