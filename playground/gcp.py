# Create credential inside directory
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

def entity_sentiment_analysis(text):
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    response = client.analyze_entity_sentiment(document=document, encoding_type='UTF32')
    return response.entities

# entity_sentiment = entity_sentiment_analysis('Google is awfully good')

# print(entity_sentiment)
# print(entity_sentiment[0].name)
# print(entity_sentiment[0].sentiment.magnitude)
# print(entity_sentiment[0].sentiment.score)
