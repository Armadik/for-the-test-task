Test piplines
========

## Install

### Clone this repository on your Docker host, cd into test directory and run compose up:

```
https://github.com/Armadik/for-the-test-task
cd for-the-test-task
docker-compose up -d
```

### Change .env:
```
ENV=home

APP_POLLING_INTERVAL=0.001
APP_RANGE_DATA=51
APP_KAFKA_HOST=kafka:9092
APP_KAFKA_TOPIC=ch-topic

#CH
CLICKHOUSE_DB=kafka
CLICKHOUSE_USER=kafka
CLICKHOUSE_PASSWORD=kafka

#Grafana
GRAFANA_ADMIN_USER=grafana
GRAFANA_ADMIN__PASSWORD=grafana
```


## Prerequisites:


## Access Grafana

```
http://localhost:3000/
```