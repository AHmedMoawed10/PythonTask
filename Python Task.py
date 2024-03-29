import pandas as pd

# Load data from CSV into a DataFrame
df = pd.read_csv('Employees.csv')

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Remove decimal places in Age column
df['Age'] = df['Age'].astype(int)

# 3. Convert USD salary to EGP (assuming 1 USD = 49 EGP)
df['Salary'] = df['Salary'] * 49

# 4. Print statistics
print("Average age:", df['Age'].mean())
print("Median salary:", df['Salary'].median())
gender_ratio = df['Gender'].value_counts(normalize=True)
print("Ratio of male to female employees:")
print("Male:", gender_ratio['Male'])
print("Female:", gender_ratio['Female'])

# 5. Write data to a new CSV file
df.to_csv('processed_data.csv', index=False)