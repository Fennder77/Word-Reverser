def reverse_words(sentence):# string, splits the sentence into words, reverses the word, and returns
    words = sentence.split()  # sentence for words
    reversed_words = [word[::-1] for word in words]  # Reverse words
    reversed_sentence = ' '.join(reversed_words)  # Putting upside down words
    return reversed_sentence

def count_vowels(sentence):# string, counts the number of occurrences of each vowel and returns a dictionary
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']#vowel dictionary
    vowel_count = {vowel: 0 for vowel in vowels}  #vowel counting dictionary
    for char in sentence:
        if char.lower() in vowels:  # vowel symbol?
            vowel_count[char.lower()] += 1  #Increasing the vowel counter
    return vowel_count

sentence = input("Enter text: ")

# Revers
reversed_sentence = reverse_words(sentence)
print("Revers words:", reversed_sentence)

# Counting vowels in a sentence
vowel_count = count_vowels(sentence)
print("Number of vowels:")
for vowel, count in vowel_count.items():
    print(vowel, ":", count)

