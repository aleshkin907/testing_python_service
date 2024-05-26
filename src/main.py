from config.config import settings
from consumer.kafka_consumer import KafkaConsumer
from consumer.kafka_reader import KafkaSolutionReader
from db.db import session
from repositories.solution_repository import Repository
from tester.tester import Tester
from config.config import consumer_conf


if __name__ == "__main__":
    repository = Repository(session)
    tester = Tester(repository)
    kafka_solution_reader = KafkaSolutionReader(consumer_conf, [settings.kafka.topic])
    consumer = KafkaConsumer(kafka_solution_reader, tester)
    consumer.read()
