"""
    a1zz6
        amir => [1,13,9,18]
"""

def encode(plain):
    return [ord(elm)-92 for elm in plain]

def decode(encode):
    return ''.join([chr(elm)+92 for elm in encode])


print(encode('amir'))
print(decode([97, 109, 105, 114]))
