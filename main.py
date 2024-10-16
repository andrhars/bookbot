def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

        print(f"--- Begin report of {path} ---")
        print("")
        print(f"{count_words(file_contents)} words found in the document")
        print("")

        for char, count in sort(count_characters(file_contents)):
            print(f"The '{char}' character was found {count} times")
        
        print("")
        print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_characters = text.lower()
    characters = {}
    for c in lower_characters:
        if c.isalpha():
            characters[c] = characters.get(c, 0) + 1
    return(characters)

def sort(dictionary):
    dict_list = [(char, count) for char, count in dictionary.items()]
    dict_list.sort(key=lambda x: x[1], reverse=True)
    return(dict_list)





main()
