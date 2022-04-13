from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256



data = input("Enter your text, you want to be encrypted: ")
data = bytes(data, 'utf-8')

####################### keyA ##########################################


keyA = get_random_bytes(32)

print("keyA: ", keyA)

cipher = AES.new(keyA, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("file.bin", "wb")
for x in (cipher.nonce, tag, ciphertext):
    file_out.write(x)
file_out.close()

######################### Pin #########################################
pin = input("Enter your new Pin:   ")
hashedPin = SHA256.new(data=bytes(str(pin), 'utf-8'))
print("hash: ", hashedPin.digest())


    


######################## keyB and encryption of keyA ##########################################


data2 = keyA

keyB = hashedPin.digest()

cipher2 = AES.new(keyB, AES.MODE_GCM)
ciphertext2, tag2 = cipher2.encrypt_and_digest(data2)

file_out2 = open("keyA_enc.bin", "wb")

for x in (cipher2.nonce, tag2, ciphertext2):
    file_out2.write(x)

file_out2.close()