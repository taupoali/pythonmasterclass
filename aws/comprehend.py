import boto3

comp = boto3.client("comprehend")
print(comp.detect_sentiment(Text="Rishi Sunak destroyed contract markets", LanguageCode="en"))