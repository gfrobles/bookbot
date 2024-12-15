def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    words = get_book_words(text)
    word_count = len(words)
    #print(word_count)
    character_count = get_book_character(text)
    #print(character_count)
    print_report(word_count, character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_words(text):
    words = text.split()
    return words

def get_book_character(text):
    lowered_text = text.lower()
    characters = {}

    for i in text:
        if i in characters:
            characters[i] = characters[i] + 1
        else:
            characters[i] = 1

    return characters
def print_report(word_count, character_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    print()
    sorted_dict = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"the '{key}' character was found {value} times")
    print("--- End report ---")

main()