#!/usr/bin/python3
from stats import get_num_words, get_char_count, get_sort
import sys
def main():
	print("============ BOOKBOT ============")
	book = get_num_words(sys.argv[1])
	char_dic = get_char_count(book)
	val = get_sort(char_dic)
	print("--------- Character Count -------")
	for x in val:
		print(f"{x['char']}: {x['num']}")
	print("============= END ===============")
if __name__ == "__main__":
	if(len(sys.argv)<2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	main()
