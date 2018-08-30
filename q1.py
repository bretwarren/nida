# Nida Krailas

name_text_file = input("Type name of file with .txt extension: ")
text = open(name_text_file, 'r').read()

# Total number of sentences
def sentence_count(text):
    sentence_count = 0
    replace = ["...", ".)"]
    for r in replace:
        text = text.replace(r, " ")
    end_punctuation = [".", "!", "?"]
    for i in end_punctuation:
        if i in text:
            sentence_count += text.count(i)
    return str(sentence_count)

# Total number of words
def total_word_count(text):
    text_to_words = text.split()
    filler = ["\n\n", "--", "..."]
    for word in text_to_words:
        for i in filler:
            if i in word:
                two_words = len(text_to_words) + 1
            else:
                two_words = 0
    return str(len(text_to_words) + two_words)

# Total number of unique words
def unique_word_count(text):
    replace = [".", "!", "?", "...", ".)", "(", ")", "--", "\n\n"]
    for r in replace:
        text = text.replace(r, " ")
        lowercase_text = text.lower()
        text_to_words = lowercase_text.split()
        unique_words = set(text_to_words)
    return str(len(unique_words))

# Print summary
print("Sentences: " + sentence_count(text))
print ("Unique words: " + unique_word_count(text))
print("Total word count: " + total_word_count(text))
