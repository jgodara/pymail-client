import base64

from Crypto.Cipher import AES

key = "6vFjZErd4WUGvc79"
cipher = AES.new(key, AES.MODE_ECB)


def encodestr(message: str):
    to_encode = message.rjust(32)
    return base64.b64encode(cipher.encrypt(to_encode)).decode("utf-8").strip()


def decodestr(message: str):
    return cipher.decrypt(base64.b64decode(message)).decode("utf-8").strip()
