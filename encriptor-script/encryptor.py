import rsa 

public_key, private_key = rsa.newkeys(1024)

open('public_key.txt', 'wb').write(public_key.save_pkcs1())
open('private_key.text', 'wb').write(rivate key.save_pkcs1())

message = open('file.txt','rb').read()
encrypted = rsa.encrypt(message, public_key)
open('encrypted.bin', 'wb').write(encrypted)

print('Encrypted file.txt -> encrypted.bin')