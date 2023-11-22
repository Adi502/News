# classify.py
from newspaper import Article
import joblib  # For model persistence

def classify_new_article(article_url):
    # Load the saved model and vectorizer
    classifier = joblib.load('classifier_model.joblib')
    vectorizer = joblib.load('tfidf_vectorizer.joblib')

    # Scrape the new article
    article = Article(article_url)
    article.download()
    article.parse()
    text = article.text

    # Vectorize the text using the trained vectorizer
    text_tfidf = vectorizer.transform([text])

    # Make predictions using the trained model
    prediction = classifier.predict(text_tfidf)[0]

    print(f'Predicted Section for the new article: {prediction}')

if __name__ == "__main__":
    new_article_url = 'https://indianexpress.com/article/education/study-abroad/elite-colleges-favour-students-with-good-academic-credentials-and-strong-identity-says-university-college-london-student-indians-in-top-colleges-8997427/'
    classify_new_article(new_article_url)
