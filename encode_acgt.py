import hashlib

password_hash = "c9735db20d0fe1ae78576484fcb6ba08a2e0d1d7bb9625a90a40264062122dbb"
password_bytes = bytes.fromhex(password_hash)
password_binary = ''.join(format(byte, '08b') for byte in password_bytes)
password_sequence = password_binary.replace('00', 'A').replace('01', 'C').replace('10', 'T').replace('11', 'G')

print(password_sequence)




#GA1A1CGAGCCGC1C1A1AAC1CAAGGG1AAGCCGAGGAA1CCGC1A1A1AA1AGGGA1C1C1CCGCAACACCACCGAAC1CACGCCG1CGCGA1C1ACA1C1CCA1AA1CA1AAAA1AGA1AAAC1ACAA1A1ACC1C1CGC1
