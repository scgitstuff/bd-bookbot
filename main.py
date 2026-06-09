import sys

from stats import countWords
from stats import countChars
from stats import sortChars
from stats import filterChars

# from stats import chars_dict_to_sorted_list

# import sys


def main():
    # 2.1
    # print("greetings boots")

    # 2.3
    # filePath = "books/frankenstein.txt"
    # print(f"Analyzing book found at {filePath}")
    # frank = getText(filePath)
    # print(frank)

    # 2.4
    # words = countWords(frank)
    # print()
    # print(f"Found {words} total words")

    # 2.6
    # chars = countChars(frank)
    # print()
    # print(chars)

    # 3.1
    # tuples = chars_dict_to_sorted_list(chars)
    # print()
    # print(tuples)

    # 3.2
    # report(frank)

    # 3.3
    # print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filePath = sys.argv[1]
    print(f"Analyzing book found at {filePath}")
    book = getText(filePath)
    report(book)


def report(book: str):
    print("============ BOOKBOT ============")
    chars = countChars(book)
    print("----------- Word Count ----------")
    print(f"Found {countWords(book)} total words")

    chars = filterChars(chars)
    lst = sortChars(chars)
    print("--------- Character Count -------")
    out = map(lambda c: formatChar(c), lst)
    s = "\n".join(out)
    print(s)


def formatChar(d: dict[str, int]) -> str:
    # there is a single char in the dict
    k = next(iter(d.keys()))
    v = d[k]

    return f"{k}: {v}"


def getText(file: str) -> str:
    text = ""
    with open(file) as f:
        text = f.read()

    return text


if __name__ == "__main__":
    main()
