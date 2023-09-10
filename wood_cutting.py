

n_rounds = int(input())

for _round in range(n_rounds): # Loop over each round
    num_customers = int(input()) # Get the number of customers
    customer_data = []

    for customer in range(num_customers): # Loop over each customer
        sizes = list(map(int, input().split()))[1:] # Get the sizes of the customers wood and convert it to integer
        total_size = sum(sizes) 
        customer_data.append((total_size, sizes)) # Append the total sum of sizes and sizes to a list

    # Sort customers by their total wood size
    customer_data.sort()

    # Compute total waiting times for each customer
    previous_times = 0
    total_wait_times = []
    for total, sizes in customer_data:
        wait_time = previous_times + total # Compute the time waited for the current customer
        total_wait_times.append(wait_time)
        previous_times += total

    avg_time = sum(total_wait_times) / num_customers
    print("{:.10f}".format(avg_time))
