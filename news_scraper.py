from newspaper import Article
import csv

def scrape_and_save_news(urls, output_file):
    # Create a CSV file for saving the data
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Text', 'Section']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through each URL and scrape the news
        for url in urls:
            article = Article(url)
            article.download()
            article.parse()

            # Write the data to the CSV file
            writer.writerow({'Title': article.title, 'Text': article.text, 'Section': 'Bollywood'})

if __name__ == "__main__":
    # List of news article URLs to scrape
    news_urls = [
        'https://indianexpress.com/article/entertainment/bollywood/ronit-roy-addressed-hrithik-roshan-as-sir-he-said-i-have-a-problem-with-you-9038229/ ',
        'https://indianexpress.com/article/entertainment/bollywood/tiger-3-box-office-day-11-early-reports-salman-khan-film-inches-towards-rs-250-crore-mark-9038087/ ',
        'https://indianexpress.com/article/entertainment/bollywood/vir-das-international-emmy-win-best-comedy-hope-we-all-just-get-sillier-9038349/ ',
        'https://indianexpress.com/article/entertainment/bollywood/orry-responds-to-being-a-liver-says-never-wants-to-be-asked-what-he-does-for-a-living-9038314/ ',
        'https://indianexpress.com/article/entertainment/bollywood/animal-trailer-ranbir-kapoor-chokes-rashmika-mandanna-sandeep-reddy-vanga-hyper-violent-kabir-singh-follow-up-9038958/',
        'https://indianexpress.com/article/entertainment/bollywood/madhur-bhandarkar-says-tamannaah-bhatia-did-not-get-her-due-9038202/ ',
        'https://indianexpress.com/article/entertainment/bollywood/shah-rukh-khan-answers-why-he-wont-do-bike-stunt-like-tom-cruise-and-how-he-deals-with-nervousness-9037982/ ',
        'https://indianexpress.com/article/entertainment/bollywood/shah-rukh-khan-rooting-for-suhana-khan-the-archies-she-loves-dunki-9038020/ ',
        'https://indianexpress.com/article/entertainment/bollywood/shah-rukh-khan-jokes-illegal-way-watch-dunki-in-theatres-ask-srk-9037955/ ',
        'https://indianexpress.com/article/entertainment/bollywood/mukesh-chhabra-says-shah-rukh-khans-dunki-will-break-all-records-calls-it-film-of-a-lifetime-100-times-better-than-3-idiots-9037309/ ',
        'https://indianexpress.com/article/entertainment/bollywood/karan-johar-recalls-when-sidharth-malhotra-kiara-advani-fighting-patched-up-over-a-meal-9037759/ ',
        'https://indianexpress.com/article/entertainment/bollywood/anurag-kashyap-to-teach-in-kerala-love-corrupting-young-minds-9037351/ ',
        'https://indianexpress.com/article/entertainment/bollywood/ranbir-kapoor-learns-telugu-from-rashmika-mandanna-gets-surprised-when-a-paparazzo-speaks-in-telugu-watch-9037654/ ',
        'https://indianexpress.com/article/entertainment/bollywood/when-shah-rukh-khan-said-he-cant-be-an-actor-i-would-have-to-hug-girls-and-gauri-has-said-no-9037231/ ',
        'https://indianexpress.com/article/entertainment/bollywood/dunki-song-lutt-putt-gaya-shah-rukh-khan-is-undisputed-king-of-romance-and-the-way-he-looks-at-taapsee-is-proof-9037498/ ',
        'https://indianexpress.com/article/entertainment/bollywood/anurag-kashyap-gifted-marijuana-misconception-drug-addict-9037295/ ',
        'https://indianexpress.com/article/entertainment/bollywood/bhumi-pednekar-shares-photo-from-hospital-as-she-gets-treatment-for-dengue-mujhe-8-din-ka-massive-torture-de-diya-9037574/ ',
        'https://indianexpress.com/article/entertainment/bollywood/sam-bahadur-song-banda-unstoppable-vicky-kaushal-is-all-action-and-no-talk-in-latest-number-9037404/ ',
        'https://indianexpress.com/article/entertainment/bollywood/shah-rukh-khan-imdb-most-popular-indian-star-of-2023-alia-bhatt-deepika-padukone-akshay-kumar-9037462/',
    ]

    # Output CSV file name
    output_csv_file = 'Bollywood_data.csv'

    # Scrape and save the news articles
    scrape_and_save_news(news_urls, output_csv_file)