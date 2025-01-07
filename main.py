def data_input():
    text = input("введите текст: ").lower()
    text.replace(".", "")
    text.replace(",", "")
    return text


def count_words(text):
    return len(text.split())


def longest_word(text):
    length = ""
    for i in text.split():
        if len(i) > len(length):
            length = i
    return length


def count_vowels(text):
    vowels = "аеёиоуыэюя"
    counter = 0
    for i in text:
        if i in vowels:
            counter += 1
    return counter


def every_word_count(text):
    word_list = {}
    for i in text.split():
        if i in word_list:
            word_list[i] += 1
        else:
            word_list[i] = 1
    return word_list


text = data_input()

print(f"количество слов: {count_words(text)}")
print(f"самое длинное слово: {longest_word(text)}")
print(f"количество гласных букв: {count_vowels(text)}")
print(f"количество раз, которое каждое слово встречается в тексте: {every_word_count(text)}")