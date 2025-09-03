#Importing Pandas and the csv file

import pandas as pd
file_path = "CSV Files/orders copy.csv"  
df = pd.read_csv(file_path)

# Preview the first few rows
df.head()

#Exploratory Data Analysis

df.info()

# Check for unique number of values.
df.nunique()

# Check for duplicated rows.
df.duplicated().sum()

# Check for null values
df.isnull().sum()

df['order_status'].value_counts()

df['order_item'].value_counts().head(10)

df['total_amount'].describe()

#Most customers spent around ₹250–₹340.
#But some expensive outlier orders raised the average bill (mean) to ₹322.
#This is common in real-world billing data.


import matplotlib.pyplot as plt
import seaborn as sns

# Set a nice theme
sns.set(style='whitegrid', palette='Set2')

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='order_status')
plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.show()

top_items = df['order_item'].value_counts().head(10)

plt.figure(figsize=(8,6))
sns.barplot(x=top_items.values, y=top_items.index, palette='viridis')
plt.title("Top 10 Most Ordered Items")
plt.xlabel("Number of Orders")
plt.ylabel("Order Item")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df['total_amount'], bins=30, kde=True, color='skyblue')
plt.title("Distribution of Total Order Amount")
plt.xlabel("Total Amount (₹)")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 4))  # Wider figure for clarity
sns.set_style("whitegrid")  # Clean background with grid

# Draw boxplot with color and line width adjustments
sns.boxplot(
    x=df['total_amount'], 
    color='skyblue', 
    linewidth=2
)

# Add better labels and title
plt.xlabel("Total Order Amount (₹)", fontsize=12)
plt.title("Distribution of Total Order Amounts", fontsize=14, fontweight='bold')
plt.xticks(fontsize=10)
plt.yticks([])  # No need for y-axis ticks on a horizontal boxplot
plt.tight_layout()
plt.show()
