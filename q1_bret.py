# Nida Krailas

#name_text_file = input("Type name of file with .txt extension: ")
#text = open(name_text_file, 'r').read()
text = open("text_sample.txt",'r').read() #hard coding for faster testing

#clean text for processing - remove special characters and lower case
def cleanText(text):
    specialCharacters = ["...",".)","\n\n", "--","(", ")",","]
    for special in specialCharacters:
        text = text.replace(special, " ")
    return text.lower()

# update all punctation to be periods
def updatePunctuation(text):
    punctuation = ["!","?"] #non period punctuation
    for punc in punctuation:
        text = text.replace(punc, ".") #replace with a period
    return text

# count sentences
def getSentenceCount(text):
    return str(len(text.split(".")))

# get words in text as array
def getWords(text):
    text = text.replace("."," ") #remove periods so that end words don't have a period appended for unique word check
    return text.split()

#count words in array
def getWordCount(words):
    return str(len(words))

#get unqiue words
def getUniqueWords(words):
    return str(len(set(words)))

# Print summary
noSpecial = cleanText(text) #store text with no special characters
uniformPunctuation = updatePunctuation(noSpecial) #store text with only periods for punctuation
words = getWords(uniformPunctuation) # must be uniformPunctuation because of the replacement of punct

print("Sentences: " + getSentenceCount(uniformPunctuation))
print ("Unique words: " + getUniqueWords(words))
print("Total word count: " + getWordCount(words))
