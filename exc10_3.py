import string
fname = input('Enter the file name: ')
try:
    fhand = open(fname, encoding='utf8')
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    #print (words)
    for x in words:
        word = x.split()
        word = word [0]
        #print (word)
        for y in range (0 , len(word)):
            letter = word[y]
            #print (letter)
            if letter.isalpha() == True:
                counts [letter] = counts.get(letter,0) + 1

#print (counts)

lst = list()
for ltr, count in list(counts.items()):
    lst.append((count, ltr))
    
lst.sort(reverse=True)

for count, ltr in lst:
    print(count, ltr)

#sanity check : how many letters
print (len(lst))