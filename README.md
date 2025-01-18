# Real-Time Sentiment Tracker for Streaming Social Media Data

This project is designed to analyze the sentiment of streaming social media data in real-time using Apache Kafka, Apache Spark on AWS EMR, and a Flask-based dashboard. The processed results are visualized dynamically to showcase sentiment trends.

---

## Features
1. **Data Streaming**:
   - Kafka streams social media data (simulated using a dataset).

2. **Real-Time Processing**:
   - Apache Spark processes data using sentiment analysis with TextBlob.

3. **Data Storage**:
   - Processed data is stored in Amazon S3.

4. **Visualization**:
   - Flask-based dashboard with Plotly graphs displays sentiment trends.

---

## Technologies Used
- **Apache Kafka**: Data streaming.
- **Apache Spark**: Real-time processing (via PySpark).
- **AWS EMR**: Cloud-based Spark cluster.
- **Flask**: Web application for dashboard.
- **Plotly**: Data visualization.
- **Amazon S3**: Data storage.
- **Python Libraries**: `textblob`, `boto3`, `kafka-python`.

---

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or above
- AWS account with access to S3 and EMR
- Apache Kafka installed locally or managed service
- Virtual environment setup for Python
- Dataset: https://www.kaggle.com/datasets/kazanova/sentiment140

### 2. Install Dependencies
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Set Up Kafka
1. Start Zookeeper:
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   ```
2. Start Kafka:
   ```bash
   bin/kafka-server-start.sh config/server.properties
   ```
3. Create a Kafka topic:
   ```bash
   bin/kafka-topics.sh --create --topic tweets --bootstrap-server localhost:9092
   ```

### 4. Set Up AWS EMR
1. Go to the AWS Management Console and navigate to the EMR service.
2. Create a cluster with the following configurations:
   - Release version: `emr-6.x.x`
   - Enable Spark and Hadoop.
   - Choose `m5.xlarge` instance types.
   - Ensure SSH access is enabled.
3. Launch the cluster.
4. Upload and execute the `spark_streaming.py` script.

### 5. Run the Kafka Producer
Stream data to Kafka:
```bash
python kafka_producer.py
```

### 6. Run the Flask Application
Launch the dashboard:
```bash
python app.py
```

Access the dashboard at `http://127.0.0.1:5000`.

---

## File Structure
```
project/
├── kafka_producer.py       # Streams data to Kafka
├── spark_streaming.py      # Spark job for real-time processing
├── app.py                  # Flask application for visualization
├── templates/
│   └── index.html          # HTML for the dashboard
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Example Output
- **Dashboard**: Displays a bar chart with the counts of positive, negative, and neutral sentiments.

---

## Future Improvements
- Add live integration with social media APIs (e.g., Twitter API).
- Use advanced sentiment analysis models for improved accuracy.
- Implement real-time notifications based on sentiment trends.
