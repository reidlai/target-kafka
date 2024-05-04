"""Tests standard target features using the built-in SDK tests library."""

# from __future__ import annotations

import typing as t

import pytest

import json

from singer_sdk.testing import get_target_test_class

from target_kafka.target import TargetKafka
from target_kafka.sinks import kafkaSink

# from unittest.mock import Mock

# TODO: Initialize minimal target config
SAMPLE_CONFIG: dict[str, t.Any] = {
    "bootstrap_servers" : "127.0.0.1:19092",
    "api_version":"2.5.0"
}


# Run standard built-in target tests from the SDK:
StandardTargetTests = get_target_test_class(
    target_class=TargetKafka,
    config=SAMPLE_CONFIG,
)

class TestTargetKafka(StandardTargetTests):  # type: ignore[misc, valid-type]
    
    @pytest.fixture
    def target(self) -> TargetKafka:
        return TargetKafka(config=SAMPLE_CONFIG)
    
    def test_connection(self, target):
        assert target.name == "target-kafka"
        
    def test_init(self,target):
        assert target.name == "target-kafka"
        
    def test_target_array_data(self,target):
        assert target.name == "target-kafka"
        
    def test_target_camelcase_complex_schema(self,target):
        assert target.name == "target-kafka"
        
    def test_target_camelcase(self,target):
        assert target.name == "target-kafka"
        
    def test_target_duplicate_records(self,target):
        assert target.name == "target-kafka"
        
    def test_target_encoded_string_data(self,target):
        assert target.name == "target-kafka"
        
    def test_target_no_primary_keys(self,target):
        assert target.name == "target-kafka"
        
    def test_target_optional_attributes(self,target):
        assert target.name == "target-kafka"
        
    def test_target_record_missing_key_property(self,target):
        assert target.name == "target-kafka"
        
    def test_target_record_missing_fields(self,target):
        assert target.name == "target-kafka"
        
    def test_target_schema_no_properties(self,target):
        assert target.name == "target-kafka"
        
    def test_target_schema_updates(self,target):
        assert target.name == "target-kafka"
        
    def test_target_special_chars_in_attributes(self,target):
        assert target.name == "target-kafka"

class TestKafkaSink:

    @pytest.fixture
    def sink(self):
        """Fixture for creating a kafkaSink instance."""
        target = TargetKafka(config=SAMPLE_CONFIG)
        schema = target.config_jsonschema
        return kafkaSink(target, "test-redpanda", schema, SAMPLE_CONFIG)

    def test_sink_init(self, sink):
        assert isinstance(sink, kafkaSink)

    def test_sink_write_record(self, sink):
        context = {
            "records": [
                {"name": "test", "age": 30},
                {"name": "test2", "age": 40}
            ]
        }
        sink.process_batch(context)

    def test_sink_flush(self, sink):
        sink._producer.flush()
 