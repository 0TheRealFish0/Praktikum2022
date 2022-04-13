from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


data = b'This is a RSA test'

KeyA = get_random_bytes(32)

cipher = AES.new(KeyA, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("file.bin", "wb")
for x in (cipher.nonce, tag, ciphertext):
    file_out.write(x)
file_out.close()

# encrypt KeyA

recipient_key = RSA.import_key(open("receiver.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)
keyA_enc = cipher_rsa.encrypt(KeyA)

file_out = open('keyA_encrypted.bin', 'wb')
for x in (keyA_enc, cipher.nonce, tag, ciphertext):
    file_out.write(x)
file_out.close()
