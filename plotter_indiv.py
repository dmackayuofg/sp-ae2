import matplotlib.pyplot as plt
import pandas as pd

# Read CSV
df = pd.read_csv('dataset2.csv')

# Parse dataset column
df[['language', 'threading', 'size']] = df['dataset'].str.split('_', expand=True)
df['size'] = df['size'].astype(int)
df['time (s)'] = df['time (s)'].astype(float)

# Languages to plot
languages = df['language'].unique()

# Colors for single vs multi
colors = {
    'single': 'orange',
    'multi': 'red'
}

for lang in languages:
    lang_df = df[df['language'] == lang]

    # Skip if only one threading type exists
    if lang_df['threading'].nunique() < 2:
        continue

    plt.figure(figsize=(8, 5))

    for thread in ['single', 'multi']:
        subset = lang_df[lang_df['threading'] == thread]
        if subset.empty:
            continue

        plt.plot(
            subset['size'],
            subset['time (s)'],
            marker='o',
            color=colors[thread],
            label=thread.title()
        )

    # Log scales
    plt.xscale('log')
    plt.yscale('log')

    # Labels & title
    plt.xlabel("Computation Size (log scale)")
    plt.ylabel("Execution Time (s, log scale)")
    plt.title(f"{lang.title()}: Single vs Multi-threaded")

    # X ticks
    #plt.xticks(
    #    [1000, 10000, 100000, 1000000, 10000000],
    #    ['1k', '10k', '100k', '1M', '10M']
    #)

    plt.legend()
    plt.grid(True, which="both", ls="--", lw=0.5)

    # Save figure
    filename = f"{lang}_single_vs_multi.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
