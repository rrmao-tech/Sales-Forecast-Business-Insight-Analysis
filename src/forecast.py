import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the 'assets' folder exists
os.makedirs("assets", exist_ok=True)

# Load dataset (use relative path for GitHub compatibility)
df = pd.read_csv("data/sales_time_series.csv")

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Create a simple forecast using 3-day moving average
df['forecast'] = df['sales'].rolling(window=3).mean()

# Create the plot
plt.figure(figsize=(10, 5))

# Plot actual sales
plt.plot(df.index, df['sales'], marker='o', label='Actual Sales')

# Plot forecast
plt.plot(df.index, df['forecast'], linestyle='--', label='Forecast')

# Add annotation for business insight
plt.annotate(
    "Sales Growth Opportunity",
    xy=(df.index[-1], df['sales'].iloc[-1]),           # Point to last data point
    xytext=(df.index[-5], df['sales'].iloc[-1] - 10),  # Offset to avoid overlap
    arrowprops=dict(
        facecolor='black',
        arrowstyle='->',
        linewidth=1.5
    ),
    fontsize=11,
    ha='left'
)

# Add title
plt.title(
    "Sales Trend & Short-term Forecast\n(Business Insight)",
    fontsize=14
)

# Label axes
plt.xlabel("Date")
plt.ylabel("Sales")

# Rotate x-axis labels for readability
plt.xticks(rotation=30)

# Show legend
plt.legend()

# Adjust layout to prevent clipping
plt.tight_layout()
plt.subplots_adjust(top=0.85)

# Save figure (for README display)
plt.savefig("assets/sales_forecast.png")

# Display the plot
plt.show()
