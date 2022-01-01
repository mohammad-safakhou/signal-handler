import json

from kafka import KafkaConsumer, KafkaProducer

from signals.strategy import strategy_calculator

producer = KafkaProducer()


def indicator_handler():
    consumer = KafkaConsumer('candles')
    for msg in consumer:
        data_list = json.loads(msg.value.decode('utf-8'))

        signal = strategy_calculator(data_list)
        producer.send('signals', str.encode(signal))
