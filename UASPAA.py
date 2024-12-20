import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value=178, seed=42):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(arr):
    """Check if all elements in the array are unique."""
    return len(arr) == len(set(arr))

def measure_time(func, *args):
    """Measure the execution time of a function."""
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    return result, end_time - start_time

# Configuration
n_values = [100, 150, 200, 250, 300, 350, 400, 450, 500]
max_value = 217
seed = 69

worst_case_times = []
average_case_times = []

for n in n_values:
    # Generate array
    arr = generate_array(n, max_value, seed)

    # Measure average case (real-world data)
    _, avg_time = measure_time(is_unique, arr)

    # Measure worst case (all unique, largest set operation)
    worst_case_array = list(range(1, n + 1))  # All unique values
    _, worst_time = measure_time(is_unique, worst_case_array)

    # Store times
    average_case_times.append(avg_time)  # Time in seconds
    worst_case_times.append(worst_time)  # Time in seconds

    # Determine uniqueness
    unique_status = "UNIQUE" if is_unique(arr) else "NOT UNIQUE"
    print(f"Array with n={n}: {unique_status}")
    print(f"Worst Case Time for n={n}: {worst_time:.10f} seconds")
    print(f"Average Case Time for n={n}: {avg_time:.10f} seconds\n")

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_case_times, label="Worst Case", marker="s", color="red")
plt.plot(n_values, average_case_times, label="Average Case", marker="o", color="blue")
plt.xlabel("Array Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Performance Comparison: Worst Case vs Average Case")
plt.xticks(n_values)
plt.legend()
plt.grid()
plt.show()