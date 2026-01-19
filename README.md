# device-detection

To prioritize fast detection of device downtime and critical battery levels for 1-1000 mobile devices, I have designed the observability platform around signal-first monitoring rather than full telemetry.
Key solutions for quick detection used are:
Device availability
Critical battery health
Technologies used:
OpenTelemetry – device metric collection
Prometheus – metrics storage & alerting
Grafana – visualization & dashboards
Docker Compose – local deployment
Git & GitHub – version control & deployment source
Mac OS

Repository Structure

device-detection/
├── docker-compose.yml          # Grafana, Prometheus, OTEL
├── otel-collector/
│   └── otel-collector.yaml     # Telemetry pipeline
├── prometheus/
│   └── prometheus.yml          # Scraping config
├── alerts/
│   └── device-alerts.yml       # Alert rules
├── device-simulator/
│   └── device.py               # Simulated device
├── README.md
└── .gitignore

Architecture Diagram:



POC starts here:
Step 1:
Clone this repository to local Window/Linux Laptop or Mac : https://github.com/dsaninfoserv/device-detection.git

Step 2: 
Get into device-detection folder/directory and run: docker compose up -d

Validate docker container running status by running command: docker ps -a

Step 3:
Run this script to setup the Opentelemetry-sdk and exporter-otlp:
pip3 install opentelemetry-sdk opentelemetry-exporter-otlp 

Step 4:
Run this script on same device for testing : 
DEVICE_ID=device-001 python3 device-simulator/device.py

Step 5:
Validate prometheus url on browser: http://localhost:9090
device_heartbeat
battery_level_percent

Step 6:
Visualize the graphs and alerts on Grafana url: http://localhost:3000
User : admin / Pwd: admin (don’t reset password)
Once logged in click on 
Connections tab → select Datasource → select Prometheus → Name : prometheus-device-detection → connection url :  http://localhost:9090 → scroll to bottom of the page and press Save & test button → then press Explore view link to access the dashboard → select the metrics (up or alerts) press run you will data on the dashboard
