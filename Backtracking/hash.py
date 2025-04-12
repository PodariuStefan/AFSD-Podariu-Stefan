import hashlib

def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()