def get_num_words(book_path):
	with open(book_path) as f:
		file_contents = f.read()
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	words = file_contents.split()
	print(f"Found {len(words)} total words")
	return file_contents

def get_char_count(book):
	book = book.lower()
	char_dic = {}
	for x in book:
		if x in char_dic.keys():
			char_dic[x]+=1
		else:
			char_dic[x]=1
	return char_dic

def sort_on(items):
	return items["num"]

def get_sort(char_dic):
	val = []
	for x in char_dic.keys():
		val.append({"char":x,"num":char_dic[x]})
	val.sort(reverse=True,key=sort_on)
	return val
