from textblob import TextBlob

def analyze_complaint(text):
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment < 0:
        mood = "Angry Complaint"
    elif sentiment == 0:
        mood = "Neutral Complaint"
    else:
        mood = "Positive Complaint"

    if "food" in text.lower():
        category = "Food"
    elif "hostel" in text.lower():
        category = "Hostel"
    elif "teacher" in text.lower():
        category = "Academics"
    else:
        category = "Other"

    return mood, category
