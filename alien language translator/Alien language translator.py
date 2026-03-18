# """You have discovered a strange alien language where:

# 1️⃣ Every word is reversed, but the sentence structure remains the same.
# 2️⃣ Every vowel (a, e, i, o, u) is replaced by the next vowel in order (a → e, e → i, i → o, o → u, u → a).
# 3️⃣ Spaces and punctuation remain unchanged."""

vowel_map = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
             'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
sentence=input("Enter a sentence : ")
words = sentence.split()  # Splits words but removes spaces
translated_words = []  # Empty list to store final words

for word in words:
    reversed_word = word[::-1]  # Reverse the word
    new_word = ""
    for letter in reversed_word:
        if letter in vowel_map:
            new_word += vowel_map[letter]  # Replace vowel
        else:
            new_word += letter  # Keep consonant same
    translated_words.append(new_word)
final_sentence = " ".join(translated_words)
print("Alien language is : ",final_sentence)





