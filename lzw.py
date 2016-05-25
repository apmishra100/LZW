from cStringIO import StringIO

def compress(uncompressed):

	dictionary_size=256
	dictionary = dict((chr(i), chr(i)) for i in range(dictionary_size))

	w = ""

	result=[]
	for c in uncompressed:
		wc=w+c
		if wc in dictionary:
			w=wc
		else:
			result.append(dictionary[w])
			dictionary[wc]=dictionary_size
			dictionary_size = dictionary_size + 1
			w=c
	if w:
		result.append(dictionary[w])

	return result

def decompress(compressed):
	dictionary_size= 256
	dictionary = dict((chr(i), chr(i)) for i in range(dictionary_size))
	result = StringIO()
	result = ""
	w=compressed.pop(0)
	result.write(w)
	result += w
	for k in compressed:
		if k in dictionary:
			entry = dictionary[k]
			print(entry)
		elif k==dictionary_size:
			entry = w + w[0]		
		else:
			print("Bad key")
		result+=entry
		
		dictionary[dictionary_size]=w+entry[0]
		dictionary_size = dictionary_size + 1

		w = entry
	return result
	

myinput = raw_input("Please enter your string:")
compressed = compress(myinput)
print(compressed)
decompress = decompress(compressed)
print(decompress)
