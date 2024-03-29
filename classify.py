from newspaper import Article
import joblib  

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
    section_mapping = {
    1: 'Bollywood',
    2: 'Cities',
    3: 'Education',
    4: 'Political',
    5: 'Sports'
    }
    section_name = section_mapping[prediction]

    print(f'Predicted Section for the new article: {section_name}')

if __name__ == "__main__":
    new_article_url = 'https://indianexpress.com/article/sports/cricket/india-versus-australia-low-key-early-audition-for-next-years-t20-world-cup-9038353/'
    classify_new_article(new_article_url)
