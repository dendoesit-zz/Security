#viginere cipher decriptor

#inputs, line of text and key to cipher with
line = input('Please provide a line of text')
key = input('Please provide the key you want to use')


# get rid of spaces, prepare a keyList and a lineList
line = line.lower().replace(' ','')
keyList = []
lineList = ''

#put all keys into a KeyList
for i in key:
    keyList.append(ord(i)-ord('a'))

#get as many numbers in keyList as letters in line

newArr = [keyList[i%len(keyList)] for i in range(len(line))]

#get numbers from letters
for i in range(len(line)):
        newChr = chr(((ord(line[i])-ord('a') + newArr[i]) % 26)+ord('a'))
        lineList += (newChr)
print(lineList)



