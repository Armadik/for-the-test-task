CREATE LIVE VIEW IF NOT EXISTS kafka.queue_alerts WITH REFRESH 0001 AS SELECT
    timestamp,
    sum(ask_01 + bid_01)/2 result
FROM  kafka.queue_kafka GROUP BY timestamp;