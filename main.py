def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    num_words = wordcounter(text)
    print(f"{num_words} words in the document")
    letter_dictionary = lettercounter(text)
    print(letter_dictionary)
    list_of_characters_report = report(letter_dictionary)
    for report_element in list_of_characters_report:
        print(f"The '{report_element['char']}' character was found {report_element['num']} times")

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

def sort_on(d):
    return d["num"]

def report(input_dictionary):
    input_dict = input_dictionary
    sorted_list_of_chars = []
    for inp_dict_element in input_dict:
        if inp_dict_element.isalpha():
           # print(f"{inp_dict_element} {input_dict[inp_dict_element]}")
            sorted_list_of_chars.append({"char" : inp_dict_element, "num" : input_dict[inp_dict_element]})
    sorted_list_of_chars.sort(reverse = True, key=sort_on)
    return sorted_list_of_chars
        


main()