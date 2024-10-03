# main.py
from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text.

    :param text: Input text
    :return: Sentiment polarity (-1.0 to 1.0, where -1 is negative and 1 is positive)
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    sentiment_score = analyze_sentiment(text)
    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print(f"The sentiment of the input text is {sentiment} (score: {sentiment_score})")
