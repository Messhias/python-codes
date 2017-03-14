
def count_words(filename):
	""" COUNT ALL THE WORDS IN A FILE """
	try:
		with open(filename) as f_object:
			contents = f_object.read()
	except FileNotFoundError:
		pass
	else:
		#COUNT THE NUM WORDS IN THE TXT
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt','moby-dick.txt','little-women.txt','siddartha.txt']

for filename in filenames:
	count_words(filename)
