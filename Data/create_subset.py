import pandas as pd

# Load the full dataset
df = pd.read_csv('Data/creditcard.csv')
print("Original shape:", df.shape)  # Should be (284807, 31)

# Create a subset (e.g., 50,000 random rows)
subset_df = df.sample(n=50000, random_state=42)
print("Subset shape:", subset_df.shape)  # Should be (50000, 31)

# Save the subset
subset_df.to_csv('Data/creditcard_subset.csv', index=False)
print("Subset saved as Data/creditcard_subset.csv")