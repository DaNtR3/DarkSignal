# OpenTelemetry imports for metrics
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus import PrometheusMetricReader


# Setup metrics
reader = PrometheusMetricReader()
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)

def createCustomMetric(metric_name, metric_description):
    # Create a counter metric
    metric_name = meter.create_counter(
        name=metric_name,
        description=metric_description,
    )
    return metric_name