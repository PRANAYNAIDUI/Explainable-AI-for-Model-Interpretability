# Get the first few rows of the dataset
print("Data Preview:")
print(df.head())

# Get summary statistics
print("\nData Summary:")
print(df.describe())

# Check the distribution of the target variable
print("\nTarget Distribution:")
print(df['target'].value_counts())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())