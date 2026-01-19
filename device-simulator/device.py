import time
import random
import os
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

device_id = os.getenv("DEVICE_ID", "device-001")

exporter = OTLPMetricExporter(
    endpoint="http://localhost:4317",
    insecure=True
)

reader = PeriodicExportingMetricReader(exporter)
metrics.set_meter_provider(MeterProvider(metric_readers=[reader]))

meter = metrics.get_meter("device-monitor")

meter.create_observable_gauge(
    "device_heartbeat",
    callbacks=[lambda options: [(1, {"device_id": device_id})]]
)

meter.create_observable_gauge(
    "battery_level_percent",
    callbacks=[lambda options: [(random.randint(10, 100), {"device_id": device_id})]]
)

print("Started device:", device_id)

while True:
    time.sleep(30)