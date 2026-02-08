import time
import random
import os
from datetime import datetime
from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Load environment variables from .env file
load_dotenv()

# Configuration
INFLUXDB_URL = os.getenv("INFLUXDB_URL", "http://localhost:8086")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUXDB_ORG = os.getenv("INFLUXDB_ORG", "my-org")
INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET", "my-bucket")

if not INFLUXDB_TOKEN:
    raise ValueError("INFLUXDB_TOKEN not found in environment variables. Please check your .env file.")

def generate_data():
    client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
    write_api = client.write_api(write_options=SYNCHRONOUS)

    print(f"Connected to InfluxDB at {INFLUXDB_URL}")
    print("Generating real-time data... Press Ctrl+C to stop.")

    try:
        while True:
            points = []
            timestamp = datetime.utcnow()

            # 1. System Metrics (simulated)
            cpu_usage = random.uniform(10.0, 90.0)
            mem_usage = random.uniform(20.0, 85.0)
            disk_io = random.uniform(0.1, 5.0)  # MB/s
            net_in = random.uniform(0.5, 100.0) # Mbps
            net_out = random.uniform(0.5, 50.0) # Mbps
            temperature = 35.0 + (cpu_usage * 0.4) + random.uniform(-2, 2)
            battery_level = max(0, 100 - (time.time() % 3600) / 36) # Slowly depleting

            points.append(Point("system_stats")
                          .tag("host", "server-01")
                          .field("cpu_usage", cpu_usage)
                          .field("mem_usage", mem_usage)
                          .field("temperature", temperature)
                          .field("battery_level", battery_level)
                          .time(timestamp, WritePrecision.NS))

            points.append(Point("network_stats")
                          .tag("interface", "eth0")
                          .field("disk_io", disk_io)
                          .field("net_in", net_in)
                          .field("net_out", net_out)
                          .time(timestamp, WritePrecision.NS))

            # 2. Business Metrics (simulated)
            active_users = int(random.gauss(500, 50))
            # Ensure values are float to avoid InfluxDB type conflict if they hit 0
            transactions_sec = float(max(0, active_users * 0.1 + random.uniform(-10, 10)))
            errors_sec = float(max(0, transactions_sec * 0.02 + random.uniform(-1, 2)))
            
            points.append(Point("business_stats")
                          .tag("region", "us-east")
                          .field("active_users", active_users)
                          .field("transactions_sec", transactions_sec)
                          .field("errors_sec", errors_sec)
                          .time(timestamp, WritePrecision.NS))

            write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=points)
            print(f"Sent metrics: CPU={cpu_usage:.1f}%, Users={active_users}, errors={errors_sec:.1f}")

            time.sleep(0.5)  # Real-time update frequency (500ms)

    except KeyboardInterrupt:
        print("\nStopping script.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    generate_data()
