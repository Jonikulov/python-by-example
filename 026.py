# Challenge 026

# Pig Latin
VOWELS = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a word: ").lower()
if word[0] in VOWELS:
    word = word + "way"
else:
    word = word[1:] + word[0] + "ay"
print(word)