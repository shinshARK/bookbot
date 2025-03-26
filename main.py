from stats import *
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    
    book_uri = sys.argv[1]
    print(f"Analyzing book found at {book_uri}...")

    book_content = get_book_text(book_uri)
    
    word_count = count_words(book_content)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    char_count = count_character_frequency(book_content)
    transformed_char_count = sort_dict(char_count)
    for entry in transformed_char_count:
        if entry['char'].isalpha():
            print(f"{entry["char"]}: {entry["count"]}")

    print("============= END ===============")


main()