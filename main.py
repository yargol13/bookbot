def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = wordcounter(text)
    print(f"{num_words} words in the document")
    letter_dictionary = lettercounter(text)
    print(letter_dictionary)

def book_text(path):
    with open(path) as f:
        return f.read()

def wordcounter(example_string):
    words = example_string.split()
    return len(words)

def lettercounter(input_string):
    letter_dic = {}
    string = input_string
    string = string.lower()
    for i in range(0,len(string)):
        current_char = string[i]
        if current_char in letter_dic:
            letter_dic[current_char] = letter_dic[current_char] + 1
        else:
            letter_dic[current_char] = 1
    return letter_dic


main()