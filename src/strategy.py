from abc import ABC, abstractmethod

class ProcessingStrategy(ABC):
    @abstractmethod
    def process(self, data):
        pass

class EncryptionStrategy(ProcessingStrategy):
    def process(self, data):
        return [int(value) ^ 0x4F for value in data]

class CompressionStrategy(ProcessingStrategy):
    def process(self, data):
        return [round(value * 0.85, 2) for value in data]

class DataProcessor:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        return self.strategy.process(data)