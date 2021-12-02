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
    elif sentence[l] == 'b' or sentence[l] == 'c' or sentence[l] == 'd' or sentence[l] == 'f' or sentence[l] == 'g' or sentence[l] == 'h' or sentence[l] == 'j' or sentence[l] == 'k' or sentence[l] == 'l' or sentence[l] == 'm' or sentence[l] == 'n' or sentence[l] == 'p' or sentence[l] == 'q' or sentence[l] == 'r' or sentence[l] == 's' or sentence[l] == 't' or sentence[l] == 'v' or sentence[l] == 'w' or sentence[l] == 'x' or sentence[l] == 'y' or sentence[l] == 'z':
        numConsonants = numConsonants + 1
    elif sentence[l] == '1' or sentence[l] == '2' or sentence[l] == '3' or sentence[l] == '4' or sentence[l] == '5' or sentence[l] == '6' or sentence[l] == '7' or sentence[l] == '8' or sentence[l] == '9' or sentence[l] == '0':
        numNumbers = numNumbers + 1
    elif (sentence[l].isspace()) == True:
        numWords = numWords + 1
    

if sentence[-1].isspace() == True:
    numWords = numWords - 1
print(numWords,numVowels,numConsonants)
# 3 Calculate
# 4 Print
