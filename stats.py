def count_words(text):
    return len(text.split())

def count_character_frequency(text):
    count = {}

    for char in list(text):
        char = char.lower()
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    return count