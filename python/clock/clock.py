def Clock(hh,mm):
	if hh>24:
		hh=1
	elif mm>=60:
		hh+=1
		mm=00
	if mm<0:
		while mm<0:
			for x in range(abs(int(mm/60))):
				mm=60+mm
			if hh==24:
				hh=0
			mm=60-(abs(mm))
			
	if hh<0:
		while hh<0:
			if hh<=24:
				hh=24-(abs(hh))
	hh = ("{0:0=2d}".format(hh))
	mm = ("{0:0=2d}".format(mm))
	return (hh)+":"+str(mm)
print((Clock(1, -4820)))
print('01:40')
