lists = [chr(i) for i in range(10, 127)]
raws = list(raw_input("cleartext >> "))
count = int(raw_input("offset >> "))
encrypt=[]
decrypt=[]
j = 0
def encipher(formal, alists):
    for i in range(len(formal)):
        for j in range(len(alists)):
            if formal[i] == alists[j]:
                k = (j + count) % len(lists)
                key = alists[k]
                encrypt.append(key)
def decipher(formal, alists):
    for i in range(len(formal)):
        for j in range(len(alists)):
            if formal[i] == alists[j]:
                a = ((j + len(lists)) - count) % len(lists)
                key = alists[a]
                decrypt.append(key)

encipher(raws,lists)
decipher(encrypt,lists)
print ("This is an encrypt: %s" % encrypt )
print ("This is a decrypt: %s" % decrypt )
