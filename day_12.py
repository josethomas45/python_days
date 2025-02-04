import rsa

public_key, private_key = rsa.newkeys(512)

message = '''Hey ,dude whats up?'''

enc_message = rsa.encrypt(message.encode(), public_key)

print("Original message:", message)
print("Encrypted message:", enc_message)

dec_message = rsa.decrypt(enc_message, private_key).decode()

print("Decrypted message:", dec_message)
