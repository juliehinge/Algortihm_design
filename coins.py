def min_payment(price, coins, idx=0, memo=None):
    if memo is None:
        memo = {}

    # Base condition: if price is 0 or less, return the overpayment (negative means exact price was reached) and 0 coins used
    if price <= 0:
        return -price, 0

    # Base condition: if no more coins to consider, return infinite price (unreachable) and infinite coins
    if idx == len(coins):
        return float('inf'), float('inf')

    # Check if result is memoized
    if (price, idx) in memo:
        return memo[(price, idx)]

    # Consider not using the current coin
    without_curr_coin = min_payment(price, coins, idx + 1, memo)
    
    # Consider using the current coin
    with_curr_coin_val, with_curr_coin_count = min_payment(price - coins[idx], coins, idx + 1, memo)
    with_curr_coin = (with_curr_coin_val, with_curr_coin_count + 1)

    # Choose the best option
    best = min(without_curr_coin, with_curr_coin)

    # Save to memo and return
    memo[(price, idx)] = best
    return best

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        price = int(input())
        n = int(input())
        coins = [int(input()) for _ in range(n)]
        overpay, coins_used = min_payment(price, coins)
        print(price + overpay, coins_used)

if __name__ == "__main__":
    main()
