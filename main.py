from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_num_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(get_book_text(f"/Users/phyatich/Developer/courses/build_bookbot/bookbot/{sys.argv[1]}"))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = get_num_chars(get_book_text(f"/Users/phyatich/Developer/courses/build_bookbot/bookbot/{sys.argv[1]}"))
    for num_char in get_sorted_num_chars(num_chars):
        print(f"{num_char['char']}: {num_char['num']}")

main()
