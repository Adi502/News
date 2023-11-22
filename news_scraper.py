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
            writer.writerow({'Title': article.title, 'Text': article.text, 'Section': 'Sports'})

if __name__ == "__main__":
    # List of news article URLs to scrape
    news_urls = [
        'https://indianexpress.com/article/sports/cricket/team-india-backroom-staff-maths-teacher-mountaineer-bus-driver-it-engineer-9036956/',
        'https://indianexpress.com/article/sports/cricket/afghanistan-to-tour-india-for-three-t20i-series-in-january-ahead-of-england-test-series-9036735/',
        'https://indianexpress.com/article/sports/football/coach-igor-stimac-india-vs-qatar-world-cup-qualifier-9036906/',
        'https://indianexpress.com/article/sports/cricket-world-cup/there-is-a-lump-in-my-throat-and-fire-in-my-heart-gautam-gambhir-returns-to-kkr-as-team-mentor-9037407/',
        'https://indianexpress.com/article/sports/cricket-world-cup/there-is-a-lump-in-my-throat-and-fire-in-my-heart-gautam-gambhir-returns-to-kkr-as-team-mentor-9037407/',
        'https://indianexpress.com/photos/sports-gallery/fifties-from-rohit-sharma-and-shreyas-iyer-guide-india-to-7-wicket-win-against-pakistan/',
        'https://indianexpress.com/article/sports/cricket/pakistan-names-wahab-riaz-as-head-of-national-selection-committee-sohail-tanvir-to-head-junior-selection-panel-9031488/',
        'https://indianexpress.com/article/sports/cricket/suryakumar-yadav-likely-to-captain-india-in-t20is-against-australia-9030636/',
        'https://indianexpress.com/article/sports/cricket/sometimes-its-nice-to-see-ball-dominate-bat-mitchell-starc-after-australia-beat-south-africa-at-eden-gardens-9030126/',
        'https://indianexpress.com/article/sports/cricket/hardik-pandya-set-to-miss-white-ball-series-against-australia-south-africa-9030057/',
        'https://indianexpress.com/article/sports/cricket/icc-pitch-consultant-raises-concerns-about-switching-of-pitch-that-might-favour-india-if-they-reach-icc-world-cup-final-9027572/',
        'https://indianexpress.com/article/sports/cricket/india-vs-new-zealand-live-score-icc-cricket-world-cup-2023-1st-semi-final-at-wankhede-stadium-mumbai-9026898/',
        'https://indianexpress.com/article/sports/cricket/dont-even-go-thereid-like-to-pick-his-brain-ravi-shastri-on-steve-smith-look-a-like-sachin-tendulkar-statue-9023697/',
        'https://indianexpress.com/article/sports/cricket/england-vs-pakistan-live-score-icc-cricket-world-cup-2023-44th-match-today-at-eden-gardens-kolkata-9022155/',
        'https://indianexpress.com/article/sports/cricket/australia-vs-bangladesh-live-score-icc-cricket-world-cup-2023-43rd-match-today-at-mca-stadium-pune-9021647/',
        'https://indianexpress.com/article/sports/cricket/learn-from-india-create-a-bigger-pool-of-players-shoaib-maliks-advice-pcb-after-pakistan-fail-to-qualify-for-the-semifinals-9022475/',
        'https://indianexpress.com/article/sports/cricket/best-opening-batsman-after-sunil-gavaskar-sourav-ganguly-on-virender-sehwag-9026124/',
        'https://indianexpress.com/article/sports/cricket/like-a-salmon-on-the-ground-shaking-glenn-maxwell-recalls-dressing-room-banter-after-astonishing-201-9025989/',
        'https://indianexpress.com/article/sports/cricket/icc-suspends-sri-lanka-crickets-membership-with-immediate-effect-due-to-government-interference-9022135/',
        'https://indianexpress.com/article/sports/cricket/south-africa-vs-afghanistan-live-score-icc-cricket-world-cup-2023-42nd-match-today-at-narendra-modi-stadium-ahmedabad-9020739/',
        # Add more URLs as needed
    ]

    # Output CSV file name
    output_csv_file = 'Sports_data.csv'

    # Scrape and save the news articles
    scrape_and_save_news(news_urls, output_csv_file)