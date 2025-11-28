from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Goal: Classify the 'Main Cuisine' based on cost and votes
# Simplification: We take the first cuisine listed as the primary class
df['Primary_Cuisine'] = df['Cuisines'].apply(lambda x: x.split(',')[0] if isinstance(x, str) else 'Unknown')

# Features: Cost, Ratings, Votes, Price Range
X = df[['Average Cost for two', 'Aggregate rating', 'Votes', 'Price range']]
y = df['Primary_Cuisine']

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# 4. Performance Report
y_pred = rf_model.predict(X_test)
print(classification_report(y_test, y_pred))
