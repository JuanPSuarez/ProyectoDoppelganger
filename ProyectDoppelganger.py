import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

# Define greetings and regards
greetings = ["Hola", "Hola que tal"]
regards = ["Chau", "Nos Vemos", "Abrazo"]
formal_greetings = ["Estimados","Buenas","Buenas tardes"]
formal_regards = ["Saludos cordiales", "Saludos"]

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to calculate sentiment score
def calculate_sentiment(text):
    sentiment = sia.polarity_scores(text)
    return sentiment["compound"]

# Function to check if a greeting is present in the text
def has_greeting(text):
    for greeting in greetings:
        if greeting.lower() in text.lower():
            return True
    return False

# Function to check if a regard is present in the text
def has_regard(text):
    for regard in regards:
        if regard.lower() in text.lower():
            return True
    return False

# Function to check if a formal greeting is present in the text
def has_formal_greeting(text):
    for greeting in formal_greetings:
        if greeting.lower() in text.lower():
            return True
    return False

# Function to check if a formal regard is present in the text
def has_formal_regard(text):
    for regard in formal_regards:
        if regard.lower() in text.lower():
            return True
    return False

# Function to calculate points based on behavior
def calculate_points(email):
    points = 0

    # Check greetings and regards
    if not has_greeting(email) or not has_regard(email):
        points += 1

    # Check formal greetings and regards
    if not has_formal_greeting(email) or not has_formal_regard(email):
        points += 2

    # Calculate sentiment score
    sentiment_score = calculate_sentiment(email)
    if sentiment_score < 0.5:
        points += 1

    return points

# Example usage
email_text = "Estimados, buenas tardes  Espero que todo vaya bien. Saludos."
points = calculate_points(email_text)
print("Points:", points)