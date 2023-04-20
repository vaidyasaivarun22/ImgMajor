import hashlib
import os
from Crypto.Cipher import AES
from PIL import Image
import math
from random import randrange, seed

def aes_encrypt(u,key,f,msg=None):
    fin = open(f,'rb') 
    image = fin.read() 
    fin.close() 
    salt =os.urandom(16)
    image =salt+image
    key=hashlib.sha256((str(key)).encode("utf-8")).digest()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext,tag= cipher.encrypt_and_digest(image)
    #stegnography
    if msg:
        steg_image = Image.frombytes("RGB", (int(math.sqrt(len(ciphertext))), int(math.sqrt(len(ciphertext)))), ciphertext)
        steg_image.putpixel((0, 0), (len(msg), len(msg)))
        i, j = 1, 0
        for c in msg:
            steg_image.putpixel((i, j), (ord(c), 0, 0))
            i += 1
            if i >= steg_image.width:
                i = 1
                j += 1
        steg_image_bytes = steg_image.tobytes()
        ciphertext = steg_image_bytes
    path=os.path.join(u,"encrypt")
    file1=open(os.path.join(path,"aesout.jpg"),"wb")
    file2=open(os.path.join(path,"n.txt"),"wb")
    file3=open(os.path.join(path,"s.txt"),"wb")
    file2.write(nonce)
    file3.write(salt)
    file1.write(ciphertext)
    file1.close()
    file2.close()
    file3.close()

def aes_decrypt(u,key,f):
    key=hashlib.sha256((str(key)).encode("utf-8")).digest()
    path=os.path.join(u,"encrypt")

    file1 = open(f,'rb') 
    file2=open(os.path.join(path,"n.txt"),"rb")
    file3=open(os.path.join(path,"s.txt"),"rb")
    image = file1.read() 
    nonce=file2.read()
    salt =file3.read()
    file1.close() 
    file2.close()
    file3.close()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(image)
    # Verify that the decrypted image starts with the expected salt value
    if plaintext[:16] != salt:
        raise ValueError("Incorrect key or corrupted data")

    # Remove the salt value from the plaintext image data
    plaintext = plaintext[16:]
    # Shred the original encrypted data to prevent recovery
    file1 = open(f, 'wb')
    file1.write(os.urandom(os.path.getsize(f)))
    file1.close()
    path=os.path.join(u,"decrypt")
    file1=open(os.path.join(path,"aesout.jpg"),"wb")
    file1.write(plaintext)
    file1.close()