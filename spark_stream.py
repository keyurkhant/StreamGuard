from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType
from pyspark.sql.functions import udf
from textblob import TextBlob

# Sentiment analysis function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return 'positive' if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'

# Define UDF
analyze_sentiment_udf = udf(analyze_sentiment, StringType())

# Spark session
spark = SparkSession.builder \
    .appName("TweetSentimentAnalysis") \
    .getOrCreate()

# Kafka stream
tweets = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "tweets") \
    .load()

# Define schema
schema = StructType().add("sentiment", StringType()).add("text", StringType())

# Process tweets
tweets_df = tweets.selectExpr("CAST(value AS STRING)").select(from_json("value", schema).alias("data")).select("data.*")
processed_df = tweets_df.withColumn("sentiment_analysis", analyze_sentiment_udf(tweets_df.text))

# Write results to S3
query = processed_df.writeStream \
    .format("json") \
    .option("path", "s3://your-bucket/tweet-sentiments/") \
    .option("checkpointLocation", "s3://your-bucket/checkpoints/") \
    .start()

query.awaitTermination()
