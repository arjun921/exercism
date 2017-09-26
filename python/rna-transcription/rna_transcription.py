def to_rna(s):
	a = str()
	for x in s:
		if x in 'GgCcTtAa':
			if x in 'Gg':
				a+='C'
			elif x in 'Cc':
				a+='G'
			elif x in 'Tt':
				a+='A'
			elif x in 'Aa':
				a+='U'
		else:
			a=''
			break
	return a
