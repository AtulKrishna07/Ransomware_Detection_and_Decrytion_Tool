key = 0x42  # Same key used in decryptor.py
plaintext = b"This is a test message."

encrypted = bytes([b ^ key for b in plaintext])

with open("sample_encrypted.bin", "wb") as f:
    f.write(encrypted)

print("Encrypted file saved as sample_encrypted.bin")
