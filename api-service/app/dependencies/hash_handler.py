import jsonpickle
import hashlib

def getHash(data: dict):
    serialized_dct = jsonpickle.encode(data)
    check_sum = hashlib.sha512(serialized_dct.encode('utf-8')).hexdigest()
    return check_sum