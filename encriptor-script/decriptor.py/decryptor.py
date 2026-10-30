import rsa 

private_key = rsa.PrivateKey.load_pkcs1(open('private_key.txt', 'rb').read())

encrypted = open('encrypted.bin', 'rb').read()
decryptor = rsa.decrypt(encrypted, private_key)

print("Descrypted:", descrypted.decode())