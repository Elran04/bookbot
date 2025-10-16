from stats import get_num_words, get_char_count, chars_dict_to_sorted_list
import sys

def get_book_text(book_path):
        with open(book_path) as f:
            file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    chars_dict = get_char_count(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()