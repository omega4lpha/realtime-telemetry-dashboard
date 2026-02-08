# Real-Time System Metrics Dashboard with Grafana & InfluxDB

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![InfluxDB](https://img.shields.io/badge/InfluxDB-v2-blueviolet?style=for-the-badge&logo=influxdb)
![Grafana](https://img.shields.io/badge/Grafana-v10-orange?style=for-the-badge&logo=grafana)

A high-performance data visualization project that simulates real-time server telemetry. This system generates random system and business metrics using **Python**, stores them in **InfluxDB (v2)**, and visualizes them in a dynamic **Grafana** dashboard with sub-second latency updates.

## Key Features

- **Real-Time Data Generation**: Python script acts as a telemetry agent, pushing data every 500ms.
- **Time-Series Storage**: Utilizes InfluxDB for efficient storage of high-frequency metric data.
- **Dynamic Visualization**: Grafana dashboard with gauges, time-series graphs, and stat panels.
- **Docker-Less Architecture**: Optimized for environments where containerization is not available (runs natively on Windows/Linux).
- **Secure Configuration**: Uses environment variables (`.env`) for credential management.

## Architecture

1.  **Data Source**: `data_generator.py` simulates a server sending CPU, Memory, Network, and Business metrics (Users/Transactions).
2.  **Storage**: InfluxDB v2 receives data via the HTTP API using the Line Protocol.
3.  **Visualization**: Grafana queries InfluxDB using the **Flux** query language to display real-time insights.

## Prerequisites

- **Python 3.8+**
- **InfluxDB v2.x** (OSS Version)
- **Grafana v10.x**

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/grafana-realtime-metrics.git
cd grafana-realtime-metrics
```

### 2. Configure Environment
Create a `.env` file in the root directory based on `.env.example`:

```bash
cp .env.example .env
```

Edit `.env` and add your InfluxDB credentials (URL, Token, Org, Bucket).

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup InfluxDB & Grafana
1.  **Start InfluxDB**: Run `influxd` (ensure it's running on `localhost:8086`).
2.  **Start Grafana**: Run `grafana-server` (accessible at `localhost:3000`).
3.  **Import Dashboard**:
    - Open Grafana (`http://localhost:3000`).
    - Go to **Dashboards** -> **New** -> **Import**.
    - Upload `dashboard.json`.
    - Select your InfluxDB datasource when prompted.

## Usage

Run the data generator to start sending metrics:

```bash
python data_generator.py
```

You should see output like:
```text
Connected to InfluxDB at http://localhost:8086
Generating real-time data... Press Ctrl+C to stop.
Sent metrics: CPU=45.2%, Users=512, errors=0.5
Sent metrics: CPU=48.1%, Users=530, errors=1.2
...
```

Open your Grafana dashboard and enjoy the real-time visualization!

## Contact

Feel free to reach out if you have questions or want to discuss data engineering and visualization.

- **LinkedIn**: [Boris Herrera Flores](https://www.linkedin.com/in/boris-herrera-flores/)
- **GitHub**: [Omega4lpha](https://github.com/omega4lpha)
