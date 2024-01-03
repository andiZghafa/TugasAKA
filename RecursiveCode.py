import matplotlib.pyplot as plt
import time

def S(n):
    if n == 1:
        return 1
    else:
        return S(n-1) + n * n * n

# Lists to store input values and elapsed times for each function call
n_values = list(range(1, 11))
elapsed_times_S = []

# Measure elapsed time for each function call of S
for n in n_values:
    start_time_S = time.time()
    S(n)
    end_time_S = time.time()
    elapsed_times_S.append(end_time_S - start_time_S)

# Create the plot
plt.plot(n_values, elapsed_times_S, marker='o', label='S function')
plt.xlabel('n')
plt.ylabel('Elapsed Time (seconds)')
plt.title('Runtime Analysis of S Function')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
