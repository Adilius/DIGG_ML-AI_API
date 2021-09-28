import jsonpickle
import hashlib

def get_checksum(data: dict):
    serialized_dct = jsonpickle.encode(data)
    checksum = hashlib.sha512(serialized_dct.encode('utf-8')).hexdigest()
    return checksum