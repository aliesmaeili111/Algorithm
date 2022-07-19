from string import ascii_letters


def encrypt(string,key):
    alpha = ascii_letters
    result = ''
    
    for ch in string :
        if ch not in alpha:
            result += ch
        else:
            new_key  = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]
            
    return result

    
    
print(encrypt('amir',4))


def dencrypt(string,key):
    key *= -1
    return encrypt(string,key)

    
    
print(dencrypt('eqmv',4))