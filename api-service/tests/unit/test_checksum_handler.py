import unittest
from unittest import mock
from app.dependencies import checksum_handler

def test_get_checksum(test_app):

    data = {
        "hello":"world"
    }

    checksum = checksum_handler.get_checksum(data)
    # This checksum should match
    assert checksum == "5990cf6959ffed7807680cbca66a23024196a11c765050a1178d40dacbd7f9368f9be01bc008015a7ac8898965bbb04d37279a95d54bbd1c049931d65ef2707b"
    # This checksum should not match
    assert checksum != "hello world"