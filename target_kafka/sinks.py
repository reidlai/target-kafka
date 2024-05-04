from singer_sdk.sinks import BatchSink
from kafka import KafkaProducer
from typing import List
import json

class kafkaSink(BatchSink):
    """kafka target sink class."""
    def __init__(self, target, stream_name, schema, key_properties):
        
        super().__init__(target=target, stream_name=stream_name, schema=schema, key_properties=key_properties)
        
        producer_config = {}
        
        # acks
        acks = self.config.get("acks", 1)
        if acks:
            producer_config["acks"] = acks
        
        # api_version
        api_version = self.config.get("api_version", None)
        if api_version:
            producer_config["api_version"] = tuple(map(int, api_version.split('.')))
            
        # api_version_auto_timeout_ms
        api_version_auto_timeout_ms = self.config.get("api_version_auto_timeout_ms", None)
        if api_version_auto_timeout_ms:
            producer_config["api_version_auto_timeout_ms"] = api_version_auto_timeout_ms
        
        # batch_size
        batch_size = self.config.get("batch_size", None)
        if batch_size:
            producer_config["batch_size"] = int(batch_size) 

        # bootstrap_servers
        bootstrap_servers = self.config.get("bootstrap_servers", None)
        if bootstrap_servers:
            if isinstance(bootstrap_servers, str):
                producer_config["bootstrap_servers"] = bootstrap_servers.split(',')   
            else:
                producer_config["bootstrap_servers"] = bootstrap_servers
        
        # buffer_memory
        buffer_memory = self.config.get("buffer_memory", None)
        if buffer_memory:
            producer_config["buffer_memory"] = buffer_memory
        
        # client_id
        client_id = self.config.get("client_id", None)
        if client_id:
            producer_config["client_id"] = client_id
            
        # compression_type
        compression_type = self.config.get("compression_type", None)
        if compression_type:
            producer_config["compression_type"] = compression_type
        
        # connections_max_idle_ms
        connections_max_idle_ms = self.config.get("connections_max_idle_ms", None)
        if connections_max_idle_ms:
            producer_config["connections_max_idle_ms"] = connections_max_idle_ms
            
        # linger_ms
        linger_ms = self.config.get("linger_ms", None)
        if linger_ms:
            producer_config["linger_ms"] = linger_ms
            
        # max_block_ms
        max_block_ms = self.config.get("max_block_ms", None)
        if max_block_ms:
            producer_config["max_block_ms"] = max_block_ms
            
        # max_in_flight_requests_per_connection
        max_in_flight_requests_per_connection = self.config.get("max_in_flight_requests_per_connection", None)
        if max_in_flight_requests_per_connection:
            producer_config["max_in_flight_requests_per_connection"] = max_in_flight_requests_per_connection
        
        # max_request_size
        max_request_size = self.config.get("max_request_size", None)
        if max_request_size:
            producer_config["max_request_size"] = max_request_size
        
        # metadata_max_age_ms
        metadata_max_age_ms = self.config.get("metadata_max_age_ms", None)
        if metadata_max_age_ms:
            producer_config["metadata_max_age_ms"] = metadata_max_age_ms
        
        # metrics_num_samples
        metrics_num_samples = self.config.get("metrics_num_samples", None)
        if metrics_num_samples:
            producer_config["metrics_num_samples"] = metrics_num_samples
        
        # metrics_reporters
        metrics_reporters = self.config.get("metrics_reporters", None)
        if metrics_reporters:
            producer_config["metrics_reporters"] = metrics_reporters
        
        # metrics_sample_window_ms
        metrrics_sample_window_ms = self.config.get("metrics_sample_window_ms", None)
        if metrrics_sample_window_ms:
            producer_config["metrics_sample_window_ms"] = metrrics_sample_window_ms
        
        # receive_buffer_bytes
        receive_buffer_bytes = self.config.get("receive_buffer_bytes", None)
        if receive_buffer_bytes:
            producer_config["receive_buffer_bytes"] = receive_buffer_bytes
        
        # reconnect_backoff_ms
        reconnect_backoff_ms = self.config.get("reconnect_backoff_ms", None)
        if reconnect_backoff_ms:
            producer_config["reconnect_backoff_ms"] = reconnect_backoff_ms
        
        # reconnect_backoff_max_ms
        reconnect_backoff_ms = self.config.get("reconnect_backoff_max_ms", None)
        if reconnect_backoff_ms:
            producer_config["reconnect_backoff_max_ms"] = reconnect_backoff_ms
        
        # request_timeout_ms
        request_timeout_ms = self.config.get("request_timeout_ms", None)
        if request_timeout_ms:
            producer_config["request_timeout_ms"] = request_timeout_ms
        
        # retries
        retries = self.config.get("retries", None)
        if retries:
            producer_config["retries"] = retries
            
        # retry_backoff_ms
        retry_backoff_ms = self.config.get("retry_backoff_ms", None)
        if retry_backoff_ms:
            producer_config["retry_backoff_ms"] = retry_backoff_ms
        
        # sasl_kerberos_domain_name
        sasl_kerberos_domain_name = self.config.get("sasl_kerberos_domain_name", None)
        if sasl_kerberos_domain_name:
            producer_config["sasl_kerberos_domain_name"] = sasl_kerberos_domain_name
        
        # sasl_kerberos_service_name
        sasl_kerberos_domain_name = self.config.get("sasl_kerberos_service_name", None)
        if sasl_kerberos_domain_name:
            producer_config["sasl_kerberos_service_name"] = sasl_kerberos_domain_name
        
        # sasl_oauth_token_provider
        sasl_oauth_token_provider = self.config.get("sasl_oauth_token_provider", None)
        if sasl_oauth_token_provider:
            producer_config["sasl_oauth_token_provider"] = sasl_oauth_token_provider
        
        # sasl_mechanism
        sasl_mechanism = self.config.get("sasl_mechanism", None)
        if sasl_mechanism:
            producer_config["sasl_mechanism"] = sasl_mechanism
        
        # sasl_plain_password
        sasl_plain_password = self.config.get("sasl_plain_password", None)
        if sasl_plain_password:
            producer_config["sasl_plain_password"] = sasl_plain_password
        
        # sasl_plain_username
        sasl_plain_username = self.config.get("sasl_plain_username", None)
        if sasl_plain_username:
            producer_config["sasl_plain_username"] = sasl_plain_username
        
        # selector
        selector = self.config.get("selector", None)
        if selector:
            producer_config["selector"] = selector
        
        # send_buffer_bytes
        send_buffer_bytes = self.config.get("send_buffer_bytes", None)
        if send_buffer_bytes:
            producer_config["send_buffer_bytes"] = send_buffer_bytes
        
        # security_protocol
        security_protocol = self.config.get("security_protocol", None)
        if security_protocol:
            producer_config["security_protocol"] = security_protocol
        
        # socket_options
        socker_options = self.config.get("socket_options", None)
        if socker_options:
            producer_config["socket_options"] = socker_options
        
        # ssl_cafile
        ssl_cafile = self.config.get("ssl_cafile", None)
        if ssl_cafile:
            producer_config["ssl_cafile"] = ssl_cafile
        
        # ssl_certfile
        ssl_certfile = self.config.get("ssl_certfile", None)
        if ssl_certfile:
            producer_config["ssl_certfile"] = ssl_certfile
        
        # ssl_ciphers
        ssl_ciphers = self.config.get("ssl_ciphers", None)
        if ssl_ciphers:
            producer_config["ssl_ciphers"] = ssl_ciphers
        
        # ssl_context
        ssl_context = self.config.get("ssl_context", None)
        if ssl_context:
            producer_config["ssl_context"] = ssl_context
        
        # ssl_crlfile
        ssl_crlfile = self.config.get("ssl_crlfile", None)
        if ssl_crlfile:
            producer_config["ssl_crlfile"] = ssl_crlfile
        
        # ssl_keyfile
        ssl_keyfile = self.config.get("ssl_keyfile", None)
        if ssl_keyfile:
            producer_config["ssl_keyfile"] = ssl_keyfile
        
        # ssl_password
        ssl_password = self.config.get("ssl_password", None)
        if ssl_password:
            producer_config["ssl_password"] = ssl_password

        self._producer = KafkaProducer(
            **producer_config
        )

    def start_batch(self, context: dict) -> None:
        """Start a batch.

        Developers may optionally add additional markers to the `context` dict,
        which is unique to this batch.

        Args:
            context: Stream partition or context dictionary.
        """
        # Sample:
        # ------
        # batch_key = context["batch_id"]
        # context["file_path"] = f"{batch_key}.csv"
        print("Starting batch")
        print(f"Context: {context}")
            
    def process_batch(self, context: dict) -> None:
        
        records = context.get("records", [])
        for record in records:
            value = json.dumps(record).encode('utf-8')
            future = self._producer.send(self.stream_name, value=value)
            # future.add_callback(self.on_success)
            # future.add_errback(self.on_error)
        self._producer.flush()

    # def on_success(self, record_metadata):
    #     print(record_metadata)
        
    # def on_error(self, exception):
    #     print(exception)
        
    def close(self):
        self._producer.close()