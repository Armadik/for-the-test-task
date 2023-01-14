-- create table
CREATE TABLE IF NOT EXISTS kafka(
                                    timestamp UInt64,
                                    bid01 FLOAT,
                                    ask01 FLOAT
) ENGINE = Kafka('kafka', 'ch-topic', 'group1', 'JSONEachRow');