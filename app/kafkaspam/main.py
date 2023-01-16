# -*- coding: utf-8 -*-
import os
import time
import random
from json import dumps
from kafka import KafkaProducer
from kafka.errors import KafkaError
from utils import get_logger

log = get_logger(__name__)


def send_kafka(data, kafka_topic, kafka_host):
    """Send kafka"""
    log.info("Creating kafka producer: " + kafka_host)

    try:
        producer = KafkaProducer(bootstrap_servers=[kafka_host],
                                 value_serializer=lambda x:
                                 dumps(x).encode('utf-8'))
        log.info("Kafka send topic: " + kafka_topic)
        producer.send(kafka_topic, value=data)
    except KafkaError as exc:
        log.info("kafka producer - Exception during connecting to broker - {}".format(exc))


def ranger_data(prefix, range_int=int(51)):
    """Generate data"""
    d = {}
    for i in range(1, range_int):
        p = prefix + f"{i:02d}"
        i = random.randrange(0, 10 * i)
        d[p] = float(i)
    return d


def get_data(range_data, kafka_topic, kafka_host):
    """Create dict"""
    u_time = {'timestamp': int(time.time())}
    bid = ranger_data("bid_", range_data)
    ask = ranger_data("ask_", range_data)
    stats_data = {
        "bid": int(sum(bid.values()) / len(bid.values())),
        "ask": int(sum(ask.values()) / len(ask.values()))
    }
    stats = {'stats': stats_data}
    data = {**u_time, **bid, **ask, **stats}
    send_kafka(data, kafka_topic, kafka_host)


def main():
    """Main entry point"""
    polling_interval = float(os.getenv("APP_POLLING_INTERVAL", 0.001))
    range_data = int(os.getenv("APP_RANGE_DATA", 10))
    kafka_host = os.getenv("APP_KAFKA_HOST", "localhost:29092")
    kafka_topic = os.getenv("APP_KAFKA_TOPIC", "my-topic")
    log.info("Star interval: " + str(polling_interval) + 'c')

    while True:
        time.sleep(polling_interval)
        get_data(range_data, kafka_topic, kafka_host)


if __name__ == "__main__":
    main()
