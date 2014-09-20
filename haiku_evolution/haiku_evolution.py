import random
import hyphenate

## OVERVIEW ##
#break down 5-7-5 syllables into subgroups
#choose a sequence of words that match the syllable lengths
#print the words in 3 lines

print "HAIKU EVOLUTION - A Collaboration between Man and Machine\n"

#print "(uses word bank -- https://github.com/first20hours/google-10000-english)"
#print "(uses syllable decomposition -- http://nedbatchelder.com/code/modules/hyphenate.html)\n"
#thinking about switching to javascript -- would use: https://code.google.com/p/hyphenator/


#####################
#read the textfile with the top 10,000 most common words in the english language, sorted by frequency
fileHandle = open('wordbank.txt', 'r')        
wordsTxt = fileHandle.read()
fileHandle.close()
wordsList = wordsTxt.split('\n')

#####################
#lists store previous haiku
line1_prev = []
line2_prev = []
line3_prev = []

#####################
#only use the top 5000 of the 10,000 word list
numWordsToInclude = 5000

wordsList = wordsList[:numWordsToInclude]

print 'INSTRUCTIONS:\nOn each iteration, Press [1] or [Enter] to keep the line from the first (left) haiku'
print '\t\tor input [2] to use the line from the second (right) haiku.\n'
print 'At any point, enter \'save\' to save the current haiku to a txt file\n'

raw_input("Press [Enter] to begin brainstorming.")

iterationCount = 0
 #max number of syllables to look for in a word
max_syls = 5


def getWordSylLen(max):
    return random.randrange(1, max+1)
    
while True:
            
    #line syllable lengths
    line1 = 5
    line2 = 7
    line3 = 5

    #breaks up lines into syllable chunks
    line1_words = []
    line2_words = []
    line3_words = []
    
    while line1 > 0:
        x = getWordSylLen(min(line1, max_syls))
        line1 -= x
        line1_words.append(x)
        
    while line2 > 0:
        x = getWordSylLen(min(line2, max_syls))
        line2 -= x
        line2_words.append(x)
        
    while line3 > 0:
        x = getWordSylLen(min(line3, max_syls))
        line3 -= x
        line3_words.append(x)
    
    line1_final = []
    line2_final = []
    line3_final = []
    
    #if(len(line1_prev) == 0):
    for numSyllables in line1_words:
        #get a word from wordsTxt which is the same number of syllables
        bySyllables = []
        randWord = ''
        while (len(bySyllables) != numSyllables): #or (charToExclude in randWord):
                i = random.randrange(0, len(wordsList))
                randWord = wordsList[i]
                bySyllables = hyphenate.hyphenate_word(randWord)
        if len(line1_final) == 0:
            randWord = randWord.capitalize()
        elif len(line1_final) == (len(line1_words) - 1):
            if( random.random() > 0.5):
                randWord = randWord + ','
        line1_final.append(randWord)
        
    #if(len(line2_prev) == 0):
    for numSyllables in line2_words:
        #get a word from wordsTxt which is the same number of syllables
        bySyllables = []
        randWord = ''
        while (len(bySyllables) != numSyllables): #or (charToExclude in randWord):
                i = random.randrange(0, len(wordsList))
                randWord = wordsList[i]
                bySyllables = hyphenate.hyphenate_word(randWord)
        if len(line2_final) == (len(line2_words) - 1):
            if( random.random() > 0.5):
                randWord = randWord + ';'
        line2_final.append(randWord)
        
    #if(len(line3_prev) == 0):
    for numSyllables in line3_words:
        #get a word from wordsTxt which is the same number of syllables
        bySyllables = []
        randWord = ''
        while (len(bySyllables) != numSyllables):
                i = random.randrange(0, len(wordsList))
                randWord = wordsList[i]
                bySyllables = hyphenate.hyphenate_word(randWord)
        if len(line3_final) == (len(line3_words) - 1):
            randWord = randWord + '.'
        line3_final.append(randWord)
            
    line1_string = ' '.join(line1_prev)
    line2_string = ' '.join(line2_prev)
    line3_string = ' '.join(line3_prev)
    
    max_len = 35
    
    print '\n'
    print 'Iteration: ' + str(iterationCount)
    print '1. '.ljust(max_len) + ' ' + '2. '
    print line1_string.ljust(max_len) + ' ' + ' '.join(line1_final)
    print line2_string.ljust(max_len) + ' ' + ' '.join(line2_final)
    print line3_string.ljust(max_len) + ' ' + ' '.join(line3_final)
    print ''
    
    if iterationCount == 0:
        save1 = "2"
        save2 = "2"
        save3 = "2"
    elif iterationCount == 1:
        save1 = raw_input("Save line 1 from which haiku? (1/2): ")
        save2 = raw_input("Save line 2 from which haiku? (1/2): ")
        save3 = raw_input("Save line 3 from which haiku? (1/2): ")
    else:
        save1 = raw_input("Line 1?: ")
        save2 = raw_input("Line 2?: ")
        save3 = raw_input("Line 3?: ")
    
    if save1 == "2":
        line1_prev = line1_final
        
    if save2 == "2":
        line2_prev = line2_final
        
    if save3 == "2":
        line3_prev = line3_final
    
    if save1 == 'save' or save2 == 'save' or save3 =='save':
        print '\n**Saved to file! (genetic_haikus.txt)**'
        fileToWrite = open('genetic_haikus.txt', 'a')
        fileToWrite.write(line1_string + '\n' + line2_string + '\n' + line3_string + '\n\n')
        fileToWrite.close()
        
    iterationCount += 1
