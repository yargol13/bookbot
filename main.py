def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = wordcounter(text)
    print(f"{num_words} words in the document")

def book_text(path):
    with open(path) as f:
        return f.read()

def wordcounter(example_string):
    words = example_string.split()
    counter = 0
    return len(words)

main()