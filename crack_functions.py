import hashlib

def hash_md5(password):
    return hashlib.md5((str(password)).encode('utf-8')).hexdigest()

def hash_sha1(password):
    return hashlib.sha1((str(password)).encode('utf-8')).hexdigest()

def hash_sha3_512(password):
    return hashlib.sha3_512((str(password)).encode('utf-8')).hexdigest()

def hash_sha3_256(password):
    return hashlib.sha3_256((str(password)).encode('utf-8')).hexdigest()

def hash_sha3_224(password):
    return hashlib.sha3_224((str(password)).encode('utf-8')).hexdigest()

def hash_sha512(password):
    return hashlib.sha512((str(password)).encode('utf-8')).hexdigest()

def hash_sha256(password):
    return hashlib.sha256((str(password)).encode('utf-8')).hexdigest()

def hash_sha384(password):
    return hashlib.sha384((str(password)).encode('utf-8')).hexdigest()
