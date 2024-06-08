"""kafka target class."""

from __future__ import annotations

from singer_sdk import typing as th
from singer_sdk.target_base import Target
from singer_sdk.helpers.capabilities import TargetCapabilities

from target_kafka.sinks import (
    kafkaSink,
)

class Targetkafka(Target):
    """Sample target for kafka."""

    name = "target-kafka"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "acks",
            th.IntegerType,
            description="used to convert user-supplied keys to bytes If not None, called as f(key), should return bytes. Default: None.",
            default=1,
        ),
        th.Property(
            "api_version",
            th.StringType,
            description="Kafka broker version. Default: None.",
            default=None,
        ),
        th.Property(
            "api_version_auto_timeout_ms",
            th.IntegerType,
            description="The timeout used to detect broker version. Default: 2000.",
            default=2000,
        ),
        th.Property(
            "batch_size",
            th.IntegerType,
            description="The producer will attempt to batch records together into fewer requests whenever multiple records are being sent to the same partition. Default: 16384.",
            default=16384,
        ),
        th.Property(
            "bootstrap_servers",
            th.StringType,
            description="host[:port] string (or list of comma separated host[:port] strings) that the consumer should contact to bootstrap initial cluster metadata.",
            required=True,
            default="127.0.0.1:9092",
        ),
        th.Property(
            "buffer_memory",
            th.IntegerType,
            description="The total bytes of memory the producer can use to buffer records waiting to be sent to the server. Default: 33554432.",
            default=33554432,
        ),
        th.Property(
            "client_id",
            th.StringType,
            description="a name for this client. This string is passed in each request to servers and can be used to identify specific server-side log entries that correspond to this client. Default: ‘kafka-python-producer-#’ (appended with a unique number per instance)",
            default="kafka-python-producer-#",
        ),
        th.Property(
            "compression_type",
            th.StringType,
            description="If not None, called as f(key), should return bytes. Default: None.",
            default=None,
        ),
        th.Property(
            "connection_max_idle_ms",
            th.IntegerType,
            description="Close idle connections after the number of milliseconds specified by this config. Default: 540000.",
            default=540000,
        ),
        th.Property(
            "linger_ms",
            th.IntegerType,
            description="The producer groups together any records that arrive in between request transmissions into a single batched request. Default: 0.",
            default=0,
        ),
        th.Property(
            "max_block_ms",
            th.IntegerType,
            description="The configuration controls how long the producer will wait for the response of a request. Default: 60000.",
            default=60000,
        ),
        th.Property(
            "max_in_flight_requests_per_connection",
            th.IntegerType,
            description="The maximum number of unacknowledged requests the client will send on a single connection before blocking. Default: 5.",
            default=5,
        ),
        th.Property(
            "max_request_size",
            th.IntegerType,
            description="The maximum size of a request in bytes. Default: 1048576.",
            default=1048576,
        ),
        th.Property(
            "metadata_max_age_ms",
            th.IntegerType,
            description="The period of time in milliseconds after which we force a refresh of metadata even if we haven’t seen any partition leadership changes to proactively discover any new brokers or partitions. Default: 300000.",
            default=300000,
        ),
        th.Property(
            "metrics_num_samples",
            th.IntegerType,
            description="The number of samples maintained to compute metrics. Default: 2.",
            default=2,
        ),
        th.Property(
            "metrics_reporters",
            th.StringType,
            description="A list of classes to use as metrics reporters. Default: None.",
            default="",
        ),
        th.Property(
            "metrics_sample_window_ms",
            th.IntegerType,
            description="The maximum time in milliseconds between metric samples. Default: 30000.",
            default=30000,
        ),
        th.Property(
            "receive_buffer_bytes",
            th.IntegerType,
            description="The size of the TCP receive buffer (SO_RCVBUF) to use when reading data. Default: None.",
            default=None,
        ),
        th.Property(
            "reconnect_backoff_ms",
            th.IntegerType,
            description="The amount of time to wait before attempting to reconnect to a given host. Default: 50.",
            default=50,
        ),
        th.Property(
            "reconnect_backoff_max_ms",
            th.IntegerType,
            description="The maximum amount of time in milliseconds to wait when reconnecting to a broker that has repeatedly failed to connect. Default: 1000.",
            default=1000,
        ),
        th.Property(
            "request_timeout_ms",
            th.IntegerType,
            description="The configuration controls the maximum amount of time the client will wait for the response of a request. Default: 30000.",
            default=30000,
        ),
        th.Property(
            "retries",
            th.IntegerType,
            description="acknowledgment of requests. Default: 0.",
            default=0,
        ),
        th.Property(
            "retry_backoff_ms",
            th.IntegerType,
            description="The amount of time to wait before attempting to retry a failed request. Default: 100.",
            default=100,
        ),
        th.Property(
            "sasl_kerberos_domain_name",
            th.StringType,
            description="Kerberos domain name to use in GSSAPI sasl authentication. Default: None.",
            default=None,
        ),
        th.Property(
            "sasl_kerberos_service_name",
            th.StringType,
            description="Service name to include in GSSAPI sasl authentication. Default: None.",
            default=None,
        ),
        th.Property(
            "sasl_oauth_token_provider",
            th.StringType,
            description="Provider for OAuthBearer token. Default: None.",
            default=None,
        ),
        th.Property(
            "sasl_mechanism",
            th.StringType,
            description="SASL mechanism to use for authentication. Default: None.",
            default=None,
        ),
        th.Property(
            "sasl_plain_password",
            th.StringType,
            description="Password for sasl plain authentication. Default: None.",
            secret=True,
            default=None,
        ),
        th.Property(
            "sasl_plain_username",
            th.StringType,
            description="Username for sasl plain authentication. Default: None.",
            default=None,
        ),
        th.Property(
            "selector",
            th.StringType,
            description="The selector to use for the producer. Default: None.",
            default=None,
        ),
        th.Property(
            "send_buffer_bytes",
            th.IntegerType,
            description="The size of the TCP send buffer (SO_SNDBUF) to use when sending data. Default: None.",
            default=None,
        ),
        th.Property(
            "security_protocol",
            th.StringType,
            description="The security protocol used to communicate with brokers. Default: None.",
            default=None,
        ),
        th.Property(
            "socket_options",
            th.StringType,
            description="List of (int, int) tuples to use as arguments to setsockopt. Default: None.",
            default=None,
        ),
        th.Property(
            "ssl_cafile",
            th.StringType,
            description="The path to a file of concatenated CA certificates in PEM format. Default: None.",
            default=None,
        ),
        th.Property(
            "ssl_certfile",
            th.StringType,
            description="The path to a file containing the client certificate in PEM format. Default: None.",
            default=None,
        ),
        th.Property(
            "ssl_ciphers",
            th.StringType,
            description="The list of encryption suites allowed for SSL connections. Default: None.",
            default=None,
        ),
        th.Property(
            "ssl_context",
            th.StringType,
            description="A SSL context to use in requests. Default: None.",
            default=None,
        ),
        th.Property(
            "ssl_crlfile",
            th.StringType,
            description="The path to a file containing certificate revocation lists. Default: None.",
            default=None,
        ),
        th.Property(
            "ssl_keyfile",
            th.StringType,
            description="The path to a file containing the client private key in PEM format. Default: None.",
            default=None,
        ),
        th.Property(
            "ssl_password",
            th.StringType,
            description="The password for the client’s private key. Default: None.",
            secret=True,
            default=None,
        ),
    ).to_dict()

    default_sink_class = kafkaSink

if __name__ == "__main__":
    Targetkafka.cli()
