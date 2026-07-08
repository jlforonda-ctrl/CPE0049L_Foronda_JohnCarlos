from factory import ProcessingFactory
from strategy import EncryptionStrategy, CompressionStrategy, DataProcessor

def main():
    data_stream = [78, 82, 91, 65, 40, 99, 88]

    service = ProcessingFactory.create("ENCRYPT")
    service.process(data_stream)

    service = ProcessingFactory.create("COMPRESS")
    service.process(data_stream)

    processor = DataProcessor()

    processor.set_strategy(EncryptionStrategy())
    encrypted = processor.execute(data_stream)
    print("Encrypted Output:", encrypted)

    processor.set_strategy(CompressionStrategy())
    compressed = processor.execute(data_stream)
    print("Compressed Output:", compressed)

if __name__ == "__main__":
    main()