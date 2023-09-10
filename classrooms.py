

n_intervals, n_classrooms= input().split(' ')


intervals = []
for interval in range(int(n_intervals)):
	line = input().split(' ')
	int_line = [int(x) for x in line]
	intervals.append(int_line)


sorted_intervals = sorted(intervals, key=lambda x: int(x[1]))



class_rooms = {idx: [] for idx in range(int(n_classrooms))}
already_chosen = []

for interval in sorted_intervals:
	for key, value in class_rooms.items():
		if not value or interval[0] >= int(value[-1][1]):
			if interval not in already_chosen:
		 		value.append(interval)
		 		already_chosen.append(interval)
		 		


count = 0
for k,v in class_rooms.items():
	count += len(v)

print(class_rooms)
print(count)