import matplotlib.pyplot as plt
import time

def S(n):
    if n == 1:
        return 1
    else:
        return S(n-1) + n * n * n

# Record the start time
start_time = time.time()

# Generate values for the function
n_values = range(1, 11)
S_values = [S(n) for n in n_values]

# Record the end time
end_time = time.time()

# Plot the function
plt.plot(n_values, S_values)
plt.xlabel("n")
plt.ylabel("S(n)")
plt.title("Sum of Cubes of First n Natural Numbers")

# Annotate the plot with the Big O complexity
plt.annotate("O(n)", xy=(10, S_values[-1]), xytext=(8, S_values[-1] + 50), arrowprops=dict(facecolor='black', shrink=0.05))

# Show the plot
plt.grid(True)
plt.show()

# Calculate and print the total elapsed time
elapsed_time = end_time - start_time
print(f"Total elapsed time: {elapsed_time:.6f} seconds")
