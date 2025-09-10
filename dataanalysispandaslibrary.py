import pandas as pd

data = {
    "Name": ["Haniyah", "Fatimah", "Huda"],
    "Age": [17, 19, 18],
    "City": ["Lahore", "Islamabad", "Karachi"]
}

df = pd.DataFrame(data)

print("Full Table:")
print(df)

print("\nNames:")
print(df["Name"])

print("\nFirst Row:")
print(df.iloc[0])

print("\nPeople older than 18:")
print(df[df["Age"] > 18])