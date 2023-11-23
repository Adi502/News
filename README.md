# News Article Classification App

This repository contains a Python application for scraping news articles, training a text classification model, and evaluating its performance. The application uses the RandomForestClassifier for text classification.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python (3.x recommended)
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```git clone https://github.com/your-username/your-repository.git```
2. Navigate to the project directory:

   ```cd your-repository```
3. Install the required Python packages:

   ```pip install -r requirements.txt```

### Usage
Scraping News Articles
To scrape news articles from a website:

```python scrape_news.py```

The scraped data will be saved to a CSV file.

### Training the Model
To train the text classification model:

```python train_model.py```

Running the App
To run the app:

```python classify.py```

Results
The accuracy, confusion matrix, and classification report will be displayed in the console. Additionally, the predictions for the test set will be saved to a CSV file (classification_report.csv).

Screenshots
![image](https://github.com/Adi502/News/assets/92010701/4a4fcc65-d776-49aa-911d-2ee184c9ef05)

Output of train_model.py. The accuracy we received here is 65%.

![image](https://github.com/Adi502/News/assets/92010701/9589b948-c473-41bc-82af-aeceff5ae7d1)

Output of train_model.py. The predicted section for Sports article is Sports.
