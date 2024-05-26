from consumer.kafka_reader import AbstractSolutionReader
from models.solution_model import SolutionSchema
from tester.tester import Tester


class KafkaConsumer:
    def __init__(self, reader: AbstractSolutionReader, tester: Tester):
        self.reader = reader
        self.tester = tester

    def read(self):
        for solution in self.reader.read_soluiton():
            solution_dto = SolutionSchema(**solution)
            self.tester.test_solution(solution_dto)
