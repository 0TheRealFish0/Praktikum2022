import logging
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import time
import threading 


start_time = time.time()
pill2kill = threading.Event()
logger = logging.getLogger()

def task1(stop_event, arg):
    n = 000000
    nonce, tag, ciphertext = 0, 0, 0
    with open('keyA_enc.bin', "rb") as file_in:
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]


    while not stop_event.wait(0):
        

        try:
            
            n_hashed = SHA256.new(data=bytes(str(n), 'utf-8'))



            cipher = AES.new(n_hashed.digest(), AES.MODE_GCM, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            stop_event.set()
            print(data)
            print()
            print()
            file_in2 = open("file.bin", "rb")
            nonce2, tag2, ciphertext2 = [ file_in2.read(x) for x in (16, 16, -1) ]

            cipher2 = AES.new(data, AES.MODE_GCM, nonce2)
            data2 = cipher2.decrypt_and_verify(ciphertext2, tag2)
            
            
            print()
            print("round: ", n)
            print()
            print(data2)
            print()
            print("--- %s seconds ---" % (time.time() - start_time))
            

        
        except ValueError:
            print("There has been an error", n, end="\r")
            n = n + 1
            
            

def task2(stop_event, arg):
    n = 166666
    nonce, tag, ciphertext = 0, 0, 0
    with open('keyA_enc.bin', "rb") as file_in:
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]


    while not stop_event.wait(0):
        
        
        try:
            
            n_hashed = SHA256.new(data=bytes(str(n), 'utf-8'))


            cipher = AES.new(n_hashed.digest(), AES.MODE_GCM, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            stop_event.set()
            print(data)
            print()
            print()
            file_in2 = open("file.bin", "rb")
            nonce2, tag2, ciphertext2 = [ file_in2.read(x) for x in (16, 16, -1) ]

            cipher2 = AES.new(data, AES.MODE_GCM, nonce2)
            data2 = cipher2.decrypt_and_verify(ciphertext2, tag2)
            
            
            print()
            print("round: ", n)
            print()
            print()
            print(data2)
            print()
            print("--- %s seconds ---" % (time.time() - start_time))
            
            
            

        except ValueError:
            print("There has been an error", n, end="\r")
            n = n + 1
            


def task3(stop_event, arg):
    n = 333332
    nonce, tag, ciphertext = 0, 0, 0
    
    with open('keyA_enc.bin', "rb") as file_in:
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    while not stop_event.wait(0):


        try:
            
            n_hashed = SHA256.new(data=bytes(str(n), 'utf-8'))


            cipher = AES.new(n_hashed.digest(), AES.MODE_GCM, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            stop_event.set()
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
            
            
            

        except ValueError:
            print("There has been an error", n, end="\r")
            n = n + 1


def task4(stop_event, arg):
    n = 499998
    nonce, tag, ciphertext = 0, 0, 0

    with open('keyA_enc.bin', "rb") as file_in:
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    while not stop_event.wait(0):

        

        try:
            
            n_hashed = SHA256.new(data=bytes(str(n), 'utf-8'))


            cipher = AES.new(n_hashed.digest(), AES.MODE_GCM, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            stop_event.set()
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
            
            
            

        except ValueError:
            print("There has been an error", n, end="\r")
            n = n + 1
            



def task5(stop_event, arg):
    n = 666664
    nonce, tag, ciphertext = 0, 0, 0

    with open('keyA_enc.bin', "rb") as file_in:
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    while not stop_event.wait(0):

        

        try:
            
            n_hashed = SHA256.new(data=bytes(str(n), 'utf-8'))


            cipher = AES.new(n_hashed.digest(), AES.MODE_GCM, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            stop_event.set()
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
            
            
            

        except ValueError:
            print("There has been an error", n, end="\r")
            n = n + 1


def task6(stop_event, arg):
    n = 833330
    nonce, tag, ciphertext = 0, 0, 0

    with open('keyA_enc.bin', "rb") as file_in:
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

    while not stop_event.wait(0):

        

        try:
            
            n_hashed = SHA256.new(data=bytes(str(n), 'utf-8'))


            cipher = AES.new(n_hashed.digest(), AES.MODE_GCM, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            stop_event.set()
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
            
            
        except ValueError:
            print("There has been an error", n, end="\r")
            n = n + 1





def main(pill2kill):

    
    t1 = threading.Thread(target=task1, name='t1', args=(pill2kill, "tasks"))
    t2 = threading.Thread(target=task2, name='t2', args=(pill2kill, "tasks"))
    t3 = threading.Thread(target=task3, name='t2', args=(pill2kill, "tasks"))
    t4 = threading.Thread(target=task4, name='t2', args=(pill2kill, "tasks"))
    t5 = threading.Thread(target=task5, name='t2', args=(pill2kill, "tasks"))
    t6 = threading.Thread(target=task6, name='t2', args=(pill2kill, "tasks"))

    

    # starting threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()



main(pill2kill)