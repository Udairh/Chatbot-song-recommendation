from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    # Simple sentiment analysis: 'positive', 'negative', 'neutral'
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'
