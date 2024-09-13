from tone_analyzer import analyze_sentiment
from song_recommender import get_recommendations

def process_message(message):
    sentiment = analyze_sentiment(message)
    recommendations = get_recommendations(sentiment)
    return {
        'sentiment': sentiment,
        'recommendations': recommendations
    }
