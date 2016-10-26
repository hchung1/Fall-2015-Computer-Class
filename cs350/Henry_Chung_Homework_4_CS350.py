alphabet = [chr(10)] + [chr(i) for i in range(32, 127)]
decrypt=[]
counter = ['0',]
def decipher(formal, alists):
    result = '0'
    count = 0
    while result == '0':
        count = count + 1
        for i in range(len(formal)):
            for j in range(len(alists)):
                if formal[i] == alists[j]:
                    a = j - count % len(alists)
                    key = alists[a]
                    decrypt.append(key)
        print(count)
        print(str(decrypt))
        result = raw_input("Is this the result? 0 = no, anything else = yes >>> ")
        if result == '0':
            while len(decrypt) > 0 :
                decrypt.pop()
        else:
            print ("The offset key is %d" % count)
            break
    print ("This is a decrypt: %s" % decrypt)
ra = raw_input("What is the file name? >>")
raw = open(ra, 'r')
raws = raw.read()
decipher(raws,alphabet)
