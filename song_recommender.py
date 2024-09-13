import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

LASTFM_API_KEY = os.getenv('LASTFM_API_KEY')

def get_recommendations(sentiment):
    # Example query based on sentiment
    query = 'happy' if sentiment == 'positive' else 'sad'
    url = f"http://ws.audioscrobbler.com/2.0/"
    params = {
        'method': 'track.search',
        'track': query,
        'api_key': LASTFM_API_KEY,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    data = response.json()
    recommendations = [track['name'] for track in data['results']['trackmatches']['track']]
    return recommendations
