import operator
import string
from collections import defaultdict

def getMostFrequentWords(inputString, numWordsToReturn):
    """Returns a list of the most frequent words in a given string"""

    strippedOfPunctuation = inputString#.translate(string.maketrans("",""), string.punctuation)

    wordCounts = defaultdict(int)
    for word in strippedOfPunctuation.split():
        wordCounts[word] += 1

    sortedWords = sorted(wordCounts.iteritems(), key=operator.itemgetter(1), reverse=True)

    return [x for x in sortedWords[:(min(numWordsToReturn, len(sortedWords)-1))]]


fileHandle = open('haiku_dictionary_reduced.txt', 'r')
str1 = fileHandle.read()
fileHandle.close()
#print str1
#parsedTextRaw = str1.split(' ')
#print parsedTextRaw

wordCounts = getMostFrequentWords(str1, 300)


totalCount = 5 #sum(x[1] for x in wordCounts)

for i in xrange(len(wordCounts)):
    (word, count) = wordCounts[i]
    wordCounts[i] = (word, int(count**(0.8)/2)) #count/totalCount)

#words = [x[0] for x in wordCounts]
print ['\'' + x[0] + '\':1' for x in wordCounts]


final = []

for (word, count) in wordCounts:
    for i in xrange(count):
        final.append(word)

print final
