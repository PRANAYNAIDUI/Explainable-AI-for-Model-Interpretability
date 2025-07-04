# Import StandardScaler
from sklearn.preprocessing import StandardScaler

# Separate features and target
X = df.drop('target', axis=1)
y = df['target']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame if needed
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)