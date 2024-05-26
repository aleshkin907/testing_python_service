from abc import ABC, abstractmethod
import json
from typing import List

from confluent_kafka import Consumer


class AbstractSolutionReader(ABC):
    @abstractmethod
    async def read_soluiton(self):
        raise NotImplementedError()
    
class KafkaSolutionReader(AbstractSolutionReader):
    def __init__(self, cfg: dict, topic: List[str]):
        self.consumer = Consumer(cfg)
        self.consumer.subscribe(topic)

    def read_soluiton(self):
        while True:
            msg = self.consumer.poll(1.0)

            if msg is None:
                continue

            yield json.loads(msg.value())
            