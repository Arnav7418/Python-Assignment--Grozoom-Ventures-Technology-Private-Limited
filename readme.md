
# **Python Script Monitoring and Alerting**

This Python script monitors its own execution and sends alerts when performance thresholds are exceeded. It utilizes Prometheus for monitoring key metrics like execution time, memory usage, and error count. Additionally, it sends alerts via a Telegram bot when certain performance thresholds are breached.

## **Features**

- **Execution Time Monitoring**: Tracks the time taken by the script to execute.
- **Memory Usage Monitoring**: Records the memory usage of the script in MB.
- **Error Counting**: Counts the number of errors encountered during execution.
- **Prometheus Metrics**: Exposes the metrics via an HTTP server, allowing Prometheus to scrape them.
- **Alerting via Telegram**: Sends alerts to a configured Telegram chat when performance issues are detected.

## **Setup and Usage**

### **1. Install Dependencies**

Ensure you have the required Python packages installed:

```bash
pip install prometheus_client psutil requests
