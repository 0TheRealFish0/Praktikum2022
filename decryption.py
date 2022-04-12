from Crypto.Cipher import AES
from Crypto.Hash import SHA256

print("Insert the Pin:")
print()
pin_ = input()
pin_ = str(pin_)



UserInput_hashed = SHA256.new(data=bytes(pin_, 'utf-8'))

try:
    file_in = open("keyA_enc.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    cipher = AES.new(UserInput_hashed.digest(), AES.MODE_GCM, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    
    print("keyA: ", data)
    print()

    file_in2 = open("file.bin", "rb")
    nonce2, tag2, ciphertext2 = [ file_in2.read(x) for x in (16, 16, -1) ]

    cipher2 = AES.new(data, AES.MODE_GCM, nonce2)
    data2 = cipher2.decrypt_and_verify(ciphertext2, tag2)

    print(data2)
    print()
    

except ValueError:
    print("wrong pin")
