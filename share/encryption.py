from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SALT = "PASS@HASH"


def hash_password(password):
    password = password.encode('utf-8')
    salt = SALT.encode('utf-8')

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32
    )

    key = kdf.derive(password)

    return key.hex()
