def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print("")
    for pair in num_letters:
        print(f"The '{pair[0]}' character was found {pair[1]} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text) -> dict:
    lowered = text.lower()
    map = {}
    for char in lowered:
        if char.isalpha():
            if char not in map:
                map[char] = 1
            else:
                map[char] = map[char] + 1
    pairs = sorted(map.items(), key=lambda x: x[1])
    return pairs


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
