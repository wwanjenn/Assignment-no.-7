# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

# STEPS
# 1 Input
print('Word, Vowel and Consonant Counter')
sentence = input('Sentence: ')
# 2 Loop
numVowels = 0
numNumbers = 0
numConsonants = 0
numWords = 1
for l in range(len(sentence)):
    
    if sentence[l] == 'a' or sentence[l] == 'e'or sentence[l] == 'i' or sentence[l] == 'o' or sentence[l] == 'u':
        numVowels = numVowels + 1
    elif sentence[l] == '1' or sentence[l] == '2' or sentence[l] == '3' or sentence[l] == '4' or sentence[l] == '5' or sentence[l] == '6' or sentence[l] == '7' or sentence[l] == '8' or sentence[l] == '9' or sentence[l] == '0':
        numNumbers = numNumbers + 1
    elif (sentence[l].isspace()) == True:
        numWords = numWords + 1


if sentence[-1].isspace() == True:
    numWords = numWords - 1
print(numWords,numVowels,numConsonants)
# 3 Calculate
# 4 Print
