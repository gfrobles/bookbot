def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    words = get_book_words(text)
    word_count = len(words)
    print(word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_words(text):
    words = text.split()
    return words

main()