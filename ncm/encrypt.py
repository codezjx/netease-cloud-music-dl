# -*- coding: utf-8 -*-

import os
import base64
import json
import binascii
from Crypto.Cipher import AES

from ncm.constants import modulus, nonce, pub_key


def encrypted_request(text):
    text = json.dumps(text)
    sec_key = create_secret_key(16)
    enc_text = aes_encrypt(aes_encrypt(text, nonce), sec_key)
    enc_sec_key = rsa_encrypt(sec_key, pub_key, modulus)
    data = {'params': enc_text, 'encSecKey': enc_sec_key}
    return data


def aes_encrypt(text, sec_key):
    pad = 16 - len(text) % 16
    text = text + chr(pad) * pad
    encryptor = AES.new(sec_key, 2, '0102030405060708')
    cipher_text = encryptor.encrypt(text)
    cipher_text = base64.b64encode(cipher_text).decode('utf-8')
    return cipher_text


def rsa_encrypt(text, public_key, p_modulus):
    text = text[::-1]
    rs = pow(int(binascii.hexlify(text), 16), int(public_key, 16), int(p_modulus, 16))
    return format(rs, 'x').zfill(256)


def create_secret_key(size):
    return binascii.hexlify(os.urandom(size))[:16]
