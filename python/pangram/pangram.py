def is_pangram(s):
	count = 0
	s = s.lower()
	s = set(s)
	flags_ = True
	for x in s:
		for y in 'qwertyuiopasdfghjklzxcvbnm':
			if x==y:
				count+=1
	flags_
	if count==26:
		flags_ = True
	else:
		flags_ = False
	return(flags_)
