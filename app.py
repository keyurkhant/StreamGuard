from flask import Flask, render_template
import boto3
import json

app = Flask(__name__)

# AWS S3 client
s3 = boto3.client('s3')
bucket_name = 'your-bucket'

@app.route('/')
def index():
    # Fetch data from S3
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix='tweet-sentiments/')
    sentiments = []
    for obj in response.get('Contents', []):
        data = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
        sentiments.append(json.loads(data['Body'].read().decode('utf-8')))

    # Aggregate data for visualization
    sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
    for sentiment in sentiments:
        sentiment_counts[sentiment['sentiment_analysis']] += 1

    return render_template('index.html', sentiment_counts=sentiment_counts)

if __name__ == '__main__':
    app.run(debug=True)
