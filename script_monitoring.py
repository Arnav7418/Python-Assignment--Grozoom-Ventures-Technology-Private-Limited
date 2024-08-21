import time
import psutil
import logging
from prometheus_client import start_http_server, Gauge, Counter
import requests
import random

# Task 1: Implement a solution to monitor the Python script’s execution
# Arnav's message - Configure logging to capture errors
logging.basicConfig(filename='script_monitoring.log', level=logging.ERROR)

# Arnav's message - Prometheus metrics to track execution time, memory usage, and error count
script_execution_time = Gauge('script_execution_time', 'Execution time of the script (seconds)')
script_memory_usage = Gauge('script_memory_usage', 'Memory usage of the script (MB)')
script_error_count = Counter('script_error_count', 'Number of errors occurred during script execution')

# Arnav's message - Start the Prometheus metrics server
start_http_server(8000)

# Task 4: Ensure that alerts are actionable and send them to the appropriate messaging channels
# Arnav's message - Telegram bot configuration for sending alerts
TELEGRAM_BOT_TOKEN = 'Hi , Arnav here - I am removing the bot token for security concern as I am uploading the code to github'
TELEGRAM_CHAT_ID = 'Hi , Doing the same with chat ID'

def send_telegram_alert(message):
    # Arnav's message - Send a message via Telegram bot
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.post(url, data=payload)

# Task 1: Simulate the main processing logic
def process_data():
    try:
        # Arnav's message - Simulating processing time with random sleep
        time.sleep(random.uniform(5, 60))  # Simulating processing time
        if random.random() < 0.1:  # 10% chance of error
            return None
        # Arnav's message - Simulating successful data processing
        return random.randint(1000, 10000)  # Simulating processed data
    except Exception:
        return None

# Task 1: Monitor the script execution
def monitor_script():
    # Arnav's message - Record the start time of the script
    start_time = time.time()

    # Arnav's message - Run the main processing logic
    processed_data = process_data()
    if processed_data is None:
        print("An error occurred during data processing.")
    else:
        print(f"Processed data: {processed_data}")

    # Arnav's message - Record the end time and calculate the execution time
    end_time = time.time()
    execution_time = end_time - start_time
    script_execution_time.set(execution_time)

    # Arnav's message - Get the memory usage in MB
    memory_usage = psutil.Process().memory_info().rss / (1024 ** 2)
    script_memory_usage.set(memory_usage)

    print(f'Script execution time: {execution_time:.2f} seconds')
    print(f'Script memory usage: {memory_usage:.2f} MB')

    # Arnav's message - Increment the error count if an error occurred
    if processed_data is None:
        script_error_count.inc()

# Task 2: Set up alerts to be triggered for performance issues
# Arnav's message - Set the thresholds for alerts
if __name__ == '__main__':
    execution_time_threshold = 60  # seconds
    memory_usage_threshold = 500  # MB
    error_rate_threshold = 3  # errors per execution

    while True:
        monitor_script()

        # Arnav's message - Check if the execution time exceeded the threshold
        execution_time = script_execution_time.get()
        if execution_time > execution_time_threshold:
            # Arnav's message - Send an alert for high execution time
            message = f'Alert: Script execution time exceeded the threshold of {execution_time_threshold} seconds!'
            print(message)
            send_telegram_alert(message)

        # Arnav's message - Check if the memory usage exceeded the threshold
        memory_usage = script_memory_usage.get()
        if memory_usage > memory_usage_threshold:
            # Arnav's message - Send an alert for high memory usage
            message = f'Alert: Script memory usage exceeded the threshold of {memory_usage_threshold} MB!'
            print(message)
            send_telegram_alert(message)

        # Arnav's message - Check if the error rate exceeded the threshold
        error_count = script_error_count.value
        if error_count > error_rate_threshold:
            # Arnav's message - Send an alert for high error rate
            message = f'Alert: Script error rate exceeded the threshold of {error_rate_threshold} errors per execution!'
            print(message)
            send_telegram_alert(message)
