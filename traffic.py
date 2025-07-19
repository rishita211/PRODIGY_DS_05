import zipfile
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your zip file path
zip_path = r"C:\Users\RISHITA\Downloads\archive (1).zip"
extract_folder = r"C:\Users\RISHITA\Documents\traffic_dataset"

# Step 1: Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)
print(f"[✅] Extracted to: {extract_folder}")

# Step 2: Load the CSV file (update if actual CSV name is different)
csv_file = os.path.join(extract_folder, "Mall_Customers.csv")
df = pd.read_csv(csv_file)

# Step 3: Basic Info
print("\n📌 Sample Data:\n", df.head())
print("\n📌 Info:")
print(df.info())
print("\n📌 Missing values:\n", df.isnull().sum())

# Step 4: Visualization 1 – Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=20, kde=True, color='lightblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(extract_folder, "age_distribution.png"))
plt.show()

# Step 5: Visualization 2 – Income vs Spending
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender')
plt.title("Spending Score vs Annual Income")
plt.tight_layout()
plt.savefig(os.path.join(extract_folder, "income_vs_spending.png"))
plt.show()

print("\n✅ Visualizations saved in:", extract_folder)
