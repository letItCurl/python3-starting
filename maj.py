def maj(word):
	list_from_word = list(word)
	for i in range(len(word)):
		if i%2 == 0:
			list_from_word[i] = list_from_word[i].upper()
		else:
			list_from_word[i] = list_from_word[i].lower()
	return "".join(list_from_word)



def mega_maj(sentence):
	sentence = sentence.strip()
	sentence_list = sentence.split(' ')
	for i in range(len(sentence_list)):
		sentence_list[i] = maj(sentence_list[i])
	return " ".join(sentence_list)

print(mega_maj("   roland armando rodriguez lopez "))
