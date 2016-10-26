#Bring in the files 
filen = raw_input("What is the file name? >>>")
text = open(filen, 'r')
string = text.read()
text.close()
if len(string)%2 == 1: # check to see of need to remove the last letter
    meet = 'odd'
else:
    meet = 'even'
#set for the loop
i = 0
j = 0
backup = 0
n = [1,0]# tested and need to be backwards to output correctly
first = [] #as in first letter
encipher = []
decypher = []
#The loop to read and reformat...
for i in range((len(string)/2) + len(string)%2):
    #function to prevent overlap
    if backup == 0:
        mine = string[j]
        first.append(mine)
        backup += 1
    one = ord(string[j])
    try:
        two = ord(string[j+1])
        if two == "":
            two = ord(first[0])
    except:
        two = ord(first[0])
    j += 2
    byte = 8
    new = one << byte | two  #new = one moved by eight and added by two. Note the byte cause 1 never interact (Ex.111 000 + 111 = 111 111)
    #setting the encrypt after block something...
    clrtxt = new
    cyp = ord('g')# this will generate an 8 bit key.
    cprtxt = clrtxt ^ cyp
    encipher.append(cprtxt)
print encipher
#starting the decrypt
for words in range((len(encipher))):
    reading = 0
    clrtxt = encipher[words] ^ cyp
    for reading in range(len(n)):#unmask the number here use mask to seperate the two connected bits
        bitlen = 8
        mask = 2**bitlen-1  # a sequence of 1 bits
        sublk = (clrtxt >> (n[reading]*bitlen)) & mask
        molding = chr(sublk)
        decypher.append(molding)
if meet == 'odd':
    decypher.pop()
string = ""
for count in range(len(decypher)):
    string = string + decypher[count]
print string
