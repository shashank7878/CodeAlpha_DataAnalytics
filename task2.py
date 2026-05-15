
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("task1.csv")

# ==============================
# Top 10 Mobile Brands Chart
# ==============================

top_brands = df['Brand'].value_counts().head(10)

plt.figure(figsize=(10,6))
top_brands.plot(kind='bar')

plt.title("Top 10 Mobile Brands")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ==============================
# Price Distribution Chart
# ==============================

# Convert price column into numeric
df['Selling Price'] = (
    df['Selling Price']
    .astype(str)
    .str.replace(r'[^0-9.]', '', regex=True)
)

df['Selling Price'] = pd.to_numeric(
    df['Selling Price'],
    errors='coerce'
)

plt.figure(figsize=(10,6))

plt.hist(df['Selling Price'].dropna(), bins=20)

plt.title("Mobile Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# ==============================
# Ratings Distribution Chart
# ==============================

df['Rating'] = pd.to_numeric(
    df['Rating'],
    errors='coerce'
)

plt.figure(figsize=(10,6))

plt.hist(df['Rating'].dropna(), bins=10)

plt.title("Mobile Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

