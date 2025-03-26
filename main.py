def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def count_words(text):
    return len(text.split())

def main():
    book_content = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_content)
    print(f"{word_count} words found in the document")


main()