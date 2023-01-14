# -*- coding: utf-8 -*-
import os
import time
import random
import json
#import kafka-python

from utils import get_logger

log = get_logger(__name__)


def ranger_data(prefix, range_int=int(51)):
    d = {}
    for i in range(1, range_int):
        p = prefix + f"{i:02d}"
        i = random.randrange(0, 10 * i)
        d[p] = i
        # print(prefix + f"{i:02d}", random.randrange(0, 10 * i), sep=":")
    return d


def get_data(range_data):
    print("timestamp: " + str(time.time()))
    bid = ranger_data("bid_", range_data)
    ask = ranger_data("ask_", range_data)
    data = {
        "bid": sum(bid.values())/len(bid.values()),
        "ask": sum(ask.values())/len(ask.values())
    }
    print(bid)
    print(ask)
    print("stats:", json.dumps(data))


def main():
    """Main entry point"""
    polling_interval = int(os.getenv("POLLING_INTERVAL", 3))
    range_data = int(os.getenv("RANGE_DATA", 10))

    while True:
        time.sleep(polling_interval)
        get_data(range_data)


if __name__ == "__main__":
    log.info("Start test app")
    main()
