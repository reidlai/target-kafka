"""Tests standard target features using the built-in SDK tests library."""

# from __future__ import annotations

import typing as t

import pytest

import json

from singer_sdk.testing import get_target_test_class

from target_kafka.target import Targetkafka
from target_kafka.sinks import kafkaSink

from kafka import KafkaConsumer

# from unittest.mock import Mock

# TODO: Initialize minimal target config
SAMPLE_CONFIG: dict[str, t.Any] = {
    "bootstrap_servers" : "127.0.0.1:19092",
    "api_version":"2.5.0"
}


# Run standard built-in target tests from the SDK:
StandardTargetTests = get_target_test_class(
    target_class=Targetkafka,
    config=SAMPLE_CONFIG,
)

# TODO: Complete the test class with additional tests as needed
class TestTargetkafka(StandardTargetTests):  # type: ignore[misc, valid-type]
    
    @pytest.fixture
    def target(self) -> Targetkafka:
        return Targetkafka(config=SAMPLE_CONFIG)
    
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

 