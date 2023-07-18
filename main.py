def reverse_words(sentence):# строка, разбивает предложение на слова, переворачивает  слово и возвращает
    words = sentence.split()  # предложение на слова
    reversed_words = [word[::-1] for word in words]  # Реверс слов
    reversed_sentence = ' '.join(reversed_words)  # Соединяем перевернутые слова
    return reversed_sentence

def count_vowels(sentence):# строка, подсчитывает количество вхождений каждой гласной и возвращает словарь
    vowels = ['a', 'о', 'и', 'ы', 'у', 'э']#словарь глачных
    vowel_count = {vowel: 0 for vowel in vowels}  #словарь для подсчета гласных
    for char in sentence:
        if char.lower() in vowels:  # символ гласный?
            vowel_count[char.lower()] += 1  # Увеличиваем счетчик гласной
    return vowel_count

# пользователь
sentence = input("Введите предложение: ")

# Переворачиваем
reversed_sentence = reverse_words(sentence)
print("Перевернутые слова:", reversed_sentence)

# Подсчитываем гласных в предложение
vowel_count = count_vowels(sentence)
print("Количество гласных:")
for vowel, count in vowel_count.items():
    print(vowel, ":", count)

