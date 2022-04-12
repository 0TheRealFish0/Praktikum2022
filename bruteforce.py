
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import time


start_time = time.time()

n = 0000

while True:
    
    try:
        n_as_string = str(n)
        n_hashed = SHA256.new(data=bytes(n_as_string, 'utf-8'))


        file_in = open('keyA_enc.bin', "rb")
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

        cipher = AES.new(n_hashed.digest(), AES.MODE_GCM, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
    
        print(data)
        print()
        print()
        file_in2 = open("file.bin", "rb")
        nonce2, tag2, ciphertext2 = [ file_in2.read(x) for x in (16, 16, -1) ]

        cipher2 = AES.new(data, AES.MODE_GCM, nonce2)
        data2 = cipher2.decrypt_and_verify(ciphertext2, tag2)

        print(data2)
        print()
        print("round: ", n)
        print()
        print("--- %s seconds ---" % (time.time() - start_time))
        break

    except ValueError:
        print("There has been an error", n, "\r")
        n = n + 1

    