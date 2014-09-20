import random
import hyphenate

## OVERVIEW ##
#break down 5-7-5 syllables into subgroups
#choose a sequence of words that match the syllable lengths
#print the words in 3 lines

print "HAIKU LIPOGRAM GENERATOR"

print "(uses word bank -- https://github.com/first20hours/google-10000-english)"
print "(uses syllable decomposition -- http://nedbatchelder.com/code/modules/hyphenate.html)\n"
#thinking about switching to javascript -- would use: https://code.google.com/p/hyphenator/


#####################
#read the textfile with the top 10,000 most common words in the english language, sorted by frequency
fileHandle = open('wordbank.txt', 'r')        
wordsTxt = fileHandle.read()
fileHandle.close()
wordsList = wordsTxt.split('\n')

while True:
	#####################
	#only use the top 5000 of the 10,000 word list
	inputNumWordsToInclude = raw_input('How large of a word bank would you like to use? [1000, 10000] (default = 5000): ')
	
	numWordsToInclude = 5000
	
	try:
		numWordsToInclude = min(10000, max(1000, int(inputNumWordsToInclude)))
	except ValueError:
		numWordsToInclude = 5000
	
	print "Using the top " + str(numWordsToInclude) + " most common words in the english language.\n"
		
	wordsList = wordsList[:numWordsToInclude]
	
	#######################
	inputCharToExclude = raw_input("Which character (a,e,i,o,u) would you like to exclude? (default 'e') : ")
	if inputCharToExclude.isalpha():
		charToExclude = inputCharToExclude[0]
	else:
		charToExclude = 'e'
	
	print "Excluding the char '" + charToExclude + "'\n"
	
	#######################
	
	numHaikus = 10
	
	inputNumHaikus = raw_input('How many haikus would you like to generate? [5, 100] (default = 10): ')
	
	try:
		numHaikus = min(100, max(5, int(inputNumHaikus)))
	except ValueError:
		numHaikus = 10
		
	print "Generating " + str(numHaikus) + " haikus."
	
	#######################
	
	def getWordSylLen(max):
	    return random.randrange(1, max+1)
	    
	#max number of syllables to look for in a word
	max_syls = 5
	
	for i in range(numHaikus):
	    
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
	        
	#     print line1_words
	#     print line2_words
	#     print line3_words
	#      
	#     print "\n"
	    
	    line1_final = []
	    line2_final = []
	    line3_final = []
	    
	    for numSyllables in line1_words:
	        #get a word from wordsTxt which is the same number of syllables
	        bySyllables = []
	        randWord = ''
	        while (len(bySyllables) != numSyllables) or (charToExclude in randWord):
	                i = random.randrange(0, len(wordsList))
	                randWord = wordsList[i]
	                bySyllables = hyphenate.hyphenate_word(randWord)
	                #print str(len(bySyllables)) + " =? " + str(numSyllables) 
	        #print "good: " + str(bySyllables)
	        line1_final.append(randWord)
	        
	    for numSyllables in line2_words:
	        #get a word from wordsTxt which is the same number of syllables
	        bySyllables = []
	        randWord = ''
	        while (len(bySyllables) != numSyllables) or (charToExclude in randWord):
	                i = random.randrange(0, len(wordsList))
	                randWord = wordsList[i]
	                bySyllables = hyphenate.hyphenate_word(randWord)
	                #print str(len(bySyllables)) + " =? " + str(numSyllables) 
	        #print "good: " + str(bySyllables)
	        line2_final.append(randWord)
	        
	        
	    for numSyllables in line3_words:
	        #get a word from wordsTxt which is the same number of syllables
	        bySyllables = []
	        randWord = ''
	        while (len(bySyllables) != numSyllables) or (charToExclude in randWord):
	                i = random.randrange(0, len(wordsList))
	                randWord = wordsList[i]
	                bySyllables = hyphenate.hyphenate_word(randWord)
	                #print str(len(bySyllables)) + " =? " + str(numSyllables) 
	        #print "good: " + str(bySyllables)
	        line3_final.append(randWord)
	    
	    print ''
	    print ' '.join(line1_final)
	    print ' '.join(line2_final)
	    print ' '.join(line3_final)
	    
	print "\n\nHAIKU LIPOGRAM GENERATOR\n"
