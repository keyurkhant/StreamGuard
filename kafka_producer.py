from kafka import KafkaProducer
import json
import time
import pandas as pd

# Load dataset
df = pd.read_csv('dataset/sentiment140.csv', encoding='latin-1', header=None)
df.columns = ['sentiment', 'id', 'date', 'query', 'user', 'text']

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Stream data
for index, row in df.iterrows():
    data = {'sentiment': row['sentiment'], 'text': row['text']}
    producer.send('tweets', value=data)
    time.sleep(0.1)

producer.flush()