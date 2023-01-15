CREATE MATERIALIZED VIEW IF NOT EXISTS kafka.queue_kafka_consumer
            TO kafka.queue_kafka
AS SELECT *
   FROM kafka.queue_kafka_from_topic;