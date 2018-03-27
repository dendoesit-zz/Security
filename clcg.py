import random
import codecs

#generate two private kyes using the congruential generator
#we start off by declaring the variables
m1 = 2147483563
a1 = 40014
m2 = 2147483399
a2 = 20692

#we seed the two numbers using the random.randint that retuns an integer.
randx = random.randint(1, 500)
randy = random.randint(1, 500)

# we define a function that calls the random numbers so that we can use it multiple times. in this case to return 10 numbers
def rng():
    for i in range (2):
        results.append(Rand())
    return results

#the function itself based on given formula
def Rand():
    global randx,randy
    randx = (a1 * randx) % m1
    randy = (a2 * randy) % m2
    result = (randx - randy) % (m1 - 1)
    return result / m1

results = []
rng()
#saving the first two values so that we can use them as private keys
privateA = results[0]
privateB = results[1]

# Generate the secret key using q = 353 and Alfa = 3 according to the Diffie-Hellman algorithm
# User A key generation:
q = 353
alfa = 3
publicA = alfa ** privateA % q
publicB = alfa ** privateB % q

k = publicB ** privateA % q
#printing the shared key
print(k)

#start of RC4 Algorithm
def KSA(key):
# Initialization of S
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + int(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]  # swap values
    return S

def StreamGeneration(S):
#Stream Generation
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap values
        K = S[(S[i] + S[j]) % 256]
        yield K

def get_keystream(key):
    #
    S = KSA(key)
    return StreamGeneration(S)

#the most important part of the code. getting a keystream of keys that we XOR with each of the value from the text and saving the value as a hexcode
def enclogic(text):
    global k
    #slight issue with types since we return a float from our calculations and float cannot be iterated over hence we need to convert it to a string and remove the dot.
    key = str(k).replace(".","")
    key = [c for c in key]
    #get keystream calling KSA and PRGA
    keystream = get_keystream(key)
    res = []
    for c in text:
        print(c)
        print(c^next(keystream))
        val = ("%02X" % (c ^ next(keystream)))# XOR and taking hex
        print(val)
        res.append(val)
    return ''.join(res)#sticking all values together

#encrypt makes sure the plaintext is an array of ascii for each character
def encrypt(plaintext):
    plaintext = [ord(c) for c in plaintext]
    return enclogic(plaintext)

#decrypting is decoding our hex_code and taking it through our encryption logic, in the end turning it back to utf-8
def decrypt(ciphertext):
    ciphertext = codecs.decode(ciphertext, 'hex_codec')
    res = enclogic(ciphertext)
    return codecs.decode(res, 'hex_codec').decode('utf-8')

#opening our text file in order to get the last 128 items
file = open('text.txt','r')
contents = file.read()
#getting the last 128 items of the array
str1 = contents[-128:]
#creating a string that will containt the ecrypted text so we can attack it to a file
encodedstr1 = encrypt(str1)
encodedfile = open('cipher.txt','w')
encodedfile.write(encodedstr1)

#since the cipher block gets saved into a text file already we want to see how the decryption works
print(encodedstr1)

def twodigithex(number):
    return ("%02X" % number)
print (twodigithex(111))

