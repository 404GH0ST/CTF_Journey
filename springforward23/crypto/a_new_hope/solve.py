
def decrypt(message, key):
    decrypted = ""
    for i in range(len(message)):
        decrypted += chr(message[i] ^ ord(key[i % len(key)]))
    
    return decrypted
key = "SAFE"
message = bytes.fromhex('072923373661312c3f2d66273661276537203f652429232b73352f283661312c3f2d6627362f22653124202a2124663c3c346a65322f22652a2e3365302028653b242a357334352d363366313b2835653a2f68653d28252628297529231e2b760c7124740c36062b2e6f661c3c3466282632326520282b353f3866233c2d2a2a2461322d36613624272966233c3366203d2d2f223b35232b3e2428317d616b1711')

print(decrypt(message, key))