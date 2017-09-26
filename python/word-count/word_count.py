def word_count(s):
	words = s.strip().split(' ')
	dict = {}
	for x in words:
		count = 0
		for y in s.strip().split():
			if x==y:
				count+=1
			dict[x]=count
	return dict

print(word_count('rah rah ah ah ah\troma roma ma\tga ga oh la la\t'))
