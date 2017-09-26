def is_isogram(s):
	s = s.lower()
	ls = set()
	flag_ = True
	dict = {}
	for x in s:
		if x!=' ':
			if x in 'qwertyuiopasdfghjklzxcvbnm':
				ls.add(x)
	for x in ls:
		count = 0
		for y in s:
			if x==y:
				count+=1
		dict[x]=count
	for x in dict:
		if dict[x]>1:
			flag_ = False
			break
		else:
			flag_ = True
	return(flag_)
