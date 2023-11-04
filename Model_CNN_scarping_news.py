import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

df = pd.read_csv(r"C://Users//HP//Pictures//Screenshots//Final CNN News Scraping Project(Sports)//sports_headlines_2.csv")
X = df['Headline']
y = df['Sport Name']

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

classifier = MultinomialNB()
classifier.fit(X_train, y_train)

with open('naive_bayes_classifier.pkl', 'wb') as file:
    pickle.dump(classifier, file)
    pickle.dump(vectorizer, file)
    pickle.dump(label_encoder, file)

with open('naive_bayes_classifier.pkl', 'rb') as file:
    loaded_classifier = pickle.load(file)
    loaded_vectorizer = pickle.load(file)
    loaded_label_encoder = pickle.load(file)

new_data = []
num_test_headlines = int(input("Enter the number of test headlines: "))
for _ in range(num_test_headlines):
    test_headline = input("Enter a test headline: ")
    new_data.append(test_headline)

new_data_vectorized = loaded_vectorizer.transform(new_data)

new_data_predictions = loaded_classifier.predict(new_data_vectorized)

predicted_labels = loaded_label_encoder.inverse_transform(new_data_predictions)

for data, label in zip(new_data, predicted_labels):
    print(f"Headline: {data}")
    print(f"Predicted Sport Name: {label}")
    print()
