import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file
df = pd.read_csv("dataset3.csv")

# Split dataset column
df[['flag', 'size']] = df['dataset'].str.split('_', expand=True)
df['size'] = df['size'].astype(int)
df['time (s)'] = df['time (s)'].astype(float)

# Set up plot
plt.figure(figsize=(10, 6))

# Colors and markers
colors = {
    'o3': 'green',
    'none': 'red'
}
markers = {
    'o3': 'o',
    'none': 'o'
}

# Plot each flag configuration
for flag in df['flag'].unique():
    subset = df[df['flag'] == flag]
    label = "O3 Enabled" if flag == 'o3' else "No Optimization"
    plt.plot(
        subset['size'],
        subset['time (s)'],
        marker=markers[flag],
        color=colors[flag],
        label=label
    )

# Log scales
plt.xscale('log')
plt.yscale('log')

# Labels and title
plt.xlabel("Computation Size (log scale)")
plt.ylabel("Execution Time (s, log scale)")
plt.title("C Performance: Compiler Optimization Comparison")



# Legend and grid
plt.legend()
plt.grid(True, which="both", ls="--", lw=0.5)

# Save to PNG
plt.savefig("c_compiler_optimization_comparison.png", dpi=300, bbox_inches="tight")

# Show plot
plt.show()
