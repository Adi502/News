import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load your labeled dataset
df = pd.read_csv('Data.csv', encoding='latin1')

# Split the data into training and testing sets
train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

# Convert text data to TF-IDF features
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  
X_train = tfidf_vectorizer.fit_transform(train_data['Text'])
X_test = tfidf_vectorizer.transform(test_data['Text'])

# Convert labels to numerical format
y_train = train_data['Section'].astype('category').cat.codes
y_test = test_data['Section'].astype('category').cat.codes

# Train Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Save predictions to a CSV file
output_df = pd.DataFrame({'Actual': test_data['Section'], 'Predicted': y_pred})
output_df.to_csv('classification_report.csv', index=False, header=['Actual', 'Predicted'])

# Calculate accuracy, confusion matrix, and classification report
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_report_str = classification_report(y_test, y_pred, target_names=df['Section'].unique())

print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print('Classification Report:')
print(classification_report_str)
