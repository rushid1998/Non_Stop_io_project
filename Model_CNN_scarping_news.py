import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



df = pd.read_csv(r"C://Users//HP//Pictures//Screenshots//Final CNN News Scraping Project(Sports)//sports_headlines_2.csv")
X = df['Headline']
y = df['Sport Name']


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

y = label_encoder.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")


results_df = pd.DataFrame({'Metric': ['Accuracy'], 'Value': [accuracy]})


results_df.to_excel('classification_results.xlsx', index=False)




