import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from factory import ProcessingFactory, EncryptionService, CompressionService
from strategy import EncryptionStrategy, CompressionStrategy, DataProcessor
from auth import generate_token, verify_token
from main import main

def test_factory():
    enc = ProcessingFactory.create("ENCRYPT")
    assert isinstance(enc, EncryptionService)
    comp = ProcessingFactory.create("COMPRESS")
    assert isinstance(comp, CompressionService)
    with pytest.raises(ValueError):
        ProcessingFactory.create("INVALID")

def test_strategy():
    processor = DataProcessor()
    data = [78, 82]
    processor.set_strategy(EncryptionStrategy())
    assert processor.execute(data) == [78 ^ 0x4F, 82 ^ 0x4F]
    processor.set_strategy(CompressionStrategy())
    assert processor.execute(data) == [round(78 * 0.85, 2), round(82 * 0.85, 2)]

def test_auth():
    token = generate_token("exam_user")
    assert isinstance(token, str)
    assert verify_token(token) == "exam_user"
    assert verify_token("fake.token.here") == "Invalid token"

def test_main_execution():
    main()