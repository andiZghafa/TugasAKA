import matplotlib.pyplot as plt
import time

def Mystery(n):
    S = 0
    for i in range(1, n + 1):
        S += i * i
    return S

# Lists to store input values and elapsed times for each function call
n_values = list(range(1, 501))
elapsed_times_Mystery = []

# Measure elapsed time for each function call of Mystery
for n in n_values:
    start_time_Mystery = time.time()
    Mystery(n)
    end_time_Mystery = time.time()
    elapsed_times_Mystery.append(end_time_Mystery - start_time_Mystery)

# Create the plot
plt.plot(n_values, elapsed_times_Mystery, marker='o', label='Mystery function')
plt.xlabel('n')
plt.ylabel('Elapsed Time (seconds)')
plt.title('Runtime Analysis of Mystery Function')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
