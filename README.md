Test piplines
========
Structure catalog
```
├── LICENSE.md
├── README.md
├── app
│   ├── Dockerfile
│   ├── kafkaspam
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── main.py
│   │   └── utils.py
│   ├── requirements.txt
│   ├── setup.cfg
│   └── setup.py
├── clickhouse
│   ├── config
│   │   └── allow_experimental_map_type.xml
│   └── initsql
│       ├── create_table_queue_kafka.sql
│       ├── create_table_queue_kafka_from_topic.sql
│       ├── create_view_queue_alerts.sql
│       └── create_view_queue_kafka_view.sql
├── docker-compose.yml
├── grafana
│   ├── alerting
│   │   └── clickhouse.yml
│   ├── dashboards
│   │   ├── clickhouse_kafka.json
│   │   └── dashboard.yml
│   └── datasources
│       └── clickhouse.yml
├── grafana_alert.png
└── grafana_dashboard.png
```

## Install

### Change .env:
```
ENV=home

#APP
APP_POLLING_INTERVAL=0.001
APP_RANGE_DATA=51
APP_KAFKA_HOST=kafka:9092
# change click_initdb/@.sql
APP_KAFKA_TOPIC=ch-topic

#KAFKA
KAFKA_VERSION=6.1.1
#CH
CLICKHOUSE_VERSION=21.8.14
CLICKHOUSE_DB=kafka
CLICKHOUSE_USER=kafka
CLICKHOUSE_PASSWORD=kafka

#Grafana
GRAFANA_VERSION=9.3.2
GRAFANA_ADMIN_USER=grafana
GRAFANA_ADMIN__PASSWORD=grafana
```


### Clone this repository on your Docker host, cd into test directory and run compose up:

```
git clone https://github.com/Armadik/for-the-test-task
cd for-the-test-task
docker-compose up -d
```

```bash
CONTAINER ID   IMAGE                              COMMAND                  CREATED         STATUS         PORTS                                        NAMES
af4be40fb726   armadik/app:home                   "python -m kafkaspam"    2 minutes ago   Up 2 minutes                                                kafkaspam
4cb177f1c1d7   grafana/grafana:9.3.2              "/run.sh"                3 minutes ago   Up 2 minutes   0.0.0.0:3000->3000/tcp                       grafana
4c6c667cec4a   confluentinc/cp-kafka:6.1.1        "/etc/confluent/dock…"   3 minutes ago   Up 2 minutes   9092/tcp, 0.0.0.0:29092->29092/tcp           kafka
d217d33438b0   yandex/clickhouse-server:21.8.14   "/entrypoint.sh"         3 minutes ago   Up 3 minutes   9000/tcp, 0.0.0.0:8123->8123/tcp, 9009/tcp   clickhouse_server
b817f7d12e48   confluentinc/cp-zookeeper:6.1.1    "/etc/confluent/dock…"   3 minutes ago   Up 3 minutes   2888/tcp, 0.0.0.0:2181->2181/tcp, 3888/tcp   zookeeper
```

## Access Grafana

Login 'GRAFANA_ADMIN_USER/GRAFANA_ADMIN__PASSWORD'(default grafana/grafana)

http://localhost:3000/
![img.png](grafana_dashboard.png)
# Create alert grafana


```sql
SELECT $__timeInterval(timestamp) as time, result FROM kafka.queue_alerts WHERE $__timeFilter(timestamp) AND   ( result > 9.9 ) GROUP BY result, time ORDER BY time ASC
```
![img.png](grafana_alert.png)
