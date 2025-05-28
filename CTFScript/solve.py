# Simple XOR decryptor for basic CTF challenges

def xor_decrypt(ciphertext, key):
    return ''.join(chr(c ^ key) for c in ciphertext)

if __name__ == '__main__':
    data = [120, 115, 119, 126, 121, 122]
    key = 42
    plaintext = xor_decrypt(data, key)
    print("Decrypted:", plaintext)
