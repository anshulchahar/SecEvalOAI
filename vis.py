import json
import matplotlib.pyplot as plt
import pandas as pd

# Load the JSON data from the file
with open('data.json', 'r') as f:
    data = json.load(f)

# --- Data Extraction and Preparation ---

# Extract the 'metrics' dictionary, which contains the core data
metrics = data.get('metrics', {})

# Extract the overall totals for the summary plot
totals = metrics.get('_totals', {})

# Prepare data for the detailed file-by-file analysis
file_metrics = {k: v for k, v in metrics.items() if k != '_totals'}

# Create a list of dictionaries, where each dictionary represents a file's metrics
plot_data = []
for filename, values in file_metrics.items():
    # Append a dictionary with the filename and its corresponding metrics
    plot_data.append({
        'filename': filename,
        'lines_of_code': values.get('loc', 0),
        'high_severity': values.get('SEVERITY.HIGH', 0),
        'medium_severity': values.get('SEVERITY.MEDIUM', 0),
        'low_severity': values.get('SEVERITY.LOW', 0),
        'high_confidence': values.get('CONFIDENCE.HIGH', 0),
        'medium_confidence': values.get('CONFIDENCE.MEDIUM', 0),
        'low_confidence': values.get('CONFIDENCE.LOW', 0),
    })

# Convert the list of dictionaries to a pandas DataFrame for easier manipulation
df = pd.DataFrame(plot_data)

# --- Visualization ---

# Set the overall style for the plots for a consistent and professional look
plt.style.use('seaborn-v0_8-whitegrid')

# Create a figure to hold all the subplots, with a smaller size for just pie charts
fig = plt.figure(figsize=(12, 6), constrained_layout=True)

# Add a main title to the entire figure to provide context
fig.suptitle('Security Scan Analysis', fontsize=24, fontweight='bold')

# Create a grid of subplots with 1 row and 2 columns for pie charts only
gs = fig.add_gridspec(1, 2)

# --- Subplot 1: Overall Severity Distribution ---
ax1 = fig.add_subplot(gs[0, 0])
severities = {
    'High': totals.get('SEVERITY.HIGH', 0),
    'Medium': totals.get('SEVERITY.MEDIUM', 0),
    'Low': totals.get('SEVERITY.LOW', 0)
}
# Filter out severities with a count of 0 to keep the plot clean
severities = {k: v for k, v in severities.items() if v > 0}
ax1.pie(severities.values(), labels=severities.keys(), autopct='%1.1f%%',
        colors=['#d9534f', '#f0ad4e', '#5cb85c'],
        wedgeprops={'edgecolor': 'white', 'linewidth': 2})
ax1.set_title('Overall Severity Distribution', fontsize=16, fontweight='bold')

# --- Subplot 2: Overall Confidence Distribution ---
ax2 = fig.add_subplot(gs[0, 1])
confidences = {
    'High': totals.get('CONFIDENCE.HIGH', 0),
    'Medium': totals.get('CONFIDENCE.MEDIUM', 0),
    'Low': totals.get('CONFIDENCE.LOW', 0)
}
# Filter out confidences with a count of 0
confidences = {k: v for k, v in confidences.items() if v > 0}
ax2.pie(confidences.values(), labels=confidences.keys(), autopct='%1.1f%%',
        colors=['#428bca', '#5bc0de', '#d9edf7'],
        wedgeprops={'edgecolor': 'white', 'linewidth': 2})
ax2.set_title('Overall Confidence Distribution', fontsize=16, fontweight='bold')

# --- Display the plots ---
plt.show()
