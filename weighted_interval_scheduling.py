n_intervals = input()

intervals = []
weights = []

for interval in range(int(n_intervals)):
    line = list(map(int, input().split(' ')))
    intervals.append(line[:2])
    weights.append(line[2])

# Sorting intervals and weights together based on interval end times
sorted_data = sorted(zip(intervals, weights), key=lambda x: x[0][1])
sorted_intervals = [item[0] for item in sorted_data]
sorted_weights = [item[1] for item in sorted_data]

def find_latest_non_conflicting(interval_list, x):
    low, high = 0, x - 1
    result = -1  
    
    while low <= high:
        mid = (low + high) // 2
        if interval_list[mid][1] <= interval_list[x][0]:
            result = mid
            low = mid + 1  
        else:
            high = mid - 1  
            
    return result

updated_weights = [0] * int(n_intervals)
updated_weights[0] = sorted_weights[0]

for current_i in range(1, int(n_intervals)):
    including_i = sorted_weights[current_i]
    
    current_j = find_latest_non_conflicting(sorted_intervals, current_i)
    if current_j != -1:
        including_i += updated_weights[current_j]

    updated_weights[current_i] = max(including_i, updated_weights[current_i-1])

print(updated_weights[-1])
