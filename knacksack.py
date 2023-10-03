def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(2)]

    # Populate the dp for the first item
    for w in range(weights[0], capacity + 1):
        dp[0][w] = values[0]

    # Build the DP table
    for i in range(1, n):
        for w in range(capacity + 1):
            not_taken = dp[(i - 1) % 2][w]
            taken = values[i] + dp[(i - 1) % 2][w - weights[i]] if w >= weights[i] else 0
            dp[i % 2][w] = max(not_taken, taken)

    return dp[(n - 1) % 2]

def find_chosen_items(dp, weights, values, capacity):
    n = len(weights)
    chosen_indices = []

    for i in reversed(range(n)):
        # Check if this item was included in the solution
        if dp[capacity] == dp[capacity - weights[i]] + values[i] if capacity - weights[i] >= 0 else 0:
            chosen_indices.append(i)
            capacity -= weights[i]
        if capacity == 0:
            break

    return chosen_indices



while True:
    try:
        capacity, n_items = map(int, input().split())
        weights = []
        values = []
        for _ in range(n_items):
            value, weight = map(int, input().split())
            values.append(value)
            weights.append(weight)
        
        dp_result = knapsack(weights, values, capacity)
        chosen_indices = find_chosen_items(dp_result, weights, values, capacity)
        
        print(len(chosen_indices))
        print(" ".join(map(str, reversed(chosen_indices))))
    except EOFError:
        break
