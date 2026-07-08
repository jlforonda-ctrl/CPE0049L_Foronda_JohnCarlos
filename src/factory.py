from abc import ABC, abstractmethod

class ProcessingService(ABC):
    @abstractmethod
    def process(self, data):
        pass

class EncryptionService(ProcessingService):
    def process(self, data):
        print("Encrypting...")

class CompressionService(ProcessingService):
    def process(self, data):
        print("Compressing...")

class ProcessingFactory:
    @staticmethod
    def create(service_type):
        service_type = service_type.upper()
        if service_type == "ENCRYPT":
            return EncryptionService()
        elif service_type == "COMPRESS":
            return CompressionService()
        else:
            raise ValueError("Unknown Service")