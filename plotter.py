import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file
df = pd.read_csv('dataset2.csv')

# Extract useful columns
df[['language', 'threading', 'size']] = df['dataset'].str.split('_', expand=True)
df['size'] = df['size'].astype(int)
df['time (s)'] = df['time (s)'].astype(float)

# Filter out c_single and java_single
df = df[~((df['language'].isin(['c', 'java'])) & (df['threading'] == 'single'))]

# Set up the plot
plt.figure(figsize=(10, 6))

# Define markers and colors
markers = {'single': 'o', 'multi': 's'}
colors = {
    'c': 'blue', 
    'java': 'green', 
    'python_single': 'orange', 
    'python_multi': 'red'
}

# Plot each combination
for lang in df['language'].unique():
    for thread in df['threading'].unique():
        subset = df[(df['language'] == lang) & (df['threading'] == thread)]
        key = f"{lang}_{thread}" if lang == 'python' else lang
        plt.plot(subset['size'], subset['time (s)'], 
                 marker=markers[thread], color=colors[key], label=f"{lang} {thread}" if lang == 'python' else lang)

# Logarithmic scale for both axes
plt.xscale('log')
plt.yscale('log')

# Labels, title, legend
plt.xlabel("Number of Steps (log scale)")
plt.ylabel("Execution Time (s, log scale)")
plt.title("Execution Time Comparison: C, Java, Python (Single vs Multi-threaded)")

# Update x-axis ticks to include the new step size
plt.xticks([1000, 10000, 100000, 1000000, 10000000],
           ['1,000', '10,000', '100,000', '1,000,000', '10,000,000'])

# Simplified legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.grid(True, which="both", ls="--", lw=0.5)
plt.show()
