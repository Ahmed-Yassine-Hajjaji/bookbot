import sys
from stats import get_num_words,get_num_characters, sort_dictionary
# get_book_text(f) reads content in f and returns it
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents 
args = sys.argv
if len(args)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_text = get_book_text(f"{args[1]}")
print("============ BOOKBOT ============")
print(f"Analyzing book found at {args[1]}")
print("----------- Word Count ----------")
print(get_num_words(book_text))
print("--------- Character Count -------")
char_counts = get_num_characters(book_text)
sorted_chars = sort_dictionary(char_counts)
for item in sorted_chars:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")
print("============= END ===============")